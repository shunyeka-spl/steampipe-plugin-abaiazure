FROM python:latest

USER root

RUN apt update -y
RUN apt install curl -y
RUN /bin/sh -c "$(curl -fsSL https://raw.githubusercontent.com/turbot/steampipe/main/install.sh)"
ENV AWS_REGION="ap-south-1"
ARG user=steampipe
ARG group=steampipe
ARG uid=9999
ARG gid=9999

RUN groupadd -g ${gid} ${group}
RUN useradd -u ${uid} -g ${group} -s /bin/sh -m ${user}

USER ${uid}:${gid}
RUN steampipe plugin install aws steampipe azure gcp

COPY entrypoint.py .

COPY aws_tables.json .

RUN pip install pymongo

ENTRYPOINT ["python", "entrypoint.py"]
