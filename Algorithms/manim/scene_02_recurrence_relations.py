"""
Chapter 2: Recurrence Relations
Manim CE animation scenes covering all concepts.

Render: manim -pqh scene_02_recurrence_relations.py <SceneName>
"""

from manim import *
import numpy as np

TEAL = "#1a8a8a"
CORAL = "#d94f4f"
AMBER = "#e8a317"
INDIGO = "#4a5da8"
GREEN = "#2e8b57"


class Scene01_WhatIsRecurrence(Scene):
    """Introduce recurrence relations with the Russian-doll analogy."""

    def construct(self):
        title = Text("Recurrence Relations", font_size=44, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Russian doll analogy — nested circles
        dolls = VGroup()
        colors = [CORAL, AMBER, GREEN, INDIGO, TEAL]
        for i, c in enumerate(colors):
            r = 1.2 - i * 0.2
            circ = Circle(radius=r, stroke_color=c, fill_color=c, fill_opacity=0.15)
            dolls.add(circ)
        dolls.next_to(title, DOWN, buff=0.6)
        for d in dolls:
            self.play(Create(d), run_time=0.4)

        analogy = Text(
            "Like Russian dolls: T(n) depends on T(smaller)",
            font_size=24, color=AMBER,
        ).next_to(dolls, DOWN, buff=0.5)
        self.play(Write(analogy))
        self.wait(1)

        example = MathTex(
            r"T(n) = 2T(n/2) + n \quad [\text{Merge Sort}]",
            font_size=30,
        ).next_to(analogy, DOWN, buff=0.4)
        self.play(Write(example))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene02_SubstitutionMethod(Scene):
    """Substitution method: guess & prove by induction."""

    def construct(self):
        title = Text("Method 1: Substitution (Guess & Prove)", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        steps = VGroup(
            Text("1. Guess the form", font_size=26, color=AMBER),
            Text("2. Prove by induction", font_size=26, color=GREEN),
            Text("3. Find valid constants", font_size=26, color=INDIGO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.5)
        for s in steps:
            self.play(FadeIn(s, shift=LEFT), run_time=0.5)

        # Example
        ex = VGroup(
            MathTex(r"T(n) = 2T(n/2) + n", font_size=28),
            MathTex(r"\text{Guess: } T(n) \le cn\log n", font_size=28, color=CORAL),
            MathTex(r"T(n) \le 2c\tfrac{n}{2}\log\tfrac{n}{2} + n", font_size=26),
            MathTex(r"= cn\log n - cn + n", font_size=26),
            MathTex(r"\le cn\log n \quad \text{when } c \ge 1 \;\checkmark", font_size=26, color=GREEN),
        ).arrange(DOWN, buff=0.25).next_to(steps, DOWN, buff=0.5)
        for e in ex:
            self.play(Write(e), run_time=0.6)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene03_RecursionTree(Scene):
    """Build a recursion tree for T(n) = 2T(n/2) + n and sum levels."""

    def construct(self):
        title = Text("Method 2: Recursion Tree", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Build tree
        node_style = {"font_size": 22}
        root = MathTex("n", **node_style, color=CORAL)
        l1a = MathTex("n/2", **node_style, color=AMBER)
        l1b = MathTex("n/2", **node_style, color=AMBER)
        l2a = MathTex("n/4", **node_style, color=GREEN)
        l2b = MathTex("n/4", **node_style, color=GREEN)
        l2c = MathTex("n/4", **node_style, color=GREEN)
        l2d = MathTex("n/4", **node_style, color=GREEN)

        root.move_to(UP * 1.5)
        l1a.move_to(LEFT * 2 + UP * 0)
        l1b.move_to(RIGHT * 2 + UP * 0)
        l2a.move_to(LEFT * 3 + DOWN * 1.2)
        l2b.move_to(LEFT * 1 + DOWN * 1.2)
        l2c.move_to(RIGHT * 1 + DOWN * 1.2)
        l2d.move_to(RIGHT * 3 + DOWN * 1.2)

        edges = VGroup(
            Line(root.get_bottom(), l1a.get_top(), stroke_width=1.5),
            Line(root.get_bottom(), l1b.get_top(), stroke_width=1.5),
            Line(l1a.get_bottom(), l2a.get_top(), stroke_width=1.5),
            Line(l1a.get_bottom(), l2b.get_top(), stroke_width=1.5),
            Line(l1b.get_bottom(), l2c.get_top(), stroke_width=1.5),
            Line(l1b.get_bottom(), l2d.get_top(), stroke_width=1.5),
        )

        nodes = VGroup(root, l1a, l1b, l2a, l2b, l2c, l2d)
        self.play(FadeIn(root))
        self.play(Create(edges[:2]), FadeIn(l1a), FadeIn(l1b))
        self.play(Create(edges[2:]), FadeIn(l2a), FadeIn(l2b), FadeIn(l2c), FadeIn(l2d))

        # Level costs on the right
        costs = VGroup(
            Text("Level 0: n", font_size=20, color=CORAL),
            Text("Level 1: n", font_size=20, color=AMBER),
            Text("Level 2: n", font_size=20, color=GREEN),
            Text("...", font_size=20),
            Text("Total levels: log n", font_size=20, color=INDIGO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(RIGHT).shift(DOWN * 0.5)
        for c in costs:
            self.play(FadeIn(c, shift=LEFT), run_time=0.4)

        result = MathTex(
            r"T(n) = n \times \log n = \Theta(n\log n)",
            font_size=28, color=GREEN,
        ).to_edge(DOWN)
        self.play(Write(result))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene04_MasterTheorem(Scene):
    """Master Theorem — the three cases with battle analogy."""

    def construct(self):
        title = Text("Master Theorem", font_size=44, color=TEAL)
        star = Text("(Most Important for GATE)", font_size=22, color=CORAL)
        hdr = VGroup(title, star).arrange(DOWN, buff=0.1)
        self.play(Write(hdr))
        self.play(hdr.animate.to_edge(UP))

        form = MathTex(
            r"T(n) = aT(n/b) + f(n)",
            font_size=32,
        ).next_to(hdr, DOWN, buff=0.4)
        self.play(Write(form))

        compare = MathTex(
            r"\text{Compare } f(n) \text{ with } n^{\log_b a}",
            font_size=28, color=AMBER,
        ).next_to(form, DOWN, buff=0.3)
        self.play(Write(compare))

        cases = VGroup(
            VGroup(
                Text("Case 1: Leaves win", font_size=22, color=INDIGO, weight=BOLD),
                MathTex(r"f(n) = O(n^{\log_b a - \varepsilon})", font_size=24),
                MathTex(r"\Rightarrow T(n) = \Theta(n^{\log_b a})", font_size=24, color=GREEN),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("Case 2: Tie", font_size=22, color=AMBER, weight=BOLD),
                MathTex(r"f(n) = \Theta(n^{\log_b a} \log^k n)", font_size=24),
                MathTex(r"\Rightarrow T(n) = \Theta(n^{\log_b a} \log^{k+1} n)", font_size=24, color=GREEN),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("Case 3: Root wins", font_size=22, color=CORAL, weight=BOLD),
                MathTex(r"f(n) = \Omega(n^{\log_b a + \varepsilon})", font_size=24),
                MathTex(r"\Rightarrow T(n) = \Theta(f(n))", font_size=24, color=GREEN),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=0.5).next_to(compare, DOWN, buff=0.4)

        for c in cases:
            box = SurroundingRectangle(c, buff=0.1, corner_radius=0.1, stroke_width=1)
            self.play(FadeIn(c), Create(box), run_time=0.8)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene05_MasterTheoremExamples(Scene):
    """Work through three classic Master Theorem examples."""

    def construct(self):
        title = Text("Master Theorem — Examples", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        examples = [
            (r"T(n)=9T(n/3)+n", "a=9, b=3", r"n^{\log_3 9}=n^2", r"n = O(n^{2-1})", "Case 1", r"\Theta(n^2)"),
            (r"T(n)=2T(n/2)+n", "a=2, b=2", r"n^{\log_2 2}=n", r"n = \Theta(n)", "Case 2", r"\Theta(n\log n)"),
            (r"T(n)=3T(n/4)+n\log n", "a=3, b=4", r"n^{0.793}", r"n\log n = \Omega(n^{0.793+\varepsilon})", "Case 3", r"\Theta(n\log n)"),
        ]

        prev = title
        for rec, params, comp, check, case, result in examples:
            grp = VGroup(
                MathTex(rec, font_size=26),
                Text(f"  {params}", font_size=20, color=AMBER),
                MathTex(r"\text{Compare: }" + check, font_size=22),
                Text(f"  => {case}", font_size=22, color=INDIGO),
                MathTex(r"T(n) = " + result, font_size=26, color=GREEN),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(prev, DOWN, buff=0.35)
            box = SurroundingRectangle(grp, buff=0.1, corner_radius=0.1, stroke_width=1, color=TEAL)
            self.play(FadeIn(grp), Create(box), run_time=1)
            prev = grp

        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene06_SpecialRecurrences(Scene):
    """Table of must-memorise special recurrences for GATE."""

    def construct(self):
        title = Text("Special Recurrences (Memorise!)", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["T(n)=T(n-1)+1", "Θ(n)"],
            ["T(n)=T(n-1)+n", "Θ(n²)"],
            ["T(n)=2T(n-1)+1", "Θ(2ⁿ)"],
            ["T(n)=2T(n/2)+n", "Θ(n log n)"],
            ["T(n)=2T(n/2)+1", "Θ(n)"],
            ["T(n)=T(n/2)+1", "Θ(log n)"],
            ["T(n)=T(√n)+1", "Θ(log log n)"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Recurrence", font_size=22, weight=BOLD),
                Text("Solution", font_size=22, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.6).next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(table))
        self.wait(1)

        trick = Text(
            "Trick: For T(√n)+c, substitute n=2^m to reduce to standard form",
            font_size=22, color=CORAL,
        ).next_to(table, DOWN, buff=0.4)
        self.play(Write(trick))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene07_CharacteristicEquation(Scene):
    """Fibonacci via characteristic equation method."""

    def construct(self):
        title = Text("Characteristic Equation — Fibonacci", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        steps = VGroup(
            MathTex(r"T(n) = T(n-1) + T(n-2)", font_size=28),
            MathTex(r"\text{Characteristic: } x^2 - x - 1 = 0", font_size=28, color=AMBER),
            MathTex(r"r_1 = \frac{1+\sqrt{5}}{2} = \varphi \approx 1.618", font_size=26),
            MathTex(r"r_2 = \frac{1-\sqrt{5}}{2} \approx -0.618", font_size=26),
            MathTex(r"T(n) = A\varphi^n + B r_2^n", font_size=28, color=GREEN),
            MathTex(r"|r_2| < 1 \;\Rightarrow\; T(n) = \Theta(\varphi^n) \approx \Theta(1.618^n)", font_size=26, color=CORAL),
        ).arrange(DOWN, buff=0.25).next_to(title, DOWN, buff=0.5)

        for s in steps:
            self.play(Write(s), run_time=0.7)
        self.wait(2)

        gate = Text(
            "GATE Result: Fibonacci grows as Θ(φⁿ), φ = Golden Ratio",
            font_size=22, color=AMBER,
        ).to_edge(DOWN)
        self.play(Write(gate))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene08_WhenMasterFails(Scene):
    """Cases when Master Theorem does not apply."""

    def construct(self):
        title = Text("When Master Theorem Fails", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        fails = VGroup(
            Text("1. Gap is only logarithmic, not polynomial", font_size=24, color=CORAL),
            MathTex(r"T(n)=2T(n/2)+n/\log n", font_size=24),
            Text("2. a < 1 (not allowed)", font_size=24, color=CORAL),
            Text("3. Non-uniform subproblems", font_size=24, color=CORAL),
            MathTex(r"T(n)=T(n/3)+T(2n/3)+n", font_size=24),
            Text("4. f(n) not asymptotically positive", font_size=24, color=CORAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.5)

        for f in fails:
            self.play(FadeIn(f, shift=LEFT), run_time=0.5)

        tip = Text(
            "Use recursion tree or Akra-Bazzi method instead!",
            font_size=22, color=GREEN,
        ).to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
