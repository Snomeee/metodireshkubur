from manim import *


class Two(Scene):
    def construct(self):
        text = Paragraph("Полином от одной переменной - это сумма мономов вида", font_size=25).shift(UP)
        polynomial_common = MathTex("P(x)=\sum_{j=0}^{n} a_{j}x^j")

        self.play(Write(text, run_time=3))
        self.play(FadeIn(polynomial_common))
        self.wait(3)
        self.play(text.animate.shift(UP*2), polynomial_common.animate.shift(UP*2))

        text_2 = Paragraph("Полином третьей степени", font_size=25)
        polynomial_3 = MathTex("P_{3}(x)=\sum_{j=0}^{3} a_{j}x^j =").shift(DOWN)
        polynomial_3_2 = MathTex("a_{0}x^0 + a_{1}x^1 + a_{2}x^2 + a_{3}x^3").shift(DOWN*2.5)
        self.play(Write(text_2, run_time=3))
        self.play(Write(polynomial_3, run_time=3))
        self.play(Write(polynomial_3_2, run_time=3))
        self.wait(2.5)

        self.play(Uncreate(text), Uncreate(polynomial_common), Uncreate(text_2), Uncreate(polynomial_3))
        self.play(polynomial_3_2.animate.shift(UP * 5.5))

        polynomial_3_3 = MathTex("d + cx^1 + bx^2 + ax^3").shift(UP*3)
        self.play(Transform(polynomial_3_2, polynomial_3_3))

        text_3 = Paragraph("Алгебраическим уравнением\nтретьей степени общего вида является", font_size=30, alignment="center").shift(UP)
        cub = MathTex("ax^3 + bx^2 + cx^1 + d = 0, a \\neq 0")
        box = SurroundingRectangle(cub, corner_radius=0.2, buff=0.3)
        text_4 = Text("Кубическое уравнение", color=YELLOW, font_size=30).shift(UP)
        self.play(Write(text_3, run_time=3))
        self.play(TransformFromCopy(polynomial_3_3, cub))
        self.play(Uncreate(polynomial_3_3), Uncreate(polynomial_3_2))
        self.play(text_3.animate.shift(UP*2))
        self.play(Create(box))
        self.play(Transform(text_3, text_4))
        self.wait(4)
        self.play(FadeOut(text_3), FadeOut(box), FadeOut(cub))
        self.wait()


