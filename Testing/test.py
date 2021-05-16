import arcade


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Ball:
    ''' This manages a ball bouncing on the scree'''

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        '''Constructor.'''


        # Take the parameters of the limit function above, and create instance variables out
        self.postion_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        '''Draw the balls with the inference variables we have. '''
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        '''Code to Control the ball's movement'''

        #move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See ifthe ball hit the edge of the screen, if so change direction
        if self.position_x < self.radius:
            self.change_x *= -1
        
        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1
        
        if self.position_y < self.radius:
            self.change_y *= -1
        
        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class MyGame(arcade.Window):
    '''Window Class'''

    def __init__(self, width, height, title):

        #call the parent class init function
        super().__init__(width, height, title)

        #Create the ball
        self.ball = Ball(50, 50 , 3, 3, 15, arcade.color.AUBURN)

    def on_draw(self):
        ''' Called whenever we need to draw the window'''




    

       