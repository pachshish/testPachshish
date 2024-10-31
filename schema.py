import graphene
from graphene import ObjectType, Field, Int, String, Date
from graphene_sqlalchemy import SQLAlchemyObjectType
from database import db_session
from models import TargetTypesModel, TargetsModel, MissionsModel, CountriesModel, CitiesModel

class Missions(SQLAlchemyObjectType):
    class Meta:
        model = MissionsModel
        interfaces = (graphene.relay.Node,)


class Query(ObjectType):
    mission_by_id = Field(Missions, mission_id=Int(required=True))
    missions_by_date = Field(Missions, data_start=Date(required=True), data_end=Date(required=True))


    def resolve_mission_by_id(self, info, mission_id):
        return db_session.query(MissionsModel).get(mission_id)

    def resolve_missions_by_date(self, info, data_start, data_end):
        return db_session.query(MissionsModel).filter(
            data_start >= MissionsModel.mission_date <= data_end
        ).all()






schema = graphene.Schema(query=Query)