"""
Chapter 13: Miscellaneous & Advanced Topics
Manim CE animation scenes covering all concepts.

Render: manim -pqh scene_13_miscellaneous.py <SceneName>
"""

from manim import *
import numpy as np

TEAL = "#1a8a8a"
CORAL = "#d94f4f"
AMBER = "#e8a317"
INDIGO = "#4a5da8"
GREEN = "#2e8b57"


class Scene01_HashTableBasics(Scene):
    """Hash function and collision resolution basics."""

    def construct(self):
        title = Text("Hashing — Hash Table Basics", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Hash function types
        functions = VGroup(
            Text("Division: h(k) = k mod m", font_size=22, color=AMBER),
            Text("Multiplication: h(k) = floor(m(kA mod 1))", font_size=22, color=GREEN),
            Text("Universal: h(k) = ((ak+b) mod p) mod m", font_size=22, color=INDIGO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.4)
        for f in functions:
            self.play(Write(f), run_time=0.5)

        # Collision resolution
        cr = VGroup(
            Text("Collision Resolution:", font_size=24, color=CORAL, weight=BOLD),
            Text("1. Chaining: linked lists at each slot", font_size=22),
            Text("2. Open Addressing: probe for next empty", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(functions, DOWN, buff=0.4)
        for c in cr:
            self.play(Write(c), run_time=0.4)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene02_OpenAddressing(Scene):
    """Probing methods: linear, quadratic, double hashing."""

    def construct(self):
        title = Text("Open Addressing — Probing", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["Linear", "(h(k)+i) mod m", "Primary clustering"],
            ["Quadratic", "(h(k)+c₁i+c₂i²) mod m", "Secondary clustering"],
            ["Double", "(h₁(k)+i·h₂(k)) mod m", "Best distribution"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Method", font_size=20, weight=BOLD),
                Text("Probe Sequence", font_size=20, weight=BOLD),
                Text("Issue", font_size=20, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.55).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(table))

        # Expected probes
        probes = VGroup(
            Text("Unsuccessful search: 1/(1-α) probes", font_size=22, color=AMBER),
            Text("α=0.5 => 2 probes | α=0.75 => 4 probes", font_size=22, color=GREEN),
            Text("h₂(k) must NEVER be 0 (infinite loop!)", font_size=22, color=CORAL),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN)
        self.play(Write(probes))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene03_RandomizedAlgorithms(Scene):
    """Las Vegas vs Monte Carlo."""

    def construct(self):
        title = Text("Randomized Algorithms", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        types = VGroup(
            VGroup(
                Text("Las Vegas", font_size=26, color=GREEN, weight=BOLD),
                Text("Always correct", font_size=20),
                Text("Randomised running time", font_size=20),
                Text("e.g., Randomised Quick Sort", font_size=18, color=AMBER),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("Monte Carlo", font_size=26, color=CORAL, weight=BOLD),
                Text("May be incorrect", font_size=20),
                Text("Guaranteed running time", font_size=20),
                Text("e.g., Miller-Rabin Primality", font_size=18, color=AMBER),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=1.5).next_to(title, DOWN, buff=0.5)

        for t in types:
            box = SurroundingRectangle(t, buff=0.15, corner_radius=0.1, stroke_width=1)
            self.play(FadeIn(t), Create(box), run_time=0.7)

        fact = Text(
            "Randomised Quick Sort: expected O(n log n) for ANY input",
            font_size=22, color=GREEN,
        ).to_edge(DOWN)
        self.play(Write(fact))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene04_LowerBounds(Scene):
    """Comparison-based lower bounds for various problems."""

    def construct(self):
        title = Text("Lower Bounds for Algorithms", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["Finding max", "n-1"],
            ["Finding max AND min", "ceil(3n/2)-2"],
            ["Finding 2nd largest", "n+ceil(log n)-2"],
            ["Sorting", "ceil(log₂(n!)) = Ω(n log n)"],
            ["Searching sorted", "Ω(log n)"],
            ["Merging", "m+n-1 (worst)"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Problem", font_size=20, weight=BOLD),
                Text("Min Comparisons", font_size=20, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.55).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(table))

        # Tournament method
        tournament = VGroup(
            Text("Max+Min tournament:", font_size=20, color=AMBER),
            Text("Compare pairs (n/2), max from winners (n/2-1), min from losers (n/2-1)", font_size=18),
            Text("= 3n/2 - 2 comparisons", font_size=20, color=GREEN),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN)
        self.play(Write(tournament))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene05_Approximation(Scene):
    """Approximation algorithms for NP-Hard problems."""

    def construct(self):
        title = Text("Approximation Algorithms", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["Vertex Cover", "2-approx"],
            ["TSP (metric)", "3/2 (Christofides)"],
            ["Set Cover", "O(ln n)"],
            ["General TSP", "No constant (unless P=NP)"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Problem", font_size=22, weight=BOLD),
                Text("Best Ratio", font_size=22, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.6).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(table))

        vc = VGroup(
            Text("Vertex Cover 2-approx:", font_size=20, color=AMBER),
            Text("Take both endpoints of maximal matching", font_size=20),
            Text("Our cover <= 2 * optimal (each matching edge needs >=1)", font_size=20, color=GREEN),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN)
        self.play(Write(vc))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene06_CatalanAndIdentities(Scene):
    """Catalan numbers and important identities for GATE."""

    def construct(self):
        title = Text("Catalan Numbers & Identities", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        catalan = MathTex(
            r"C(n) = \frac{(2n)!}{(n+1)!\,n!} = \frac{\binom{2n}{n}}{n+1}",
            font_size=28, color=AMBER,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(catalan))

        values = Text(
            "C(0)=1, C(1)=1, C(2)=2, C(3)=5, C(4)=14, C(5)=42",
            font_size=22, color=GREEN,
        ).next_to(catalan, DOWN, buff=0.3)
        self.play(Write(values))

        appearances = VGroup(
            Text("Appearances:", font_size=22, color=CORAL, weight=BOLD),
            Text("Distinct binary trees with n nodes", font_size=20),
            Text("Ways to parenthesise n+1 factors", font_size=20),
            Text("Valid arrangements of n pairs of parentheses", font_size=20),
            Text("Paths in n*n grid without crossing diagonal", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(values, DOWN, buff=0.3)
        for a in appearances:
            self.play(FadeIn(a, shift=LEFT), run_time=0.3)

        identity = MathTex(
            r"a^{\log_b c} = c^{\log_b a} \quad\text{(GATE favourite!)}",
            font_size=26, color=INDIGO,
        ).to_edge(DOWN)
        self.play(Write(identity))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
