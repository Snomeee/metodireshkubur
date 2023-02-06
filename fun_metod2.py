from manim import *


class metod_two(Scene):
    def construct(self):
        grafik = Line(), Line(DOWN,UP)
        self.add(grafik)