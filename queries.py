import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from graphene import ObjectType, Field, Int, String, Date, List
from graphql import GraphQLError
from database import db_session
from models import TargetTypesModel, TargetsModel, MissionsModel, CountriesModel, CitiesModel

class Missions(SQLAlchemyObjectType):
    class Meta:
        model = MissionsModel
        interfaces = (graphene.relay.Node,)


class Query(ObjectType):
    mission_by_id = Field(Missions, mission_id=Int(required=True))
    missions_by_date = List(Missions, date_start=Date(required=True), date_end=Date(required=True))
    missions_by_country = List(Missions, country_name=String(required=True))
    mission_by_industry = List(Missions, industry=String(required=True))

    @staticmethod
    def resolve_mission_by_id(self, info, mission_id):
        mission = db_session.query(MissionsModel).get(mission_id)
        if mission is None:
            raise GraphQLError('Mission not found')
        return mission

    @staticmethod
    def resolve_missions_by_date(root, info, date_start, date_end):
        missions = db_session.query(MissionsModel).filter(
            MissionsModel.mission_date.between(date_start, date_end)
        )
        if missions is None:
            raise GraphQLError('Missions not found')
        return missions

    @staticmethod
    def resolve_missions_by_country(self, info, country_name):
        country = db_session.query(CountriesModel).filter(CountriesModel.country_name == country_name).first()
        missions = (
            db_session.query(MissionsModel)
            .join(TargetsModel)
            .join(CitiesModel)
            .filter(CitiesModel.country_id == CountriesModel.country_id)
            .all()
        )
        if missions is None:
            raise GraphQLError('Missions not found')
        return missions

    @staticmethod
    def resolve_mission_by_industry(self, info, industry):
        missions = (db_session.query(MissionsModel)
                    .join(TargetsModel, TargetsModel.mission_id == MissionsModel.mission_id)
                    .filter(TargetsModel.target_industry == industry)
                    ).all()
        if missions is None:
            raise GraphQLError('Missions not found')
        return missions








schema = graphene.Schema(query=Query)