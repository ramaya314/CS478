CS 478 Assignment 5
====
This is a docker container of an LLM agent that will read a URL containing a ULA and produce a sumarized bullet point list of the terms. 

to run the container, first install docker at https://docs.docker.com/engine/install/ then run

```
./run.bat
```

or (contents of run.bat)

```
docker pull ramayar/cs478llm:latest
docker run -it --rm ramayar/cs478llm:latest
```

The agent will then spin up with the container. You can then give a ULA url to the agent to sumarize.

some example ULA urls are:

- Google: https://policies.google.com/terms?hl=en
- Facebook: https://www.facebook.com/legal/terms?_rdr
- Instagram: https://help.instagram.com/581066165581870 