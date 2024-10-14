
import asyncio
import json
from src.lights.wiz import change_living_room_lights, rainbow_effect, default_effect
from src.lights.phillips import change_kitchen_lights, reset_kitchen_lights

def get_rbg(color):
    codes = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'orange': (255, 105, 0),
        'purple': (15, 0, 255),
        'rainbow': rainbow_effect
    }
    return codes.get(color.lower(), default_effect)

# Map of song titles and "Colors" to be mapped into the
with open('song_scenes.json', 'r') as file:
    SPECIAL_COLORS = json.load(file)

async def update_light_scene(playback):
    # TODO: Color Differences between hue and WIZ lights.
    song = playback.get('song')
    duration_s = playback.get('duration_ms') / 1000

    if song in SPECIAL_COLORS:
        new_color = SPECIAL_COLORS.get(song)
        color_value = get_rbg(new_color)
        print(f'Changing lights to {new_color}')
        await change_living_room_lights(color_value, duration_s)
        await change_kitchen_lights(color_value)
    else:
        # No special color for this song
        color_value = get_rbg('default')
        await change_living_room_lights(color_value)
        await reset_kitchen_lights()

