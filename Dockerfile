FROM python:3.8.2-alpine

ENV APP_HOME=/app
RUN mkdir -p ${APP_HOME}
WORKDIR ${APP_HOME}

COPY requirements.txt ./requirements.txt
RUN pip3 install  -r requirements.txt

ADD app ./
RUN chmod +x ${APP_HOME}/scripts/*.sh
ENTRYPOINT ["/app/scripts/docker-entrypoint.sh"]
CMD /app/scripts/run.sh
