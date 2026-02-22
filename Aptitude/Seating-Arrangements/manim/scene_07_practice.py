"""
Scene 07: GATE / ESE / PSU / BANK Practice Problems — Animated Solutions
==========================================================================
Manim CE script — covers Chapter 7:
  7.1 GATE Linear Problem (full walkthrough)
  7.2 GATE Circular Problem (full walkthrough)
  7.3 Banking Double-Row Problem (direction trap demo)
  7.4 Formula Quick Reference (animated)

Render all:  manim -pqh scene_07_practice.py
"""

from manim import *
import numpy as np

TEAL    = "#1a8a8a"
CORAL   = "#d94f4f"
AMBER   = "#e8a317"
INDIGO  = "#4a5da8"
GREEN   = "#2e8b57"
BG      = "#ffffff"
DARK    = "#1a1a2e"


def circle_positions(n, radius=2.0, start_angle=PI / 2):
    """Return n evenly-spaced points on a circle (top = first)."""
    return [
        radius * np.array([
            np.cos(start_angle - i * TAU / n),
            np.sin(start_angle - i * TAU / n),
            0
        ])
        for i in range(n)
    ]


# ====================================================================
# Scene 7.1 — GATE Linear Problem
# ====================================================================
class GATELinearProblem(Scene):
    """
    Problem G1: Five people (P, Q, R, S, T) sit in a row facing North.
      1. R sits in the middle
      2. P is immediately to the left of R
      3. Q sits at the right end
      4. S is not adjacent to Q
      5. T takes the remaining position

    Question: Who sits at the left end?
    Answer: S
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("GATE Practice: 5-Person Linear", font_size=30, color=DARK)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))

        # ── Problem statement ───────────────────────────────────
        problem = VGroup(
            Text("P, Q, R, S, T sit in a row facing North.", font_size=16, color=DARK),
            Text("1. R sits in the middle", font_size=14, color=DARK),
            Text("2. P is immediately to the left of R", font_size=14, color=DARK),
            Text("3. Q sits at the right end", font_size=14, color=DARK),
            Text("4. S is not adjacent to Q", font_size=14, color=DARK),
            Text("5. T takes remaining position", font_size=14, color=DARK),
            Text("Q: Who sits at the left end?", font_size=16, color=CORAL),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        problem.to_edge(LEFT, buff=0.4).shift(DOWN * 0.3)
        self.play(FadeIn(problem), run_time=1)

        # ── Build empty row ─────────────────────────────────────
        n = 5
        row = VGroup()
        for i in range(n):
            sq = Square(side_length=0.75, stroke_color=TEAL, fill_color=WHITE, fill_opacity=1)
            idx = Text(str(i + 1), font_size=12, color=DARK)
            idx.next_to(sq, DOWN, buff=0.06)
            row.add(VGroup(sq, idx))
        row.arrange(RIGHT, buff=0.06)
        row.shift(RIGHT * 2 + UP * 1.5)
        self.play(*[FadeIn(s) for s in row])

        steps_area = RIGHT * 2 + DOWN * 0.5

        # ── Step 1: R in middle (pos 3) ─────────────────────────
        step1 = Text("R at pos 3 (middle of 5)", font_size=16, color=TEAL)
        step1.move_to(steps_area)
        r_label = Text("R", font_size=22, color=TEAL)
        r_label.move_to(row[2][0])
        self.play(Write(step1), FadeIn(r_label, scale=1.5))
        self.play(problem[1].animate.set_color(GREEN))
        self.wait(0.3)

        # ── Step 2: P immediately left of R -> pos 2 ───────────
        self.play(FadeOut(step1))
        step2 = Text("P left of R -> pos 2", font_size=16, color=CORAL)
        step2.move_to(steps_area)
        p_label = Text("P", font_size=22, color=CORAL)
        p_label.move_to(row[1][0])
        self.play(Write(step2), FadeIn(p_label, scale=1.5))
        self.play(problem[2].animate.set_color(GREEN))
        self.wait(0.3)

        # ── Step 3: Q at right end -> pos 5 ─────────────────────
        self.play(FadeOut(step2))
        step3 = Text("Q at right end -> pos 5", font_size=16, color=AMBER)
        step3.move_to(steps_area)
        q_label = Text("Q", font_size=22, color=AMBER)
        q_label.move_to(row[4][0])
        self.play(Write(step3), FadeIn(q_label, scale=1.5))
        self.play(problem[3].animate.set_color(GREEN))
        self.wait(0.3)

        # ── Step 4: S not adjacent to Q ─────────────────────────
        # Q at pos 5. Adjacent = pos 4. S cannot be at pos 4.
        # Remaining: pos 1 and 4. S must be at pos 1.
        self.play(FadeOut(step3))
        step4 = Text("S not adj Q (pos5).\nRemaining: 1,4. S can't be 4 -> S=1", font_size=14, color=INDIGO)
        step4.move_to(steps_area)
        s_label = Text("S", font_size=22, color=INDIGO)
        s_label.move_to(row[0][0])
        self.play(Write(step4), FadeIn(s_label, scale=1.5))
        self.play(problem[4].animate.set_color(GREEN))
        self.wait(0.3)

        # ── Step 5: T remaining -> pos 4 ────────────────────────
        self.play(FadeOut(step4))
        t_label = Text("T", font_size=22, color=GREEN)
        t_label.move_to(row[3][0])
        self.play(FadeIn(t_label, scale=1.5))
        self.play(problem[5].animate.set_color(GREEN))

        # ── Answer ──────────────────────────────────────────────
        answer = Text("Answer: S sits at the left end", font_size=22, color=GREEN)
        answer.to_edge(DOWN, buff=0.4)
        hl = SurroundingRectangle(row[0], color=GREEN, buff=0.05, stroke_width=3)
        self.play(Create(hl), Write(answer))
        self.wait(2)


# ====================================================================
# Scene 7.2 — GATE Circular Problem
# ====================================================================
class GATECircularProblem(Scene):
    """
    Problem G2: Six people (A-F) sit around a table facing center.
      1. Fix A at top (anchor)
      2. C is opposite A
      3. B is immediately CW from A
      4. D is immediately ACW from C
      5. E is opposite B
      6. F takes remaining

    Q: Who is opposite D?
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("GATE Practice: 6-Person Circular", font_size=30, color=DARK)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))

        n = 6
        radius = 1.5
        positions = circle_positions(n, radius=radius)

        table = Circle(radius=0.7, stroke_color=DARK, stroke_width=1,
                       fill_color="#f5f5f5", fill_opacity=0.3)
        table.move_to(LEFT * 2.5 + DOWN * 0.3)

        seats = VGroup()
        for i, pos in enumerate(positions):
            shifted = pos + LEFT * 2.5 + DOWN * 0.3
            c = Circle(radius=0.27, stroke_color=TEAL, fill_color=WHITE, fill_opacity=1)
            c.move_to(shifted)
            num = Text(str(i + 1), font_size=12, color=DARK)
            num.move_to(shifted)
            seats.add(VGroup(c, num))

        self.play(Create(table), *[FadeIn(s) for s in seats])

        # Clues
        clues_text = [
            "1. A at top (pos 1) [anchor]",
            "2. C opposite A -> pos 4",
            "3. B imm. CW from A -> pos 2",
            "4. D imm. ACW from C -> pos 5",
            "5. E opposite B -> pos 5...",
            "   Wait: pos 5 = D! -> E at pos 5?",
            "   Recalc: Opposite of pos 2 = pos 5.",
            "   But D is at pos 5. Conflict!",
            "   Re-read: D ACW from C (pos 4) = pos 3",
            "   E opposite B (pos 2) = pos 5",
            "6. F remaining -> pos 6",
        ]

        # Actually let's do it cleanly:
        # pos 1: A (anchor)
        # pos 4: C (opposite A, since n/2 = 3, so pos 1+3 = 4)
        # pos 2: B (CW from A = next CW = pos 2)
        # D ACW from C: pos 4, ACW = pos 3
        # E opposite B: opposite of pos 2 = pos 2+3 = pos 5
        # F remaining: pos 6

        clean_clues = [
            "1. A at pos 1 (anchor)",
            "2. C opposite A -> pos 4",
            "3. B immediately CW from A -> pos 2",
            "4. D immediately ACW from C -> pos 3",
            "5. E opposite B -> pos 5",
            "6. F remaining -> pos 6",
            "Q: Who is opposite D (pos 3)?",
        ]
        clue_panel = VGroup(*[
            Text(c, font_size=12, color=DARK) for c in clean_clues
        ]).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        clue_panel.to_edge(RIGHT, buff=0.3).shift(UP * 0.3)
        self.play(FadeIn(clue_panel))

        # ── Place people step by step ───────────────────────────
        placement = [
            (0, "A", TEAL),
            (3, "C", CORAL),
            (1, "B", AMBER),
            (2, "D", INDIGO),
            (4, "E", GREEN),
            (5, "F", DARK),
        ]

        for step, (idx, name, color) in enumerate(placement):
            person = Text(name, font_size=20, color=color)
            person.move_to(seats[idx])
            self.play(
                FadeIn(person, scale=1.5),
                seats[idx][0].animate.set_stroke(color=color, width=3),
                clue_panel[step].animate.set_color(GREEN),
                run_time=0.5
            )
            self.wait(0.2)

        # ── Answer: opposite of D (pos 3) = pos 3+3 = pos 6 = F ──
        opp_line = DashedLine(
            seats[2].get_center(), seats[5].get_center(),
            dash_length=0.1, color=AMBER, stroke_width=2
        )
        self.play(Create(opp_line))

        answer = Text("Answer: F is opposite D", font_size=22, color=GREEN)
        answer.to_edge(DOWN, buff=0.4)
        self.play(Write(answer), clue_panel[6].animate.set_color(GREEN))
        self.wait(2)


# ====================================================================
# Scene 7.3 — Banking Double-Row Direction Trap
# ====================================================================
class BankingDoubleRowTrap(Scene):
    """
    Demonstrates the most common banking exam mistake:
    confusing directions between rows.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Banking Exam: Double-Row Direction Trap", font_size=28, color=DARK)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))

        # ── Setup ───────────────────────────────────────────────
        clue = Text(
            'Clue: "B is 2nd to the LEFT of A in Row 1 (facing South)"',
            font_size=18, color=DARK
        )
        clue.next_to(title, DOWN, buff=0.4)
        self.play(Write(clue))

        n = 5

        # ── WRONG interpretation ────────────────────────────────
        wrong_title = Text("WRONG: Using North convention", font_size=18, color=CORAL)
        wrong_row = VGroup()
        wrong_labels = ["_", "B", "_", "A", "_"]
        for lbl in wrong_labels:
            sq = Square(side_length=0.6, stroke_color=CORAL, fill_color=CORAL, fill_opacity=0.06)
            t = Text(lbl, font_size=18, color=CORAL)
            t.move_to(sq)
            wrong_row.add(VGroup(sq, t))
        wrong_row.arrange(RIGHT, buff=0.03)
        wrong_grp = VGroup(wrong_title, wrong_row).arrange(DOWN, buff=0.2)
        wrong_grp.shift(LEFT * 0 + DOWN * 0.5)

        cross = Cross(wrong_grp, stroke_color=CORAL, stroke_width=3)
        wrong_explain = Text(
            "North: left = paper-left = pos - k. So B at pos 2. WRONG!",
            font_size=14, color=CORAL
        )
        wrong_explain.next_to(wrong_grp, DOWN, buff=0.15)

        # ── RIGHT interpretation ────────────────────────────────
        right_title = Text("CORRECT: Using South convention", font_size=18, color=GREEN)
        right_row = VGroup()
        right_labels = ["_", "_", "_", "A", "_"]
        # South: left = +pos. B at pos 4+2 = 6? Wait, n=5.
        # If A at pos 4: B = 4+2 = 6 > 5. Invalid.
        # Let's set A at pos 2: B = 2+2 = 4.
        right_labels = ["_", "A", "_", "B", "_"]
        for lbl in right_labels:
            sq = Square(side_length=0.6, stroke_color=GREEN, fill_color=GREEN, fill_opacity=0.06)
            t = Text(lbl, font_size=18, color=GREEN)
            t.move_to(sq)
            right_row.add(VGroup(sq, t))
        right_row.arrange(RIGHT, buff=0.03)
        right_grp = VGroup(right_title, right_row).arrange(DOWN, buff=0.2)
        right_grp.next_to(wrong_explain, DOWN, buff=0.4)

        right_explain = Text(
            "South: left = paper-right = pos + k. A at pos 2, B at pos 4. CORRECT!",
            font_size=14, color=GREEN
        )
        right_explain.next_to(right_grp, DOWN, buff=0.15)

        self.play(FadeIn(wrong_grp, shift=LEFT))
        self.play(Create(cross), Write(wrong_explain))
        self.wait(0.5)
        self.play(FadeIn(right_grp, shift=LEFT), Write(right_explain))
        self.wait(1)

        takeaway = Text(
            "TAKEAWAY: Always check the facing direction BEFORE applying left/right!",
            font_size=18, color=AMBER
        )
        takeaway.to_edge(DOWN, buff=0.3)
        self.play(Write(takeaway))
        self.wait(2)


# ====================================================================
# Scene 7.4 — Formula Quick Reference
# ====================================================================
class FormulaQuickReference(Scene):
    """All formulas in one animated cheat sheet."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("All Formulas — Quick Reference", font_size=32, color=DARK)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))

        formulas = [
            (r"L + R = n + 1", "Position from left + right", TEAL),
            (r"\text{Between} = |p_1 - p_2| - 1", "Linear between count", TEAL),
            (r"\text{Middle} = \lceil n/2 \rceil", "Odd n only", TEAL),
            (r"\text{Circular: } (n-1)!", "Arrangements", CORAL),
            (r"\text{Opposite} = (p + n/2 - 1) \bmod n + 1", "Even n only", CORAL),
            (r"\text{Face N: left} = p - k", "North direction", INDIGO),
            (r"\text{Face S: left} = p + k", "South direction", INDIGO),
            (r"\text{Face center: Left = CW}", "Circular rule", AMBER),
            (r"\text{Face outward: Left = ACW}", "Circular rule", AMBER),
            (r"\text{Block positions} = n - m + 1", "Sliding block", GREEN),
        ]

        rows = VGroup()
        for latex, desc, color in formulas:
            formula = MathTex(latex, font_size=22, color=color)
            description = Text(desc, font_size=14, color=DARK)
            r = VGroup(formula, description).arrange(RIGHT, buff=0.5)
            rows.add(r)

        rows.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        rows.next_to(title, DOWN, buff=0.4)

        if rows.height > 5.5:
            rows.scale_to_fit_height(5.5)

        for r in rows:
            self.play(FadeIn(r, shift=RIGHT), run_time=0.35)

        self.wait(3)
