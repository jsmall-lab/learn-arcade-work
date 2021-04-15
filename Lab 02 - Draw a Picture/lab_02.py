#importing arcade libary
import arcade

#open window
arcade.open_window(1000, 800, "House")

#window colour
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

#Render Start
arcade.start_render()

#House base Rectangle
arcade.draw_rectangle_filled(500, 200, 800, 400, arcade.color.GRAY_BLUE)

#base of house second colour
arcade.draw_xywh_rectangle_filled(100, 0, 800, 25, arcade.color.BLACK)

#window left side
arcade.draw_xywh_rectangle_outline(150, 200, 150, 150, arcade.color.BLACK)
arcade.draw_xywh_rectangle_filled(150, 200, 150, 150, arcade.color.LIGHT_GRAY)
arcade.draw_line(225, 200, 225, 350, arcade.color.BLACK)
arcade.draw_line(150, 275, 300, 275, arcade.color.BLACK)

#window right side
arcade.draw_xywh_rectangle_outline(700, 200, 150, 150, arcade.color.BLACK)
arcade.draw_xywh_rectangle_filled(700, 200, 150, 150, arcade.color.LIGHT_GRAY)
arcade.draw_line(775, 200, 775, 350, arcade.color.BLACK)
arcade.draw_line(700, 275, 850, 275, arcade.color.BLACK)

#door
arcade.draw_xywh_rectangle_filled(450, 0, 100, 200, arcade.color.LIGHT_BROWN)
arcade.draw_circle_filled(460, 100, 8, arcade.color.DARK_BROWN)

#outside grass
arcade.draw_xywh_rectangle_filled(0, 0, 100, 50, arcade.color.DARK_GREEN)
arcade.draw_xywh_rectangle_filled(900, 0, 100, 50, arcade.color.DARK_GREEN)

#Roof
arcade.draw_polygon_filled(((100, 400),
                          (300, 500),
                          (500, 625),
                          (700, 500),
                          (900, 400)
                          ),
                          arcade.color.TERRA_COTTA)

#sun
arcade.draw_circle_filled(900, 700, 100, arcade.color.YELLOW)






#Render Finish
arcade.finish_render()

#run
arcade.run()