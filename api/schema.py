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
    actor = graphene.Field(Actor, id=graphene.String(), primary_name=graphene.String())
    movie = graphene.Field(Actor, id=graphene.String(), primary_title=graphene.String())

    all_actors = SQLAlchemyConnectionField(Actor.connection)
    all_movies = SQLAlchemyConnectionField(Movie.connection)

    def resolve_actor(root, info, id=None, primary_name=None):
        query = Actor.get_query(info)
        if id:
            query = query.filter(ActorModel.id == id)
        if primary_name:
            query = query.filter(ActorModel.primary_name == primary_name)
        return query.first()

    def resolve_movie(root, info, id=None, primary_title=None):
        query = Actor.get_query(info)
        if id:
            query = query.filter(ActorModel.id == id)
        if primary_title:
            query = query.filter(ActorModel.primary_title == primary_title)
        return query.first()


schema = graphene.Schema(query=Query)