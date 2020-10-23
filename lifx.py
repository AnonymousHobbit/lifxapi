import os
from pprint import pprint
from dotenv import load_dotenv
from lifxapi import LifxAPI

load_dotenv()

TOKEN = os.getenv("TOKEN")
lifx = LifxAPI(TOKEN)
lights = lifx.get_lights()

lifx.set_state(color="blue")
scenes = lifx.get_scenes()
lifx.set_scene(scenes["Work"])
