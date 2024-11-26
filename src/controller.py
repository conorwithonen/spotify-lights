import os
from src.utils import load_songs_file, lookup_song, song_timestamp_to_ms
from src.lights import wiz, phillips
import asyncio

SONG_FILE = 'song_scenes.json'
SPECIAL_SONGS = load_songs_file(SONG_FILE)
LATENCY_BUFFER_MS = 0

# # Ugh
hue_bulbs = phillips.get_hue_lights_by_name('Island')
LIGHTS = [
    # Living room
    wiz.Wiz(os.getenv('CENTER_FLOOD_IP')),
    wiz.Wiz(os.getenv('LEFT_FLOOD_IP')),
    # Kitchen
    *hue_bulbs
    
]

async def change_registered_lights(*lights, color: str):
    '''Sets all lights to a set color
    
    arguments:
    lights -- Any number of Light objects
    color -- Name of the color to update Ex. Red
    '''
    # TODO: Color as optional non-string for eventual dynamic scene set
    tasks = [l.set_color(color) for l in lights]
    await asyncio.gather(*tasks)

async def reset_registered_lights(*lights):
    '''Resets all lights to default scene if they have
        static color. Does nothing if color is None.
        
    arguments:
    lights -- Any number of Light objects
    '''
    # TODO: Not assume that a light is in a color state.
    tasks = [l.reset() for l in lights if l.color]
    await asyncio.gather(*tasks)

async def update_lights(playback):
    '''Updates all lights based on playback info
    
    arguments:
    playback -- dict of info from spotify
    '''
    song = playback.get('song')
    progress_ms = playback.get('progress_ms')
    special_song = lookup_song(SPECIAL_SONGS, song)
    if special_song:
        # Gets wait time by substracting progress_ms from delay
        new_color = special_song.get('color')
        delay_until = special_song.get('delay_until')
        if delay_until:
            delay_ms = song_timestamp_to_ms(delay_until)
            wait_time = delay_ms - progress_ms + LATENCY_BUFFER_MS
            print(f'Delaying light change for {wait_time}ms. Buffer: {LATENCY_BUFFER_MS}ms')
            await asyncio.sleep(wait_time / 1000)
        print(f'Changing lights to {new_color}')
        await change_registered_lights(*LIGHTS, color=new_color)
    else:
        await reset_registered_lights(*LIGHTS)

