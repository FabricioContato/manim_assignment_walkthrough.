from manim import *
from util import *

class p_of_river_crossing_path(Scene):
    def construct(self):
        
        # Get the width and height of the camera frame
        frame_width = config.frame_width
        frame_height = config.frame_height

        # Create a rectangle with the exact dimensions of the frame
        full_screen_rect = Rectangle(width=frame_width, height=frame_height, color=BLUE, fill_opacity=1)

        width = int(config.frame_width * 0.4)
        height = int(config.frame_height * 0.4)

        top_rect = Rectangle(height=height, width=width, color=GREEN, fill_opacity=1)
        top_rect.to_edge(UP, buff=0)

        bot_rect = Rectangle(height=height, width=width, color=GREEN, fill_opacity=1)
        bot_rect.to_edge(DOWN, buff=0)

        width = int(config.frame_width * 0.25)
        height = int(config.frame_height * 1)

        left_rect = Rectangle(height=height, width=width, color=GREEN, fill_opacity=1)
        left_rect.to_edge(LEFT, buff=0)

        right_rect = Rectangle(height=height, width=width, color=GREEN, fill_opacity=1)
        right_rect.to_edge(RIGHT, buff=0)

        dif = Difference(full_screen_rect, top_rect)
        dif = Difference(dif, bot_rect)
        dif = Difference(dif, left_rect)
        dif = Difference(dif, right_rect, color=BLUE, fill_opacity=1)

        width = int(config.frame_width * 0.15)
        height = int(config.frame_height * 0.15)

        bridge1 = Rectangle(height=height, width=width, color=LIGHT_BROWN, fill_opacity=1) 
        #bridge1.move_to([mid(top_rect.get_x(), left_rect.get_x()), top_rect.get_y(), 0])
        
        bridge1.next_to(top_rect, LEFT, buff=-0.2)

        bridge2 = bridge1.copy()
        bridge2.next_to(bot_rect, LEFT, buff=-0.2)

        bridge4 = bridge1.copy()
        bridge4.next_to(top_rect, RIGHT, buff=-0.2)

        bridge5 = bridge1.copy()
        bridge5.next_to(bot_rect, RIGHT, buff=-0.2)

        width = int(config.frame_width * 0.10)
        height = int(config.frame_height * 0.45)

        bridge3 = Rectangle(height=height, width=width, color=LIGHT_BROWN, fill_opacity=1) 


        # Add the rectangle to the scene
        #self.add(full_screen_rect)
        #self.play(Write(full_screen_rect),
        #          Write(top_rect),
        #          Write(bot_rect),
        #          Write(left_rect),
        #          Write(right_rect),
        #            run_time=5)
        self.play(Write(dif), Write(bridge1), Write(bridge2))
        self.play(Write(bridge4), Write(bridge5), Write(bridge3))
        self.wait(5)