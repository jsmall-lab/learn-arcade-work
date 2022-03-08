import arcade
import random

WIDTH = 700
HEIGHT = 700
TITLE = 'Shooting Game'

PLAYER_SCAILING = 1.8
COIN_SCAILING = 0.7
LAZER_SCAILING = 0.5

LAZER_SPEED = 10

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.player = None
        self.coin_list = None
        self.bullet_list = None
        self.score = 0
        self.set_mouse_visible(False)
        self.bullet = None
        
    
    def setup(self):
        self.player = arcade.Sprite('character.png-1.png.png', PLAYER_SCAILING)
        self.player.center_y = 100
        self.player.center_x = WIDTH/2
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.score = 0
        arcade.set_background_color(arcade.color.BLACK)
        for i in range(90):
            coin = arcade.Sprite('coin.png', COIN_SCAILING)
            coin.center_x = random.randint(0, WIDTH)
            coin.center_y = random.randint(200, HEIGHT)
            self.coin_list.append(coin)
    
    
    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.coin_list.draw()
        self.bullet_list.draw()
        arcade.draw_text(f'Score {self.score}', 20, HEIGHT - 20, arcade.color.WHITE)
        

    def update(self, delta_time):
        self.bullet_list.update()
        for bullet in self.bullet_list:
            touching = arcade.check_for_collision_with_list(bullet, self.coin_list)
            for coin in touching:
                self.score += 1
                coin.kill()
                bullet.kill()
            if bullet.center_y > HEIGHT + 50:
                bullet.kill()  
                print('it worked')
        
        


    def on_mouse_motion(self, x, y, dx, dy):
        self.player.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        
        bullet = arcade.Sprite('New Piskel-1.png.png', LAZER_SCAILING)
        bullet.center_x = x
        bullet.center_y = self.player.center_y
        bullet.change_y = LAZER_SPEED
        self.bullet_list.append(bullet)
        
       
        
      


    




game = Game()
game.setup()
arcade.run()

    

