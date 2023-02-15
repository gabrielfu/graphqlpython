import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import ActorModel, MovieModel


class Actor(SQLAlchemyObjectType):
    class Meta:
        model = ActorModel
        interfaces = (relay.Node,)


class Movie(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_actors = SQLAlchemyConnectionField(Actor.connection)
    all_movies = SQLAlchemyConnectionField(Movie.connection)


schema = graphene.Schema(query=Query)