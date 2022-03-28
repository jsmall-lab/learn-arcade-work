import arcade

WIDTH = 1600
HEIGHT = 800
TITLE = "test"

CHARACTER_SCAILING = 2
BULLET_SCAILING = 1

PLAYER_ACCELERATION = 0.05
PLAYER_DEACCELERATION = 0.02
PLAYER_CHANGE_ANGLE_SPEED = 3
PLAYER_ANGLE_DECCELERATION = 0.03

class TestGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)



        self.player_sprite = None

        self.scene = None

        self.player_speed = None

        
        self.accelerating_up = None
        self.accelerating_down = None
        self.accelerating_left = None
        self.accelerating_right = None
        self.moving = None
        self.moving_angle = None

        self.player_bullet = None
        self.player_bullet_list = None

        arcade.set_background_color(arcade.color.BLACK)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("player")

        self.player_bullet_list = arcade.SpriteList()

        image_source = "practice_game_year_13/stuff/main_character.png.png" 
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCAILING)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 400
        self.scene.add_sprite("player", self.player_sprite)

        
        self.player_speed = 0
        self.accelerating_up = False
        self.accelerating_down = False
        self.accelerating_left = False
        self.accelerating_right = False
        self.moving = False
        self.moving_angle = False

    def on_draw(self):
        self.clear()

        self.player_sprite.draw()
        self.scene.draw()

    def update(self, delta_time):
        
        self.scene.update()

        if self.accelerating_right == True:
            self.player_sprite.change_x += PLAYER_ACCELERATION
        if self.accelerating_left == True:
            self.player_sprite.change_x -= PLAYER_ACCELERATION
        if self.accelerating_up == True:
            self.player_sprite.change_y += PLAYER_ACCELERATION
        if self.accelerating_down == True:
            self.player_sprite.change_y -= PLAYER_ACCELERATION
        if not self.moving:
            if self.player_sprite.change_x > 0:
                self.player_sprite.change_x -= PLAYER_DEACCELERATION
            elif self.player_sprite.change_x < 0:
                self.player_sprite.change_x += PLAYER_DEACCELERATION
            if self.player_sprite.change_y > 0:
                self.player_sprite.change_y -= PLAYER_DEACCELERATION
            elif self.player_sprite.change_y < 0:
                self.player_sprite.change_y += PLAYER_DEACCELERATION
        if not self.moving_angle:
            if self.player_sprite.change_angle < 0:
                self.player_sprite.change_angle += PLAYER_ANGLE_DECCELERATION
            if self.player_sprite.change_angle > 0:
                self.player_sprite.change_angle -= PLAYER_ANGLE_DECCELERATION
                

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
            self.moving_angle = True
        if key == arcade.key.RIGHT:
            self.player_sprite.change_angle = -PLAYER_CHANGE_ANGLE_SPEED
            self.moving_angle = True
        if key == arcade.key.SPACE:
            image_source = "practice_game_year_13/stuff/laser.png"
            self.bullet = arcade.Sprite(image_source, BULLET_SCAILING)
            self.bullet.center_x = (self.player_sprite.center_x + 10)
            self.bullet.center_y = self.player_sprite.center_y
            self.bullet.change_x = 3
            self.player_bullet_list.append(self.bullet)
            self.scene.add_sprite_list("bullets", self.player_bullet_list)

    
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
            self.moving_angle = False
        if key == arcade.key.RIGHT:
            self.moving_angle = False
def main():
    window = TestGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()