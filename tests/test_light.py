import unittest
from src.classes.light import Light
ip = '192.168.0.100'
brand = 'wiz'

class TestLight(unittest.TestCase):

    def setUp(self) -> None:
        self.light = Light(ip, brand)
        
    def test_initial_state(self):
        'Testing initialization and light is turned off'
        self.assertEqual(self.light.brand, brand)
        self.assertEqual(self.light.brightness, 0)
        self.assertFalse(self.light.is_on)
        
    def test_turn_on(self):
        self.light.turn_on()
        self.assertTrue(self.light.is_on)
    
    def test_turn_off(self):
        self.light.turn_on()
        self.light.turn_off()
        self.assertFalse(self.light.is_on)
    
    def test_set_color(self):
        self.light.set_color('purple')
        self.assertEqual(self.light.color, 'purple')
        self.assertIsNone(self.light.scene)
    
    def test_set_scene(self):
        self.light.set_scene('party')
        self.assertEqual(self.light.scene, 'party')
        self.light.set_scene(7)
        self.assertEqual(self.light.scene, 7)
        self.assertIsNone(self.light.color)
    
    def test_set_brightness(self):
        self.light.set_brightness(5)
        self.assertEqual(self.light.brightness, 5)
    
    def test_toggle(self):
        self.light.toggle()
        self.assertTrue(self.light.is_on)
        self.light.toggle()
        self.assertFalse(self.light.is_on)
    
    def test_get_state(self):
        self.light.turn_on()
        self.light.set_color('Maroon')
        self.light.set_brightness(13)
        self.assertDictEqual(
            self.light.get_state(),
            {'is_on': True, 'color': 'Maroon', 'brightness':13}
            )
        
    def test_reset(self):
        self.light.set_scene(4)
        self.light.reset()
        self.assertEqual(self.light.scene, 0)