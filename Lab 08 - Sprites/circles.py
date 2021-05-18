import arcade
from math import cos, sin

WIDTH = 800
HEIGHT = 800
TITLE = 'Circles'

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.angle = 0
        self.radius = 300

    def setup(self):
        self.coin = arcade.Sprite('coin.png')
        self.coin.center_x = WIDTH/2 + 300
        self.coin.center_y =HEIGHT/2 + 0

    
    def update(self, delta_time):
        self.coin.center_x = WIDTH/2 + self.radius * cos(self.angle)
        self.coin.center_y = HEIGHT/2 + self.radius * sin(self.angle)
        self.angle += 0.02

    def on_draw(self):
        arcade.start_render()
        self.coin.draw()

game = Game()
game.setup()
arcade.run()
