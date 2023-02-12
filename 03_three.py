from manim import *


class Three(Scene):
    def construct(self):
        text = Paragraph("Кубическое уравнение может иметь\n от 1 до 3 корней", font_size=30, alignment="center",
                         line_spacing=1.5)
        text_2 = Paragraph("Рассмотрим методы решения\nособых типов уравнений", font_size=30, alignment="center",
                           line_spacing=1.5)
        self.play(Write(text, run_time=3))
        self.play(FadeOut(text))
        self.play(Write(text_2, run_time=3))
        self.play(FadeOut(text_2))

        text_3 = Text("Метод #1", font_size=30, t2c={'#1': BLUE}).shift(UP)
        text_4 = MathTex("d=0")
        self.play(Write(text_3, run_time=1))
        self.play(Write(text_4, run_time=1))
        self.wait(2)
        self.play(FadeOut(text_3), FadeOut(text_4))
        self.wait()
