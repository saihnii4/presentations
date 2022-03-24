# Биеийн жингээ хянах, зохицуулах аргууд

from manim import *
from manim_presentation import Slide

template = TexTemplate(preamble="""\\usepackage[utf8]{inputenc}
\\usepackage{lmodern}
\\usepackage{amsmath}
\\usepackage{amssymb}
\\usepackage{dsfont}
\\usepackage{setspace}
\\usepackage{tipa}
\\usepackage{relsize}
\\usepackage{textcomp}
\\usepackage{mathrsfs}
\\usepackage{calligra}
\\usepackage{wasysym}
\\usepackage{ragged2e}
\\usepackage{physics}
\\usepackage{xcolor}
\\usepackage{microtype}
\\usepackage[UTF8]{ctex}""")

template.add_to_preamble(
    "\\usepackage[english, main=mongolian]{babel}\n\\babeltags{mongolian=mongolian}\n\\babeltags{english=english}")
template.add_to_preamble("\\usepackage[T1,T2A]{fontenc}")
template.add_to_preamble("\\tracinglostchars=2")
template.add_to_preamble("\\usepackage{microtype}")

template.add_to_document("\singlespacing")
template.add_to_document(
    "\\newcommand*{\\bfrac}[2]{\\genfrac{}{}{0pt}{}{#1}{#2}}")

VMobject.set_default(color=BLACK)


class Introduction(Slide):
    def construct(self):
        self.authors = ["Дөлгөөн", "Мишээл", "Бөртэ", "Бишрэл"]

        text = Text(
            "Биеийн жингээ хянах, зохицуулах аргууд").shift(UP*2.5)

        credits = VGroup()

        credits_header = Text(
            "Багийн гишүүд", font_size=32).shift(UP/2)

        credits.add(credits_header)

        for i, author in enumerate(self.authors):
            credits.add(Text(author, font_size=28).shift(
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
        self.pause()

        self.play(Write(credits.submobjects[0]))
        self.pause()
        self.play(*[Write(obj) for obj in credits.submobjects[1:]])

        self.wait()


class BMI(Slide):
    def construct(self):
        VMobject.set_default(color=BLACK)

        definition_scene = VGroup()

        header = Text("BMI гэж юу вэ?", color=YELLOW)
        header.move_to((-(header.width/2), 0, 0)).shift(UP*2)

        explanations = ["Таны биеийн жин хэвийн түвшинд байгаа эсэхийг хэмжихэд зөвхөн биеийн жин хангалтгүй юм", "Өндөр, нам хүмүүсийн хэвийн жин ялгаатай байх тул биеийн жингийн индексээр та өөрийгөө хэвийн жинтэй эсэхээ мэдэх боломжтой",
                        "Энэ үзүүлэлт нь хүн бүрийн хувьд бүрэн нийцтэй байх албагүй. Тухайлбал хэрэв та илүү булчинлаг төрлийн хүн бол таны биеийн жингийн индекс таныг таргалалттай гэж дүгнэх боломжтой"]

        rendered_explanations = VGroup(*[Tex("""\\parbox{7cm}{\\textmongolian{%s}}""" % (
            explanation), tex_template=template) for explanation in explanations])

        for explanation in rendered_explanations:
            explanation.align_to(header, LEFT, alignment_vect=LEFT)

        definition_scene.add(header, rendered_explanations)

        # too lazy to shift every sub-element to the left
        definition_scene.shift(LEFT/2)

        self.play(Write(header))
        self.pause()

        for explanation in rendered_explanations:
            self.play(Write(explanation, run_time=4))
            self.pause()
            self.play(FadeOut(explanation, run_time=1))
            self.wait(0.5)

        self.pause()

        self.play(FadeOut(header))
        self.pause()

        formula_scene = VGroup()

        bmi_formula = MathTex(
            """BMI = \\frac{m}{h^2}""", tex_template=template)
        header = Text("BMI-ийн томьёо юу вэ?", color=YELLOW)

        bmi_formula_with_explanation = MathTex(
            "BMI = \\frac{m}{h^2}", """\\bfrac{\\leftarrow  weight (kg)}{\\leftarrow  height (m)}""", tex_template=template)

        formula_scene.add(header, bmi_formula_with_explanation)

        self.play(Write(header))
        self.pause()

        self.play(header.animate.shift(UP*2), Write(bmi_formula))
        self.pause()

        self.play(TransformMatchingTex(
            bmi_formula, bmi_formula_with_explanation))

        self.pause()

        self.play(FadeOut(formula_scene))

        # Example:

        example_scene = VGroup()

        jish = Text("Жишээ:", color=BLUE)
        example_formula = MathTex("BMI = \\frac{58kg}{1.81^2}")
        answer = MathTex("BMI = \\frac{58kg}{1.81^2}", "= 17.7")

        conclusion = Paragraph("Underweight буюу жин багатай", color=RED, alignment="center").align_to(
            example_formula, LEFT).shift(LEFT*3).shift(DOWN*2.5)

        bmi_table = ImageMobject("bmi_chart.jpeg").shift(RIGHT*2.5)

        example_scene.add(jish, example_formula, answer, conclusion)

        self.play(Write(jish))
        self.play(jish.animate.shift(LEFT*4).shift(UP*2))
        self.play(Write(example_formula))
        self.pause()
        self.play(TransformMatchingTex(example_formula, answer))
        self.pause()
        self.play(answer.animate.shift(LEFT*2.5))
        self.play(FadeIn(bmi_table))
        self.pause()
        self.play(Write(conclusion))

        self.play(FadeOut(example_scene))


class MeasuringWeight(Slide):
    def construct(self):
        text = Paragraph("Жин хэмжих",
                         alignment="center", color=YELLOW).shift(UP*2.5)

        instruction_1 = """\\parbox{7cm}{\\begin{itemize}
        \\item \\textmongolian{Стандартаар баталгаажсан жин, өндөр хэмжигчийг ашиглана}
        \\item \\textmongolian{Хэмжилт хийх өрөө дулаан байна}
        \\item \\textmongolian{Аль болох хувцсаа нимгэлнэ}
        \\item \\textmongolian{Үсний боолтыг тайлна}
        \end{itemize}
        """

        instruction_2 = """\\parbox{7cm}{\\begin{itemize}
        \\item \\textmongolian{Дэлгэц дээр 0.0 тоо харагдах хүртэл хүлээсний дараа жин хэмжигч дээр хөдөлгөөнгүй зогсоно}
        \\item \\textmongolian{Жингийн утга 3 секундэд тогтворжино}
        \\item \\textmongolian{Дэлгэц дээр гарсан жинг хэмжсэн тоог аравны нарийвчлалтай тэмдэглэнэ}
        \\end{itemize}}"""

        instruction_1 = Tex(instruction_1, tex_template=template).shift(
            DOWN).align_to(text, alignment_vect=RIGHT)

        instruction_2 = Tex(instruction_2, tex_template=template).shift(
            DOWN).align_to(text, alignment_vect=RIGHT)

        self.play(Write(text))
        self.pause()

        self.play(FadeIn(instruction_1))
        self.pause()

        self.play(FadeOut(instruction_1))
        self.play(FadeIn(instruction_2))

        self.pause()
        self.play(FadeOut(instruction_2))
        self.play(FadeOut(text))

        self.wait()


class MeasuringHeight(Slide):
    def construct(self):
        text = Paragraph("Өндрийг хэмжих",
                         alignment="center", color=YELLOW).shift(UP*2.5)

        instruction_1 = """\\parbox{7cm}{\\begin{itemize}
        \\item \\textmongolian{Өндөр хэмжихэд стандартаар баталгаажсан, хананд бэхлэх зориулалттай өндөр хэмжигчийг ашиглана.}
        \\item \\textmongolian{Өндөр хэмжигчийг тэгшхэн хана, багана гэх мэт хавтгай талбарт тулган шалтай тэгш өнöөг үүсгэн хөдөлгөөнгүй байрлуулна.}
        \end{itemize}
        """

        instruction_2 = """\\parbox{7cm}{\\begin{itemize}
        \\item \\textmongolian{Хэмжигч бэхэлсэн хананд хүүхдийг зөв байрлуулж зогсооно. Үүнд: чихний сувгаас нүдний доод зовхи хүртэлх босоо шугам нь самбартай перпендикуляр байхаар толгойг байрлуулна.}
        \\end{itemize}}"""

        instruction_3 = """\\parbox{7cm}{\\begin{itemize}
        \\item \\textmongolian{Хүүхдийн бие толгойн ар дагз, далны шонтон, өгзөг, шилбэ, өсгий гэсэн 5 цэгээр хананд тулсан байх ёстой.}
        \\end{itemize}}"""

        instruction_1 = Tex(instruction_1, tex_template=template).shift(
            DOWN).align_to(text, alignment_vect=RIGHT)

        instruction_2 = Tex(instruction_2, tex_template=template).shift(
            DOWN).align_to(text, alignment_vect=RIGHT)

        instruction_3 = Tex(instruction_3, tex_template=template).shift(
            DOWN).align_to(text, alignment_vect=RIGHT)

        self.play(Write(text))
        self.pause()

        self.play(FadeIn(instruction_1))
        self.pause()

        self.play(FadeOut(instruction_1))
        self.play(FadeIn(instruction_2))

        self.pause()
        self.play(FadeOut(instruction_2))

        self.play(FadeIn(instruction_3))
        self.pause()

        self.play(FadeOut(instruction_3, text))

        self.wait()


class MethodsToLoseWeight(Slide):
    def construct(self):
        text = Paragraph("Жингээ хасах аргууд",
                         alignment="center", color=ORANGE).shift(UP*1.5)
        self.play(Write(text))
        self.pause()

        methods = ["\\item \\textmongolian{Эрүүл хоололт}", "\\item \\textmongolian {Хорт зуршлаас зайлс хийх}",
                   "\\item \\textmongolian {Тогтмол дасгал хийх}", "\\item \\textmongolian {Хоолоо зөв пропорцоор идэх}"]

        bulleted_list = VGroup(*[Tex("""\\parbox{7cm}{\\begin{itemize}%s\\end{itemize}}""" % (
            method), tex_template=template).align_to(text, alignment_vect=RIGHT) for method in methods])

        for i, el in enumerate(bulleted_list.submobjects):
            self.play(Write(el.shift(i*2/3*DOWN)))
            self.pause()

        self.play(VGroup(bulleted_list, text).animate.shift(
            DOWN*5).set_opacity(0))

        self.wait()


class Goodbye(Slide):
    def construct(self):
        text = Paragraph("Анхаарлаа хандуулсанд та бүхэнд баярлалаа",
                         alignment="center", color=YELLOW)

        self.play(ApplyWave(text))

        self.wait(2)
