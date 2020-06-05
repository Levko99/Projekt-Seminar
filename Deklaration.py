import pandas as pd
from gurobipy import *

# ------------------------- Excel-Dateien ------------------------------------------------------------------------------
schedules = 'Schedule.xlsx'
aircrafts = 'Aircrafts.xlsx'
through_values = 'Through_Values.xlsx'
airports = 'Airports.xlsx'

class Deklaration:
# ---------------------- Aircraft-Datei --------------------------------------------------------------------------------

# TODO Aicrafttype[0][i]:
#       i=0: AIRCRAFT_ID
#       i=1: AIRLINE
#       i=2: PRODUCER
#       i=3: TYPE
#       i=4: COUNT
#       i=5: SEATS
#       i=6: RANGE
#       i=7: FEASIBLE_AIRPORTS
#       i=8: AIRCRAFT_USAGE_COSTS
#       i=9: AIRCRAFT_KM_COSTS
#       i=10: MAINTENANCE_COSTS
#       i=11: MAINTENANCE_DURATION
#       i=12: MAINTENANCE_TOTALTIME
#       i=13: MAINTENANCE_FLYINGTIME
#       i=14: MAINTENANCE_FLYINGTIME

df = pd.read_excel(aircrafts)
Aircrafttypes = {}

for i in range(0, 6):  # TODO müsste noch automatisch an Spaltenanzahl des Excel Sheets angepasst werden
    list = []
    list.append(df['AIRCRAFT_ID'][i])
    list.append(df['AIRLINE'][i])
    list.append(df['PRODUCER'][i])
    list.append(df['TYPE'][i])
    list.append(df['COUNT'][i])
    list.append(df['SEATS'][i])
    list.append(df['RANGE'][i])
    list.append(df['FEASIBLE_AIRPORTS'][i])
    list.append(df['AIRCRAFT_USAGE_COSTS'][i])
    list.append(df['AIRCRAFT_KM_COSTS'][i])
    list.append(df['MAINTENANCE_COSTS'][i])
    list.append(df['MAINTENANCE_DURATION'][i])
    list.append(df['MAINTENANCE_TOTALTIME'][i])
    list.append(df['MAINTENANCE_FLYINGTIME'][i])
    list.append(df['MAINTENANCE_STARTS'][i])
    Aircrafttypes[i] = list

# -------------------------------------------- Schedule-Datei --------------------------------------------------------

# TODO Flights[0][i]:
#       i=0: FLIGHT_NUMBER
#       i=1: FLIGHT_TYPE
#       i=2: EXECUTING_AIRLINE
#       i=3: ORIGIN_IATA
#       i=4: DESTINATION_IATA
#       i=5: DEPARTURE_TIME
#       i=6: ARRIVAL_TIME
#       i=7: DISTANCE
#       i=8: DURATION
#       i=9: DEMAND
#       i=10: CANCELLATION_COSTS
#       i=11: COSTS_PER_SPILLED_PASSENGER
#       i=12: PRE_FLIGHT_TA_TIME
#       i=13: POST_FLIGHT_TA_TIME


sf = pd.read_excel(schedules)
Flights = {}

for i in range(0, 100):  # TODO müsste noch automatisch an Spaltenanzahl des Excel Sheets angepasst werden
    list = []
    list.append(sf['FLIGHT_NUMBER'][i])
    list.append(sf['FLIGHT_TYPE'][i])
    list.append(sf['EXECUTING_AIRLINE'][i])
    list.append(sf['ORIGIN_IATA'][i])
    list.append(sf['DESTINATION_IATA'][i])
    list.append(sf['DEPARTURE_TIME'][i])
    list.append(sf['ARRIVAL_TIME'][i])
    list.append(sf['DISTANCE'][i])
    list.append(sf['DURATION'][i])
    list.append(sf['DEMAND'][i])
    list.append(sf['CANCELLATION_COSTS'][i])
    list.append(sf['COSTS_PER_SPILLED_PASSENGER'][i])
    list.append(sf['PRE_FLIGHT_TA_TIME'][i])
    list.append(sf['POST_FLIGHT_TA_TIME'][i])
    Flights[i] = list

# -------------------------------------- Airport-Datei ---------------------------------------------------------
# TODO Airport['DUS'][i] / Airport[FLights[j][4]][i]:
#       i=0: AIRPORT_CITY
#       i=1: AIRPORT_TYPE
#       i=2: AIRPORT_CATEGORY
#       i=3: AIRPORT_TA_MULTIPLIER
# der key ist hier: AIRPORT_IATA


af = pd.read_excel("Airports.xlsx")

Airports = {}
for i in range(0, 6):  # TODO müsste noch automatisch an Spaltenanzahl des Excel Sheets angepasst werden,hier bla
    list = []
    list.append(af['AIRPORT_CITY'][i])
    list.append(af['AIRPORT_TYPE'][i])
    list.append(af['AIRPORT_CATEGORY'][i])
    list.append(af['AIRPORT_TA_MULTIPLIER'][i])
    Airports[af['AIRPORT_IATA'][i]] = list

# -------------------------------------- Konstruktor ---------------------------------------------------------
def __init__(self):
    self.Flights = Flights
    self.Aircrafttypes = Aircrafttypes
    self.Airptorts = Airports