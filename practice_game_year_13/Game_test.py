from pickle import TRUE
import arcade

WIDTH = 1600
HEIGHT = 800
TITLE = "test"

CHARACTER_SCAILING = 2
PLAYER_ACCELERATION = 0.05
PLAYER_DEACCELERATION = 0.02
PLAYER_CHANGE_ANGLE_SPEED = 3

class TestGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)

        arcade.set_background_color(arcade.color.BLACK)

        self.player_sprite = None

        self.player_speed = None

        self.accelerating_x = None
        self.accelerating_y = None

    def setup(self):
        
        self.player_sprite = arcade.Sprite("practice_game_year_13/stuff/main_character.png.png", CHARACTER_SCAILING)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 400

        self.player_speed = 0
        self.accelerating_up = False
        self.accelerating_down = False
        self.accelerating_left = False
        self.accelerating_right = False
        self.moving = False

    def on_draw(self):
        self.clear()

        self.player_sprite.draw()

    def update(self, delta_time):
        self.player_sprite.update()

        if self.accelerating_right == True:
            self.player_sprite.change_x += PLAYER_ACCELERATION
        if self.accelerating_left == True:
            self.player_sprite.change_x -= PLAYER_ACCELERATION
        if self.accelerating_up == True:
            self.player_sprite.change_y += PLAYER_ACCELERATION
        if self.accelerating_down == True:
            self.player_sprite.change_y -= PLAYER_ACCELERATION
        if self.moving == False:
            if self.player_sprite.change_x > 0:
                self.player_sprite.change_x -= PLAYER_DEACCELERATION
            elif self.player_sprite.change_x < 0:
                self.player_sprite.change_x += PLAYER_DEACCELERATION
            if self.player_sprite.change_y > 0:
                self.player_sprite.change_y -= PLAYER_DEACCELERATION
            elif self.player_sprite.change_y < 0:
                self.player_sprite.change_y += PLAYER_DEACCELERATION
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.accelerating_up = True
            self.moving = True
        if key == arcade.key.S:
            self.accelerating_down = True
            self.moving = True
        if key == arcade.key.D:
            self.accelerating_right = True
            self.moving = True
        if key == arcade.key.A:
            self.accelerating_left = True
            self.moving = True
        if key == arcade.key.LEFT:
            self.player_sprite.change_angle = PLAYER_CHANGE_ANGLE_SPEED
        if key == arcade.key.RIGHT:
            self.player_sprite.change_angle = -PLAYER_CHANGE_ANGLE_SPEED

    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.W:
            self.accelerating_up = False
            self.moving = False
        if key == arcade.key.S:
            self.accelerating_down = False
            self.moving = False
        if key == arcade.key.D:
            self.accelerating_right = False
            self.moving = False
        if key == arcade.key.A:
            self.accelerating_left = False
            self.moving = False
        if key == arcade.key.LEFT:
            self.player_sprite.change_angle -= PLAYER_CHANGE_ANGLE_SPEED
        if key == arcade.key.RIGHT:
            self.player_sprite.change_angle -= -PLAYER_CHANGE_ANGLE_SPEED
def main():
    window = TestGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()