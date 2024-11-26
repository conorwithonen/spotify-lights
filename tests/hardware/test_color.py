from src.scenes import update_light_scene

# Playback object that would "reset" to the default party
regular_pb = {
    'artist': 'Converge, Chelsea Wolfe',
    'song': 'Coil',
    'duration_ms': 368453}

# Playback object that would trigger a special scene
special_pb = {
    'artist': 'Misfits',
    'song': 'Halloween',
    'duration_ms': 368453}

update_light_scene(special_pb)