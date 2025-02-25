from manim import *
from util import *

class n_plus1_heads_fair_and_unfair_coin(Scene):
    def construct(self):
        question_text = Text("""
                             A box contains two coins: 
                             a regular coin and one fake two-headed coin (P(H)=1). 
                             I choose a coin at random and toss it n times. 
                             If the first n coin tosses result in heads, 
                             what is the probability that the (n+1)th coin toss will also result in heads?""").scale(.5)
        
        p_of_fcoin_unfcoin =  MathTex(r"P(F_{c})= P(F_{c}^c) = \frac{1}{2}")

        p_of_n_plus1th_heads = MathTex(r"P(Hn+1) = P(Hn+1|F_{c}) \cdot P(F_{c}) +  P(Hn+1|F_{c}^c) \cdot P(F_{c}^c)")

        meaning_of_sets_Fc_Fcc = VGroup(
                            VGroup(MathTex(r"F_{c} :"),Text("Fair coin")).arrange(RIGHT, buff=0.2),
                            VGroup(MathTex(r"F_{c}^c :"),Text("two-headed coin (not fair coin)")).arrange(RIGHT, buff=0.2)
                            ).scale(0.7).arrange(DOWN, buff=0.2)
        
        meaning_of_sets_hnplus_hn = VGroup(
                            VGroup(MathTex(r"H_{n+1th} :"),Text("Set of outcomes with heads on the n+1 th toss")).arrange(RIGHT, buff=0.2),
                            VGroup(MathTex(r"H_{n} :"),Text("Set of outcomes with heads on the n firt tosses")).arrange(RIGHT, buff=0.2)
                            ).scale(0.7).arrange(DOWN, buff=0.2)
        
        #test = MathTex(r"\frac{", r"x", r"}",r"{T}")

        n_plus1_heads_example = MathTex(r" \frac{?}{1^{th}} \; \; \frac{?}{2^{th}}\; \; \bullet\bullet\bullet \; \; \frac{?}{n^{th}}  \; \;  \frac{H}{(n+1)^{th}}")
        n_heads_example = MathTex(r" \frac{H}{1^{th}} \; \; \frac{H}{2^{th}}\; \; \bullet\bullet\bullet \; \; \frac{H}{n^{th}}  \; \;  \frac{?}{(n+1)^{th}}")
        all_heads_example = MathTex(r" \frac{H}{1^{th}} \; \; \frac{H}{2^{th}}\; \; \bullet\bullet\bullet \; \; \frac{H}{n^{th}}  \; \;  \frac{H}{(n+1)^{th}}")
        
        the_question_wants1 = MathTex(r"P(H_{n+1th} | H_{n})=", "?")
        the_question_wants2 = MathTex(r"P(H_{n+1th} | H_{n})=", r" \frac{P(H_{n} | H_{n+1th}) \cdot P(H_{n+1th})}{P(H_{n})}")
        the_question_wants3 = MathTex(r"P(H_{n+1th} | H_{n})=", r"\frac{P(H_{n} \cap H_{n+1th} )}{P(H_{n})}")
        the_question_wants4 = MathTex(r"P(H_{n+1th} | H_{n})=", r" \frac{\frac{1}{2} \cdot ((\frac{1}{2})^{n+1} + 1)}{P(H_{n})}")
        the_question_wants5 = MathTex(r"P(H_{n+1th} | H_{n})=", r" \frac{\frac{1}{2} \cdot ((\frac{1}{2})^{n+1} + 1)}{\frac{1}{2} \cdot ((\frac{1}{2})^{n} + 1)}")
        the_question_wants6 = MathTex(r"P(H_{n+1th} | H_{n})=", r" \frac{(\frac{1}{2})^{n+1} + 1}{(\frac{1}{2})^{n} + 1}")
        the_question_wants7 = MathTex(r"P(H_{n+1th} | H_{n})=", r" \frac{(2^{-1})^{n+1} + 1}{(2^{-1})^{n} + 1}")
        the_question_wants8 = MathTex(r"P(H_{n+1th} | H_{n})=", r" \frac{(2)^{-n-1} + 1}{(2)^{-n} + 1}")
        the_question_wants9 = MathTex(r"P(H_{n+1th} | H_{n})=", r" \frac{(2)^{-n-1} + 1}{(2)^{-n} + 1} \cdot \frac{2^{n}}{2^{n}")
        the_question_wants10 = MathTex(r"P(H_{n+1th} | H_{n})=", r" \frac{(2)^{-1} + 2^{n}}{1 + 2^{n}}")

        p_of_n_plus1_heads = MathTex(r"P(H_{n+1})=", r"P(H_{n+1} | F_{c}) \cdot P(F_{c}) + P(H_{n+1} | F_{c}^c) \cdot P(F_{c}^c)")

        s_set = VGroup(Square(side_length=5), MathTex(r"S").scale(1.3))
        s_set[-1].next_to(s_set[0],direction=LEFT, buff=0, aligned_edge=UP).shift(RIGHT * s_set[-1].width).scale(1/1.3)
        hn_set = VGroup(Circle(radius=1, color=RED, fill_opacity=0), MathTex(r"H_{n}"))
        hn1th_set = VGroup(Circle(radius=1, color=GREEN, fill_opacity=0), MathTex(r"P(H_{n+1th})").scale(.7))
        VGroup(hn_set, hn1th_set).arrange(direction=DOWN, buff=-.5)
        venn_diagram = VGroup(s_set, hn_set, hn1th_set)

        intersenction_set = Intersection(hn_set[0], hn1th_set[0], color=ORANGE, fill_opacity=0) #MathTex(r"Hm").scale(0.7)

        aux_sqrs = VGroup(Square(side_length=10),Square(side_length=10)).arrange(direction=RIGHT, buff=0)

        fcoin_intersection_part = Intersection(intersenction_set, aux_sqrs[0], color=BLUE, fill_opacity=1)
        nfcoin_intersection_part = Intersection(intersenction_set, aux_sqrs[1], color=PURPLE, fill_opacity=1)
        fcoin_hn_part = Intersection(hn_set[0], aux_sqrs[0], color=BLUE, fill_opacity=1).set_opacity(0)
        nfcoin_hn_part = Intersection(hn_set[0], aux_sqrs[1], color=PURPLE, fill_opacity=1).set_opacity(0)

        

        #VGroup(venn_diagram, fcoin_hn_part, nfcoin_hn_part).to_edge(LEFT, buff=0)
        #venn_diagram.center()

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text="""Our question states the following
                  A box contains two coins: 
                  a regular coin and one fake two-headed coin. 
                  I choose a coin at random and toss it n times. 
                  If the first n coin tosses result in heads, 
                  what is the probability that the n + 1 coin toss will also result in heads?""",
            cue_word="following",
            file_name="introduction",
            replace_older_file=False,
            sync=False )

        self.wait(cue_time)
        self.play(Write(question_text), run_time=remaning_time_after_cue)

        self.wait(0.6)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """Now, let's see what our question asks for.
                     We must find the probability of heads in the n plus 1 toss given that the n previus results are heads 
                     """,
            cue_word="probability",
            file_name="what_the_question_wants",
            replace_older_file=False,
            sync=False
                                            )

        self.wait(cue_time)
        self.play(question_text.animate.to_edge(UP))
        self.play(Write(the_question_wants1), run_time=remaning_time_after_cue)

        self.wait(0.5)

        meaning_of_sets_hnplus_hn.next_to(the_question_wants1, DOWN, buff=0.4)
        n_plus1_heads_example.next_to(meaning_of_sets_hnplus_hn, DOWN, buff=0.7)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= "H n plus 1 is the set of outcomes with heads in the n plus 1 toss" ,
            cue_word="set",
            file_name="H_n_plus_1_is_the_set",
            replace_older_file=False,
            sync=False
                                            )
        
        self.wait(cue_time)
        self.play(Write(meaning_of_sets_hnplus_hn[0]), Write(n_plus1_heads_example))

        self.wait(1.2)

        n_heads_example.move_to(n_plus1_heads_example.get_center())

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= "H n  is the set of outcomes with heads in the first n tosses" ,
            cue_word="set",
            file_name="H_n_is_the_set",
            replace_older_file=False,
            sync=False
                                            )
        
        self.play(FadeOut(n_plus1_heads_example), run_time=cue_time)
        self.play(
            Write(meaning_of_sets_hnplus_hn[1]),  
            Write(n_heads_example)
            )

        self.wait(1.5)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= "Thanks to Bayes' Theorem, we have the following" ,
            cue_word="Theorem",
            file_name="Bayesian_theorem",
            replace_older_file=False,
            sync=False
                                            )
        
        self.wait(cue_time)
        self.play(
            FadeOut(meaning_of_sets_hnplus_hn),
            FadeOut(n_heads_example),
            TransformMatchingTex(the_question_wants1, the_question_wants2),
            run_time=remaning_time_after_cue
            )
        
        self.wait(1.2)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= "Let's work with the intersection form of the numerator." ,
            cue_word="intersection",
            file_name="intersection_form_of_the_numerator",
            replace_older_file=False,
            sync=False
                                            )
        
        self.wait(cue_time)
        self.play(TransformMatchingTex(the_question_wants2, the_question_wants3))

        all_heads_example.next_to(the_question_wants3, DOWN, buff=0.5)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """This intersection can be interpreted as the set where all n plus 1 tosses are heads.
                   """ ,
            cue_word="all",
            file_name="intersection_can_be_interpreted",
            replace_older_file=False,
            sync=False
                                            )
        
        self.wait(cue_time)
        self.play(
            the_question_wants3[0].animate.set_opacity(0.25),
            the_question_wants3[1][0:2].animate.set_opacity(0.25),
            the_question_wants3[1][11:].animate.set_opacity(0.25),
            Write(all_heads_example),
            run_time=remaning_time_after_cue
            )
        
        self.wait(1.5)

        #meaning_of_sets_Fc_Fcc.next_to(all_heads_example, DOWN, buff=0.3)
        meaning_of_sets_Fc_Fcc.to_edge(DOWN, buff=0)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """But if I ask you the probability of n plus 1 Heads.
                     You may answer that:
                     It depends on the coin we are using.
                     The fair coin, or the double heads coin
                   """ ,
            cue_word="answer that",
            file_name="the_coin_we_are_using",
            replace_older_file=False,
            sync=False
                                            )

        self.wait(cue_time)
        self.play(Write(meaning_of_sets_Fc_Fcc), run_time=remaning_time_after_cue)

        self.wait(2)

        VGroup(
            venn_diagram, 
            intersenction_set,
            fcoin_intersection_part,
            nfcoin_intersection_part,
            fcoin_hn_part,
            nfcoin_hn_part
            ).next_to(meaning_of_sets_Fc_Fcc, UP, buff=-.2)
        
        VGroup(
            venn_diagram, 
            intersenction_set,
            fcoin_intersection_part,
            nfcoin_intersection_part,
            fcoin_hn_part,
            nfcoin_hn_part
            ).scale(0.8)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """Let's take a look at a venn diagram
                   """ ,
            cue_word="look",
            file_name="venn_diagram",
            replace_older_file=False,
            sync=False
                                            )
        
        self.wait(cue_time)
        self.play(
            FadeOut(all_heads_example),
            the_question_wants3[0].animate.set_opacity(0),
            the_question_wants3[1][0:2].animate.set_opacity(0),
            the_question_wants3[1][11:].animate.set_opacity(0)
            )
        self.play(the_question_wants3.animate.to_edge(RIGHT))
        self.play(Write(venn_diagram))

#the_question_wants3.animate.move_to(all_heads_example.get_center())
        
        self.wait(2)

        self.play(Write(intersenction_set), the_question_wants3.animate.set_color(ORANGE))

        self.play(Write(fcoin_intersection_part), meaning_of_sets_Fc_Fcc[0].animate.set_color(BLUE))
        self.play(Write(nfcoin_intersection_part), meaning_of_sets_Fc_Fcc[1].animate.set_color(PURPLE))

        venn_diagram.add(
            intersenction_set,
            fcoin_intersection_part,
            nfcoin_intersection_part,
            fcoin_hn_part,
            nfcoin_hn_part
            )

        self.play(venn_diagram.animate.to_edge(LEFT, buff=0))

        hn_inter_hnplus1 = MathTex(r"P(H_{n} \cap H_{n+1th})", "=", r"P(H_{n} \cap H_{n+1th} \cap F_{c})", "+", r"P(H_{n} \cap H_{n+1th} \cap F_{c}^c)")
        hn_inter_hnplus1.scale(0.7).next_to(venn_diagram, RIGHT, buff=0.2)

        self.play(Write(hn_inter_hnplus1), FadeOut(the_question_wants3))

        hn_inter_hnplus1_eq_hall =  MathTex(r"H_{n} \cap H_{n+1th} = H_{all}")
        hn_inter_hnplus1_eq_hall.next_to(hn_inter_hnplus1, UP, buff=1, aligned_edge=LEFT)
        
        self.play(Write(hn_inter_hnplus1_eq_hall))

        hall = MathTex(r"P(H_{all})", "=", r"P(H_{all} \cap F_{c})", "+", r"P(H_{all} \cap F_{c}^c)")
        hall.next_to(venn_diagram, RIGHT, buff=0.2)

        self.play(TransformMatchingTex(hn_inter_hnplus1, hall))

        hall2 = MathTex(r"P(H_{all})", "=", r"P(H_{all} | F_{c}) \cdot P(F_{c})", "+", r"P(H_{all} | F_{c}^c) \cdot P(F_{c}^c)")
        hall2.scale(0.9).next_to(venn_diagram, RIGHT, buff=0.2)
        self.play(TransformMatchingTex(hall,hall2))

        p_of_hall_given_fc = MathTex(r"P(H_{all} | F_{c})=", r"(\frac{1}{2})^{n+1}")
        p_of_hall_given_fcc = MathTex(r"P(H_{all} | F_{c}^c)=", "1")
        p_of_hall_given_group = VGroup(p_of_hall_given_fc, p_of_hall_given_fcc).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        p_of_hall_given_group.scale(0.85)

        p_of_fcoin_unfcoin.scale(0.85)
        p_of_fcoin_unfcoin.next_to(hall2, DOWN, buff=0.3, aligned_edge=LEFT)
        

        p_of_hall_given_group.next_to(p_of_fcoin_unfcoin, RIGHT, buff=2 , aligned_edge=UP)

        p_of_fcoin_unfcoin.next_to(p_of_hall_given_group, LEFT, buff=2 )

        self.play(Write(p_of_fcoin_unfcoin))


        self.play(Write(p_of_hall_given_group[0][0]))

        self.play(Write(p_of_hall_given_group[0][1]))

        self.play(Write(p_of_hall_given_group[1][0]))

        self.play(Write(p_of_hall_given_group[1][1]))
        

        hall3 = MathTex(r"P(H_{all})", "=", r"(\frac{1}{2})^{n+1} \cdot \frac{1}{2}", "+", r"1 \cdot \frac{1}{2}")
        hall3.move_to(hall2.get_center()).align_to(hall2, LEFT)

        self.play(TransformMatchingTex(hall2, hall3))

        hall4 = MathTex(r"P(H_{all})", "=", r"\frac{1}{2} \cdot ((\frac{1}{2})^{n+1} + 1)")

        hall4.move_to(hall3.get_center()).align_to(hall3, LEFT)

        self.play(TransformMatchingTex(hall3, hall4))

        self.play(hall4.animate.scale(0.7))

        self.play(
            hall4.animate.next_to(hn_inter_hnplus1_eq_hall, RIGHT, buff=0.5),
            FadeOut(p_of_fcoin_unfcoin),
            FadeOut(p_of_hall_given_group),
            FadeOut(fcoin_intersection_part),
            FadeOut(nfcoin_intersection_part),
            FadeOut(intersenction_set))
        
        the_question_wants3.set_opacity(1).set_color(WHITE)
        the_question_wants3.next_to(venn_diagram, RIGHT, buff=0.2)

        self.play(FadeIn(the_question_wants3))

        the_question_wants4.move_to(the_question_wants3.get_center()).align_to(the_question_wants3, LEFT)

        self.play(TransformMatchingTex(the_question_wants3, the_question_wants4))

        self.play(FadeOut(hall4), FadeOut(hn_inter_hnplus1_eq_hall))

        self.play(
            the_question_wants4[0].animate.set_opacity(0.25),
            the_question_wants4[-1][:-6].animate.set_opacity(0.25))
        
        self.play(fcoin_hn_part.animate.set_opacity(1))
        self.play(nfcoin_hn_part.animate.set_opacity(1))

        self.play(FadeOut(the_question_wants4))

        p_of_hn_eq1 = MathTex("P(H_{n})", "=", r"P(H_{n} \cap F_{c}) + P(H_{n} \cap F_{c}^c)")

        p_of_hn_eq1.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)

        self.play(Write(p_of_hn_eq1))

        p_of_hn_eq2 = MathTex("P(H_{n})", "=", r"P(H_{n} | F_{c}) \cdot P(F_{c}) + P(H_{n} | F_{c}^c) \cdot P(F_{c}^c)")
        p_of_hn_eq2.scale(.9)
        p_of_hn_eq2.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)

        p_of_hn_eq3 = MathTex("P(H_{n})", "=", r"\frac{1}{2}^n \cdot \frac{1}{2} + 1 \cdot \frac{1}{2}")
        p_of_hn_eq4 = MathTex("P(H_{n})", "=", r"\frac{1}{2} \cdot (\frac{1}{2}^n + 1 )")

        self.play(TransformMatchingTex(p_of_hn_eq1, p_of_hn_eq2))

        p_of_hn_given_fc1 = MathTex(r"P(H_{n} | F_{c})=", r" 2 \cdot \frac{1}{2}^{n+1}")
        p_of_hn_given_fcc = MathTex(r"P(H_{n} | F_{c}^c)=", "1")
        p_of_hn_given_group = VGroup(p_of_hn_given_fc1, p_of_hn_given_fcc).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        p_of_hn_given_group.next_to(p_of_fcoin_unfcoin, RIGHT, buff=1.3)

        p_of_hn_given_fc2 = MathTex(r"P(H_{n} | F_{c})=", r" \frac{1}{2}^{-1} \cdot \frac{1}{2}^{n+1}")
        p_of_hn_given_fc2.move_to(p_of_hn_given_fc1.get_center()).align_to(p_of_hn_given_fc1, LEFT)
        p_of_hn_given_fc3 = MathTex(r"P(H_{n} | F_{c})=", r" \frac{1}{2}^{n}")
        p_of_hn_given_fc3.move_to(p_of_hn_given_fc1.get_center()).align_to(p_of_hn_given_fc1, LEFT)

        self.play(FadeIn(p_of_fcoin_unfcoin))

        self.play(Write(p_of_hn_given_fc1[0]))

        n_heads_example.move_to(meaning_of_sets_Fc_Fcc.get_center())

        self.play(FadeOut(meaning_of_sets_Fc_Fcc))
        self.play(FadeIn(n_heads_example))

        n_heads_outcomes_for_fc = VGroup(
            MathTex(r" \frac{H}{1^{th}} \; \; \frac{H}{2^{th}}\; \; \bullet\bullet\bullet \; \; \frac{H}{n^{th}}  \; \;  \frac{H}{(n+1)^{th}}").scale(0.5),
            MathTex(r" \frac{H}{1^{th}} \; \; \frac{H}{2^{th}}\; \; \bullet\bullet\bullet \; \; \frac{H}{n^{th}}  \; \;  \frac{T}{(n+1)^{th}}").scale(0.5)
        ).arrange(DOWN, buff=0.1).to_edge(DOWN, buff=0)

        self.play(FadeOut(n_heads_example))
        self.play(FadeIn(n_heads_outcomes_for_fc))

        self.play(Write(p_of_hn_given_fc1[1]))

        self.play(TransformMatchingTex(p_of_hn_given_fc1, p_of_hn_given_fc2))
        self.play(TransformMatchingTex(p_of_hn_given_fc2, p_of_hn_given_fc3))

        self.play(Write(p_of_hn_given_fcc[0]))

        n_heads_outcomes_for_fcc = all_heads_example
        n_heads_outcomes_for_fcc.move_to(meaning_of_sets_Fc_Fcc.get_center())

        self.play(FadeOut(n_heads_outcomes_for_fc))
        self.play(FadeIn(n_heads_example))
        self.play(TransformMatchingTex(n_heads_example, n_heads_outcomes_for_fcc))

        self.play(Write(p_of_hn_given_fcc[1]))

        self.play(FadeOut(n_heads_outcomes_for_fcc))

        p_of_hn_eq3.move_to(p_of_hn_eq2.get_center()).align_to(p_of_hn_eq2, LEFT)
        p_of_hn_eq4.move_to(p_of_hn_eq2.get_center()).align_to(p_of_hn_eq2, LEFT)

        self.play(TransformMatchingTex(p_of_hn_eq2, p_of_hn_eq3))
        self.play(TransformMatchingTex(p_of_hn_eq3, p_of_hn_eq4))

        self.play(
            FadeOut(p_of_fcoin_unfcoin),
            FadeOut(p_of_hn_given_group),
            FadeOut(p_of_hn_given_fc3),
            p_of_hn_eq4.animate.next_to(venn_diagram, RIGHT, buff=.2, aligned_edge=UP)
        )

        the_question_wants4.set_opacity(1)
        self.play(FadeIn(the_question_wants4))
        the_question_wants5.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)
        self.play(TransformMatchingTex(the_question_wants4, the_question_wants5))
        the_question_wants6.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)
        self.play(TransformMatchingTex(the_question_wants5, the_question_wants6))
        the_question_wants7.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)
        self.play(TransformMatchingTex(the_question_wants6, the_question_wants7))
        the_question_wants8.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)
        self.play(TransformMatchingTex(the_question_wants7, the_question_wants8))
        the_question_wants9.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)
        self.play(TransformMatchingTex(the_question_wants8, the_question_wants9))
        the_question_wants10.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)
        self.play(TransformMatchingTex(the_question_wants9, the_question_wants10))