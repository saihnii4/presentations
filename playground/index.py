from manim_presentation import Slide
from manim import *


class Example(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)

        self.play(GrowFromCenter(circle))
        self.pause()

        self.play(FadeOut(circle))
        self.wait()


class Example2(Slide):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = 1.0
        self.f_x = lambda x: x ** 2
        self.f_prime_x = lambda x: 2*x

    def construct(self):
        axes = Axes([-10.0, 10.0, 2], [-10.0, 10.0, 2], tips=False,
                    axis_config={"include_numbers": True})

        graph = axes.plot(self.f_x, color=BLUE)

        self.play(GrowFromCenter(VGroup(axes, graph)))
        self.pause()

        f_x = MathTex('y = x^2').move_to([2, -1, 0])

        self.play(Write(f_x))

        # Some basic Calculus

        m = axes.slope_of_tangent(self.x, graph)
        y = self.f_x(self.x)

        c = y - (m*self.x)
        print(c)

        tangent_line = axes.plot(lambda x: 2*x-1, color=RED)
        self.play(GrowFromCenter(tangent_line))
        self.pause()

        tangent_intersection = Dot(axes.coords_to_point(1, 1), color=ORANGE)
        label = Text("(1, 1)", font_size=24).next_to(tangent_intersection)

        self.play(FadeIn(tangent_intersection))
        self.play(Write(label))

        self.wait()


class Example3(Slide):
    def construct(self):
        text = Text(
            "200 students record the time, t minutes, for their journey from home to school.\nThe cumulative frequency diagram shows the results.")

        self.play(FadeIn(text))
        self.pause()
