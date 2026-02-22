"""
Chapter 1: Algorithm Analysis & Asymptotic Notations
Manim CE animation scenes covering all concepts.

Render: manim -pqh scene_01_algorithm_analysis.py <SceneName>
"""

from manim import *
import numpy as np

# Colour palette (consistent with repo design)
TEAL = "#1a8a8a"
CORAL = "#d94f4f"
AMBER = "#e8a317"
INDIGO = "#4a5da8"
GREEN = "#2e8b57"


class Scene01_WhatIsAnAlgorithm(Scene):
    """Visualise the five Knuth properties of an algorithm."""

    def construct(self):
        title = Text("What is an Algorithm?", font_size=44, color=TEAL)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # Recipe analogy
        recipe = VGroup(
            Text("Input", font_size=28, color=AMBER),
            MathTex(r"\rightarrow", font_size=36),
            Text("Finite Steps", font_size=28, color=GREEN),
            MathTex(r"\rightarrow", font_size=36),
            Text("Output", font_size=28, color=CORAL),
        ).arrange(RIGHT, buff=0.4)
        self.play(FadeIn(recipe, shift=UP))
        self.wait(1)

        # Five properties
        props = [
            ("Finiteness", "Must terminate"),
            ("Definiteness", "Each step is precise"),
            ("Input", "Zero or more inputs"),
            ("Output", "One or more outputs"),
            ("Effectiveness", "Steps are basic"),
        ]
        prop_grp = VGroup()
        for name, desc in props:
            row = VGroup(
                Text(name, font_size=24, color=INDIGO, weight=BOLD),
                Text(f" — {desc}", font_size=22),
            ).arrange(RIGHT, buff=0.2)
            prop_grp.add(row)
        prop_grp.arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(recipe, DOWN, buff=0.6)

        for p in prop_grp:
            self.play(FadeIn(p, shift=LEFT), run_time=0.5)
        self.wait(1.5)

        # Trap callout
        trap = Text(
            "GATE Trap: A procedure that runs forever is NOT an algorithm!",
            font_size=22, color=CORAL,
        ).next_to(prop_grp, DOWN, buff=0.5)
        box = SurroundingRectangle(trap, color=CORAL, buff=0.15)
        self.play(Write(trap), Create(box))
        self.wait(2)
        self.play(FadeOut(VGroup(title, recipe, prop_grp, trap, box)))


class Scene02_WhyAnalyze(Scene):
    """Time vs Space complexity dimensions."""

    def construct(self):
        title = Text("Why Analyse Algorithms?", font_size=44, color=TEAL)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # Two dimensions
        time_box = VGroup(
            Text("Time Complexity", font_size=28, color=CORAL, weight=BOLD),
            Text("T(n) — number of operations", font_size=22),
        ).arrange(DOWN, buff=0.15)
        space_box = VGroup(
            Text("Space Complexity", font_size=28, color=INDIGO, weight=BOLD),
            Text("S(n) — memory used", font_size=22),
        ).arrange(DOWN, buff=0.15)

        boxes = VGroup(time_box, space_box).arrange(RIGHT, buff=1.5).next_to(title, DOWN, buff=0.8)
        t_rect = SurroundingRectangle(time_box, color=CORAL, buff=0.2, corner_radius=0.1)
        s_rect = SurroundingRectangle(space_box, color=INDIGO, buff=0.2, corner_radius=0.1)

        self.play(Create(t_rect), FadeIn(time_box))
        self.play(Create(s_rect), FadeIn(space_box))
        self.wait(1)

        insight = Text(
            "We count fundamental operations, not wall-clock time.",
            font_size=24, color=GREEN,
        ).next_to(boxes, DOWN, buff=0.8)
        self.play(Write(insight))
        self.wait(2)
        self.play(FadeOut(VGroup(title, time_box, space_box, t_rect, s_rect, insight)))


class Scene03_BigONotation(Scene):
    """Big-O definition with visual proof and limit test."""

    def construct(self):
        title = Text("Big-O Notation — O(g(n))", font_size=42, color=TEAL)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        defn = MathTex(
            r"f(n) = O(g(n))", r"\;\text{if}\;",
            r"\exists\, c > 0,\, n_0 > 0",
            r"\;\text{s.t.}\;",
            r"f(n) \le c \cdot g(n)",
            r"\;\forall\, n \ge n_0",
            font_size=30,
        )
        defn[0].set_color(CORAL)
        defn[4].set_color(AMBER)
        self.play(Write(defn.next_to(title, DOWN, buff=0.5)))
        self.wait(1)

        # Graph demonstration: f(n)=3n+2, g(n)=n, c=4
        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 50, 10],
            x_length=5, y_length=3.5,
            axis_config={"include_numbers": True, "font_size": 20},
        ).next_to(defn, DOWN, buff=0.6).shift(LEFT * 0.5)
        labels = axes.get_axis_labels(x_label="n", y_label="")

        f_graph = axes.plot(lambda x: 3 * x + 2, x_range=[0, 10], color=CORAL)
        g_graph = axes.plot(lambda x: 4 * x, x_range=[0, 10], color=GREEN)
        f_label = Text("f(n)=3n+2", font_size=18, color=CORAL).next_to(f_graph, RIGHT, buff=0.1)
        g_label = Text("c·g(n)=4n", font_size=18, color=GREEN).next_to(g_graph, RIGHT, buff=0.1)

        self.play(Create(axes), Write(labels))
        self.play(Create(f_graph), Write(f_label))
        self.play(Create(g_graph), Write(g_label))

        # Mark n0
        n0_dot = Dot(axes.c2p(2, 8), color=AMBER, radius=0.08)
        n0_label = MathTex(r"n_0=2", font_size=22, color=AMBER).next_to(n0_dot, DOWN)
        self.play(FadeIn(n0_dot), Write(n0_label))
        self.wait(1)

        conclusion = Text(
            "For n >= 2: 3n+2 <= 4n  =>  3n+2 = O(n)",
            font_size=22, color=GREEN,
        ).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene04_BigOmegaAndTheta(Scene):
    """Big-Omega (lower bound) and Big-Theta (tight bound)."""

    def construct(self):
        title = Text("Big-Ω (Lower Bound)  &  Big-Θ (Tight Bound)", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        omega_def = MathTex(
            r"f(n) = \Omega(g(n))", r"\;\Leftrightarrow\;",
            r"f(n) \ge c \cdot g(n)",
            r"\;\forall\, n \ge n_0",
            font_size=28,
        ).next_to(title, DOWN, buff=0.5)
        omega_def[0].set_color(INDIGO)
        self.play(Write(omega_def))

        theta_def = MathTex(
            r"f(n) = \Theta(g(n))", r"\;\Leftrightarrow\;",
            r"c_1 g(n) \le f(n) \le c_2 g(n)",
            font_size=28,
        ).next_to(omega_def, DOWN, buff=0.4)
        theta_def[0].set_color(GREEN)
        self.play(Write(theta_def))
        self.wait(1)

        # Sandwich graph for Theta
        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 120, 20],
            x_length=5.5, y_length=3,
            axis_config={"include_numbers": True, "font_size": 18},
        ).next_to(theta_def, DOWN, buff=0.5)
        f_plot = axes.plot(lambda x: 3 * x ** 2 + 5 * x + 2, x_range=[0.1, 10], color=CORAL)
        c1_plot = axes.plot(lambda x: 3 * x ** 2, x_range=[0.1, 10], color=INDIGO)
        c2_plot = axes.plot(lambda x: 10 * x ** 2, x_range=[0.1, 7], color=GREEN)

        f_lab = Text("f(n)", font_size=16, color=CORAL).next_to(f_plot.get_end(), RIGHT, buff=0.1)
        c1_lab = MathTex(r"c_1 n^2", font_size=20, color=INDIGO).next_to(c1_plot.get_end(), RIGHT, buff=0.1)
        c2_lab = MathTex(r"c_2 n^2", font_size=20, color=GREEN).next_to(
            axes.c2p(7, 10 * 49), RIGHT, buff=0.1
        )

        self.play(Create(axes))
        self.play(Create(c1_plot), Write(c1_lab))
        self.play(Create(f_plot), Write(f_lab))
        self.play(Create(c2_plot), Write(c2_lab))
        self.wait(1)

        note = Text("f is sandwiched => Θ(n²)", font_size=24, color=AMBER).to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene05_LittleOAndOmega(Scene):
    """Little-o and little-omega (strict bounds)."""

    def construct(self):
        title = Text("Strict Bounds: o(g) and ω(g)", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        table_data = [
            ["Notation", "Relation", "Analogy"],
            ["f = O(g)", "f ≤ g", "≤"],
            ["f = Ω(g)", "f ≥ g", "≥"],
            ["f = Θ(g)", "f = g", "="],
            ["f = o(g)", "f < g", "<"],
            ["f = ω(g)", "f > g", ">"],
        ]
        table = Table(
            [[c for c in row] for row in table_data[1:]],
            col_labels=[Text(h, font_size=22, weight=BOLD) for h in table_data[0]],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.65).next_to(title, DOWN, buff=0.6)

        self.play(FadeIn(table))
        self.wait(1)

        limit = MathTex(
            r"\text{Limit test: } \lim_{n\to\infty} \frac{f(n)}{g(n)} = "
            r"\begin{cases} 0 & \Rightarrow o(g) \\ c & \Rightarrow \Theta(g) \\"
            r" \infty & \Rightarrow \omega(g) \end{cases}",
            font_size=26,
        ).next_to(table, DOWN, buff=0.5)
        self.play(Write(limit))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene06_GrowthRatesRace(Scene):
    """Animated race of growth-rate functions."""

    def construct(self):
        title = Text("Growth Rate Race", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        axes = Axes(
            x_range=[1, 20, 5], y_range=[0, 100, 20],
            x_length=8, y_length=4.5,
            axis_config={"include_numbers": True, "font_size": 18},
        ).next_to(title, DOWN, buff=0.5)
        x_lab = axes.get_x_axis_label("n", font_size=24)
        self.play(Create(axes), Write(x_lab))

        funcs = [
            (lambda x: 1, "O(1)", TEAL),
            (lambda x: np.log2(max(x, 1)), "O(log n)", GREEN),
            (lambda x: x, "O(n)", INDIGO),
            (lambda x: x * np.log2(max(x, 1)), "O(n log n)", AMBER),
            (lambda x: x ** 2, "O(n²)", CORAL),
        ]

        for fn, label_text, color in funcs:
            safe_fn = lambda x, f=fn: min(f(x), 100)
            graph = axes.plot(safe_fn, x_range=[1, 20], color=color, use_smoothing=True)
            lab = Text(label_text, font_size=16, color=color)
            y_val = safe_fn(20)
            if y_val >= 100:
                lab.next_to(axes.c2p(14, 95), RIGHT, buff=0.1)
            else:
                lab.next_to(graph.get_end(), RIGHT, buff=0.1)
            self.play(Create(graph), Write(lab), run_time=0.8)

        self.wait(1)

        order = MathTex(
            r"O(1) < O(\log n) < O(n) < O(n\log n) < O(n^2) < O(2^n) < O(n!)",
            font_size=24, color=AMBER,
        ).to_edge(DOWN)
        self.play(Write(order))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene07_BestWorstAverage(Scene):
    """Best, worst, and average case visualised on linear search."""

    def construct(self):
        title = Text("Best · Worst · Average Case", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Array
        arr_vals = [7, 3, 9, 1, 5, 8, 2, 6]
        arr = VGroup()
        for v in arr_vals:
            sq = Square(side_length=0.6, stroke_color=INDIGO)
            txt = Text(str(v), font_size=22)
            arr.add(VGroup(sq, txt))
        arr.arrange(RIGHT, buff=0).next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(arr))

        key = Text("Search for key = 7", font_size=24, color=AMBER).next_to(arr, DOWN, buff=0.5)
        self.play(Write(key))

        # Best case — found at index 0
        highlight = SurroundingRectangle(arr[0], color=GREEN, buff=0.05)
        best_txt = Text("Best case: found at index 0 -> O(1)", font_size=22, color=GREEN)
        best_txt.next_to(key, DOWN, buff=0.4)
        self.play(Create(highlight), Write(best_txt))
        self.wait(1)

        # Worst case
        self.play(FadeOut(highlight))
        worst_txt = Text("Worst case: element at end or absent -> O(n)", font_size=22, color=CORAL)
        worst_txt.next_to(best_txt, DOWN, buff=0.3)
        self.play(Write(worst_txt))
        self.wait(1)

        avg_txt = Text("Average case: ~n/2 checks -> O(n)", font_size=22, color=AMBER)
        avg_txt.next_to(worst_txt, DOWN, buff=0.3)
        self.play(Write(avg_txt))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene08_CodeAnalysisPatterns(Scene):
    """Animated loop analysis patterns commonly tested in GATE."""

    def construct(self):
        title = Text("Loop Analysis Patterns", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        patterns = [
            ("i = 1; i <= n; i *= 2", "O(log n)", "Variable doubles each step"),
            ("i = n; i >= 1; i /= 2", "O(log n)", "Variable halves each step"),
            ("Nested: i -> n, j -> i", "O(n²)", "Sum 1+2+...+n = n(n+1)/2"),
            ("i *= 2, j *= 2", "O(log²n)", "Both logarithmic"),
            ("i *= 2, j -> i", "O(n)", "Geometric series: 1+2+4+...+n"),
            ("i*i <= n", "O(√n)", "Loop runs √n times"),
            ("i -> n, j += i", "O(n log n)", "Harmonic series"),
        ]

        grp = VGroup()
        for code, cpx, note in patterns:
            row = VGroup(
                Text(code, font_size=18, color=WHITE).set_width(4),
                Text(cpx, font_size=20, color=CORAL, weight=BOLD),
                Text(note, font_size=16, color=GREEN),
            ).arrange(RIGHT, buff=0.3)
            grp.add(row)
        grp.arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.5)

        for row in grp:
            self.play(FadeIn(row, shift=LEFT), run_time=0.5)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene09_SpaceComplexity(Scene):
    """Space complexity comparison of sorting algorithms."""

    def construct(self):
        title = Text("Space Complexity", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        formula = MathTex(
            r"\text{Total Space} = \text{Input Space} + \text{Auxiliary Space}",
            font_size=30,
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(formula))

        data = [
            ["Merge Sort", "O(n log n)", "O(n)"],
            ["Quick Sort", "O(n log n)", "O(log n)"],
            ["Heap Sort", "O(n log n)", "O(1)"],
            ["Insertion Sort", "O(n²)", "O(1)"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Algorithm", font_size=22, weight=BOLD),
                Text("Time", font_size=22, weight=BOLD),
                Text("Aux Space", font_size=22, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.6).next_to(formula, DOWN, buff=0.5)

        self.play(FadeIn(table))
        self.wait(1)

        trap = Text(
            "Quick Sort uses O(n) stack space in worst case!",
            font_size=22, color=CORAL,
        ).next_to(table, DOWN, buff=0.4)
        box = SurroundingRectangle(trap, color=CORAL, buff=0.1)
        self.play(Write(trap), Create(box))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene10_PropertiesOfNotations(Scene):
    """Reflexive, symmetric, transitive, transpose-symmetric properties."""

    def construct(self):
        title = Text("Properties of Asymptotic Notations", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["", "O", "Ω", "Θ"],
            ["Reflexive", "✓", "✓", "✓"],
            ["Symmetric", "✗", "✗", "✓"],
            ["Transitive", "✓", "✓", "✓"],
        ]
        table = Table(
            [row[1:] for row in data[1:]],
            row_labels=[Text(row[0], font_size=22) for row in data[1:]],
            col_labels=[Text(h, font_size=24, weight=BOLD, color=AMBER) for h in data[0][1:]],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.65).next_to(title, DOWN, buff=0.6)

        self.play(FadeIn(table))
        self.wait(1)

        transpose = MathTex(
            r"f(n) = O(g(n)) \Leftrightarrow g(n) = \Omega(f(n))",
            font_size=28, color=GREEN,
        ).next_to(table, DOWN, buff=0.5)
        label = Text("Transpose Symmetry (GATE Favorite!)", font_size=22, color=CORAL)
        label.next_to(transpose, DOWN, buff=0.2)
        self.play(Write(transpose), Write(label))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
