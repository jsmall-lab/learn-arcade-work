import arcade 

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

#grass function
def draw_grass():
    arcade.draw_xywh_rectangle_filled(0, 0, 1000, 200, arcade.color.LIGHT_GREEN)

def bear():
    #Body
    arcade.draw_ellipse_filled(400, 230, 80, 50, arcade.color.SIENNA, 0)
    arcade.draw_ellipse_filled(440, 235, 40, 15, arcade.color.SIENNA, 375)
    arcade.draw_circle_filled(455, 230, 20, arcade.color.SIENNA)
    arcade.draw_ellipse_filled(390, 200, 50, 15, arcade.color.SIENNA, 90 )
    arcade.draw_ellipse_filled(425, 200, 50, 15, arcade.color.SIENNA, 90 )
    
    #Eyes
    
#main Code
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Forest")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
    arcade.start_render()

    draw_grass()
    
    bear()

    #Finish and Run
    arcade.finish_render()
    arcade.run()

main()    
