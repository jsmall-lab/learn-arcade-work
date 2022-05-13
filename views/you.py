import random
import math
import arcade

WIDTH = 1600
HEIGHT = 800
TITLE = "test"

CHARACTER_SCAILING = 2

DEFAULT_DAMPNING = 1.0

PLAYER_ACCELERATION = 6000
PLAYER_DEACCELERATION = 0.02
PLAYER_CHANGE_ANGLE_SPEED = 3
PLAYER_ANGLE_DECCELERATION = 100
PLAYER_MASS = 20
PLAYER_FRICTION = 0.2
PLAYER_MAX_SPEED = 215
PLAYER_DAMPNING =0.58


METEOR_MOVEMENT_CONSTANT = 7
METEOR_MASS = 20
METEOR_FRICTION = 2.0


class TestGame(arcade.View):
    def __init__(self):
        super().__init__()

        self.player_sprite = None

        self.scene = None

        self.player_speed = None

        self.accelerating_up = None
        self.accelerating_down = None
        self.accelerating_left = None
        self.accelerating_right = None
        self.key_pressed = None
        self.moving_angle = None

        self.physics_engine = None

        self.camera = None

        self.physics_engine = None

        arcade.set_background_color(arcade.color.BLACK)

        self.setup()

    def setup(self):

        self.scene = arcade.Scene()
        self.scene.add_sprite_list("player")
        self.scene.add_sprite_list("rocks")
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=DEFAULT_DAMPNING,
                                                    gravity=(0, 0))

        self.player_bullet_list = arcade.SpriteList()

        self.camera = arcade.Camera(WIDTH, HEIGHT)

        image_source = "assets/player_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCAILING)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 400
        self.scene.add_sprite("player", self.player_sprite)

        self.player_speed = 0
        self.accelerating_up = False
        self.accelerating_down = False
        self.accelerating_left = False
        self.accelerating_right = False
        self.key_pressed = False
        self.moving_angle = False
        rock_choices = [
            "meteorGrey_tiny1.png",
            "meteorGrey_tiny2.png",
            "meteorGrey_small1.png",
            "meteorGrey_small2.png",
            "meteorGrey_med1.png",
            "meteorGrey_med2.png",
            "meteorGrey_big4.png",
            "meteorGrey_big1.png",
            "meteorGrey_big2.png",
            "meteorGrey_big3.png",
           ]
        for i in range(20):
            rock = arcade.Sprite(
                f":resources:images/space_shooter/{random.choice(rock_choices)}",
                0.5 + random.random() * 2,
                center_x = random.randint(0, WIDTH),
                center_y = random.randint(0, HEIGHT),


            )
            mass = METEOR_MASS * (rock.center_y * rock.center_y ) 
            rock.change_x = (
                random.random() * METEOR_MOVEMENT_CONSTANT
                - METEOR_MOVEMENT_CONSTANT / 2
            )
            rock.change_y = (
                random.random() * METEOR_MOVEMENT_CONSTANT
                - METEOR_MOVEMENT_CONSTANT / 2
            )
            self.scene["rocks"].append(rock)
            self.physics_engine.add_sprite(rock, mass=mass, friction=METEOR_FRICTION, elasticity=0.7)
            self.physics_engine.get_physics_object(rock).body.velocity = (random.randint(-100, 100), random.randint(-100, 100))
        self.physics_engine.add_sprite(self.player_sprite, mass=PLAYER_MASS, friction=PLAYER_FRICTION, elasticity=0.4, moment_of_inertia=math.inf, max_horizontal_velocity=PLAYER_MAX_SPEED, max_vertical_velocity=PLAYER_MAX_SPEED, damping=PLAYER_DAMPNING)




    def on_draw(self):
        self.clear()

        self.camera.use()

        self.scene.draw()

    def on_update(self, delta_time):
        # self.scene.update()

        self.center_camera()

        #Accelleration
        player_body = self.physics_engine.get_physics_object(self.player_sprite).body
        if self.accelerating_right:
            player_body.apply_force_at_world_point((PLAYER_ACCELERATION, 0), (0, 0))
        if self.accelerating_left:
            player_body.apply_force_at_world_point((-PLAYER_ACCELERATION, 0), (0, 0))
        if self.accelerating_up:
            player_body.apply_force_at_world_point((0, PLAYER_ACCELERATION), (0, 0))
        if self.accelerating_down:
            player_body.apply_force_at_world_point((0, -PLAYER_ACCELERATION), (0, 0))

        #decelleration
        print(player_body.velocity)
                                                                                                                                                             
        
        



        for rock in self.scene["rocks"]:
            if rock.center_x < 0:
                rock.center_x = WIDTH
            if rock.center_x > WIDTH:
                rock.center_x = 0
            if rock.center_y < 0:
                rock.center_y = HEIGHT
            if rock.center_y > HEIGHT:
                rock.center_y = 0

        self.physics_engine.step()

        # for rock in self.scene["rocks"]:
        # touching = arcade.check_for_collision_with_list(rock, self.scene["rocks"])

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.accelerating_up = True
        if key == arcade.key.S:
            self.accelerating_down = True

        if key == arcade.key.D:
            self.accelerating_right = True

        if key == arcade.key.A:
            self.accelerating_left = True



    def on_key_release(self, key, modifiers):
        if key == arcade.key.W:
            self.accelerating_up = False

        if key == arcade.key.S:
            self.accelerating_down = False

        if key == arcade.key.D:
            self.accelerating_right = False

        if key == arcade.key.A:
            self.accelerating_left = False


    def center_camera(self):
        screen_center_x = self.player_sprite.center_x - WIDTH / 2
        screen_center_y = self.player_sprite.center_y - HEIGHT / 2

        # if screen_center_x < 0:
        # screen_center_x = 0
        # if screen_center_y < 0:
        # screen_center_y = 0

        player_centered = screen_center_x, screen_center_y
        self.camera.move_to(player_centered)

