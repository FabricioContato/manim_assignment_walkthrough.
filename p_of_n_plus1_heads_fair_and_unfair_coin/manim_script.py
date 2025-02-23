from manim import *
from util import *

class n_plus1_heads_fair_and_unfair_coin(Scene):
    def construct(self):
        question_text = Text("""
                             A box contains two coins: a regular coin and one fake two-headed coin (P(H)=1). I choose a coin at random and toss it n 
                             times. If the first n
                             coin tosses result in heads, what is the probability that the (n+1)th
                             coin toss will also result in heads?""").scale(.3)
        
        p_of_fcoin_unfcoin_group =  VGroup(MathTex("P(Fc)=0.5"), MathTex("P(Fc^c)=0.5")).arrange(direction=DOWN, buff=0.2)

        p_of_n_plus1th_heads = MathTex(r"P(Hn+1) = P(Hn+1|Fc) \cdot P(Fc) +  P(Hn+1|Fc^c) \cdot P(Fc^c)")

        meaning_of_sets_Fc_Fcc = VGroup(
                            VGroup(MathTex(r"Fc :"),Text("Fair coin")).arrange(RIGHT, buff=0.2),
                            VGroup(MathTex(r"Fc^c :"),Text("two-headed coin (not fair coin)")).arrange(RIGHT, buff=0.2)
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
        the_question_wants4 = MathTex(r"P(H_{n+1th} | H_{n})=", r" \frac{P(H_{n+1})}{P(H_{n})}")

        p_of_n_plus1_heads = MathTex(r"P(H_{n+1})=", r"P(H_{n+1} | Fc) \cdot P(Fc) + P(H_{n+1} | Fc^c) \cdot P(Fc^c)")

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
        fcoin_hn_part = Intersection(hn_set[0], aux_sqrs[0], color=BLUE, fill_opacity=1)
        nfcoin_hn_part = Intersection(hn_set[0], aux_sqrs[1], color=PURPLE, fill_opacity=1)

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
            replace_older_file=True,
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
            text= "H n plus 1 is the set of heads in the n plus 1 toss" ,
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
            text= "H n  is the set of heads in the first n tosses" ,
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

        meaning_of_sets_Fc_Fcc.next_to(all_heads_example, DOWN, buff=0.3)

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
        self.play(Write(meaning_of_sets_Fc_Fcc))

        self.wait(2)

        