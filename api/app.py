import uvicorn
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from db import init_db, db_session
from schema import schema

app = FastAPI()
app.debug = True

@app.on_event("startup")
def startup():
    init_db()

@app.on_event("shutdown")
def shutdown():
    db_session.remove()

app.mount("/graphql", GraphQLApp(schema, on_get=make_graphiql_handler()))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)