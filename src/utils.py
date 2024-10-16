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