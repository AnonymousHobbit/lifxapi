import os
from pprint import pprint
from dotenv import load_dotenv
from lifxapi import LifxAPI

load_dotenv()

TOKEN = os.getenv("TOKEN")
lifx = LifxAPI(TOKEN)

scenes = lifx.get_scenes()

lifx.set_scene(scenes["Calm"])
lifx.set_state(brightness=0.8)
