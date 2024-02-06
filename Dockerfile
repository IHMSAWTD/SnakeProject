FROM ubuntu:latest
LABEL authors="ub"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

ENTRYPOINT ["top", "-b"]