"""
Chapter 10: String Matching Algorithms
Manim CE animation scenes covering all concepts.

Render: manim -pqh scene_10_string_matching.py <SceneName>
"""

from manim import *
import numpy as np

TEAL = "#1a8a8a"
CORAL = "#d94f4f"
AMBER = "#e8a317"
INDIGO = "#4a5da8"
GREEN = "#2e8b57"


class Scene01_NaiveMatching(Scene):
    """Naive string matching: slide pattern one by one."""

    def construct(self):
        title = Text("Naive String Matching", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Text and pattern
        text_str = "AAAAAB"
        pattern_str = "AAB"

        text_boxes = VGroup()
        for c in text_str:
            sq = Square(side_length=0.6, stroke_color=INDIGO)
            t = Text(c, font_size=22)
            text_boxes.add(VGroup(sq, t))
        text_boxes.arrange(RIGHT, buff=0).next_to(title, DOWN, buff=0.6)
        text_label = Text("Text:", font_size=20, color=AMBER).next_to(text_boxes, LEFT, buff=0.3)
        self.play(FadeIn(text_boxes), Write(text_label))

        pat_boxes = VGroup()
        for c in pattern_str:
            sq = Square(side_length=0.6, stroke_color=CORAL)
            t = Text(c, font_size=22, color=CORAL)
            pat_boxes.add(VGroup(sq, t))
        pat_boxes.arrange(RIGHT, buff=0).next_to(text_boxes, DOWN, buff=0.3)
        pat_boxes.align_to(text_boxes, LEFT)
        pat_label = Text("Pattern:", font_size=20, color=CORAL).next_to(pat_boxes, LEFT, buff=0.3)
        self.play(FadeIn(pat_boxes), Write(pat_label))

        # Slide pattern
        for shift in range(len(text_str) - len(pattern_str) + 1):
            target_x = text_boxes[shift].get_left()[0]
            current_x = pat_boxes[0].get_left()[0]
            dx = target_x - current_x
            if abs(dx) > 0.01:
                self.play(pat_boxes.animate.shift(RIGHT * dx), run_time=0.3)

            match = True
            for j in range(len(pattern_str)):
                if text_str[shift + j] != pattern_str[j]:
                    text_boxes[shift + j][0].set_fill(CORAL, opacity=0.2)
                    self.play(text_boxes[shift + j][0].animate.set_fill(CORAL, opacity=0.2), run_time=0.2)
                    match = False
                    break
                else:
                    text_boxes[shift + j][0].set_fill(GREEN, opacity=0.2)
                    self.play(text_boxes[shift + j][0].animate.set_fill(GREEN, opacity=0.2), run_time=0.2)

            if match:
                found = Text(f"Match at shift {shift}!", font_size=22, color=GREEN)
                found.next_to(pat_boxes, DOWN, buff=0.3)
                self.play(Write(found))

            # Reset colors
            for i in range(len(text_str)):
                text_boxes[i][0].set_fill(WHITE, opacity=0)

        complexity = MathTex(
            r"\text{Worst: } O((n-m+1) \times m) = O(nm)",
            font_size=24, color=CORAL,
        ).to_edge(DOWN)
        self.play(Write(complexity))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene02_KMP_LPS(Scene):
    """KMP: build the LPS (failure function) array step by step."""

    def construct(self):
        title = Text("KMP — LPS Array Construction", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        pattern = "ABCABD"
        pat_boxes = VGroup()
        for c in pattern:
            sq = Square(side_length=0.7, stroke_color=INDIGO)
            t = Text(c, font_size=24)
            pat_boxes.add(VGroup(sq, t))
        pat_boxes.arrange(RIGHT, buff=0).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(pat_boxes))

        # Index labels
        idx_labels = VGroup()
        for i in range(len(pattern)):
            lbl = Text(str(i), font_size=16, color=AMBER).next_to(pat_boxes[i], UP, buff=0.05)
            idx_labels.add(lbl)
        self.play(FadeIn(idx_labels))

        # LPS values
        lps = [0, 0, 0, 1, 2, 0]
        lps_boxes = VGroup()
        for v in lps:
            sq = Square(side_length=0.7, stroke_color=GREEN)
            t = Text(str(v), font_size=24, color=GREEN)
            lps_boxes.add(VGroup(sq, t))
        lps_boxes.arrange(RIGHT, buff=0).next_to(pat_boxes, DOWN, buff=0.3)
        lps_label = Text("LPS:", font_size=20, color=GREEN).next_to(lps_boxes, LEFT, buff=0.3)

        for i, box in enumerate(lps_boxes):
            self.play(FadeIn(box), run_time=0.4)
        self.play(Write(lps_label))

        explanation = VGroup(
            Text("LPS[i] = longest proper prefix that is also suffix", font_size=20, color=AMBER),
            Text('P="ABCABD": AB is prefix & suffix of ABCAB => LPS[4]=2', font_size=18),
        ).arrange(DOWN, buff=0.1).next_to(lps_boxes, DOWN, buff=0.4)
        self.play(Write(explanation))

        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene03_KMP_Search(Scene):
    """KMP search: O(n+m) with failure function skip."""

    def construct(self):
        title = Text("KMP Search — O(n + m)", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        key_insight = VGroup(
            Text("Key insight: on mismatch, don't restart!", font_size=24, color=CORAL),
            Text("Use LPS to skip already-matched prefix", font_size=22, color=GREEN),
        ).arrange(DOWN, buff=0.1).next_to(title, DOWN, buff=0.4)
        self.play(Write(key_insight))

        why_linear = VGroup(
            Text("Why O(n)?", font_size=24, color=AMBER, weight=BOLD),
            Text("Each step: either i advances (at most n times)", font_size=20),
            Text("  or j decreases (at most n times total)", font_size=20),
            Text("Total steps <= 2n => O(n)", font_size=22, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(key_insight, DOWN, buff=0.4)
        for w in why_linear:
            self.play(Write(w), run_time=0.4)

        complexity = VGroup(
            Text("Preprocessing: O(m) — building LPS", font_size=20),
            Text("Matching: O(n)", font_size=20),
            Text("Total: O(n + m)", font_size=22, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN)
        self.play(Write(complexity))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene04_RabinKarp(Scene):
    """Rabin-Karp: rolling hash for string matching."""

    def construct(self):
        title = Text("Rabin-Karp Algorithm", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        idea = Text(
            "Use hashing to compare pattern with text windows",
            font_size=22, color=AMBER,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(idea))

        hash_formula = MathTex(
            r"h(s{+}1) = d \times (h(s) - T[s] \times d^{m-1}) + T[s{+}m]",
            font_size=24, color=GREEN,
        ).next_to(idea, DOWN, buff=0.3)
        label = Text("Rolling hash update — O(1) per slide", font_size=20, color=INDIGO)
        label.next_to(hash_formula, DOWN, buff=0.15)
        self.play(Write(hash_formula), Write(label))

        complexity = VGroup(
            Text("Best/Average: O(n + m)", font_size=22, color=GREEN),
            Text("Worst: O(nm) — many hash collisions", font_size=22, color=CORAL),
            Text("Great for multiple pattern search!", font_size=22, color=AMBER),
        ).arrange(DOWN, buff=0.15).next_to(label, DOWN, buff=0.4)
        for c in complexity:
            self.play(Write(c), run_time=0.4)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene05_FiniteAutomaton(Scene):
    """Finite automaton based matching."""

    def construct(self):
        title = Text("Finite Automaton Matching", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        idea = VGroup(
            Text("Build a DFA for the pattern", font_size=24, color=AMBER),
            Text("Process text through DFA in single pass", font_size=22),
        ).arrange(DOWN, buff=0.15).next_to(title, DOWN, buff=0.5)
        self.play(Write(idea))

        complexity = VGroup(
            Text("Preprocessing: O(m|Σ|) — transition table", font_size=22, color=CORAL),
            Text("Matching: O(n) — one pass", font_size=22, color=GREEN),
            Text("Space: O(m|Σ|)", font_size=22),
        ).arrange(DOWN, buff=0.15).next_to(idea, DOWN, buff=0.4)
        for c in complexity:
            self.play(Write(c), run_time=0.4)

        vs_kmp = Text(
            "KMP uses O(m) space vs O(m|Σ|) for automaton",
            font_size=22, color=INDIGO,
        ).to_edge(DOWN)
        self.play(Write(vs_kmp))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene06_StringMatchingComparison(Scene):
    """Comparison table of all string matching algorithms."""

    def construct(self):
        title = Text("String Matching — Comparison", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["Naive", "None", "O(nm)", "O(1)"],
            ["KMP", "O(m)", "O(n)", "O(m)"],
            ["Rabin-Karp", "O(m)", "O(n) avg", "O(1)"],
            ["FA", "O(m|Σ|)", "O(n)", "O(m|Σ|)"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Algorithm", font_size=20, weight=BOLD),
                Text("Preprocess", font_size=20, weight=BOLD),
                Text("Match", font_size=20, weight=BOLD),
                Text("Space", font_size=20, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.55).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(table))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
