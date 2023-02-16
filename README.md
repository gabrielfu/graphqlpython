# GraphQL Server
This is a toy example of GraphQL FastAPI server for a modified version of 
[IMDB dataset](https://www.imdb.com/interfaces/), retrieved on 15 Feb 2023.

The backend database is a PostgreSQL db. 

## Usage
Run server:
```shell
docker-compose up --build -d
```

Example Query:
```python
import requests

url = "http://localhost:8000/graphql"
body = """
{
  actor (primaryName: "Chris Hemsworth") {
    primaryName,
    birthYear,
    movies {
      edges {
        node {
          primaryTitle,
          region,
          startYear,
          runtimeMinutes,
          averageRating,
          numVotes
        }
      }
    } 
  }
}
"""
r = requests.post(url=url, json={"query": body})
r.raise_for_status()
r.json()

# output:
# {'data': {'actor': {'primaryName': 'Chris Hemsworth',
#    'birthYear': 1983,
#    'movies': {'edges': [{'node': {'primaryTitle': 'Thor: Ragnarok',
#        'region': 'US',
#        'startYear': 2017,
#        'runtimeMinutes': 130,
#        'averageRating': 7.9,
#        'numVotes': 761413}},
#      {'node': {'primaryTitle': 'The Cabin in the Woods',
#        'region': 'US',
#        'startYear': 2011,
#        'runtimeMinutes': 95,
#        'averageRating': 7.0,
#        'numVotes': 425020}},
#      {'node': {'primaryTitle': 'Avengers: Infinity War',
#        'region': 'US',
#        'startYear': 2018,
#        'runtimeMinutes': 149,
#        'averageRating': 8.4,
#        'numVotes': 1094492}},
#      {'node': {'primaryTitle': 'Avengers: Endgame',
#        'region': 'US',
#        'startYear': 2019,
#        'runtimeMinutes': 181,
#        'averageRating': 8.4,
#        'numVotes': 1147208}}]}}}}
```