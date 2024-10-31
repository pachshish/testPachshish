from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()



class CitiesModel(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String)
    country_id = Column(Integer, ForeignKey("countries.country_id"))
    latitude = Column(Float)
    longitude = Column(Float)

class CountriesModel(Base):
     __tablename__ = 'countries'
     country_id = Column(Integer, primary_key=True)
     country_name = Column(String)

class MissionsModel(Base):
    __tablename__ ='missions'
    mission_id = Column(Integer, primary_key=True)
    mission_date = Column(Date)
    airborne_aircraft = Column(Float)
    attacking_aircraft = Column(Float)
    bombing_aircraft = Column(Float)
    aircraft_returned = Column(Float)
    aircraft_failed = Column(Boolean)
    aircraft_damaged = Column(Float) #? אולי זה טייפ אחר
    aircraft_lost  = Column(Boolean)

    # targets = relationship(
    #     "TargetsModel",
    #     back_populates="missions"
    #
    # )

class TargetsModel(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey("missions.mission_id"))
    target_industry = Column(String)
    city_id = Column(Integer, ForeignKey("cities.city_id"))
    target_type_id = Column(Integer, ForeignKey("targetTypes.target_type_id"))
    target_priority = Column(Integer)

    # missions = relationship(
    #     "MissionsModel",
    #     back_populates="targets"
    #
    # )

class TargetTypesModel(Base):
    __tablename__ = 'targetTypes'
    target_type_id = Column(Integer, primary_key=True)
    target_type_name = Column(String)