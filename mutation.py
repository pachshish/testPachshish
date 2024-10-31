import graphene
from graphene import ObjectType, Field, Int, String, Date, List, Float, Mutation
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from database import db_session
from models import TargetTypesModel, TargetsModel, MissionsModel, CountriesModel, CitiesModel
from queries import schema


# class Missions(ObjectType):
#     class Meta:
#         model = MissionsModel
#         interfaces = (graphene.relay.Node,)

# class Mutation(ObjectType):
#     add_mission = AddMission.Field()

class AddMission(Mutation):
    class Arguments:
        id=String(required=True),
        missionId=Int(required=True),
        missionDate=Date(required=True),
        airborneAircraft=Float(required=True),
        attackingAircraft=Float(required=True),
        bombingAircraft=Float(required=True),
        aircraftReturned=Float(required=True),
        aircraftFailed=Float(required=True),
        aircraftDamaged=Float(required=True),
        aircraftLost=Float(required=True)

    mission = Field(lambda: MissionsModel)

    def mutate(self, id, missionId, missionDate, airborneAircraft, attackingAircraft, bombingAircraft, aircraftReturned, aircraftFailed, aircraftDamaged, aircraftLost):
        new_mission = MissionsModel(id=id, missionId=missionId, missionDate=missionDate, airborneAircraft=airborneAircraft, attackingAircraft=attackingAircraft, bombingAircraft=bombingAircraft, aircraftReturned=aircraftReturned, aircraftFailed=aircraftFailed, aircraftDamaged=aircraftDamaged, aircraftLost=aircraftLost)
        db_session.add(new_mission)
        db_session.commit()
        return AddMission(mission=new_mission)

