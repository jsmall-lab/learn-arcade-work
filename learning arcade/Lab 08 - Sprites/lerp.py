import arcade
import random



WIDTH = 800
HEIGHT = 800
TITLE = 'Lerp'

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
        self.player = None
        self.set_mouse_visible(True)


    def setup(self):
        self.player = arcade.Sprite('character.png-1.png.png ')
        self.player.center_x = 200
        self.player.center_y = 400
     
    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        

    def update(self, delta_time):
        self.player.center_x = arcade.utils.lerp(self.player.center_x, self._mouse_x, 0.1)
        self.player.center_y = arcade.utils.lerp(self.player.center_y, self._mouse_y, 0.1)

       
game = Game()
game.setup()
arcade.run()
