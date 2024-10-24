import unittest
        
from src import utils

class TestUtils(unittest.TestCase):
    
    def test_translate_color(self):
        f = utils.translate_color
        self.assertEqual(f('red'), (255,0, 0))
        self.assertEqual(f('Red'), (255,0, 0))
        self.assertEqual(f('blue'), (0, 0, 255))
        self.assertIsNone(f('cyan'))
        
    def test_load_songs_file(self):
        f = utils.load_songs_file()
        self.assertIsNotNone(f)
        self.assertTrue('Lemonade' in f)

    def test_rgb_to_xy(self):
        color = (255, 255, 255)
        xy = utils.rgb_to_xy(*color)
        self.assertEqual(xy, [0.32272672086556803, 0.32902290955907926])

    def test_song_timestamp_to_ms(self):
        self.assertEqual(
            utils.song_timestamp_to_ms('2:30'),
            150000
        )