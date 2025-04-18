# docker build -t crewai-server .
# docker save -o crewai-server.tar b91af1c91fb8
# docker run -it -p 8000:8000 -d --env-file <.env> <image>
FROM crewai_with_project

WORKDIR /app/generate_crewai

COPY ./src/*.py ./src
COPY ./src/__templates__ ./src/__templates__
COPY ./run.sh .
RUN chmod +x ./run.sh

EXPOSE 8000
CMD ["sh", "./run.sh"]
