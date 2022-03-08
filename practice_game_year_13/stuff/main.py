"""
Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

CHARACTER_SCAILING = 4
TILE_SCAILING = 0.5

PLAYER_MOVEMENT_SPEED = 9
PLAYER_JUMP_SPEED = 20

GRAVITY = 1

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
    	
        self.scene = None

        self.player_sprite = None

        self.physics_engine = None

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.scene = arcade.Scene()


        self.scene.add_sprite_list("player")
        self.scene.add_sprite_list("wall", use_spatial_hash= True)

        image_source = "main_character.png.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCAILING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.scene.add_sprite("player", self.player_sprite)

        for x in range(0, 1250, 64):
            wall = arcade.Sprite("grassMid.png", TILE_SCAILING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("wall", wall)

        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("boxCrate_single.png", TILE_SCAILING)
            wall.position = coordinate
            self.scene.add_sprite("wall", wall)
        
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene.get_sprite_list("wall")
        )

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["wall"]
        )
    def on_draw(self):
        """Render the screen."""

        self.clear()
    

        self.scene.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump() or True:
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()