"""
Chapter 5: Divide and Conquer
Manim CE animation scenes covering all concepts.

Render: manim -pqh scene_05_divide_and_conquer.py <SceneName>
"""

from manim import *
import numpy as np

TEAL = "#1a8a8a"
CORAL = "#d94f4f"
AMBER = "#e8a317"
INDIGO = "#4a5da8"
GREEN = "#2e8b57"


class Scene01_DCParadigm(Scene):
    """Divide-Conquer-Combine three-step paradigm."""

    def construct(self):
        title = Text("Divide and Conquer", font_size=44, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        steps = VGroup()
        labels = [
            ("DIVIDE", CORAL, "Break into smaller subproblems"),
            ("CONQUER", AMBER, "Solve each recursively"),
            ("COMBINE", GREEN, "Merge solutions together"),
        ]
        for name, color, desc in labels:
            box = VGroup(
                Text(name, font_size=28, color=color, weight=BOLD),
                Text(desc, font_size=20),
            ).arrange(DOWN, buff=0.1)
            rect = SurroundingRectangle(box, color=color, buff=0.15, corner_radius=0.1)
            steps.add(VGroup(box, rect))
        steps.arrange(RIGHT, buff=0.6).next_to(title, DOWN, buff=0.8)

        arrows = VGroup(
            Arrow(steps[0].get_right(), steps[1].get_left(), buff=0.1, stroke_width=2),
            Arrow(steps[1].get_right(), steps[2].get_left(), buff=0.1, stroke_width=2),
        )

        for s in steps:
            self.play(FadeIn(s), run_time=0.6)
        self.play(Create(arrows))

        recurrence = MathTex(
            r"T(n) = aT(n/b) + f(n)",
            font_size=30, color=AMBER,
        ).next_to(steps, DOWN, buff=0.6)
        self.play(Write(recurrence))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene02_MaxSubarray(Scene):
    """D&C approach for maximum subarray problem."""

    def construct(self):
        title = Text("Maximum Subarray (D&C)", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        arr_vals = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        arr = VGroup()
        for v in arr_vals:
            sq = Square(side_length=0.55, stroke_color=INDIGO)
            txt = Text(str(v), font_size=18)
            arr.add(VGroup(sq, txt))
        arr.arrange(RIGHT, buff=0).next_to(title, DOWN, buff=0.6)
        self.play(FadeIn(arr))

        mid = len(arr_vals) // 2
        div_line = DashedLine(
            arr[mid].get_top() + UP * 0.2, arr[mid].get_bottom() + DOWN * 0.2,
            color=CORAL,
        )
        self.play(Create(div_line))

        cases = VGroup(
            Text("Case 1: Entirely in left half", font_size=20, color=GREEN),
            Text("Case 2: Entirely in right half", font_size=20, color=AMBER),
            Text("Case 3: Crossing the midpoint", font_size=20, color=CORAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(arr, DOWN, buff=0.5)
        for c in cases:
            self.play(FadeIn(c, shift=LEFT), run_time=0.4)

        # Highlight crossing subarray [4, -1, 2, 1]
        for i in [3, 4, 5, 6]:
            arr[i][0].set_fill(GREEN, opacity=0.3)
        self.play(*[arr[i][0].animate.set_fill(GREEN, opacity=0.3) for i in [3, 4, 5, 6]])

        result = MathTex(
            r"T(n) = 2T(n/2) + O(n) = O(n\log n)",
            font_size=24, color=GREEN,
        ).to_edge(DOWN)
        note = Text("Kadane's DP: O(n), but D&C is a classic GATE question", font_size=18, color=AMBER)
        note.next_to(result, UP, buff=0.15)
        self.play(Write(note), Write(result))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene03_Strassen(Scene):
    """Strassen's matrix multiplication: 7 multiplications."""

    def construct(self):
        title = Text("Strassen's Matrix Multiplication", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        standard = VGroup(
            Text("Standard D&C: 8 multiplications", font_size=24, color=CORAL),
            MathTex(r"T(n) = 8T(n/2) + O(n^2) = O(n^3)", font_size=24),
        ).arrange(DOWN, buff=0.1).next_to(title, DOWN, buff=0.4)
        self.play(Write(standard))

        strassen = VGroup(
            Text("Strassen: 7 multiplications!", font_size=24, color=GREEN, weight=BOLD),
            MathTex(r"T(n) = 7T(n/2) + O(n^2) = O(n^{\log_2 7}) \approx O(n^{2.807})", font_size=24),
        ).arrange(DOWN, buff=0.1).next_to(standard, DOWN, buff=0.3)
        self.play(Write(strassen))

        # Show M1-M7
        ms = VGroup(
            MathTex(r"M_1 = (A_{11}+A_{22})(B_{11}+B_{22})", font_size=20),
            MathTex(r"M_2 = (A_{21}+A_{22})B_{11}", font_size=20),
            MathTex(r"M_3 = A_{11}(B_{12}-B_{22})", font_size=20),
            MathTex(r"M_4 = A_{22}(B_{21}-B_{11})", font_size=20),
            MathTex(r"M_5 = (A_{11}+A_{12})B_{22}", font_size=20),
            MathTex(r"M_6 = (A_{21}-A_{11})(B_{11}+B_{12})", font_size=20),
            MathTex(r"M_7 = (A_{12}-A_{22})(B_{21}+B_{22})", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(strassen, DOWN, buff=0.3).shift(LEFT)
        self.play(FadeIn(ms), run_time=1)

        gate = Text(
            "Best known: O(n^2.3729). Lower bound: Ω(n²)",
            font_size=20, color=AMBER,
        ).to_edge(DOWN)
        self.play(Write(gate))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene04_Karatsuba(Scene):
    """Karatsuba fast integer multiplication."""

    def construct(self):
        title = Text("Karatsuba Multiplication", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        standard = MathTex(
            r"\text{Standard: } 4 \text{ multiplications} \;\Rightarrow\; O(n^2)",
            font_size=26,
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(standard))

        trick = VGroup(
            MathTex(r"P_1 = x_H \cdot y_H", font_size=24),
            MathTex(r"P_2 = x_L \cdot y_L", font_size=24),
            MathTex(r"P_3 = (x_H+x_L)(y_H+y_L)", font_size=24),
            MathTex(r"x \cdot y = P_1 \cdot 10^n + (P_3 - P_1 - P_2) \cdot 10^{n/2} + P_2", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).next_to(standard, DOWN, buff=0.4)
        for t in trick:
            self.play(Write(t), run_time=0.5)

        result = VGroup(
            Text("Only 3 multiplications!", font_size=24, color=CORAL, weight=BOLD),
            MathTex(r"T(n) = 3T(n/2) + O(n) = O(n^{\log_2 3}) \approx O(n^{1.585})", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN)
        self.play(Write(result))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene05_ClosestPair(Scene):
    """Closest pair of points in O(n log n)."""

    def construct(self):
        title = Text("Closest Pair of Points", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Plot points
        np.random.seed(42)
        points = [(np.random.uniform(-4, 4), np.random.uniform(-2, 2)) for _ in range(12)]
        dots = VGroup()
        for x, y in points:
            dots.add(Dot(point=[x, y, 0], color=INDIGO, radius=0.08))
        dots.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(dots))

        # Dividing line
        mid_x = sorted(points, key=lambda p: p[0])[6][0]
        div_line = DashedLine([mid_x, -2.5, 0], [mid_x, 2, 0], color=CORAL)
        self.play(Create(div_line))

        steps = VGroup(
            Text("1. Sort by x, divide at midpoint", font_size=20, color=AMBER),
            Text("2. Recursively find closest in each half (δL, δR)", font_size=20, color=GREEN),
            Text("3. δ = min(δL, δR)", font_size=20, color=GREEN),
            Text("4. Check strip of width 2δ — only 6-7 comparisons each!", font_size=20, color=CORAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_edge(DOWN).shift(UP * 0.3)
        for s in steps:
            self.play(FadeIn(s, shift=LEFT), run_time=0.4)

        result = MathTex(
            r"T(n) = 2T(n/2) + O(n) = O(n\log n)",
            font_size=24, color=GREEN,
        ).to_edge(DOWN)
        self.play(Write(result))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene06_MedianOfMedians(Scene):
    """Median of Medians SELECT algorithm — O(n) worst case."""

    def construct(self):
        title = Text("Median of Medians — O(n) Selection", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        steps = VGroup(
            Text("1. Divide into groups of 5", font_size=22, color=AMBER),
            Text("2. Find median of each group — O(n)", font_size=22, color=AMBER),
            Text("3. Recursively find median of medians — T(n/5)", font_size=22, color=AMBER),
            Text("4. Use as pivot to partition", font_size=22, color=AMBER),
            Text("5. Recurse on appropriate side — T(7n/10)", font_size=22, color=AMBER),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.5)
        for s in steps:
            self.play(FadeIn(s, shift=LEFT), run_time=0.4)

        proof = VGroup(
            MathTex(r"T(n) = T(n/5) + T(7n/10) + O(n)", font_size=26, color=CORAL),
            MathTex(r"1/5 + 7/10 = 9/10 < 1", font_size=24),
            MathTex(r"\Rightarrow T(n) = O(n)", font_size=28, color=GREEN),
        ).arrange(DOWN, buff=0.15).next_to(steps, DOWN, buff=0.4)
        for p in proof:
            self.play(Write(p), run_time=0.5)

        gate = Text(
            "Groups of 3 don't work: 1/3 + 2/3 = 1 (no shrinkage)",
            font_size=20, color=CORAL,
        ).to_edge(DOWN)
        self.play(Write(gate))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
