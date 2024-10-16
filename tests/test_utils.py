import unittest
        
from src.classes.light import Light
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