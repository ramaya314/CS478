FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive

# install python and required packages
RUN apt-get update && \
    apt-get install -y software-properties-common git && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.10 python3.10-venv python3.10-distutils python3.10-dev \
                       curl build-essential g++ && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# set Python 3.10 as default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1 && \
    update-alternatives --install /usr/bin/pip pip /usr/local/bin/pip3.10 1

# install Gentopia with the Huggingface extras
RUN pip install gentopia
# fix error with access to openai.ChatCompletion
RUN pip install openai==0.28

# clone gentpool
# RUN git clone https://github.com/Gentopia-AI/Gentopia.git /Gentopia
RUN apt-get install -y git
RUN git clone https://github.com/Gentopia-AI/GentPool.git /GentPool

#fix error with model_cards.json not found
COPY ./model_cards.json /usr/local/lib/python3.10/dist-packages/gentopia/resource/model_cards.json

COPY ./.env /GentPool/.env
COPY ./pool /GentPool/gentpool/pool
RUN chmod +x -R /GentPool/gentpool/pool
WORKDIR /GentPool

#entrypoint
COPY entrypoint.sh /GentPool/entrypoint.sh
RUN chmod +x /GentPool/entrypoint.sh
ENTRYPOINT ["/GentPool/entrypoint.sh"]