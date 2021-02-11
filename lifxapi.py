import requests

'''
 - This program is a python version of the lifx API
 - Official api link: https://api.developer.lifx.com/docs/

 @author AnonymousHobbit
'''


class LifxAPI:

    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
        }

    ################################################################
    # BASIC METHODS OF THE API
    ################################################################

    #GET ALL THE LIGHTS
    def get_lights(self, id="all"):
        print("[+] Retrieving lights")

        response = requests.get(f'https://api.lifx.com/v1/lights/{id}', headers=self.headers).json()
        return {response[i]["label"]:response[i]["id"] for i in range(len(response))}

    #SET THE STATE
    def set_state(self, id="all", power=None, color=None, brightness=None, duration=None, infrared=None, fast="false"):

        data = {
            "power": power,
            "color": color,
            "brightness": brightness,
            "duration": duration,
            "infrared": infrared,
            "fast": fast
        }

        r = requests.put(f'https://api.lifx.com/v1/lights/{id}/state', data=data, headers=self.headers)
        return r.content.decode()

    #SET THE STATES
    def set_states(self, id="all", states=None):
        r = requests.put('https://api.lifx.com/v1/lights/states', data=json.dumps(data), headers=self.headers)
        return r.content.decode()


    def toggle_power(self, id="all"):
        r = requests.post(f'https://api.lifx.com/v1/lights/{id}/toggle', headers=self.headers)
        return r.content.decode()


    #RETRIEVE ALL SCENES
    def get_scenes(self):
        print("[+] Retrieving scenes")
        response = requests.get('https://api.lifx.com/v1/scenes', headers=self.headers).json()
        return {response[i]["name"]:response[i]["uuid"] for i in range(len(response))}

    #SET THE SCENE WITH ID
    def set_scene(self, uuid=None, duration=None, ignore=None, fast="false"):

        if not uuid:
            print("[!] Please set uuid as an argument")
            return

        data = {
            "duration": duration,
            "ignore": ignore,
            "fast": fast
        }
        print("[+] Activating scene with id:",uuid)
        r = requests.put(f'https://api.lifx.com/v1/scenes/scene_id:{uuid}/activate', headers=self.headers)
        return r.content.decode()

    #Validate color
    def validate(self, color=None):

        if not color:
            print("[!] Please set color string as an argument")
            return

        data = {
            'string': color
        }

        r = requests.get('https://api.lifx.com/v1/color', data=data, headers=self.headers)
        return r.content.decode()

    def effects_off(self, id="all", power_off="true"):
        data = {
            "power_off": power_off
        }

        r = requests.post(f'https://api.lifx.com/v1/lights/{id}/effects/off', data=data, headers=self.headers)


    ################################################################
    # CUSTOM EFFECTS
    ################################################################

    #Breathing effect
    def breathe(self, id="all", color=None, from_color=None, period=None, cycles=None, persist="false", power_on="true", peak=None):
        if not color:
            print("[!] Please set color as an argument")
            return

        data = {
            "color":color,
            "from_color":from_color,
            "period":period,
            "cycles":cycles,
            "persist": persist,
            "power_on": power_on,
            "peak": peak
        }

        r = requests.post(f'https://api.lifx.com/v1/lights/{id}/effects/breathe', data=data, headers=self.headers)
        return r.content.decode()

    #Move effect
    def move(self, id="all", duration=None, period=None, cycles=None, power_on="true", fast="false"):
        data = {
            "duration": duration,
            "period":period,
            "cycles":cycles,
            "power_on": power_on,
            "fast": fast
        }
        r = requests.post(f'https://api.lifx.com/v1/lights/{id}/effects/move', data=data, headers=self.headers)
        return r.content.decode()

    #Morphing effect
    def morph(self, id="all", period=None, duration=None, palette=None, power_on="true", fast="false"):

        data = {
            "period": period,
            "duration": duration,
            "palette": palette,
            "power_on": power_on,
            "fast": fast
        }

        r = requests.post(f'https://api.lifx.com/v1/lights/{id}/effects/morph', data=data, headers=self.headers)
        return r.content.decode()

    #Flame effect
    def flame(self, id="all", period=None, duration=None, power_on="true", fast="false"):
        data = {
            "period": period,
            "duration": duration,
            "power_on": power_on,
            "fast": fast
        }
        r = requests.post(f'https://api.lifx.com/v1/lights/{id}/effects/flame', data=data, headers=self.headers)
        return r.content.decode()

    #Pulse effect
    def pulse(self, id="all", color=None, from_color=None, period=None, cycles=None, persist="false", power_on="true"):
        if not color:
            print("[!] Please set color as an argument")
            return

        data = {
            "color": color,
            "from_color": from_color,
            "period": period,
            "cycles": cycles,
            "persist": persist,
            "power_on": power_on
        }

        r = requests.post(f'https://api.lifx.com/v1/lights/{id}/effects/pulse', data=data, headers=self.headers)
        return r.content.decode()

    #Cycle effect
    def cycle(self, id="all", defaults=None, direction="forward", states=None):
        if not states:
            print("[!] Please set states as an argument")
            return
        data = {
            "states": states
        }
        r = requests.post(f'https://api.lifx.com/v1beta1/lights/{id}/cycle', data=data, headers=self.headers)
        return r.content.decode()
