import arcade
from arcade.experimental import Shadertoy
class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(width=1920, height=1080)

        self.time = 0.0

        shader_file_path = 'circle_1.glsl'
        window_size = self.get_size()
        self.shadertoy = Shadertoy(size=self.get_size(), main_source=open(shader_file_path).read())

    def on_draw(self):
        self.shadertoy.program['pos'] = self.mouse['x'], self.mouse['y']
        self.shadertoy.program['color'] = arcade.get_three_float_color(arcade.color.LIGHT_BLUE)
        self.shadertoy.render(time=self.time)    

    def on_update(self, delta_time):
        self.time += delta_time


if __name__ == "__main__":
    MyGame()
    arcade.run()