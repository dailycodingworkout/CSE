"""
Chapter 3: Searching Algorithms
Manim CE animation scenes covering all concepts.

Render: manim -pqh scene_03_searching.py <SceneName>
"""

from manim import *
import numpy as np

TEAL = "#1a8a8a"
CORAL = "#d94f4f"
AMBER = "#e8a317"
INDIGO = "#4a5da8"
GREEN = "#2e8b57"


def make_array(vals, highlight_idx=None, highlight_color=AMBER):
    """Helper: create a row of squares with values."""
    arr = VGroup()
    for i, v in enumerate(vals):
        sq = Square(side_length=0.6, stroke_color=INDIGO)
        if i == highlight_idx:
            sq.set_fill(highlight_color, opacity=0.3)
        txt = Text(str(v), font_size=20)
        idx = Text(str(i), font_size=14, color=AMBER).next_to(sq, DOWN, buff=0.05)
        arr.add(VGroup(sq, txt, idx))
    arr.arrange(RIGHT, buff=0)
    return arr


class Scene01_LinearSearch(Scene):
    """Animate linear search step by step."""

    def construct(self):
        title = Text("Linear Search", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        vals = [7, 3, 9, 1, 5, 8, 2, 6]
        arr = make_array(vals).next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(arr))

        key_txt = Text("Search for: 5", font_size=26, color=CORAL).next_to(arr, DOWN, buff=0.5)
        self.play(Write(key_txt))

        pointer = Triangle(fill_color=CORAL, fill_opacity=1).scale(0.15).rotate(PI)
        pointer.next_to(arr[0], UP, buff=0.1)
        self.play(FadeIn(pointer))

        for i, v in enumerate(vals):
            self.play(pointer.animate.next_to(arr[i], UP, buff=0.1), run_time=0.3)
            if v == 5:
                arr[i][0].set_fill(GREEN, opacity=0.4)
                self.play(arr[i][0].animate.set_fill(GREEN, opacity=0.4))
                found = Text(f"Found at index {i}!", font_size=24, color=GREEN)
                found.next_to(key_txt, DOWN, buff=0.3)
                self.play(Write(found))
                break
            else:
                arr[i][0].set_fill(CORAL, opacity=0.15)
                self.play(arr[i][0].animate.set_fill(CORAL, opacity=0.15), run_time=0.2)

        complexity = MathTex(
            r"\text{Best: }O(1)\quad\text{Worst: }O(n)\quad\text{Avg: }O(n)",
            font_size=24,
        ).to_edge(DOWN)
        self.play(Write(complexity))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene02_BinarySearch(Scene):
    """Animate binary search with halving visual."""

    def construct(self):
        title = Text("Binary Search", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        vals = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
        arr = make_array(vals).scale(0.9).next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(arr))

        key_txt = Text("Search for: 23", font_size=26, color=CORAL).next_to(arr, DOWN, buff=0.5)
        self.play(Write(key_txt))

        # Binary search steps
        low, high = 0, len(vals) - 1
        key = 23
        step = 0
        info_area = VGroup().next_to(key_txt, DOWN, buff=0.3)

        while low <= high:
            mid = (low + high) // 2
            step += 1
            step_txt = Text(
                f"Step {step}: low={low} high={high} mid={mid} A[{mid}]={vals[mid]}",
                font_size=18, color=AMBER,
            )
            info_area.add(step_txt)
            info_area.arrange(DOWN, buff=0.15).next_to(key_txt, DOWN, buff=0.3)
            self.play(Write(step_txt), run_time=0.5)

            # Highlight mid
            arr[mid][0].set_fill(AMBER, opacity=0.3)
            self.play(arr[mid][0].animate.set_fill(AMBER, opacity=0.3), run_time=0.3)

            if vals[mid] == key:
                arr[mid][0].set_fill(GREEN, opacity=0.5)
                self.play(arr[mid][0].animate.set_fill(GREEN, opacity=0.5))
                break
            elif vals[mid] < key:
                for i in range(low, mid + 1):
                    arr[i][0].set_fill(CORAL, opacity=0.1)
                low = mid + 1
            else:
                for i in range(mid, high + 1):
                    arr[i][0].set_fill(CORAL, opacity=0.1)
                high = mid - 1

        # Complexity derivation
        derivation = VGroup(
            MathTex(r"\text{After } k \text{ steps: } n/2^k \text{ remain}", font_size=22),
            MathTex(r"n/2^k = 1 \;\Rightarrow\; k = \log_2 n", font_size=22, color=GREEN),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN)
        self.play(Write(derivation))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene03_BinaryVsTernary(Scene):
    """Compare binary search vs ternary search — why binary wins."""

    def construct(self):
        title = Text("Binary vs Ternary Search", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        comparison = VGroup(
            VGroup(
                Text("Binary Search", font_size=26, color=GREEN, weight=BOLD),
                MathTex(r"1 \text{ comparison/step}", font_size=24),
                MathTex(r"\log_2 n \text{ steps}", font_size=24),
                MathTex(r"\text{Total: } \log_2 n", font_size=24, color=GREEN),
            ).arrange(DOWN, buff=0.15),
            VGroup(
                Text("Ternary Search", font_size=26, color=CORAL, weight=BOLD),
                MathTex(r"2 \text{ comparisons/step}", font_size=24),
                MathTex(r"\log_3 n \text{ steps}", font_size=24),
                MathTex(r"\text{Total: } 2\log_3 n \approx 1.26\log_2 n", font_size=24, color=CORAL),
            ).arrange(DOWN, buff=0.15),
        ).arrange(RIGHT, buff=1.5).next_to(title, DOWN, buff=0.6)

        for c in comparison:
            box = SurroundingRectangle(c, buff=0.15, corner_radius=0.1, stroke_width=1)
            self.play(FadeIn(c), Create(box), run_time=0.8)

        verdict = Text(
            "Binary search wins! Ternary does ~26% more comparisons.",
            font_size=24, color=AMBER,
        ).to_edge(DOWN)
        self.play(Write(verdict))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene04_InterpolationSearch(Scene):
    """Show how interpolation search estimates position using value distribution."""

    def construct(self):
        title = Text("Interpolation Search", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        formula = MathTex(
            r"\text{pos} = \text{low} + \frac{(\text{key} - A[\text{low}]) \times "
            r"(\text{high} - \text{low})}{A[\text{high}] - A[\text{low}]}",
            font_size=26,
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(formula))

        # Analogy
        analogy = Text(
            "Like finding 'A' in a phone book — start near the beginning!",
            font_size=22, color=AMBER,
        ).next_to(formula, DOWN, buff=0.4)
        self.play(Write(analogy))

        # Complexity
        data = [
            ["Best", "O(1)"],
            ["Average (uniform)", "O(log log n)"],
            ["Worst (non-uniform)", "O(n)"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Case", font_size=22, weight=BOLD),
                Text("Time", font_size=22, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.55).next_to(analogy, DOWN, buff=0.4)
        self.play(FadeIn(table))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene05_JumpSearch(Scene):
    """Jump search with optimal block size derivation."""

    def construct(self):
        title = Text("Jump Search", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Array with jump blocks
        vals = list(range(1, 17))
        arr = make_array(vals).scale(0.55).next_to(title, DOWN, buff=0.6)
        self.play(FadeIn(arr))

        block_size = 4  # sqrt(16) = 4
        colors_list = [CORAL, AMBER, GREEN, INDIGO]
        for block_idx in range(4):
            start = block_idx * block_size
            for i in range(start, start + block_size):
                arr[i][0].set_fill(colors_list[block_idx], opacity=0.2)
            self.play(
                *[arr[i][0].animate.set_fill(colors_list[block_idx], opacity=0.2)
                  for i in range(start, start + block_size)],
                run_time=0.4,
            )

        # Optimal block size derivation
        derivation = VGroup(
            MathTex(r"\text{Total comparisons} = \frac{n}{m} + m", font_size=26),
            MathTex(r"\frac{d}{dm}\left(\frac{n}{m}+m\right) = -\frac{n}{m^2}+1 = 0", font_size=26, color=AMBER),
            MathTex(r"m = \sqrt{n}", font_size=28, color=GREEN),
            MathTex(r"\text{Time: } O(\sqrt{n})", font_size=28, color=CORAL),
        ).arrange(DOWN, buff=0.2).next_to(arr, DOWN, buff=0.5)
        for d in derivation:
            self.play(Write(d), run_time=0.6)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene06_ExponentialSearch(Scene):
    """Exponential search: doubling jumps then binary search."""

    def construct(self):
        title = Text("Exponential Search", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        idea = Text(
            "Jump by 1, 2, 4, 8, 16, ... then binary search in found range",
            font_size=22, color=AMBER,
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(idea))

        # Show doubling with number line
        line = NumberLine(x_range=[0, 64, 8], length=10, include_numbers=True)
        line.next_to(idea, DOWN, buff=0.6)
        self.play(Create(line))

        jumps = [1, 2, 4, 8, 16, 32, 64]
        for j in jumps:
            dot = Dot(line.n2p(j), color=CORAL, radius=0.08)
            lab = Text(str(j), font_size=16, color=CORAL).next_to(dot, UP, buff=0.1)
            self.play(FadeIn(dot), Write(lab), run_time=0.3)

        # Highlight range
        brace = Brace(Line(line.n2p(16), line.n2p(32)), DOWN, color=GREEN)
        brace_txt = Text("Binary search here: O(log n)", font_size=18, color=GREEN)
        brace_txt.next_to(brace, DOWN, buff=0.1)
        self.play(Create(brace), Write(brace_txt))

        complexity = MathTex(
            r"\text{Total: } O(\log n) + O(\log n) = O(\log n)",
            font_size=26, color=GREEN,
        ).to_edge(DOWN)
        self.play(Write(complexity))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene07_SearchComparison(Scene):
    """Master comparison table of all searching algorithms."""

    def construct(self):
        title = Text("Searching Algorithms — Comparison", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["Linear", "O(1)", "O(n)", "O(n)", "No"],
            ["Binary", "O(1)", "O(log n)", "O(log n)", "Yes"],
            ["Ternary", "O(1)", "O(log n)", "O(log n)", "Yes"],
            ["Interpolation", "O(1)", "O(log log n)", "O(n)", "Uniform"],
            ["Jump", "O(1)", "O(√n)", "O(√n)", "Yes"],
            ["Exponential", "O(1)", "O(log n)", "O(log n)", "Yes"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Algorithm", font_size=18, weight=BOLD),
                Text("Best", font_size=18, weight=BOLD),
                Text("Average", font_size=18, weight=BOLD),
                Text("Worst", font_size=18, weight=BOLD),
                Text("Sorted?", font_size=18, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.5).next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(table))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])
