import os
from src.lights.light import Light
from src.utils import translate_color, rgb_to_xy
from phue import Bridge
import asyncio



class Hue(Light):
    brand = 'Phillips'
    b = Bridge(os.getenv('HUE_BRIDGE_IP'))
    def __init__(self, phue_light, group_id):
        super().__init__(self.b.ip, self.brand)
        self.bulb = phue_light
        self.__default_scene = os.getenv('NORMAL_PARTY_SCENE')
        self.__group_id = group_id

        
    async def turn_on(self):
        super().turn_on()
        self.bulb.on = True
        
    async def turn_off(self):
        super().turn_off()
        self.bulb.on = False
    
    async def set_scene(self, _scene):
        # Wiz values Only 1 to 32. 4 is Party
        super().set_scene(_scene)
        self.b.activate_scene(
            scene_id=_scene,
            group_id=self.__group_id
        )
        
    async def set_color(self, color):
        '''Turns on the physical bulb using the wizlight package'''
        # TODO: Color Differences between hue and WIZ lights.
        super().set_color(color)
        _rgb = translate_color(color)
        _xy = rgb_to_xy(*_rgb)
        if not self.bulb.on:
            self.bulb.on = True
        self.bulb.xy = _xy
        self.bulb.brightness = 254
        
    async def reset(self):
        '''Turns the light from special colors to default'''
        await self.set_scene(self.__default_scene)

def get_hue_lights_by_name(name):
    b = Bridge(os.getenv('HUE_BRIDGE_IP'))
    group_id = b.get_group_id_by_name(name)
    lights = b.lights
    filtered_lights = [l for l in lights if str(name) in l.name]
    return [Hue(l, group_id) for l in filtered_lights]

def get_lights_by_group_name(name='Kitchen'):
    b = Bridge(os.getenv('HUE_BRIDGE_IP'))
    group_id = b.get_group_id_by_name(name)
    group_lights = b.get_group(group_id).get('lights') # Only returns light ids
    light_objects = [l for l in b.lights if str(l.light_id) in group_lights]
    return [Hue(l, group_id) for l in light_objects]
