import os
import asyncio
from phue import Bridge
import sys
import colorsys

# ----------------------------- Configuration -----------------------------
# Replace with your Hue Bridge IP address
BRIDGE_IP = os.getenv('HUE_BRIDGE_IP')  # Example IP; replace with your bridge's IP.
DEFAULT_SCENE = os.getenv('NORMAL_PARTY_SCENE')
NORMAL_SCENE = os.getenv('NORMAL_KITCHEN_SCENE')
KITCHEN_GROUP = os.getenv('KITCHEN_GROUP')
# ---------------------------------------------------------------------------

async def rgb_to_xy(red, green, blue):
    """Converts RGB to CIE 1931 XY color space for Hue lights."""
    # Normalize RGB values to 0-1 range
    r = red / 255.0
    g = green / 255.0
    b = blue / 255.0

    # Apply gamma correction
    r = ((r + 0.055) / (1.0 + 0.055)) ** 2.4 if r > 0.04045 else (r / 12.92)
    g = ((g + 0.055) / (1.0 + 0.055)) ** 2.4 if g > 0.04045 else (g / 12.92)
    b = ((b + 0.055) / (1.0 + 0.055)) ** 2.4 if b > 0.04045 else (b / 12.92)

    # Convert RGB to XYZ using the Wide RGB D65 conversion formula
    X = r * 0.664511 + g * 0.154324 + b * 0.162028
    Y = r * 0.283881 + g * 0.668433 + b * 0.047685
    Z = r * 0.000088 + g * 0.072310 + b * 0.986039

    # Convert XYZ to xy
    if (X + Y + Z) == 0:
        return [0, 0]
    else:
        x = X / (X + Y + Z)
        y = Y / (X + Y + Z)
        return [x, y]

async def reset_kitchen_lights():
    # Resets kitchen to the default "Party scene"
    try:
        # Connect to the Hue Bridge
        b = Bridge(BRIDGE_IP)
        print(f"Connecting to the Hue Bridge at {BRIDGE_IP}...")

        b.activate_scene(
            scene_id=DEFAULT_SCENE,
            group_id=KITCHEN_GROUP
            )

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


async def end_party():
    # Resets kitchen to the default "Party scene"
    try:
        # Connect to the Hue Bridge
        b = Bridge(BRIDGE_IP)
        print(f"Connecting to the Hue Bridge at {BRIDGE_IP}...")

        b.activate_scene(
            scene_id=NORMAL_SCENE,
            group_id=KITCHEN_GROUP
            )

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

async def change_kitchen_lights(rgb_color):
    try:
        # Connect to the Hue Bridge
        b = Bridge(BRIDGE_IP)
        print(f"Connecting to the Hue Bridge at {BRIDGE_IP}...")

        # If running for the first time, press the bridge button and uncomment the next line
        # b.connect()

        # Retrieve all lights
        lights = b.lights
        print(f"Total lights found: {len(lights)}")

        # Filter lights with "Island" in their name (case-insensitive)
        island_lights = [light for light in lights if 'island' in light.name.lower()]

        if not island_lights:
            print("No lights with 'Island' in their name were found.")
            sys.exit(1)

        print(f"Found {len(island_lights)} 'Island' light(s): {[light.name for light in island_lights]}")

        # Convert the provided RGB color to XY format
        xy_color = await rgb_to_xy(*rgb_color)
        print(f"RGB {rgb_color} converted to XY: {xy_color}")

        # Update each light with the new color
        for light in island_lights:
            print(f"Updating light '{light.name}' with XY color {xy_color}...")
            light.on = True  # Ensure the light is turned on
            light.xy = xy_color  # Set the xy color
            light.brightness = 254  # Max brightness (adjust as needed)
            print(f"Light '{light.name}' updated.")

        print("All 'Island' lights have been updated.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    from dotenv import load_dotenv

    load_dotenv()
    BRIDGE_IP = os.getenv('HUE_BRIDGE_IP')  # Example IP; replace with your bridge's IP.
    DEFAULT_SCENE = os.getenv('NORMAL_PARTY_SCENE')
    NORMAL_SCENE = os.getenv('NORMAL_KITCHEN_SCENE')
    KITCHEN_GROUP = os.getenv('KITCHEN_GROUP')

    asyncio.run(end_party())