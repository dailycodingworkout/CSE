"""
Chapter 11: Complexity Classes & NP-Completeness
Manim CE animation scenes covering all concepts.

Render: manim -pqh scene_11_complexity_classes.py <SceneName>
"""

from manim import *
import numpy as np

TEAL = "#1a8a8a"
CORAL = "#d94f4f"
AMBER = "#e8a317"
INDIGO = "#4a5da8"
GREEN = "#2e8b57"


class Scene01_WhyThisMatters(Scene):
    """P vs NP — the million dollar question."""

    def construct(self):
        title = Text("Complexity Classes", font_size=44, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        question = MathTex(r"P \stackrel{?}{=} NP", font_size=60, color=CORAL)
        question.next_to(title, DOWN, buff=0.5)
        self.play(Write(question))

        subtitle = Text(
            "$1 Million Millennium Prize Problem",
            font_size=24, color=AMBER,
        ).next_to(question, DOWN, buff=0.3)
        self.play(Write(subtitle))

        why = VGroup(
            Text("Know when to stop searching for efficient algorithms", font_size=22, color=GREEN),
            Text("Recognise NP-Complete problems in exams", font_size=22, color=GREEN),
            Text("Use approximation/heuristic algorithms instead", font_size=22, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(subtitle, DOWN, buff=0.5)
        for w in why:
            self.play(FadeIn(w, shift=LEFT), run_time=0.4)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene02_PAndNP(Scene):
    """Class P and Class NP definitions."""

    def construct(self):
        title = Text("P and NP", font_size=44, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        p_box = VGroup(
            Text("Class P", font_size=28, color=GREEN, weight=BOLD),
            Text("Solvable in polynomial time", font_size=20),
            Text("Sorting, Shortest path, MST, 2-SAT", font_size=18, color=AMBER),
        ).arrange(DOWN, buff=0.1)
        p_rect = SurroundingRectangle(p_box, color=GREEN, buff=0.15, corner_radius=0.1)

        np_box = VGroup(
            Text("Class NP", font_size=28, color=INDIGO, weight=BOLD),
            Text("Verifiable in polynomial time", font_size=20),
            Text("SAT, Hamiltonian, Clique, Subset Sum", font_size=18, color=AMBER),
        ).arrange(DOWN, buff=0.1)
        np_rect = SurroundingRectangle(np_box, color=INDIGO, buff=0.15, corner_radius=0.1)

        boxes = VGroup(
            VGroup(p_box, p_rect), VGroup(np_box, np_rect)
        ).arrange(RIGHT, buff=1).next_to(title, DOWN, buff=0.6)

        self.play(FadeIn(p_box), Create(p_rect))
        self.play(FadeIn(np_box), Create(np_rect))

        key = MathTex(r"P \subseteq NP", font_size=32, color=GREEN).next_to(boxes, DOWN, buff=0.4)
        self.play(Write(key))

        note = Text(
            "P: can SOLVE efficiently | NP: can VERIFY efficiently",
            font_size=22, color=CORAL,
        ).to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene03_NPHardComplete(Scene):
    """NP-Hard and NP-Complete with Venn diagram."""

    def construct(self):
        title = Text("NP-Hard and NP-Complete", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Venn diagram
        np_circle = Circle(radius=1.8, stroke_color=INDIGO, fill_color=INDIGO, fill_opacity=0.1)
        nph_circle = Circle(radius=2, stroke_color=CORAL, fill_color=CORAL, fill_opacity=0.05)
        nph_circle.shift(RIGHT * 1.2)
        np_circle.shift(LEFT * 0.3)
        venn = VGroup(np_circle, nph_circle).next_to(title, DOWN, buff=0.5)

        np_label = Text("NP", font_size=24, color=INDIGO, weight=BOLD).move_to(np_circle.get_center() + LEFT * 0.8)
        nph_label = Text("NP-Hard", font_size=24, color=CORAL, weight=BOLD).move_to(nph_circle.get_center() + RIGHT * 0.8)
        npc_label = Text("NP-\nComplete", font_size=20, color=AMBER, weight=BOLD).move_to(
            (np_circle.get_center() + nph_circle.get_center()) / 2
        )
        p_label = Text("P", font_size=22, color=GREEN, weight=BOLD).move_to(np_circle.get_center() + LEFT * 0.3 + DOWN * 0.5)

        self.play(Create(np_circle), Create(nph_circle))
        self.play(Write(np_label), Write(nph_label), Write(npc_label), Write(p_label))

        defn = VGroup(
            Text("NP-Complete = NP ∩ NP-Hard", font_size=24, color=AMBER),
            Text("Hardest problems in NP", font_size=22, color=CORAL),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN)
        self.play(Write(defn))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene04_Reductions(Scene):
    """Polynomial-time reductions and how to prove NP-Complete."""

    def construct(self):
        title = Text("Polynomial-Time Reductions", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        reduction = MathTex(
            r"A \le_p B", font_size=36, color=AMBER,
        ).next_to(title, DOWN, buff=0.5)
        meaning = Text(
            '"If we can solve B, we can solve A"',
            font_size=22, color=GREEN,
        ).next_to(reduction, DOWN, buff=0.2)
        self.play(Write(reduction), Write(meaning))

        # How to prove NP-Complete
        steps = VGroup(
            Text("To prove X is NP-Complete:", font_size=24, color=CORAL, weight=BOLD),
            Text("1. Show X is in NP (verifiable in poly time)", font_size=22),
            Text("2. Take known NPC problem Y", font_size=22),
            Text("3. Show Y <=p X (reduce FROM known TO new)", font_size=22, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(meaning, DOWN, buff=0.4)
        for s in steps:
            self.play(Write(s), run_time=0.5)

        trap = Text(
            "TRAP: Don't reduce in the wrong direction!",
            font_size=22, color=CORAL,
        ).to_edge(DOWN)
        box = SurroundingRectangle(trap, color=CORAL, buff=0.1)
        self.play(Write(trap), Create(box))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene05_FamousNPC(Scene):
    """List of famous NP-Complete problems and reduction chain."""

    def construct(self):
        title = Text("Famous NP-Complete Problems", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        problems = VGroup(
            Text("SAT, 3-SAT, Vertex Cover, Independent Set", font_size=22, color=AMBER),
            Text("Clique, Hamiltonian Cycle, TSP (decision)", font_size=22, color=AMBER),
            Text("Subset Sum, Graph Coloring (>=3), Partition", font_size=22, color=AMBER),
            Text("0/1 Knapsack (decision), Set Cover, 3D Matching", font_size=22, color=AMBER),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(title, DOWN, buff=0.4)
        for p in problems:
            self.play(FadeIn(p, shift=LEFT), run_time=0.4)

        chain = VGroup(
            Text("Standard Reduction Chain:", font_size=22, color=CORAL, weight=BOLD),
            Text("SAT -> 3-SAT -> Clique -> Vertex Cover", font_size=20, color=GREEN),
            Text("3-SAT -> Hamiltonian -> TSP", font_size=20, color=GREEN),
            Text("3-SAT -> Subset Sum -> Partition -> Knapsack", font_size=20, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(problems, DOWN, buff=0.3)
        for c in chain:
            self.play(Write(c), run_time=0.4)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene06_PvsNPC(Scene):
    """Problems in P vs NP-Complete: the 2-vs-3 pattern."""

    def construct(self):
        title = Text("P vs NP-Complete: The Pattern", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["2-SAT", "P", "3-SAT", "NPC"],
            ["2-Coloring", "P", "3-Coloring", "NPC"],
            ["Euler Path", "P", "Hamiltonian", "NPC"],
            ["Frac Knapsack", "P", "0/1 Knapsack", "NPC"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Easy", font_size=20, weight=BOLD, color=GREEN),
                Text("Class", font_size=20, weight=BOLD),
                Text("Hard", font_size=20, weight=BOLD, color=CORAL),
                Text("Class", font_size=20, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.55).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(table))

        pattern = Text(
            "Often '2 vs 3' determines complexity!",
            font_size=24, color=AMBER,
        ).to_edge(DOWN)
        self.play(Write(pattern))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene07_PseudoPolynomial(Scene):
    """Pseudo-polynomial algorithms and approximation."""

    def construct(self):
        title = Text("Pseudo-Polynomial & Approximation", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        pseudo = VGroup(
            Text("Pseudo-Polynomial:", font_size=24, color=AMBER, weight=BOLD),
            Text("Polynomial in numeric VALUE, exponential in BITS", font_size=22),
            Text("Example: 0/1 Knapsack O(nW) — if W=2^n, it's exponential", font_size=20, color=CORAL),
            Text("Weakly NPC: Knapsack, Subset Sum, Partition", font_size=20, color=GREEN),
            Text("Strongly NPC: 3-SAT, TSP, 3-Coloring", font_size=20, color=CORAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(title, DOWN, buff=0.4)
        for p in pseudo:
            self.play(Write(p), run_time=0.4)

        approx = VGroup(
            Text("Approximation: Vertex Cover (2x), TSP (3/2x Christofides)", font_size=20, color=INDIGO),
        ).next_to(pseudo, DOWN, buff=0.3)
        self.play(Write(approx))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
