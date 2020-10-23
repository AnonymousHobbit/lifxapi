import requests


class LifxAPI:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
        }

    #GET ALL THE LIGHTS
    def get_lights(self, id="all"):
        print("[+] Retrieving lights")
        response = requests.get('https://api.lifx.com/v1/lights/all', headers=self.headers).json()

        return {response[i]["label"]:response[i]["id"] for i in range(len(response))}

    #SET THE STATE
    def set_state(self, id="all", power=None, color=None, brightness=None, duration=None, infrared=None, fast=None):

        payload = {
            "power": power,
            "color": color,
            "brightness": brightness,
            "duration": duration,
            "infrared": infrared,
            "fast": fast
        }

        requests.put(f'https://api.lifx.com/v1/lights/{id}/state', data=payload, headers=self.headers)

    #RETRIEVE ALL SCENES
    def get_scenes(self):
        print("[+] Retrieving scenes")
        response = requests.get('https://api.lifx.com/v1/scenes', headers=self.headers).json()
        return {response[i]["name"]:response[i]["uuid"] for i in range(len(response))}

    #SET THE SCENE WITH ID
    def set_scene(self, id):
        if not id:
            return "[!] Please set id as an argument"

        requests.put(f'https://api.lifx.com/v1/scenes/scene_id:{id}/activate', headers=self.headers)
