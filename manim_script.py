from manim import *
from util import *

class Ex35(Scene):
    def construct(self):

        # creating graphic objects

        question_text = Text(text="""
        You and I play the following game: 
        I toss a coin repeatedly. The coin is unfair and P(H)=p.
        The game ends the first time that two consecutive heads (HH) or two consecutive tails (TT) are observed.
        I win if (HH) is observed and you win if (TT) is observed.
        Given that I won the game, find the probability that the first coin toss resulted in head?"""
                            ).scale(.4)

        p_of_h_t_group = VGroup(MathTex(r"P(H)=p"), MathTex("P(T)=1-p=q")).arrange(direction=DOWN, buff=0.2, aligned_edge=LEFT)
        
        p_fh_given_iw_1 = MathTex("P(Fh|Iw)=", "?")
        p_fh_given_iw_2 = MathTex("P(Fh|Iw)=", r"\frac{P(Iw|Fh)\cdot P(Fh)}{P(Iw)}")
        p_fh_given_iw_3 = MathTex("P(Fh|Iw)=", r"\frac{P(Iw\cap Fh)}{P(Iw)}")
        p_fh_given_iw_4 = MathTex("P(Fh|Iw)=", r"\frac{p^{2}\cdot (1 - pq)^{-1}}{P(Iw)}")
        p_fh_given_iw_5 = MathTex("P(Fh|Iw)=", r"\frac{p^{2}\cdot (1 - pq)^{-1}}{p^{2}\cdot(1 + q) \cdot (1 - pq)^{-1}}")
        p_fh_given_iw_6 = MathTex("P(Fh|Iw)=", r"\frac{1}{1 + q}")
        p_fh_given_iw_7 = MathTex("P(Fh|Iw)=", r"\frac{1}{1 + (1 - p)}")
        p_fh_given_iw_8 = MathTex("P(Fh|Iw)=", r"\frac{1}{2 - p}")

        p_iw_1 = MathTex("P(Iw)=", r"P(Iw\cap Fh)+P(Iw\cap Ft)")
        p_iw_2 = MathTex("P(Iw)=", r"p^{2}\cdot (1 - pq)^{-1} + p^{2}q \cdot (1 - pq)^{-1}")
        p_iw_3 = MathTex("P(Iw)=", r"p^{2}\cdot(1 + q) \cdot (1 - pq)^{-1}")

        iw_outcomes_sample_group = VGroup(MathTex("HH").scale(.8))
        aux_list = ["HH"]
        for i in range(6):
            next_letter = ("T","H")[i%2]
            aux_list = [next_letter] + aux_list
            iw_outcomes_sample_group.add(MathTex(*aux_list).scale(.8))

        iw_outcomes_sample_group.add(MathTex("..."))

        iw_outcomes_sample_group.arrange(direction=UP, aligned_edge=RIGHT)

        p_of_iw_outcomes_sample_group = VGroup(*[MathTex("P(",outcome.get_tex_string(),")=").scale(.8).next_to(outcome, RIGHT, buff=0.2) for outcome in iw_outcomes_sample_group[:-1]])
        
        [outcome.align_to(p_of_iw_outcomes_sample_group[-1], direction=RIGHT) for outcome in p_of_iw_outcomes_sample_group[:-1]]

        p_of_iw_outcomes_sample_second_halth_group = VGroup()

        for outcome in iw_outcomes_sample_group[:-1]:
            if len(outcome[:]) % 2 == 1:
                p_of_iw_outcomes_sample_second_halth_group.add(MathTex(f"P(HT)^{{{ len(outcome[:-1]) // 2}}} \\cdot " if  len(outcome[:-1]) > 0 else "", r" P(HH)").scale(.8))
            else:
                p_of_iw_outcomes_sample_second_halth_group.add(MathTex(f"P(TH)^{{{ len(outcome[:-2]) // 2}}} \\cdot " if  len(outcome[:-2]) > 0 else "", r" P(THH)").scale(.8))

        p_of_fh_intersection_iw = MathTex(r"P(Iw\cap Fh)=", r"\frac{a1}{1-r}")

        p_of_fh_intersection_iw_2 =  MathTex(r"P(Iw\cap Fh)=", r"\frac{p^{2}}{1-pq}")

        p_of_ft_intersection_iw_1 = MathTex(r"P(Iw\cap Ft)=", r"\frac{a1}{1-r}")

        p_of_ft_intersection_iw_2 =  MathTex(r"P(Iw\cap Ft)=", r"\frac{p^{2}q}{1-pq}")

        p_of_hh_ht_group = VGroup(MathTex("P(HH)=p^{2}"), MathTex("P(HT)=pq")).arrange(direction=DOWN, aligned_edge=LEFT)

        p_of_thh_th_group = VGroup(MathTex("P(THH)=p^{2}q"), MathTex("P(TH)=pq")).arrange(direction=DOWN, aligned_edge=LEFT)

        # Animating

        #introduction
        add_parallel_audioTTS_with_animation(
            scene=self,
            animation=Write(question_text),
            text= "Our question states the following",
            cue_word="states",
            file_name="introduction",
            replace_older_file=False
                                            )

        #self.play(Write(question_text))

        self.play(question_text.animate.to_edge(UP))

        self.play(Write(p_of_h_t_group))

        self.play(p_of_h_t_group.animate.to_edge(DL))

        self.play(Write(p_fh_given_iw_1))

        self.play(TransformMatchingTex(p_fh_given_iw_1, p_fh_given_iw_2))

        self.play(TransformMatchingTex(p_fh_given_iw_2, p_fh_given_iw_3))

        self.play(p_fh_given_iw_3.animate.to_edge(DR))

        self.play(Write(iw_outcomes_sample_group))

        self.play(*[outcome.animate.set_color(RED) for outcome in iw_outcomes_sample_group[0:-1:2]])

        p_of_iw_outcomes_sample_group.set_color(BLACK)

        self.play(VGroup(iw_outcomes_sample_group, p_of_iw_outcomes_sample_group).animate.center())

        self.play(*[Write(outcome.set_color(WHITE)) for outcome in p_of_iw_outcomes_sample_group[0::2]])

        [outcome_r.next_to(outcome_l, RIGHT, buff=0.2) for outcome_l, outcome_r in zip(p_of_iw_outcomes_sample_group[:], p_of_iw_outcomes_sample_second_halth_group[:])]

        p_of_iw_outcomes_sample_second_halth_group.set_color(BLACK)

        self.play(VGroup(iw_outcomes_sample_group, p_of_iw_outcomes_sample_group, p_of_iw_outcomes_sample_second_halth_group).animate.center())

        self.play([Write(outcome.set_color(WHITE)) for outcome in p_of_iw_outcomes_sample_second_halth_group[::2]])

        self.play(FadeOut(iw_outcomes_sample_group))

        p_of_fh_intersection_iw.set_color(BLACK).next_to(p_of_iw_outcomes_sample_second_halth_group, RIGHT, aligned_edge=UP, buff=0.3)

        self.play(VGroup(p_of_iw_outcomes_sample_group, p_of_iw_outcomes_sample_second_halth_group, p_of_fh_intersection_iw).animate.center())

        self.play(Write(p_of_fh_intersection_iw.set_color(WHITE)))

        p_of_hh_ht_group.next_to(p_of_fh_intersection_iw, DOWN, aligned_edge=LEFT)

        p_of_fh_intersection_iw_2.move_to(p_of_fh_intersection_iw.get_center()).align_to(p_of_fh_intersection_iw, direction=LEFT)

        self.play(Write(p_of_hh_ht_group))

        self.play(TransformMatchingTex(p_of_fh_intersection_iw, p_of_fh_intersection_iw_2))

        self.play(FadeOut(VGroup(p_of_iw_outcomes_sample_group, p_of_iw_outcomes_sample_second_halth_group, p_of_hh_ht_group)))

        self.play(p_fh_given_iw_3.animate.center())

        self.play(TransformMatchingTex(p_fh_given_iw_3, p_fh_given_iw_4))

        self.play(p_fh_given_iw_4.animate.to_edge(DR), p_of_fh_intersection_iw_2.animate.next_to(p_of_h_t_group, direction=UP, buff=0.1))

        self.play(VGroup(p_of_fh_intersection_iw_2, p_of_h_t_group).animate.scale(.5))

        self.play(VGroup(p_of_fh_intersection_iw_2, p_of_h_t_group).animate.to_edge(DL))

        iw_outcomes_sample_group.center()

        self.play(Write(iw_outcomes_sample_group))

        p_iw_1.scale(0.6).next_to(iw_outcomes_sample_group, RIGHT)

        self.play(Write(p_iw_1))

        self.play(FadeOut(p_iw_1))

        red_into_white_animations = [outcome.animate.set_color(WHITE) for outcome in iw_outcomes_sample_group[:-1:2]]
        white_into_blue_animations = [outcome.animate.set_color(BLUE) for outcome in iw_outcomes_sample_group[1:-1:2]]

        self.play(*red_into_white_animations,*white_into_blue_animations)

        [p_of_iw_outcomes_sample_group[-1 - i].next_to(iw_outcomes_sample_group[-2 - i], RIGHT, buff=.2) for i in range(7)]

        [outcome.align_to(p_of_iw_outcomes_sample_group[-1], RIGHT) for outcome in p_of_iw_outcomes_sample_group[:-1]]

        p_of_iw_outcomes_sample_group.set_color(BLACK)

        self.play(VGroup(iw_outcomes_sample_group, p_of_iw_outcomes_sample_group).animate.center())

        self.play(*[Write(outcome.set_color(WHITE)) for outcome in p_of_iw_outcomes_sample_group[1::2]])

        [p_of_iw_outcomes_sample_second_halth_group[-1 - i].next_to(p_of_iw_outcomes_sample_group[-1 - i], RIGHT, buff=.2) for i in range(7)]

        [outcome.align_to(p_of_iw_outcomes_sample_second_halth_group[-1], LEFT) for outcome in p_of_iw_outcomes_sample_second_halth_group[:-1]]

        p_of_iw_outcomes_sample_second_halth_group.set_color(BLACK)

        self.play(VGroup(iw_outcomes_sample_group, p_of_iw_outcomes_sample_group, p_of_iw_outcomes_sample_second_halth_group).animate.center())

        self.play(*[Write(outcome.set_color(WHITE)) for outcome in p_of_iw_outcomes_sample_second_halth_group[1::2]])

        self.play(FadeOut(iw_outcomes_sample_group))

        p_of_ft_intersection_iw_1.next_to(p_of_iw_outcomes_sample_second_halth_group, RIGHT, aligned_edge=UP, buff=0.5).set_color(BLACK)
        
        self.play(VGroup(p_of_iw_outcomes_sample_group, p_of_iw_outcomes_sample_second_halth_group, p_of_ft_intersection_iw_1).animate.center())

        self.play(Write(p_of_ft_intersection_iw_1.set_color(WHITE)))

        p_of_thh_th_group.next_to(p_of_ft_intersection_iw_1, DOWN, aligned_edge=LEFT, buff=.5)

        self.play(Write(p_of_thh_th_group))

        p_of_ft_intersection_iw_2.move_to(p_of_ft_intersection_iw_1.get_center())

        self.play(TransformMatchingTex(p_of_ft_intersection_iw_1, p_of_ft_intersection_iw_2))

        self.play(FadeOut(VGroup(p_of_iw_outcomes_sample_group, p_of_iw_outcomes_sample_second_halth_group, p_of_thh_th_group)))

        p_iw_1.scale(1/.6).center()

        self.play(Write(p_iw_1))

        self.play(p_of_fh_intersection_iw_2.animate.scale(1/.5))

        self.play(p_of_fh_intersection_iw_2.animate.next_to(p_of_ft_intersection_iw_2, LEFT))

        self.play(TransformMatchingTex(p_iw_1, p_iw_2))

        self.play(TransformMatchingTex(p_iw_2, p_iw_3))

        self.play(
            FadeOut(p_of_ft_intersection_iw_2),
            FadeOut(p_of_fh_intersection_iw_2),
            p_iw_3.animate.next_to(Point(), direction=DOWN, buff=1.5),
            p_fh_given_iw_4.animate.center())

        self.play(TransformMatchingTex(p_fh_given_iw_4, p_fh_given_iw_5))

        self.play(TransformMatchingTex(p_fh_given_iw_5, p_fh_given_iw_6))

        self.play(TransformMatchingTex(p_fh_given_iw_6, p_fh_given_iw_7))

        self.play(TransformMatchingTex(p_fh_given_iw_7, p_fh_given_iw_8))