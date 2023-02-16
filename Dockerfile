FROM python:3.9-slim

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . .
ENV PATH="/app:${PATH}"
ENV FIXTURE_MOVIES_PATH="/app/data/imdb/movies.csv"
ENV FIXTURE_ACTORS_PATH="/app/data/imdb/actors.csv"
ENV FIXTURE_ASSOCIATION_PATH="/app/data/imdb/actor_movie.csv"

EXPOSE 8000
CMD ["python3", "./api/app.py"]