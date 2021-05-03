import arcade


WIDTH = 800
HEIGHT = 600
TITLE = 'Sprites'


class Game(arcade.Window):
    def _init_(self):
        super()._init_(WIDTH, HEIGHT, TITLE)
        self.player_sprite = None
    
    def setup(self):
        self.player_sprite = arcade.Sprite("./player_image.png", center_x=WIDTH/2, center_y=HEIGHT/2)
  
    
    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()

game = Game()
game.setup()
arcade.run()

