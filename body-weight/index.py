# Биеийн жингээ хянах, зохицуулах аргууд

from calendar import c
import math
import pathlib
from tkinter import Image
from manim import *


class ModifiedText(Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.set_color(BLACK)


class Introduction(Scene):
    def construct(self):
        self.authors = ["Дөлгөөн", "Мишээл", "Бөртэ", "Бишрэл"]
        # self.camera.background_color = WHITE

        text = ModifiedText(
            "Биеийн жингээ хянах, зохицуулах аргууд").shift(UP*2.5)

        credits = VGroup()

        credits_header = ModifiedText(
            "Багийн гишүүд", font_size=32).shift(UP/2)

        credits.add(credits_header)

        for i, author in enumerate(self.authors):
            credits.add(ModifiedText(author, font_size=28).shift(
                np.array((0, -i/2, 0))))

        for i, (prev_author, curr_author) in enumerate(zip(credits.submobjects, credits.submobjects[1:])):
            if not curr_author:
                break

            curr_author.align_to(prev_author, LEFT)

        credits_header.align_to(credits.submobjects[1], LEFT)

        credits.move_to([np.array((-4.35, 1, 0))]).shift(DOWN)

        image = ImageMobject("scale.png").move_to(
            np.array((4.75, 0, 0))).align_to(text, RIGHT)
        self.play(Write(text, run_time=2))
        self.play(FadeIn(image))
        self.wait(1)

        self.play(Write(credits, run_time=5))
        self.wait(2)

class BMI(Scene):
    def construct(self):
        pass

class MeasuringHeight(Scene):
    def construct(self):
        pass

class Exercises(Scene):
    def construct(self):
        pass