@echo off

@REM echo Building the LLM image...
@REM docker build -t ramayar/cs478llm .

echo Running the LLM container...
docker pull ramayar/cs478llm:latest
docker run -it --rm ramayar/cs478llm:latest