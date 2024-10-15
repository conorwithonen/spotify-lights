

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