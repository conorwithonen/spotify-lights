class Light:
    def __init__(self, ip, brand) -> None:
        self.ip = str(ip)
        self.brand = brand
        self.is_on = False
        self.color = 'warm_white'
        self.brightness = 0
        self.scene = None
        self.__default_scene = 0
        
    def __str__(self) -> str:
        return f'{self.brand} bulb at {self.ip}: {self.get_state()}'
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def set_color(self, color):
        self.color = color
        # A light can only do one thing
        self.scene = None
    
    def set_brightness(self, brightness):
        self.brightness = brightness
        
    def set_scene(self, scene):
        self.scene = scene
        self.color = None
    
    def toggle(self):
        self.is_on = not self.is_on
    
    def get_state(self):
        return {
                'is_on': self.is_on,
                'color': self.color,
                'brightness': self.brightness
                }
        
    def reset(self):
        '''Turns the bulb back to the default state'''
        self.scene = self.__default_scene
    
# Methods to update all lights, agnostic of brand
