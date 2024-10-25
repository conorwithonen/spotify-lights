import json
def translate_color(color_name):
    '''Translates color names to mapped RGB'''
    codes = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'orange': (255, 105, 0),
        'purple': (15, 0, 255)
    }
    return codes.get(color_name.lower(), None)


def load_songs_file(filename='song_scenes_examples.json'):
    '''Map of song titles and "Colors", returns dict'''
    with open (filename, 'r') as file:
        return json.load(file)
    
def rgb_to_xy(red, green, blue):
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
    
def song_timestamp_to_ms(time: str):
    '''Takes m:ss timestamp str and converts to ms'''
    try:
        min, sec = map(int,time.split(':'))
        ms = (min * 60 + sec) * 1000
        return ms
    except ValueError:
        raise ValueError("Invalid time format. Use m:ss")
    
def lookup_song(all_songs, lookup_value, lookup_key='songTitle'):
    '''Looksup up json object in array of objects'''
    for song in all_songs:
        if song.get(lookup_key) == lookup_value:
            return song