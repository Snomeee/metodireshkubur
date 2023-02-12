from manim import *


class Method1(Scene):
    def construct(self):
        cub = MathTex("ax^3 + bx^2 + cx + 0 = 0").shift(UP * 3)
        quadro = MathTex("x(ax^2+bx+c)=0").shift(UP * 2)
        self.play(Write(cub, run_time=5))
        self.play(Write(quadro, run_time=5))

        line = Line(start=UP, end=DOWN * 3.5).shift(LEFT * 2.5)
        self.play(Create(line))

        first = MathTex("x=0").next_to(line, LEFT).shift(UP * 2).shift(LEFT * 0.5)
        second_1 = MathTex("ax^2+bx+c=0").next_to(line, RIGHT).shift(UP * 2).shift(RIGHT * 0.5)
        second_2 = MathTex("x_{1}=\\frac{-b-\\sqrt{b^2-4ac}}{2a}").next_to(line, RIGHT).shift(UP * 0.7).shift(
            RIGHT * 0.5)
        second_3 = MathTex("x_{2}=\\frac{-b+\\sqrt{b^2-4ac}}{2a}").next_to(line, RIGHT).shift(DOWN * 0.9).shift(
            RIGHT * 0.5)

        self.play(Write(first, run_time=5))
        self.play(Write(second_1, run_time=5))
        self.play(Write(second_2, run_time=5))
        self.play(Write(second_3, run_time=5))
        self.wait()
        self.play(Indicate(first, scale_factor=1.05, run_time=2),
                  Indicate(second_2, scale_factor=1.05, run_time=2),
                  Indicate(second_3, scale_factor=1.05, run_time=2))
        self.play(FadeOut(cub), FadeOut(quadro), FadeOut(first), FadeOut(second_1), FadeOut(second_2), FadeOut(second_3), FadeOut(line))
        self.wait()
