# GraphQL Server

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
```