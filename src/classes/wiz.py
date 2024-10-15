from src.classes.light import Light
from src.utils import translate_color
import asyncio
from pywizlight import wizlight, PilotBuilder

class Wiz(Light):
    def __init__(self, ip):
        super().__init__(ip, 'Wiz')
        self.bulb = wizlight(ip)
        self.default_scene = 4
        
    async def turn_on(self):
        super().turn_on()
        await self.bulb.turn_on()
        
    async def turn_off(self):
        super().turn_off()
        await self.bulb.turn_off()
    
    async def set_scene(self, scene):
        # Wiz values Only 1 to 32. 4 is Party
        return super().set_scene(scene)
        
    async def set_color(self, color):
        '''Turns on the physical bulb using the wizlight package'''
        super().set_color(color)
        # color string to rgb tuple
        _rgb = translate_color(color)
        pb = PilotBuilder(rgb=_rgb)
        await self.bulb.turn_on(pb)
        
    async def reset(self):
        '''Turns the light from special colors to default'''
        state = await self.bulb.updateState()
        await self.set_scene(state.get_scene_id())
        if self.current_scene != self.default_scene:
            pb = PilotBuilder(scene=self.default_scene)
            await self.bulb.turn_on(pb)