from manim import *

class Ex35(Scene):
    def construct(self):
        p_of_h_t_group = VGroup(MathTex(r"P(H)=p"), MathTex("P(T)=1-p=q")).arrange(direction=DOWN, buff=0.2, aligned_edge=LEFT)
        
        p_fh_given_Iw_1 = MathTex("P(Fh|Iw)=", "?")
        p_fh_given_Iw_2 = MathTex("P(Fh|Iw)=", r"\frac{P(Iw|Fh)\cdot P(Fh)}{P(Iw)}")
        p_fh_given_Iw_3 = MathTex("P(Fh|Iw)=", r"\frac{P(Iw\cap Fh)}{P(Iw)}")
        p_fh_given_Iw_4 = MathTex("P(Fh|Iw)=", r"\frac{p^{2}\cdot (1 - pq)^{-1}}{P(Iw)}")
        p_fh_given_Iw_5 = MathTex("P(Fh|Iw)=", r"\frac{p^{2}\cdot (1 - pq)^{-1}}{p^{2}\cdot(1 + q) \cdot (1 - pq)^{-1}}")
        p_fh_given_Iw_6 = MathTex("P(Fh|Iw)=", r"\frac{1}{1 + q}")
        p_fh_given_Iw_7 = MathTex("P(Fh|Iw)=", r"\frac{1}{1 + (1 - p)}")
        p_fh_given_Iw_8 = MathTex("P(Fh|Iw)=", r"\frac{1}{2 - p}")

        
        #self.play(Write(p_fh_given_Iw_8))