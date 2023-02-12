from manim import *


class One(Scene):
    def construct(self):
        title = Paragraph("Методы нахождения\nрациональных нулей полинома\nот одной переменной", font_size=40,
                          alignment="center", t2c={'рациональных нулей': BLUE}, line_spacing=1.5)
        self.play(Write(title, run_time=5))
        self.wait(3)
        self.play(FadeOut(title))
        self.wait()
