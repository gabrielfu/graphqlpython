# GraphQL Server
This is a toy example of GraphQL FastAPI server for a modified version of 
[IMDB dataset](https://www.imdb.com/interfaces/), retrieved on 15 Feb 2023.

## Usage
Run server:
```shell
docker-compose up --build -d
```

Example Query:
```python
import requests
import pprint

url = "http://localhost:8000/graphql"
body = """
{
  actor (primaryName: "Satomi Ishihara") {
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
pprint.pprint(r.json())

# output:
# {'data': {'actor': {'birthYear': 1986,
#                     'movies': {'edges': [{'node': {'averageRating': 6.8,
#                                                    'numVotes': 29025,
#                                                    'primaryTitle': 'Shin '
#                                                                    'Godzilla',
#                                                    'region': 'US',
#                                                    'runtimeMinutes': 120,
#                                                    'startYear': 2016}},
#                                          {'node': {'averageRating': 5.1,
#                                                    'numVotes': 14361,
#                                                    'primaryTitle': 'Attack on '
#                                                                    'Titan Part '
#                                                                    '1',
#                                                    'region': 'GB',
#                                                    'runtimeMinutes': 98,
#                                                    'startYear': 2015}}]},
#                     'primaryName': 'Satomi Ishihara'}}}
```