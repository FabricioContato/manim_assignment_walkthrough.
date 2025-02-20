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

        fh_is = VGroup(MathTex("Fh "), Text(": Heads in the first coin toss").scale(0.7)).arrange(RIGHT).next_to(p_fh_given_iw_1, DOWN)
        iw_is = VGroup(MathTex("Iw "), Text(": I won (HH observed)").scale(0.7)).arrange(RIGHT).next_to(fh_is, DOWN, buff=0.2)
        fh_iw_are = VGroup(fh_is, iw_is)

        p_iw_1 = MathTex("P(Iw)=", r"P(Iw\cap Fh)", r"+", r"P(Iw\cap Ft)")
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

        add_parallel_audioTTS_with_animation(
            scene=self,
            animation=Write(question_text),
            text= "Our question states the following",
            cue_word="states",
            file_name="introduction",
            replace_older_file=False
                                            )
        
        self.wait(0.8)

        add_parallel_audioTTS_with_animation(
            scene=self,
            animation=[question_text.animate.to_edge(UP), Write(p_of_h_t_group)],
            text= "Before anything else, let's define the probability of Heads and Tails.",
            cue_word="probability",
            file_name="p_of_heads_tails",
            replace_older_file=False
                                            )
        
        self.play(p_of_h_t_group.animate.to_edge(DL))

        add_parallel_audioTTS_with_animation(
            scene=self,
            animation=Write(p_fh_given_iw_1),
            text= """Now, let's see what our question asks for.
                     We must find the probability of getting Heads on the first coin toss given that I won.""",
            cue_word="probability",
            file_name="what_the_question_wants",
            replace_older_file=False
                                            )

        self.wait(0.8)

        add_parallel_audioTTS_with_animation(
            scene=self,
            animation=Write(fh_iw_are),
            text= "Let's call Heads on the first coin toss F h, and I win as I w",
            cue_word="F h",
            file_name="what_fh_iw_are",
            replace_older_file=False
                                            )
        
        self.wait(0.8)
        
        add_parallel_audioTTS_with_animation(
            scene=self,
            animation=[FadeOut(fh_iw_are), TransformMatchingTex(p_fh_given_iw_1, p_fh_given_iw_2)],
            text= "Thanks to Bayes' Theorem, we have the following",
            cue_word="Theorem",
            file_name="Bayesian_theorem",
            replace_older_file=False
                                            )
        
        self.wait(0.8)
        
        add_parallel_audioTTS_with_animation(
            scene=self,
            animation=TransformMatchingTex(p_fh_given_iw_2, p_fh_given_iw_3),
            text= "Let's work with the intersection form of the numerator.",
            cue_word="intersection",
            file_name="intersection_form_of_the_numerator",
            replace_older_file=False
                                            )
        
        self.wait(0.8)

        add_parallel_audioTTS_with_animation(
            scene=self,
            animation=p_fh_given_iw_3.animate.to_edge(DR),
            text= "This intersection accounts for each outcome where I win and the first coin is Heads. But first, let's take a look at a sample of outcomes where I win.",
            cue_word="sample",
            file_name="intersection_accounts_for",
            replace_older_file=False
                                            )
        
        self.wait(0.8)

        add_parallel_audioTTS_with_animation(
            scene=self,
            animation=Write(iw_outcomes_sample_group[0]),
            text= "The first outcome where I win is the simplest one, consisting of only two Heads.",
            cue_word="two",
            file_name="first_outcome_where_I_win",
            replace_older_file=False
                                            )

        self.wait(0.8)

        add_parallel_audioTTS_with_animation(
            scene=self,
            animation=Write(iw_outcomes_sample_group[1]),
            text= """The second outcome where I win consists of three coin tosses. It must start with Tails, since it is not possible for a sequence to have three consecutive Heads.
                     Note that it is not part of the intersection we saw earlier, since it does not start with Heads.""",
            cue_word="Tails",
            file_name="second_outcome_where_I_win",
            replace_older_file=False
                                            )
        
        self.wait(0.8)

        add_parallel_audioTTS_with_animation(
            scene=self,
            animation=Write(iw_outcomes_sample_group[2]),
            text= """The third outcome where I win consists of four coin tosses. It must start with Heads, since two Tails couldn't be observed if I won.
                     Note that it start with Heads. So it is part of the intersection we saw earlier .""",
            cue_word="Heads",
            file_name="third_outcome_where_I_win",
            replace_older_file=False
                                            )
        
        self.wait(1.2)

        add_parallel_audioTTS_with_animation(
            scene=self,
            animation=Write(iw_outcomes_sample_group[3:]),
            text= """We can continue following this pattern as long as we want. There are an infinite number of possible outcomes where I win.""",
            cue_word="infinite",
            file_name="infinit_possible_outcomes",
            replace_older_file=False
                                            )

        self.wait(0.8)

        add_parallel_audioTTS_with_animation(
            scene=self,
            animation=AnimationGroup([outcome.animate.set_color(RED) for outcome in iw_outcomes_sample_group[0:-1:2]], run_time=1),
            text= """Let's highlight the outcomes that belong to the intersection we want. These are the ones that start with H. """,
            cue_word="start",
            file_name="outcomes_that_start_with_H",
            replace_older_file=False
                                            )

        self.wait(1)

        p_of_iw_outcomes_sample_group.set_color(BLACK)

        self.play(VGroup(iw_outcomes_sample_group, p_of_iw_outcomes_sample_group).animate.center())

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self, 
            text="""The probability of the intersection is the sum of the probabilities of each of its outcome.""",
            cue_word="outcome",
            file_name="sum_of_the_probability1",
            replace_older_file=False,
            sync=True
            )
        #self.wait(cue_time)
        self.play(*[Write(outcome.set_color(WHITE)) for outcome in p_of_iw_outcomes_sample_group[0::2]])

        self.wait(0.8)

        [outcome_r.next_to(outcome_l, RIGHT, buff=0.2) for outcome_l, outcome_r in zip(p_of_iw_outcomes_sample_group[:], p_of_iw_outcomes_sample_second_halth_group[:])]

        p_of_iw_outcomes_sample_second_halth_group.set_color(BLACK)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""We can't consider all the infinite probabilities here, but let's see if these probabilities follow any pattern.""",
            file_name='any_pattern1',
            cue_word="follow",
            replace_older_file=False,
            sync=False
        )

        self.wait(cue_time)
        self.play(VGroup(iw_outcomes_sample_group, p_of_iw_outcomes_sample_group, p_of_iw_outcomes_sample_second_halth_group).animate.center(), run_time=remaning_time_after_cue/2 )
        self.play(*[Write(outcome.set_color(WHITE)) for outcome in p_of_iw_outcomes_sample_second_halth_group[::2]], run_time=remaning_time_after_cue/2)

        self.wait(1)

        p_of_fh_intersection_iw.set_color(BLACK).next_to(p_of_iw_outcomes_sample_second_halth_group, RIGHT, aligned_edge=UP, buff=0.3)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""Note that it follows an infinite geometric sequence. Therefore, to sum all of them, we just need a simple formula.""",
            file_name="infinite_geometric_sequence",
            cue_word="them",
            replace_older_file=False,
            sync=False
        )
        self.wait(cue_time)
        self.play(FadeOut(iw_outcomes_sample_group), run_time=remaning_time_after_cue/3)
        self.play(VGroup(p_of_iw_outcomes_sample_group, p_of_iw_outcomes_sample_second_halth_group, p_of_fh_intersection_iw).animate.center(), run_time=remaning_time_after_cue/3)
        self.play(Write(p_of_fh_intersection_iw.set_color(WHITE)), run_time=remaning_time_after_cue/3)

        self.wait(1)

        p_of_hh_ht_group.next_to(p_of_fh_intersection_iw, DOWN, aligned_edge=LEFT)

        p_of_fh_intersection_iw_2.move_to(p_of_fh_intersection_iw.get_center()).align_to(p_of_fh_intersection_iw, direction=LEFT)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""a 1.  is the first term of the sequence. Here, it is P of H H""",
            file_name="p_of_hh",
            cue_word="it",
            replace_older_file=False,
            sync=False
        )

        self.wait(cue_time)
        self.play(Write(p_of_hh_ht_group[0]), run_time=remaning_time_after_cue)

        self.wait(1)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""r.  the ratio of the sequence. Here, it is P of H T""",
            file_name="p_of_ht",
            cue_word="it",
            replace_older_file=False,
            sync=False
        )

        self.wait(cue_time)
        self.play(Write(p_of_hh_ht_group[1]), run_time=remaning_time_after_cue)

        self.wait(1)

        self.play(TransformMatchingTex(p_of_fh_intersection_iw, p_of_fh_intersection_iw_2))

        self.play(FadeOut(VGroup(p_of_iw_outcomes_sample_group, p_of_iw_outcomes_sample_second_halth_group, p_of_hh_ht_group)))

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""Now, let's update our main equation.""",
            file_name="update_our_main_equation",
            cue_word="update",
            replace_older_file=False,
            sync=False
        )

        self.wait(cue_time)
        self.play(p_fh_given_iw_3.animate.center(), run_time=remaning_time_after_cue)
        self.play(TransformMatchingTex(p_fh_given_iw_3, p_fh_given_iw_4))

        self.wait(1)

        iw_outcomes_sample_group.center()

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""In order to finish our main equation. We just need P of I win. 
                    So, let's take a second look at our sample of outcomes.""",
            file_name="to_finish_our_main_equation",
            cue_word="look",
            replace_older_file=False,
            sync=False
        )
        self.wait(cue_time)
        self.play(p_fh_given_iw_4.animate.to_edge(DR), p_of_fh_intersection_iw_2.animate.next_to(p_of_h_t_group, direction=UP, buff=0.1))
        self.play(VGroup(p_of_fh_intersection_iw_2, p_of_h_t_group).animate.scale(.5))
        self.play(VGroup(p_of_fh_intersection_iw_2, p_of_h_t_group).animate.to_edge(DL))
        self.play(Write(iw_outcomes_sample_group))

        self.wait(1)

        p_iw_1.scale(0.6).next_to(iw_outcomes_sample_group, RIGHT)

        red_into_white_animations = [outcome.animate.set_color(WHITE) for outcome in iw_outcomes_sample_group[:-1:2]]
        white_into_blue_animations = [outcome.animate.set_color(BLUE) for outcome in iw_outcomes_sample_group[1:-1:2]]

        p_iw_1[-3].set_color(RED)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""Note that to find P of I win. we need to sum the probabilities of each of these infinite outcomes.
                    We already have the sum of those that start with Heads. We still need the sum of those that start with Tails.""",
            file_name="We_still_need_the_sum_of",
            cue_word="have",
            replace_older_file=False,
            sync=False
        )
        self.wait(cue_time)
        self.play(Write(p_iw_1), run_time=remaning_time_after_cue/2)
        self.play(*red_into_white_animations,*white_into_blue_animations, p_iw_1[-3].animate.set_color(WHITE) ,p_iw_1[-1].animate.set_color(BLUE), run_time=remaning_time_after_cue/2)

        self.wait(1)

        self.play(FadeOut(p_iw_1))
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

        self.wait(1)

        p_of_ft_intersection_iw_1.next_to(p_of_iw_outcomes_sample_second_halth_group, RIGHT, aligned_edge=UP, buff=0.5).set_color(BLACK)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""Note that they are also an infinite geometric sequence.""",
            file_name="they_also_are_a_infinite_geometric",
            cue_word="geometric",
            replace_older_file=False,
            sync=False
        )
        self.wait(cue_time)
        self.play(FadeOut(iw_outcomes_sample_group))
        self.play(VGroup(p_of_iw_outcomes_sample_group, p_of_iw_outcomes_sample_second_halth_group, p_of_ft_intersection_iw_1).animate.center())
        self.play(Write(p_of_ft_intersection_iw_1.set_color(WHITE)))

        self.wait(1)

        p_of_thh_th_group.next_to(p_of_ft_intersection_iw_1, DOWN, aligned_edge=LEFT, buff=.5)


        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""a 1.  is the first term of the sequence. Here, it is P of T H H""",
            file_name="P_of_THH",
            cue_word="it",
            replace_older_file=False,
            sync=False
        )
        self.wait(cue_time)
        self.play(Write(p_of_thh_th_group[0]), run_time=remaning_time_after_cue)

        self.wait(1)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""r.  is the ratio of the sequence. Here, it is P of T H""",
            file_name="P_of_TH",
            cue_word="it",
            replace_older_file=False,
            sync=False
        )
        self.wait(cue_time)
        self.play(Write(p_of_thh_th_group[1]), run_time=remaning_time_after_cue)

        self.wait(1)

        p_of_ft_intersection_iw_2.move_to(p_of_ft_intersection_iw_1.get_center())
        self.play(TransformMatchingTex(p_of_ft_intersection_iw_1, p_of_ft_intersection_iw_2))
        self.play(FadeOut(VGroup(p_of_iw_outcomes_sample_group, p_of_iw_outcomes_sample_second_halth_group, p_of_thh_th_group)))

        self.wait(1)

        p_iw_1.set_color(WHITE).scale(1/.6).center()

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""Now we can find the P of I win""",
            file_name="we_can_find_the_P_of_I_win",
            cue_word="P",
            replace_older_file=False,
            sync=False
        )
        self.wait(cue_time)

        self.play(Write(p_iw_1))

        self.play(p_of_fh_intersection_iw_2.animate.scale(1/.5))

        self.play(p_of_fh_intersection_iw_2.animate.next_to(p_of_ft_intersection_iw_2, LEFT))

        self.wait(1)

        self.play(TransformMatchingTex(p_iw_1, p_iw_2))

        self.wait(1)

        self.play(TransformMatchingTex(p_iw_2, p_iw_3))

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""With that we can complete our main equation""",
            file_name="we_can_complete_our_main_equation",
            cue_word=None,
            replace_older_file=False,
            sync=True
        )
        #self.wait(cue_time)

        self.play(
            FadeOut(p_of_ft_intersection_iw_2),
            FadeOut(p_of_fh_intersection_iw_2),
            p_iw_3.animate.next_to(Point(), direction=DOWN, buff=1.5),
            p_fh_given_iw_4.animate.center())
        
        self.wait(1)

        self.play(TransformMatchingTex(p_fh_given_iw_4, p_fh_given_iw_5))
        self.play(FadeOut(p_iw_3))

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""Let's get rid of common factors.""",
            file_name="common_factors",
            cue_word=None,
            replace_older_file=False,
            sync=True
        )

        self.play(TransformMatchingTex(p_fh_given_iw_5, p_fh_given_iw_6))

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""Remember that q, is 1 minus p""",
            file_name="Remanber_that_q",
            cue_word=None,
            replace_older_file=False,
            sync=True
        )

        self.play(TransformMatchingTex(p_fh_given_iw_6, p_fh_given_iw_7))

        self.wait(1)

        self.play(TransformMatchingTex(p_fh_given_iw_7, p_fh_given_iw_8))

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""There we have it""",
            file_name="There_we_have_it",
            cue_word=None,
            replace_older_file=False,
            sync=True
        )
        self.wait(1)