from manim import *

class Ex35(Scene):
    def construct(self):
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

        iw_outcomes_sample_group = VGroup(MathTex("HH"))
        aux_list = ["HH"]
        for i in range(6):
            next_letter = ("T","H")[i%2]
            aux_list = [next_letter] + aux_list
            iw_outcomes_sample_group.add(MathTex(*aux_list))

        iw_outcomes_sample_group.add(MathTex("..."))

        iw_outcomes_sample_group.arrange(direction=UP, aligned_edge=RIGHT)

        #animation_list = [outcome[-2:].animate.set_color(RED) for outcome in iw_outcomes_sample_group[1:-1:2]]

        p_of_iw_outcomes_sample_group = VGroup(*[MathTex("P(",outcome.get_tex_string(),")=") for outcome in iw_outcomes_sample_group[:-1]]).arrange(direction=UP, aligned_edge=RIGHT)
        
        p_of_iw_outcomes_sample_second_halth_group = VGroup()

        for outcome in iw_outcomes_sample_group[:-1]:
            if len(outcome[:]) % 2 == 1:
                p_of_iw_outcomes_sample_second_halth_group.add(MathTex(f"P(HT)^{{{ len(outcome[:-1]) // 2}}} \cdot " if  len(outcome[:-1]) > 0 else "", r" P(HH)"))
            else:
                p_of_iw_outcomes_sample_second_halth_group.add(MathTex(f"P(TH)^{{{ len(outcome[:-2]) // 2}}} \cdot " if  len(outcome[:-2]) > 0 else "", r" P(THH)"))

        p_of_iw_outcomes_sample_second_halth_group.arrange(direction=UP, aligned_edge=RIGHT)

        #self.play(Write(p_of_iw_outcomes_sample_second_halth_group))
        self.play(*[Write(outcome) for outcome in p_of_iw_outcomes_sample_second_halth_group[1::2]])