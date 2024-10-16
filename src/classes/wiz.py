from src.classes.light import Light
from src.utils import translate_color
import asyncio
from pywizlight import wizlight, PilotBuilder

class Wiz(Light):
    brand = 'Wiz'
    def __init__(self, ip):
        super().__init__(ip, self.brand)
        self.bulb = wizlight(ip)
        self.__default_scene = 4
        
    async def turn_on(self):
        super().turn_on()
        await self.bulb.turn_on()
        
    async def turn_off(self):
        super().turn_off()
        await self.bulb.turn_off()
    
    async def set_scene(self, _scene):
        # Wiz values Only 1 to 32. 4 is Party
        super().set_scene(_scene)
        pb = PilotBuilder(scene=_scene)
        await self.bulb.turn_on(pb)
        
    async def set_color(self, color):
        '''Turns on the physical bulb using the wizlight package'''
        # TODO: Color Differences between hue and WIZ lights.
        super().set_color(color)

        _rgb = translate_color(color)
        pb = PilotBuilder(rgb=_rgb)
        await self.bulb.turn_on(pb)
        
    async def reset(self):
        '''Turns the light from special colors to default'''
        # hardware_state = await self.bulb.updateState()
        # await self.set_scene(state.get_scene_id())
        # if self.scene != self.default_scene:
        await self.set_scene(self.__default_scene)
            
    