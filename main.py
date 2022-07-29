import arcade
from arcade.experimental import Shadertoy
class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(width=1920, height=1080)

        self.time = 0.0
        self.reset = 0.0

        shader_file_path_1 = 'circle_1.glsl'
        shader_file_path_2 = 'explosion.glsl'
        self.shadertoy_1 = Shadertoy(size=self.get_size(), main_source=open(shader_file_path_1).read())
        self.shadertoy_2 = Shadertoy(size=self.get_size(), main_source=open(shader_file_path_2).read())
        self.bob = False


    def on_draw(self):
        
        self.pos = self.mouse['x'], self.mouse['y']
        self.color = arcade.get_three_float_color(arcade.color.LIGHT_BLUE)
        self.shadertoy_1.program['pos'] = self.pos
        self.shadertoy_1.program['color'] = self.color
        self.shadertoy_2.program['pos'] = self.pos
        self.shadertoy_1.render()
        if self.bob:
            
            self.shadertoy_2.render(time=self.time)
            #if self.reset > 1.97:
               # self.bob = False
                #self.reset = 0.0
                

        
        #self.shadertoy_1.render(time=self.time) 
        

    def on_update(self, delta_time):
        if self.bob:
            self.time += delta_time
            self.reset += delta_time
        
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.bob = True
        
        


if __name__ == "__main__":
    window = MyGame()
    window.center_window()
    arcade.run()