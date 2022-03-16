# Биеийн жингээ хянах, зохицуулах аргууд

from calendar import c
from curses import COLOR_YELLOW
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
        definition_scene = VGroup()

        text = ModifiedText("BMI гэж юу вэ?", color=YELLOW)
        text.move_to((text.width-self.camera.frame_width/2, 0, 0)).shift(UP*2)
        print(self.camera.frame_width)

        explanation = Tex(
            """\parbox{7cm}{According to the CDC, the Body Mass Index of a person is their weight in kilograms divided by the square of height in meters. A high BMI suggests high body fatness.}""")
        explanation.align_to(text, LEFT).shift(RIGHT/2)

        definition_scene.add(text, explanation)

        # too lazy to shift every sub-element to the left
        definition_scene.shift(LEFT/2)

        self.play(Write(text))
        self.wait(2)

        self.play(Write(explanation, run_time=10))
        self.wait(2)

        self.play(FadeOut(definition_scene))
        self.wait(2)

        formula_scene = VGroup()

        bmi_formula = MathTex("BMI = \frac{m}{h^2}")
        header = ModifiedText("BMI-ийн томьёо юу вэ?", color=YELLOW)

        formula_scene.add(bmi_formula, header)

        self.play(Write(header))
        self.play(Write(formula_scene))


class MeasuringHeight(Scene):
    def construct(self):
        self.instructions = ["Take off most of your clothes", "Calibrate the scale", "Stand still on the scale for 3 seconds", "Use an accurate scale", "Place the scale against a flat surface",
                             "Place yourself on the scale, ensuring that your eye is directly perpendicular to the wall", " Хүүхдийн бие толгойн ар дагз, далны шонтон, өгзөг, шилбэ, өсгий гэсэн 5 цэгээр хананд тулсан байх ёстой"]

        text = ModifiedText("Steps to measure your height")
        text.move_to((text.width-self.camera.frame_width/2, 0, 0)).shift(UP*2)
        print(self.camera.frame_width)

        self.play(Write(text))
        self.wait(2)

        instruction_vgroup = VGroup()


class Exercises(Scene):
    def construct(self):
        text = ModifiedText("Exercises to lose weight")
        text.move_to((text.width-self.camera.frame_width/2, 0, 0)).shift(UP*2)
        print(self.camera.frame_width)

        self.play(Write(text))
        self.wait(2)
