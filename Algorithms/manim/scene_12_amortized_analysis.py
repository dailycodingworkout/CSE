"""
Chapter 12: Amortized Analysis
Manim CE animation scenes covering all concepts.

Render: manim -pqh scene_12_amortized_analysis.py <SceneName>
"""

from manim import *
import numpy as np

TEAL = "#1a8a8a"
CORAL = "#d94f4f"
AMBER = "#e8a317"
INDIGO = "#4a5da8"
GREEN = "#2e8b57"


class Scene01_WhatIsAmortized(Scene):
    """Amortized analysis: average cost per operation in a sequence."""

    def construct(self):
        title = Text("Amortized Analysis", font_size=44, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        analogy = Text(
            "Piggy bank: daily deposits, occasional large withdrawals",
            font_size=22, color=AMBER,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(analogy))

        key = VGroup(
            Text("NOT average-case analysis (no probability!)", font_size=22, color=CORAL),
            Text("Worst-case guarantee for a SEQUENCE of operations", font_size=22, color=GREEN),
        ).arrange(DOWN, buff=0.15).next_to(analogy, DOWN, buff=0.4)
        for k in key:
            self.play(Write(k), run_time=0.5)

        methods = VGroup(
            Text("Three methods:", font_size=24, color=INDIGO, weight=BOLD),
            Text("1. Aggregate Method", font_size=22, color=AMBER),
            Text("2. Accounting (Banker's) Method", font_size=22, color=GREEN),
            Text("3. Potential (Physicist's) Method", font_size=22, color=CORAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(key, DOWN, buff=0.4)
        for m in methods:
            self.play(FadeIn(m, shift=LEFT), run_time=0.4)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene02_AggregateMethod(Scene):
    """Aggregate method: Stack with Multipop example."""

    def construct(self):
        title = Text("Method 1: Aggregate", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        formula = MathTex(
            r"\text{Amortized cost} = \frac{T(n)}{n}",
            font_size=30, color=AMBER,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(formula))

        example = VGroup(
            Text("Stack with MULTIPOP(k):", font_size=24, color=GREEN, weight=BOLD),
            Text("PUSH cost 1, POP cost 1, MULTIPOP(k) cost k", font_size=20),
            Text("Worst single MULTIPOP: O(n)", font_size=20, color=CORAL),
        ).arrange(DOWN, buff=0.1).next_to(formula, DOWN, buff=0.3)
        self.play(Write(example))

        analysis = VGroup(
            Text("But: each element pushed at most once => total pushes <= n", font_size=20, color=GREEN),
            Text("Each element popped at most once => total pops <= n", font_size=20, color=GREEN),
            Text("Total cost of n operations <= 2n", font_size=20, color=AMBER),
            MathTex(r"\text{Amortized} = \frac{2n}{n} = O(1)", font_size=26, color=GREEN),
        ).arrange(DOWN, buff=0.15).next_to(example, DOWN, buff=0.3)
        for a in analysis:
            self.play(Write(a), run_time=0.5)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene03_AccountingMethod(Scene):
    """Accounting method: overcharge cheap, subsidise expensive."""

    def construct(self):
        title = Text("Method 2: Accounting (Banker's)", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        idea = Text(
            "Overcharge cheap operations to prepay for expensive ones",
            font_size=22, color=AMBER,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(idea))

        data = [
            ["PUSH", "1", "2", "+1 credit"],
            ["POP", "1", "0", "use credit"],
            ["MULTIPOP(k)", "k", "0", "use k credits"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Op", font_size=20, weight=BOLD),
                Text("Actual", font_size=20, weight=BOLD),
                Text("Amortised", font_size=20, weight=BOLD),
                Text("Credit", font_size=20, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.55).next_to(idea, DOWN, buff=0.3)
        self.play(FadeIn(table))

        rule = Text(
            "Rule: total amortised >= total actual (credit never negative)",
            font_size=20, color=CORAL,
        ).to_edge(DOWN)
        self.play(Write(rule))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene04_PotentialMethod(Scene):
    """Potential method with the stack example."""

    def construct(self):
        title = Text("Method 3: Potential (Physicist's)", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        formula = MathTex(
            r"\hat{c}_i = c_i + \Phi(D_i) - \Phi(D_{i-1})",
            font_size=28, color=GREEN,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(formula))

        requirements = VGroup(
            MathTex(r"\Phi(D_0) = 0", font_size=24),
            MathTex(r"\Phi(D_i) \ge 0 \;\forall\, i", font_size=24),
        ).arrange(DOWN, buff=0.1).next_to(formula, DOWN, buff=0.3)
        self.play(Write(requirements))

        # Stack example
        example = VGroup(
            Text("Φ = number of elements in stack", font_size=22, color=AMBER),
            Text("PUSH: actual=1, ΔΦ=+1, amortised=2", font_size=20),
            Text("POP: actual=1, ΔΦ=-1, amortised=0", font_size=20),
            Text("MULTIPOP(k): actual=k, ΔΦ=-k, amortised=0", font_size=20),
            Text("=> Amortised O(1) per operation!", font_size=22, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(requirements, DOWN, buff=0.3)
        for e in example:
            self.play(Write(e), run_time=0.4)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene05_DynamicArray(Scene):
    """Dynamic array doubling: amortised O(1) insert."""

    def construct(self):
        title = Text("Dynamic Array — Amortised Doubling", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Show capacity doubling
        sizes = [1, 2, 4, 8, 16]
        bars = VGroup()
        for s in sizes:
            bar = Rectangle(
                width=0.3 * s, height=0.5,
                fill_color=INDIGO, fill_opacity=0.5, stroke_width=1,
            )
            lbl = Text(str(s), font_size=16).next_to(bar, UP, buff=0.05)
            bars.add(VGroup(bar, lbl))
        bars.arrange(RIGHT, buff=0.3, aligned_edge=DOWN).next_to(title, DOWN, buff=0.5)
        for b in bars:
            self.play(FadeIn(b), run_time=0.3)

        # Analysis
        analysis = VGroup(
            Text("Resize costs: 1 + 2 + 4 + ... + 2^k < 2n", font_size=22, color=AMBER),
            Text("Total for n inserts = n (inserts) + 2n (resizes) = 3n", font_size=22),
            MathTex(r"\text{Amortised} = \frac{3n}{n} = O(1)", font_size=26, color=GREEN),
        ).arrange(DOWN, buff=0.15).next_to(bars, DOWN, buff=0.5)
        for a in analysis:
            self.play(Write(a), run_time=0.5)

        app = Text(
            "This is why ArrayList/vector/list have O(1) amortised append!",
            font_size=20, color=CORAL,
        ).to_edge(DOWN)
        self.play(Write(app))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene06_UnionFindSplay(Scene):
    """Amortised analysis of Union-Find and Splay Trees."""

    def construct(self):
        title = Text("Union-Find & Splay Trees", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        uf = VGroup(
            Text("Union-Find (with rank + path compression)", font_size=24, color=AMBER, weight=BOLD),
            Text("Actual worst per op: O(log n)", font_size=22),
            MathTex(r"\text{Amortised: } O(\alpha(n)) \approx O(1)", font_size=24, color=GREEN),
            Text("α(n) = inverse Ackermann — practically constant!", font_size=20, color=INDIGO),
        ).arrange(DOWN, buff=0.15).next_to(title, DOWN, buff=0.4)
        for u in uf:
            self.play(Write(u), run_time=0.4)

        splay = VGroup(
            Text("Splay Trees", font_size=24, color=CORAL, weight=BOLD),
            Text("Single op worst case: O(n)", font_size=22),
            Text("m operations on n nodes: O(m log n) total", font_size=22),
            MathTex(r"\text{Amortised: } O(\log n)", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.15).next_to(uf, DOWN, buff=0.4)
        for s in splay:
            self.play(Write(s), run_time=0.4)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene07_WhichMethod(Scene):
    """When to use which amortised analysis method."""

    def construct(self):
        title = Text("Which Method to Use?", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["Aggregate", "Total easy to bound", "Easiest"],
            ["Accounting", "Different op costs", "Medium"],
            ["Potential", "Rigorous proofs", "Hardest"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Method", font_size=22, weight=BOLD),
                Text("Best When", font_size=22, weight=BOLD),
                Text("Difficulty", font_size=22, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.6).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(table))

        tip = Text(
            "For GATE: aggregate usually suffices!",
            font_size=24, color=AMBER,
        ).to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
