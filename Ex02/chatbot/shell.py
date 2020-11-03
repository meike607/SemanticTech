#!/usr/bin/python3
# conda activate env_st
# pip install rivescript
# pip install requests

from rivescript import RiveScript

rs = RiveScript()
rs.load_directory("./brain")
rs.sort_replies()

while True:
    msg = input("You> ")
    if msg == "/quit":
        quit()
    reply = rs.reply("localuser", msg)
    print("Bot>", reply)


"""
# TEST API REQUESTS
# API
# https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0/geoservice
# Docs
# https://www.rivescript.com/docs/tutorial

import sys
import requests

# FIXME use REST API instead with data selection
# e.g. https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_COVID19/FeatureServer/0/query?where=1%3D1&outFields=AnzahlFall,AnzahlTodesfall,NeuerFall,NeuGenesen,AnzahlGenesen,NeuerTodesfall&returnGeometry=false&outSR=4326&f=json
# https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0
URL = "https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.geojson"
try:
    response = requests.get(URL)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

response = response.json()
items = response["features"]
current_cases = sum(
    [
        item["properties"]["AnzahlFall"]
        for item in items
        if item["properties"]["NeuerFall"] in [0, 1]
    ]
)
current_cases_delta = sum(
    [
        item["properties"]["AnzahlFall"]
        for item in items
        if item["properties"]["NeuerFall"] in [-1, 1]
    ]
)
current_death_cases = sum(
    [
        item["properties"]["AnzahlTodesfall"]
        for item in items
        if item["properties"]["NeuerFall"] in [0, 1]
    ]
)
current_death_cases_delta = sum(
    [
        item["properties"]["AnzahlTodesfall"]
        for item in items
        if item["properties"]["NeuerFall"] in [-1, 1]
    ]
)

current_recovered_cases = sum(
    [
        item["properties"]["AnzahlGenesen"]
        for item in items
        if item["properties"]["NeuGenesen"] in [0, 1]
    ]
)
current_recovered_cases_delta = sum(
    [
        item["properties"]["AnzahlGenesen"]
        for item in items
        if item["properties"]["NeuGenesen"] in [-1, 1]
    ]
)
print(f"Anzahl Fälle der aktuellen Publikation: {current_cases}")
print(f"Anzahl Fälle Delta zum Vortag: {current_cases_delta}")
print(f"Anzahl Todesfälle der aktuellen Publikation: {current_death_cases}")
print(f"Anzahl Todesfälle Delta zum Vortag: {current_death_cases_delta}")
print(f"Anzahl Genesen der aktuellen Publikation: {current_recovered_cases}")
print(f"Anzahl Genesen Delta zum Vortag: {current_recovered_cases_delta}")
"""
