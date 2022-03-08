import arcade
import random



WIDTH = 800
HEIGHT = 800
TITLE = 'Sprites'

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
        self.score = 0
        self.coin_list = None
        self.player = None
        self.set_mouse_visible(True)


    def setup(self):
        self.coin_list = arcade.SpriteList()
        #self.score = 0
        self.player = arcade.Sprite('character.png-1.png.png ')
        self.player.center_x = 200
        self.player.center_y = 400
        for i in range(50):
            coin = arcade.Sprite('coin.png', 0.45)
            coin.center_x = random.randint(0, WIDTH)
            coin.center_y = random.randint(0, HEIGHT)
            self.coin_list.append(coin)


    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.coin_list.draw()
        arcade.draw_text(str(self.score), WIDTH /2, HEIGHT  /2, arcade.color.BLACK, 70)
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.player.center_x = x
        self.player.center_y = y

    def update(self, delta_time):
        touched_coins = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in touched_coins:
            self.score += 1
            coin.kill()

        if len(self.coin_list) == 0:
            self.setup()

game = Game()
game.setup()
arcade.run()
