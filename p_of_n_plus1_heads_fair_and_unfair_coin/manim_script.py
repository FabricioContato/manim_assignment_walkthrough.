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
                            VGroup(MathTex(r"H_{n+1th} :"),Text("Set of outcomes with Heads on the (n+1)th toss.")).arrange(RIGHT, buff=0.2),
                            VGroup(MathTex(r"H_{n} :"),Text("Set of outcomes with Heads in the first n tosses.")).arrange(RIGHT, buff=0.2)
                            ).scale(0.7).arrange(DOWN, buff=0.2)

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

        intersenction_set = Intersection(hn_set[0], hn1th_set[0], color=ORANGE, fill_opacity=0)

        aux_sqrs = VGroup(Square(side_length=10),Square(side_length=10)).arrange(direction=RIGHT, buff=0)

        fcoin_intersection_part = Intersection(intersenction_set, aux_sqrs[0], color=BLUE, fill_opacity=1)
        nfcoin_intersection_part = Intersection(intersenction_set, aux_sqrs[1], color=PURPLE, fill_opacity=1)
        fcoin_hn_part = Intersection(hn_set[0], aux_sqrs[0], color=BLUE, fill_opacity=1).set_opacity(0)
        nfcoin_hn_part = Intersection(hn_set[0], aux_sqrs[1], color=PURPLE, fill_opacity=1).set_opacity(0)

        hn_inter_hnplus1 = MathTex(r"P(H_{n} \cap H_{n+1th})", "=", r"P(H_{n} \cap H_{n+1th} \cap F_{c})", "+", r"P(H_{n} \cap H_{n+1th} \cap F_{c}^c)")

        hn_inter_hnplus1_eq_hall =  MathTex(r"H_{n} \cap H_{n+1th} = H_{all}")

        hall = MathTex(r"P(H_{all})", "=", r"P(H_{all} \cap F_{c})", "+", r"P(H_{all} \cap F_{c}^c)")

        hall2 = MathTex(r"P(H_{all})", "=", r"P(H_{all} | F_{c}) \cdot P(F_{c})", "+", r"P(H_{all} | F_{c}^c) \cdot P(F_{c}^c)")

        p_of_hall_given_fc = MathTex(r"P(H_{all} | F_{c})=", r"(\frac{1}{2})^{n+1}")

        p_of_hall_given_fcc = MathTex(r"P(H_{all} | F_{c}^c)=", "1")

        p_of_hall_given_group = VGroup(p_of_hall_given_fc, p_of_hall_given_fcc).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        hall3 = MathTex(r"P(H_{all})", "=", r"(\frac{1}{2})^{n+1} \cdot \frac{1}{2}", "+", r"1 \cdot \frac{1}{2}")

        hall4 = MathTex(r"P(H_{all})", "=", r"\frac{1}{2} \cdot ((\frac{1}{2})^{n+1} + 1)")

        p_of_hn_eq1 = MathTex("P(H_{n})", "=", r"P(H_{n} \cap F_{c}) + P(H_{n} \cap F_{c}^c)")

        p_of_hn_eq2 = MathTex("P(H_{n})", "=", r"P(H_{n} | F_{c}) \cdot P(F_{c}) + P(H_{n} | F_{c}^c) \cdot P(F_{c}^c)")

        p_of_hn_eq3 = MathTex("P(H_{n})", "=", r"\frac{1}{2}^n \cdot \frac{1}{2} + 1 \cdot \frac{1}{2}")

        p_of_hn_eq4 = MathTex("P(H_{n})", "=", r"\frac{1}{2} \cdot (\frac{1}{2}^n + 1 )")

        p_of_hn_given_fc1 = MathTex(r"P(H_{n} | F_{c})=", r" 2 \cdot \frac{1}{2}^{n+1}")

        p_of_hn_given_fcc = MathTex(r"P(H_{n} | F_{c}^c)=", "1")

        p_of_hn_given_group = VGroup(p_of_hn_given_fc1, p_of_hn_given_fcc).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        p_of_hn_given_fc2 = MathTex(r"P(H_{n} | F_{c})=", r" \frac{1}{2}^{-1} \cdot \frac{1}{2}^{n+1}")

        p_of_hn_given_fc3 = MathTex(r"P(H_{n} | F_{c})=", r" \frac{1}{2}^{n}")

        n_heads_outcomes_for_fc = VGroup(
                    MathTex(r" \frac{H}{1^{th}} \; \; \frac{H}{2^{th}}\; \; \bullet\bullet\bullet \; \; \frac{H}{n^{th}}  \; \;  \frac{H}{(n+1)^{th}}").scale(0.5),
                    MathTex(r" \frac{H}{1^{th}} \; \; \frac{H}{2^{th}}\; \; \bullet\bullet\bullet \; \; \frac{H}{n^{th}}  \; \;  \frac{T}{(n+1)^{th}}").scale(0.5)
                ).arrange(DOWN, buff=0.1).to_edge(DOWN, buff=0)

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
                     We must find the probability of heads in the n plus 1 toss given that the previous n results were Heads. 
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
            text= "H n plus 1 is the set of outcomes with Heads on the n plus 1 toss." ,
            cue_word="set",
            file_name="H_n_plus_1_is_the_set",
            replace_older_file=False,
            sync=False
                                            )
        
        self.wait(cue_time)
        self.play(Write(meaning_of_sets_hnplus_hn[0]), Write(n_plus1_heads_example))

        self.wait(2)

        n_heads_example.move_to(n_plus1_heads_example.get_center())

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= "H n is the set of outcomes with Heads in the first n tosses." ,
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
            text= "Thanks to Bayes' theorem, we have the following." ,
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
            text= "Let's use the intersection form of the numerator." ,
            cue_word="intersection",
            file_name="intersection_form_of_the_numerator",
            replace_older_file=False,
            sync=False
                                            )
        
        self.wait(cue_time)
        self.play(TransformMatchingTex(the_question_wants2, the_question_wants3), run_time=remaning_time_after_cue)

        self.wait(1)

        all_heads_example.next_to(the_question_wants3, DOWN, buff=0.5)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """This intersection can be interpreted as the set where all n plus 1 tosses are Heads.
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

        meaning_of_sets_Fc_Fcc.to_edge(DOWN, buff=0)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """But if I ask you the probability of getting n plus 1 Heads
                     You may answer that:
                     it depends on the coin we are using.
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
            text= """Let's take a look at a Venn diagram
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

        self.wait(1)

        self.play(Write(intersenction_set), the_question_wants3.animate.set_color(ORANGE))

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """The orange part is our intersection.
                     Part of its outcomes comes from the fair coin.
                   """ ,
            cue_word=None,
            file_name="The_orange_part",
            replace_older_file=False,
            sync=True
            )

        self.play(Write(fcoin_intersection_part), meaning_of_sets_Fc_Fcc[0].animate.set_color(BLUE))

        self.wait(1)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """And part from the double heads coin
                   """ ,
            cue_word=None,
            file_name="from_the_double_heads_coin",
            replace_older_file=False,
            sync=True
            )

        self.play(Write(nfcoin_intersection_part), meaning_of_sets_Fc_Fcc[1].animate.set_color(PURPLE))

        self.wait(1)

        venn_diagram.add(
            intersenction_set,
            fcoin_intersection_part,
            nfcoin_intersection_part,
            fcoin_hn_part,
            nfcoin_hn_part
            )
        
        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """In other words,
                     the probability of our intersection is equal to the following equation
                   """ ,
            cue_word="intersection",
            file_name="intersection_is_equal",
            replace_older_file=False,
            sync=False
            )
        
        self.wait(cue_time)

        self.play(venn_diagram.animate.to_edge(LEFT, buff=0))

        hn_inter_hnplus1.scale(0.7).next_to(venn_diagram, RIGHT, buff=0.2)

        self.play(Write(hn_inter_hnplus1), FadeOut(the_question_wants3))

        self.wait(1.5)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """In order to simplify our notation,
                     let's call our intersection H all
                   """ ,
            cue_word="intersection",
            file_name="call_our_intersection_by_H_all",
            replace_older_file=False,
            sync=False
            )
        
        self.wait(cue_time)

        hn_inter_hnplus1_eq_hall.next_to(hn_inter_hnplus1, UP, buff=1, aligned_edge=LEFT)
        
        self.play(Write(hn_inter_hnplus1_eq_hall))

        self.wait(1.8)

        hall.next_to(venn_diagram, RIGHT, buff=0.2)

        self.play(TransformMatchingTex(hn_inter_hnplus1, hall))

        self.wait(1)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """Note that our equation can be seen as the law of total probability,
                     and as such, we can rewrite it as follows
                   """ ,
            cue_word="rewrite",
            file_name="total_probability_law",
            replace_older_file=False,
            sync=False
            )
        
        self.wait(cue_time)

        hall2.scale(0.9).next_to(venn_diagram, RIGHT, buff=0.2)
        self.play(TransformMatchingTex(hall,hall2))

        p_of_hall_given_group.scale(0.85)

        p_of_fcoin_unfcoin.scale(0.85)
        p_of_fcoin_unfcoin.next_to(hall2, DOWN, buff=0.3, aligned_edge=LEFT)

        p_of_hall_given_group.next_to(p_of_fcoin_unfcoin, RIGHT, buff=2 , aligned_edge=UP)

        p_of_fcoin_unfcoin.next_to(p_of_hall_given_group, LEFT, buff=2 )

        self.wait(2)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """Since each coin is chosen at random, 
                     their probabilities are one half.
                   """ ,
            cue_word="probabilities",
            file_name="each_coin_is_chosen_at_random",
            replace_older_file=False,
            sync=False
            )

        self.wait(cue_time)

        self.play(Write(p_of_fcoin_unfcoin))

        self.wait(1.5)

        self.play(FadeOut(meaning_of_sets_Fc_Fcc))
        self.play(Write(p_of_hall_given_group[0][0]))

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """The probability of H all given a fair coin
                     can be read as the probability of n plus 1 heads out of a fair coin
                   """ ,
            cue_word="n plus 1",
            file_name="n_plus_1_heads_out_of_a_fair_coin",
            replace_older_file=True,
            sync=False
            )

        self.wait(cue_time)

        all_heads_example.move_to(meaning_of_sets_Fc_Fcc.get_center())

        self.play(FadeIn(all_heads_example), run_time=remaning_time_after_cue)

        self.wait(2)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """
                     which is one half to the power of n plus 1.
                   """ ,
            cue_word="one half",
            file_name="the_power_of_n_plus_1",
            replace_older_file=True,
            sync=False
            )

        self.wait(cue_time)

        self.play(Write(p_of_hall_given_group[0][1], run_time=remaning_time_after_cue))

        self.wait(1.5)

        self.play(Write(p_of_hall_given_group[1][0]))

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """The probability of H all given an unfair coin 
                     can be read as the probability of n plus 1 heads out of a double heads coin,
                     which can only be 1
                   """ ,
            cue_word="which",
            file_name="n_plus_1_heads_out_of_a_double_heads_coin",
            replace_older_file=False,
            sync=False
        )

        self.wait(cue_time)

        self.play(Write(p_of_hall_given_group[1][1]), run_time=remaning_time_after_cue)
        self.play(FadeOut(all_heads_example))
        
        hall3.move_to(hall2.get_center()).align_to(hall2, LEFT)

        self.wait(1)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """Now, we can rewrite our H all equation as follows
                   """ ,
            cue_word=None,
            file_name="rewrite_our_h_all_equation",
            replace_older_file=False,
            sync=True
        )

        self.play(TransformMatchingTex(hall2, hall3))

        hall4.move_to(hall3.get_center()).align_to(hall3, LEFT)

        self.wait(1.5)

        self.play(TransformMatchingTex(hall3, hall4))

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """Let's update our main equation.
                   """ ,
            cue_word="update",
            file_name="update_our_main_equation",
            replace_older_file=False,
            sync=False
        )

        self.wait(cue_time)

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

        self.wait(1.5)
        
        self.play(TransformMatchingTex(the_question_wants3, the_question_wants4))

        self.play(FadeOut(hall4), FadeOut(hn_inter_hnplus1_eq_hall))

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """Now, let's find the probability of H n
                   """ ,
            cue_word="of",
            file_name="probability_of_H_n",
            replace_older_file=False,
            sync=False
        )

        self.wait(cue_time)

        self.play(
            the_question_wants4[0].animate.set_opacity(0.25),
            the_question_wants4[-1][:-6].animate.set_opacity(0.25))

        self.wait(2)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """Note that part of the H n outcomes comes from the fair coin.
                   """ ,
            cue_word=False,
            file_name="hn_outcomes_are_from_the_fair_coin",
            replace_older_file=False,
            sync=True
        )
        
        self.play(fcoin_hn_part.animate.set_opacity(1))

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """And part from the double heads coin
                   """ ,
            cue_word=None,
            file_name="from_the_double_heads_coin",
            replace_older_file=False,
            sync=True
            )


        self.play(nfcoin_hn_part.animate.set_opacity(1))

        self.wait(1.5)

        self.play(FadeOut(the_question_wants4))

        p_of_hn_eq1.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """In other words,
                     the probability of H n is equal to the following equation
                   """ ,
            cue_word="H n",
            file_name="In_other_words_P_of_hn",
            replace_older_file=False,
            sync=False
            )
        
        self.wait(cue_time)
        
        self.play(Write(p_of_hn_eq1), run_time=remaning_time_after_cue)

        p_of_hn_eq2.scale(.9)
        p_of_hn_eq2.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)

        self.wait(2)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """Note that our equation can be seen as the law of total probability,
                     and as such, we can rewrite it as follows:
                   """ ,
            cue_word="rewrite",
            file_name="total_probability_law",
            replace_older_file=False,
            sync=False
            )
        
        self.wait(cue_time)

        self.play(TransformMatchingTex(p_of_hn_eq1, p_of_hn_eq2))

        p_of_hn_given_group.next_to(p_of_fcoin_unfcoin, RIGHT, buff=1.3)

        p_of_hn_given_fc2.move_to(p_of_hn_given_fc1.get_center()).align_to(p_of_hn_given_fc1, LEFT)

        p_of_hn_given_fc3.move_to(p_of_hn_given_fc1.get_center()).align_to(p_of_hn_given_fc1, LEFT)

        self.wait(1.5)
        
        self.play(FadeIn(p_of_fcoin_unfcoin))

        self.wait(1.5)

        self.play(Write(p_of_hn_given_fc1[0]))

        n_heads_example.move_to(meaning_of_sets_Fc_Fcc.get_center())

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """The probability of H n given a fair coin
                     can be read as 
                     the probability of getting Heads in the first n tosses with a fair coin.
                   """ ,
            cue_word="n tosses",
            file_name="n_heads_out_of_a_fair_coin",
            replace_older_file=False,
            sync=False
            )
        
        self.wait(cue_time)

        #self.play(FadeOut(meaning_of_sets_Fc_Fcc))
        self.play(FadeIn(n_heads_example), run_time=remaning_time_after_cue)

        self.wait(2)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """The question mark on the n plus 1 coin toss can be either Heads or Tails. 
                     It means that we have 2 possible outcomes.
                   """ ,
            cue_word="2 possible",
            file_name="means_that_we_have_2",
            replace_older_file=False,
            sync=False
            )
        
        self.wait(cue_time)

        self.play(FadeOut(n_heads_example))
        self.play(FadeIn(n_heads_outcomes_for_fc))

        self.wait(1.5)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """The sum of their probabilities is the following
                   """ ,
            cue_word=None,
            file_name="sum_of_their_probabilities",
            replace_older_file=False,
            sync=True
            )

        self.play(Write(p_of_hn_given_fc1[1]))

        self.wait(2)

        self.play(TransformMatchingTex(p_of_hn_given_fc1, p_of_hn_given_fc2))

        self.wait(2)

        self.play(TransformMatchingTex(p_of_hn_given_fc2, p_of_hn_given_fc3))

        self.wait(1)

        self.play(Write(p_of_hn_given_fcc[0]))

        n_heads_outcomes_for_fcc = all_heads_example
        n_heads_outcomes_for_fcc.move_to(meaning_of_sets_Fc_Fcc.get_center())

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """The probability of H n given a double heads coin
                     can be read as 
                     the probability of getting Heads in the first n tosses with a double heads coin.
                   """ ,
            cue_word="n tosses",
            file_name="n_heads_out_of_a_unfair_coin",
            replace_older_file=False,
            sync=False
            )
        
        self.wait(cue_time)

        self.play(FadeOut(n_heads_outcomes_for_fc))
        self.play(FadeIn(n_heads_example), run_time=remaning_time_after_cue)

        self.wait(1)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """The question mark on the n plus 1 coin toss can only be Heads, 
                     revealing one possible outcome.
                   """ ,
            cue_word="Heads",
            file_name="can_only_be_Heads",
            replace_older_file=False,
            sync=False
            )
        
        self.wait(cue_time)

        self.play(TransformMatchingTex(n_heads_example, n_heads_outcomes_for_fcc))

        self.wait(remaning_time_after_cue)

        self.wait(2)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """Since a double heads coin can only show Heads, 
                     the probability of this outcome can only be 1
                   """ ,
            cue_word="only be",
            file_name="can_only_be_1",
            replace_older_file=False,
            sync=False
            )
        
        self.wait(cue_time)

        self.play(Write(p_of_hn_given_fcc[1]))

        self.play(FadeOut(n_heads_outcomes_for_fcc))

        p_of_hn_eq3.move_to(p_of_hn_eq2.get_center()).align_to(p_of_hn_eq2, LEFT)
        p_of_hn_eq4.move_to(p_of_hn_eq2.get_center()).align_to(p_of_hn_eq2, LEFT)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """Now, we can rewrite our h n equation as follows
                   """ ,
            cue_word=None,
            file_name="rewrite_our_h_n_equation",
            replace_older_file=False,
            sync=True
        )


        self.play(TransformMatchingTex(p_of_hn_eq2, p_of_hn_eq3))

        self.wait(2)

        self.play(TransformMatchingTex(p_of_hn_eq3, p_of_hn_eq4))

        self.wait(1)

        self.play(
            FadeOut(p_of_fcoin_unfcoin),
            FadeOut(p_of_hn_given_group[1]),
            FadeOut(p_of_hn_given_fc3),
            p_of_hn_eq4.animate.next_to(venn_diagram, RIGHT, buff=.2, aligned_edge=UP)
        )

        the_question_wants4.set_opacity(1)
        self.play(FadeIn(the_question_wants4))
        the_question_wants5.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)
        
        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """Let's update our main equation
                   """ ,
            cue_word=None,
            file_name="update_our_main_equation",
            replace_older_file=False,
            sync=True
        )
        
        self.play(TransformMatchingTex(the_question_wants4, the_question_wants5))
        the_question_wants6.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)

        self.wait(2)

        self.play(TransformMatchingTex(the_question_wants5, the_question_wants6), FadeOut(p_of_hn_eq4))
        the_question_wants7.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)
        
        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """One half can be written as 2 to the power of minus 1
                   """ ,
            cue_word="minus",
            file_name="written_as_2_to",
            replace_older_file=False,
            sync=False
        )

        self.wait(cue_time)
        
        self.play(TransformMatchingTex(the_question_wants6, the_question_wants7))
        the_question_wants8.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)
        
        self.wait(2)
        
        self.play(TransformMatchingTex(the_question_wants7, the_question_wants8))
        the_question_wants9.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)
        
        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """Here we have a solution,
                     but if you don't like the minus n as an exponential,
                     we can work on it a little more
                   """ ,
            cue_word=None,
            file_name="a_little_more",
            replace_older_file=False,
            sync=True
        )

        self.play(TransformMatchingTex(the_question_wants8, the_question_wants9))
        the_question_wants10.move_to(the_question_wants4.get_center()).align_to(the_question_wants4, LEFT)
        
        self.wait(2)
        
        self.play(TransformMatchingTex(the_question_wants9, the_question_wants10))

        self.wait(1)

        _, cue_time, remaning_time_after_cue = add_audio_to_video_from_text(
            scene=self,
            text= """There we have it
                   """ ,
            cue_word=None,
            file_name="end",
            replace_older_file=False,
            sync=True
        )

        self.wait(2)

