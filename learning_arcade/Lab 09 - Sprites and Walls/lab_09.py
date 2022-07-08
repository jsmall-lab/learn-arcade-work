import arcade


WIDTH = 700
HEIGHT = 700
TITLE = 'Sprites and Walls'

PLAYER_SCAILING = 0.8
BOX_SCAILING = 0.5
MOVEMENT_SPEED = 3


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.player = None
        self.wall_list = None
        self.set_mouse_visible(False)
        self.physics_engine = None
   


    def setup(self):
        self.player =arcade.Sprite('character.png-1.png.png', PLAYER_SCAILING)
        self.player.center_y = 100
        self.player.center_x = WIDTH/2
        self.wall_list = arcade.SpriteList()

        box_cords = [[400, 500], [470, 500], [400, 570], [470, 570]]

        for coord in box_cords:
            wall = arcade.Sprite(":resources:images/tiles/boxcrate_double.png", BOX_SCAILING)
            wall.center_x = coord[0]
            wall.center_y = coord[1]
            self.wall_list.append(wall)
        for i in range(13):
            wall = arcade.Sprite(":resources:images/tiles/boxcrate_double.png", BOX_SCAILING)
            wall.center_x = i * 64 + 32
            wall.center_y = 32 
            self.wall_list.append(wall)
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.wall_list.draw()


    def update(self, delta_time):
        self.physics_engine.update()
        self.player.update()
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        if key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        if key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0


game = Game()
game.setup()
arcade.run() 
