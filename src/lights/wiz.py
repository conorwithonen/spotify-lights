import os
import asyncio
from pywizlight import wizlight, PilotBuilder

DEFAULT_SCENE = os.getenv('WIZ_PARTY_SCENE')

# List of IPs for bulbs pulled from environment
BULBS = [
    os.getenv('CENTER_FLOOD_IP'),
    os.getenv('LEFT_FLOOD_IP')
]

# "Dynamic Effects"
async def rainbow_effect(duration=10):
    # Works okay
# Define the rainbow colors (RGB format)
    rainbow_colors = [
        (255, 0, 0),    # Red
        (255, 127, 0),  # Orange
        (255, 255, 0),  # Yellow
        (0, 255, 0),    # Green
        (0, 0, 255),    # Blue
        (75, 0, 130),   # Indigo
        (148, 0, 211)   # Violet
    ]
    start_time = asyncio.get_event_loop().time()
    while True:
        elapsed_time = asyncio.get_event_loop().time() - start_time
        if elapsed_time >= duration:
            print(f"Stopping after {elapsed_time:.2f} seconds")
            break
        for color in rainbow_colors:
            for bulb in BULBS:
                await set_static_color(bulb ,color)
            await asyncio.sleep(1)

async def default_effect(duration=None):
    for bulb in BULBS:
        await return_to_default(bulb)

# Bulb Interfaces
async def set_warm_white(bulb_ip):
    # Sends color data to the actual light bulb
    bulb = wizlight(bulb_ip)
    await bulb.turn_on(PilotBuilder(warm_white=255))

async def set_static_color(bulb_ip, color):
    # Sends color data to the actual light bulb
    bulb = wizlight(bulb_ip)
    await bulb.turn_on(PilotBuilder(rgb=color))

async def return_to_default(bulb_ip):
    # Sends color data to the actual light bulb
    bulb = wizlight(bulb_ip)
    state = await bulb.updateState()
    current_scene = state.get_scene()
    if current_scene != 'Party':
        await bulb.turn_on(PilotBuilder(scene=DEFAULT_SCENE))

# Controller function
async def change_living_room_lights(rgb, duration=None):
    # Sends either the color or effect to a bulb.
    if type(rgb) == tuple:
        for bulb in BULBS:
            await set_static_color(bulb, rgb)
    else:
        # Effect function
        if duration:
            print(f'Running {rgb.__name__} for {duration} seconds...')
        await rgb(duration)

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    BULBS = [
        os.getenv('CENTER_FLOOD_IP'),
        os.getenv('LEFT_FLOOD_IP')
    ]
    async def reset():
        for bulb in BULBS:
            await set_warm_white(bulb)

    asyncio.run(reset())
