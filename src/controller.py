import os
from src.utils import load_songs_file
from src.classes import wiz

SONG_FILE = 'song_scenes.json'
SPECIAL_COLORS = load_songs_file(SONG_FILE)
LIGHTS = [
    # Living room
    wiz.Wiz(os.getenv('CENTER_FLOOD_IP')),
    wiz.Wiz(os.getenv('LEFT_FLOOD_IP'))
]


async def change_registered_lights(*lights, color: str):
    '''Sets all lights to a set color
    
    arguments:
    lights -- Any number of Light objects
    color -- Name of the color to update Ex. Red
    '''
    # TODO: Color as optional non-string for eventual dynamic scene set
    for light in lights:
        light.set_color(color)

async def reset_registered_lights(*lights):
    '''Resets all lights to default scene if they have
        static color. Does nothing if color is None.
        
    arguments:
    lights -- Any number of Light objects
    '''
    # TODO: Not assume that a light is in a color state.
    for light in lights:
        if light.color:
            light.reset()

async def update_lights(playback):
    '''Updates all lights based on playback info
    
    arguments:
    playback -- dict of info from spotify
    '''
    song = playback.get('song')

    if song in SPECIAL_COLORS:
        new_color = SPECIAL_COLORS.get(song)
        print(f'Changing lights to {new_color}')
        await change_registered_lights(*LIGHTS, new_color)
    else:
        await reset_registered_lights(*LIGHTS)
