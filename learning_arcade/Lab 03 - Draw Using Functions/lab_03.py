import arcade 

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

#grass function
def draw_grass():
    arcade.draw_xywh_rectangle_filled(0, 0, 1000, 200, arcade.color.LIGHT_GREEN)

def draw_bear(x, y):
    #Body
    arcade.draw_ellipse_filled(400 + x, 230 + y, 80, 50, arcade.color.SIENNA, 0)
    arcade.draw_ellipse_filled(440 + x , 235 + y, 40, 15, arcade.color.SIENNA, 375)
    arcade.draw_circle_filled(455 + x, 230 + y, 20, arcade.color.SIENNA)#Head
    arcade.draw_ellipse_filled(390 + x, 200 + y, 50, 15, arcade.color.SIENNA, 90)
    arcade.draw_ellipse_filled(425 + x, 200 + y, 50, 15, arcade.color.SIENNA, 90)
    arcade.draw_circle_filled(360 + x, 230 + y, 5,  arcade.color.SIENNA)
    
    #Eyes
    arcade.draw_circle_filled(450 + x, 230 + y, 5, arcade.color.WHITE)

    #Ears
    arcade.draw_circle_filled(455 + x, 252.5 + y, 5, arcade.color.SIENNA)

def on_draw(delta_time):
    arcade.start_render()

    draw_grass()
    draw_bear(on_draw.bear1_x, -50)
    draw_bear(on_draw.bear2_x, 25)
    
  


    #Moving bear to left
    on_draw.bear1_x += 1
    on_draw.bear2_x += 2
       
#creating bear x
on_draw.bear1_x = 150
on_draw.bear2_x = 160
#main Code
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Forest")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
    

    #call_on_draw every 60th of a second
    arcade.schedule(on_draw, 1/60)
    arcade.run()

    #Finish and Run
    arcade.finish_render()
 


main()    
