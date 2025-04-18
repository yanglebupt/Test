# docker build -t crewai .
FROM ubuntu
SHELL ["/bin/bash", "-c"]

# 需要梯子
RUN apt-get update && apt-get install -y curl
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"
RUN apt-get install -y build-essential
RUN uv tool install crewai -i https://mirrors.aliyun.com/pypi/simple