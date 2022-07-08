import arcade
from math import cos, sin

WIDTH = 700
HEIGHT = 700
TITLE = 'Circles'

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.angle = 0
        self.moon_angle = 5
        self.radius = 300
        self.moon_radius = 60

    def setup(self):
        self.coin = arcade.Sprite('coin.png', 0.5)
        self.moon = arcade.Sprite('coin.png', 0.3)
        self.coin.center_x = WIDTH/2 + 300
        self.coin.center_y =HEIGHT/2 + 0
        self.moon.center_x = self.coin.center_x + self.moon_radius * cos(self.moon_angle)
        self.moon.center_y = self.coin.center_y + self.moon_radius * sin(self.moon_angle)
        self.moon_angle += 0.05


    
    def update(self, delta_time):
        self.coin.center_x = WIDTH/2 + self.radius * cos(self.angle)
        self.coin.center_y = HEIGHT/2 + self.radius * sin(self.angle)
        self.angle += 0.009
        self.moon.center_x = self.coin.center_x + self.moon_radius * cos(self.moon_angle)
        self.moon.center_y = self.coin.center_y + self.moon_radius * sin(self.moon_angle)
        self.moon_angle += 0.03
       
    
    def on_draw(self):
        
        self.coin.draw()
        self.moon.draw()

game = Game()
game.setup()
arcade.run()
