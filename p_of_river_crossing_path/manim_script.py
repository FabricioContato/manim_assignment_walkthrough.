from manim import *
from util import *

class p_of_river_crossing_path(Scene):
    def construct(self):
        
        # Get the width and height of the camera frame
        frame_width = config.frame_width
        frame_height = config.frame_height

        # Create a rectangle with the exact dimensions of the frame
        full_screen_rect = Rectangle(width=frame_width, height=frame_height, color=BLUE, stroke_width=20)

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

        label_A = Text("a").scale(2).move_to(left_rect.get_center())

        right_rect = Rectangle(height=height, width=width, color=GREEN, fill_opacity=1)
        right_rect.to_edge(RIGHT, buff=0)

        label_B = Text("b").scale(2).move_to(right_rect.get_center())

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

        bridge1 = VGroup(bridge1, Text("1").move_to(bridge1.get_center()))
        bridge2 = VGroup(bridge2, Text("2").move_to(bridge2.get_center()))
        bridge3 = VGroup(bridge3, Text("3").move_to(bridge3.get_center()))
        bridge4 = VGroup(bridge4, Text("4").move_to(bridge4.get_center()))
        bridge5 = VGroup(bridge5, Text("5").move_to(bridge5.get_center()))

        river_bridge_group = VGroup(full_screen_rect, label_A, label_B, dif, bridge1, bridge2, bridge3, bridge4, bridge5)
        
        def animate_bridge_state(bridge_number_list):

            animation_list = []

            for bridge_number in bridge_number_list:

                opacity = 1 if bridge_number > 0 else 0.4

                if abs(bridge_number) == 1:
                    animation_list.append(bridge1.animate.set_opacity(opacity))
                elif abs(bridge_number) == 2:
                    animation_list.append(bridge2.animate.set_opacity(opacity))
                elif abs(bridge_number) == 3:
                    animation_list.append(bridge3.animate.set_opacity(opacity))
                elif abs(bridge_number) == 4:
                    animation_list.append(bridge4.animate.set_opacity(opacity))
                elif abs(bridge_number) == 5:
                    animation_list.append(bridge5.animate.set_opacity(opacity))

            return AnimationGroup(animation_list)
            
        def animate_bridge_highlight(bridge_number_list):

            animation_list = []

            for bridge_number in bridge_number_list:

                color = YELLOW if bridge_number > 0 else LIGHT_BROWN

                if abs(bridge_number) == 1:
                    animation_list.append(bridge1.animate.set_stroke(color))
                elif abs(bridge_number) == 2:
                    animation_list.append(bridge2.animate.set_stroke(color))
                elif abs(bridge_number) == 3:
                    animation_list.append(bridge3.animate.set_stroke(color))
                elif abs(bridge_number) == 4:
                    animation_list.append(bridge4.animate.set_stroke(color))
                elif abs(bridge_number) == 5:
                    animation_list.append(bridge5.animate.set_stroke(color))

            return AnimationGroup(animation_list)

        
        question_text = Text("""
                             You would like to go from point (a) to point (b) 
                             There are 5 bridges on different branches of the river
                             Bridge i is open with probability Pi, i=1,2,3,4,5. 
                             Let A be the event that there is a path from (a) to (b)
                             and let Bk be the event that kth bridge is open.
                                     a) Find P(A)      b) Find P(B3|A)
                             """).scale(0.6).to_edge(UP,buff=0)
        
        river_bridge_group.scale(0.6).next_to(question_text, DOWN, buff=0.2)
        
                
        self.play(Write(question_text))
        self.play(Write(river_bridge_group))

        methods = Text("""
            Find P(A) by:
            1th : Inclusion-Exclusion Principle
            2th : Finding P of the complement of A
            3th : By finding P of each oucome of A
             """).scale(0.6).move_to(question_text.get_center())
        
        self.play(FadeOut(question_text), Write(methods))


        #we  can spot some simple paths that allow gooing from a to b

        vertices = ["1", "4"]
        edges = [("1", "4")]
        layout = {"1": LEFT, "4": RIGHT}

        _1_to_4 = Graph(vertices=vertices, edges=edges, layout=layout, labels=True)
        
        vertices = ["1", "3", "5"]
        edges = [("1", "3"), ("3", "5")]
        layout = {"1": LEFT, "3": RIGHT, "5": 3*RIGHT}
        
        _1_to_3_to_5 =  Graph(vertices=vertices, edges=edges, layout=layout, labels=True)
        #_1_to_3_to_5.move_to(methods.get_center())

        vertices = ["2", "5"]
        edges = [("2", "5")]
        layout = {"2": LEFT, "5": RIGHT}
        
        _2_to_5 =  Graph(vertices=vertices, edges=edges, layout=layout, labels=True)
        #_2_to_5.move_to(methods.get_center())

        vertices = ["2", "3", "4"]
        edges = [("2", "3"), ("3", "4")]
        layout = {"2": LEFT, "3": RIGHT, "4": 3*RIGHT}
        
        _2_to_3_to_4 =  Graph(vertices=vertices, edges=edges, layout=layout, labels=True)
        #_2_to_3_to_4.move_to(methods.get_center())

        graph_group = VGroup(_1_to_4, _1_to_3_to_5, _2_to_5, _2_to_3_to_4).arrange(RIGHT)
        graph_group.scale(0.8).move_to(methods.get_center())

        

        self.play(FadeOut(methods), Write(graph_group))

        self.play(animate_bridge_highlight([1,4]))

        self.play(animate_bridge_state([-2,-3,-5]))
        self.play(animate_bridge_state([2,-3,-5]))
        self.play(animate_bridge_state([-2,3,-5]))
        self.play(animate_bridge_state([-2,-3,5]))
        self.play(animate_bridge_state([2,3,-5]))
        self.play(animate_bridge_state([-2,3,5]))
        self.play(animate_bridge_state([2,-3,5]))
        self.play(animate_bridge_state([2,3,5]))

        self.play(graph_group.animate.to_edge(UP))

        b_intersection_sub_sets = VGroup(
        MathTex("B_{1} \cap B_{4}").next_to(_1_to_4, DOWN, buff=0.2),
        MathTex("B_{1} \cap B_{3} \cap B_{5}").next_to(_1_to_3_to_5, DOWN, buff=0.2),
        MathTex("B_{2} \cap B_{5}").next_to(_2_to_5, DOWN, buff=0.2),
        MathTex("B_{2} \cap B_{3} \cap B_{4}").next_to(_2_to_3_to_4, DOWN, buff=0.2))

        c_sub_sets = VGroup(
        MathTex("C_{1,4}").next_to(b_intersection_sub_sets[0], DOWN, buff=0.2),
        MathTex("C_{1,3,5}").next_to(b_intersection_sub_sets[1], DOWN, buff=0.2),
        MathTex("C_{2,5}").next_to(b_intersection_sub_sets[2], DOWN, buff=0.2),
        MathTex("C_{2,3,4}").next_to(b_intersection_sub_sets[3], DOWN, buff=0.2))

        self.play(Write(b_intersection_sub_sets[0]))

        self.play(animate_bridge_highlight([1,-4,3,5]))

        self.play(animate_bridge_state([-2,-4]))
        self.play(animate_bridge_state([2,-4]))
        self.play(animate_bridge_state([-2,4]))
        self.play(animate_bridge_state([2,4]))

        self.play(Write(b_intersection_sub_sets[1]))

        self.play(Write(b_intersection_sub_sets[2:]))

        self.play(Write(c_sub_sets))

        self.play(FadeOut(b_intersection_sub_sets))

        self.play(c_sub_sets.animate.move_to(b_intersection_sub_sets.get_center()))

        a_equal_untion_group = VGroup(MathTex("A ="), c_sub_sets[0].copy(), MathTex("\cup").next_to(c_sub_sets[0], RIGHT, buff=.2), c_sub_sets[1].copy(), MathTex("\cup").next_to(c_sub_sets[1], RIGHT, buff=.2) , c_sub_sets[2].copy(), MathTex("\cup").next_to(c_sub_sets[2], RIGHT, buff=.2), c_sub_sets[3].copy())
        a_equal_untion_group.arrange(RIGHT, buff=.2 ,center=False)
        a_equal_untion_group.next_to(b_intersection_sub_sets, DOWN, buff=.2)

        self.play(FadeIn(a_equal_untion_group))

        self.play(FadeOut(a_equal_untion_group))


        p_of_a_group_1 = VGroup(
            MathTex("P(A) = P(C_{1,4}) + P(C_{1,3,5}) + P(C_{2,5}) + P(C_{2,3,4})"),
            MathTex("- P(C_{1,4} \cap C_{1,3,5}) - P(C_{1,4} \cap C_{2,5}) - P(C_{1,4} \cap C_{2,3,4})"),
            MathTex("- P(C_{1,3,5} \cap C_{2,5}) - P(C_{1,3,5} \cap C_{2,3,4}) - P(C_{2,5} \cap C_{2,3,4})"),
            MathTex("+ P(C_{1,4} \cap C_{1,3,5} \cap C_{2,5}) + P(C_{1,4} \cap C_{1,3,5} \cap C_{2,3,4})"),
            MathTex("+ P(C_{1,4} \cap C_{2,5} \cap C_{2,3,4}) + P(C_{1,3,5} \cap C_{2,5} \cap C_{2,3,4})"),
            MathTex("- P(C_{1,4} \cap C_{1,3,5} \cap C_{2,5} \cap C_{2,3,4})")
        ).arrange(DOWN, buff=.2, aligned_edge=LEFT).next_to(c_sub_sets, DOWN, buff=.2)
        
        
        #p_of_a_initial_part = MathTex("P(A) = P(C_{1,4}) + P(C_{1,3,5}) + P(C_{2,5}) + P(C_{2,3,4})")
        #p_of_a_initial_part.move_to(a_equal_untion_group.get_center())
        
        self.play(Write(p_of_a_group_1[0]))

        self.play(FadeOut(river_bridge_group), FadeOut(graph_group), FadeOut(c_sub_sets))

        #p_of_a_second_part =  MathTex("- P(C_{1,4} \cap C_{1,3,5}) - P(C_{1,4} \cap C_{2,5}) - P(C_{1,4} \cap C_{2,3,4}) - P(C_{1,3,5} \cap C_{2,5})")
        #p_of_a_second_part.scale(.7)
        #p_of_a_second_part.next_to(p_of_a_initial_part, DOWN, aligned_edge=RIGHT)

        self.add(p_of_a_group_1[1:2+1])
        self.add(p_of_a_group_1[3:4+1])
        self.add(p_of_a_group_1[-1])

        c14_inter_c235_1 = MathTex("C_{1,4} \cap C_{1,3,5} =", " B_{1} \cap B_{4} \; \; \; \cap \; \; \; B_{1} \cap B_{3} \cap B_{5}")
        c14_inter_c235_1.next_to(p_of_a_group_1, DOWN, buff=1)

        self.play(Write(c14_inter_c235_1))
        
        c14_inter_c235_2 = MathTex("C_{1,4} \cap C_{1,3,5} =", " B_{1} \cap B_{3} \cap B_{4} \cap B_{5}")
        c14_inter_c235_2.move_to(c14_inter_c235_1.get_center()).align_to(c14_inter_c235_1, LEFT)

        self.play(TransformMatchingTex(c14_inter_c235_1, c14_inter_c235_2))

        c14_inter_c235_3 = MathTex("C_{1,4} \cap C_{1,3,5} =", " C_{1,3,4,5}")
        c14_inter_c235_3.move_to(c14_inter_c235_2.get_center()).align_to(c14_inter_c235_2, LEFT)

        self.play(TransformMatchingTex(c14_inter_c235_2, c14_inter_c235_3))

        p_of_a_group_2 = VGroup(
            MathTex("P(A) = P(C_{1,4}) + P(C_{1,3,5}) + P(C_{2,5}) + P(C_{2,3,4})"),
            MathTex("- P(C_{1,3,4,5}) - P(C_{1,2,4,5}) - P(C_{1,2,3,4})"),
            MathTex("- P(C_{1,2,3,5}) - P(C_{1,2,3,4,5}) - P(C_{2,3,4,5})"),
            MathTex("+ P(C_{1,2,3,4,5}) + P(C_{1,2,3,4,5})"),
            MathTex("+ P(C_{1,2,3,4,5}) + P(C_{1,2,3,4,5})"),
            MathTex("- P(C_{1,2,3,4,5})")
        ).arrange(DOWN, buff=.2, aligned_edge=LEFT).next_to(c_sub_sets, DOWN, buff=.2)

        self.play(FadeOut(p_of_a_group_1))
        self.play(FadeIn(p_of_a_group_2))

        p_of_a_group_3 = VGroup(
            MathTex("P(A) = P(C_{1,4}) + P(C_{1,3,5}) + P(C_{2,5}) + P(C_{2,3,4})"),
            MathTex("- P(C_{1,3,4,5}) - P(C_{1,2,4,5}) - P(C_{1,2,3,4})"),
            MathTex("- P(C_{1,2,3,5}) - P(C_{2,3,4,5})"),
            MathTex("+ 2 \cdot P(C_{1,2,3,4,5})")
        ).arrange(DOWN, buff=.2, aligned_edge=LEFT).next_to(c_sub_sets, DOWN, buff=.2)

        self.play(FadeOut(p_of_a_group_2))
        self.play(FadeIn(p_of_a_group_3))


        self.wait(5)