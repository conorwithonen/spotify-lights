# Semi-Custom Spotify Light Sequencer

A fast and dirty script process to watch the "currently playing" song on your spotify and deploy pre-defined static colors depending on what the song is. I would have liked a better app that actually follows OOP principles but I did not start this project until a couple weeks before a Halloween party so that is my bad.

# The Goal
During a party there would be a default state of lights, likely slowly fading through a chromatic scale of colors. Then when a song defined in the `song_scenes.json` file comes on, the lights would switch to the defined color accordingly. Giving that song a little more atmosphere. Songs not defined in the file would simply keep the lights in the default state.

# Running
Note: I highly recommend setting up some static IP reservations in your router panel / wherever you manage DHCP. Otherwise your lightbulbs / Hue bridge will change IPs.
For the hue bridge, you might have to press the "join" button on the bridge right before starting if this is the first time you are running this application.

## Starting Application
1. Create a Shopify application. [Spotify Apps](https://developer.spotify.com/documentation/web-api/concepts/apps)
2. Create a song_scenes.json file with matching song titles and colors.
3. Clone down and install the packages.
```
cd shopify-lights && source venv/bin/activate
pip install -r requirements.txt
```
4. Create a `.env` file from the example file and fill out with your own credentials.
5. Update the IP addresses of all the lighting information in the `.env` file.
6. Play some music on Spotify from whatever application.
7. With the virtual environment activated, run the main file using `python main.py`


# Todo:
- Refine the exiting process
- Improve the auth token state refreshing
- Clean up the static color mapping
- Improve static color mapping so that each brand of light can accept different RGB values per "named" color"
    This is simply because the WIZ and Hue lights do not really match when passed a static RGB value and editing the RGB that WIZ gets is probably a lot easier than editing the gamma correction or whatever in the Hue library.
- Better light patterns in general.