"""
Scene 02: Linear Seating Arrangements
======================================
Manim CE script — covers Chapter 2 concepts:
  2.1 What is a Linear Arrangement (endpoints property)
  2.2 Direction Convention (North / South flip)
  2.3 Position Mathematics (formulas with derivation)
  2.4 Solved Example — Basic Linear (GATE Style) step-by-step
  2.5 Edge Cases (left-of vs immediately-left, odd/even middle)
  2.6 The L + R = n + 1 Identity (visual proof)
  2.7 The Swap Trick
  2.8 Tricks summary

Render all:  manim -pqh scene_02_linear.py
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


# ====================================================================
# Scene 2.1 — What Is a Linear Arrangement?
# ====================================================================
class LinearBasics(Scene):
    """
    Shows a straight row, highlights endpoints vs middle seats,
    and the key property: endpoints have 1 neighbour.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Linear Arrangement — The Basics", font_size=36, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # ── Build a row of 6 seats ──────────────────────────────
        n = 6
        seats = self._row(n)
        seats.move_to(UP * 0.5)
        self.play(*[FadeIn(s, shift=UP) for s in seats])
        self.wait(0.5)

        # ── Highlight endpoints ─────────────────────────────────
        end_l = SurroundingRectangle(seats[0], color=CORAL, buff=0.05)
        end_r = SurroundingRectangle(seats[n - 1], color=CORAL, buff=0.05)
        end_label = Text("END positions: 1 neighbour only", font_size=20, color=CORAL)
        end_label.next_to(seats, DOWN, buff=0.4)
        self.play(Create(end_l), Create(end_r), Write(end_label))
        self.wait(0.5)

        # ── Highlight middle seats ──────────────────────────────
        mid_rects = VGroup(*[
            SurroundingRectangle(seats[i], color=GREEN, buff=0.05)
            for i in range(1, n - 1)
        ])
        mid_label = Text("MIDDLE positions: 2 neighbours each", font_size=20, color=GREEN)
        mid_label.next_to(end_label, DOWN, buff=0.3)
        self.play(
            *[Create(r) for r in mid_rects],
            Write(mid_label)
        )
        self.wait(1)

        # ── Contrast with circular ──────────────────────────────
        contrast = Text(
            "Key difference from circular: Linear has TWO endpoints,\n"
            "Circular has NONE (wraps around).",
            font_size=20, color=INDIGO
        )
        contrast.to_edge(DOWN, buff=0.5)
        self.play(Write(contrast))
        self.wait(2)

    @staticmethod
    def _row(n):
        seats = VGroup()
        for i in range(n):
            sq = Square(side_length=0.7, stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.08)
            t = Text(str(i + 1), font_size=20, color=TEAL)
            t.move_to(sq)
            seats.add(VGroup(sq, t))
        seats.arrange(RIGHT, buff=0.05)
        return seats


# ====================================================================
# Scene 2.2 — Direction Convention (North / South)
# ====================================================================
class DirectionConvention(Scene):
    """
    Side-by-side: all facing North vs all facing South.
    Shows how left/right flip on paper.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Direction Convention: North vs South", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        n = 5

        # ── North-facing row ────────────────────────────────────
        north_label = Text("All Face NORTH", font_size=22, color=TEAL)
        north_row = self._labeled_row(n, TEAL)
        north_arrow = Arrow(LEFT * 0.5, RIGHT * 0.5, color=TEAL, stroke_width=3)
        north_dir = Text("Right", font_size=16, color=TEAL)
        north_dir_l = Text("Left", font_size=16, color=TEAL)
        north_arrow_grp = VGroup(north_dir_l, north_arrow, north_dir).arrange(RIGHT, buff=0.1)

        face_arrow_n = Arrow(DOWN * 0.3, UP * 0.5, color=TEAL, stroke_width=2)
        face_label_n = Text("Facing", font_size=12, color=TEAL)

        north_grp = VGroup(north_label, north_row, north_arrow_grp).arrange(DOWN, buff=0.3)
        north_grp.shift(LEFT * 3.5 + DOWN * 0.5)

        face_arrow_n.next_to(north_row, RIGHT, buff=0.3)
        face_label_n.next_to(face_arrow_n, RIGHT, buff=0.1)

        # ── South-facing row ───────────────────────────────────
        south_label = Text("All Face SOUTH", font_size=22, color=CORAL)
        south_row = self._labeled_row(n, CORAL)
        south_arrow = Arrow(LEFT * 0.5, RIGHT * 0.5, color=CORAL, stroke_width=3)
        south_dir = Text("Left", font_size=16, color=CORAL)
        south_dir_l = Text("Right", font_size=16, color=CORAL)
        south_arrow_grp = VGroup(south_dir_l, south_arrow, south_dir).arrange(RIGHT, buff=0.1)

        face_arrow_s = Arrow(UP * 0.3, DOWN * 0.5, color=CORAL, stroke_width=2)
        face_label_s = Text("Facing", font_size=12, color=CORAL)

        south_grp = VGroup(south_label, south_row, south_arrow_grp).arrange(DOWN, buff=0.3)
        south_grp.shift(RIGHT * 3.5 + DOWN * 0.5)

        face_arrow_s.next_to(south_row, RIGHT, buff=0.3)
        face_label_s.next_to(face_arrow_s, RIGHT, buff=0.1)

        # ── Animate ─────────────────────────────────────────────
        self.play(
            FadeIn(north_grp, shift=DOWN),
            FadeIn(face_arrow_n), FadeIn(face_label_n)
        )
        self.play(
            FadeIn(south_grp, shift=DOWN),
            FadeIn(face_arrow_s), FadeIn(face_label_s)
        )
        self.wait(1)

        # ── Key insight ─────────────────────────────────────────
        insight = Text(
            "Facing South: Left/Right on paper are REVERSED!\n"
            "left (person) = right (paper),  right (person) = left (paper)",
            font_size=20, color=AMBER
        )
        insight.to_edge(DOWN, buff=0.4)
        self.play(Write(insight))
        self.wait(2)

    @staticmethod
    def _labeled_row(n, color):
        seats = VGroup()
        for i in range(n):
            sq = Square(side_length=0.6, stroke_color=color, fill_color=color, fill_opacity=0.08)
            t = Text(str(i + 1), font_size=18, color=color)
            t.move_to(sq)
            seats.add(VGroup(sq, t))
        seats.arrange(RIGHT, buff=0.03)
        return seats


# ====================================================================
# Scene 2.3 — Position Mathematics
# ====================================================================
class PositionMathematics(Scene):
    """
    Visual derivation of the position formulas.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Position Formulas — Derivation", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        n = 7
        seats = VGroup()
        for i in range(n):
            sq = Square(side_length=0.65, stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.06)
            t = Text(str(i + 1), font_size=18, color=TEAL)
            t.move_to(sq)
            seats.add(VGroup(sq, t))
        seats.arrange(RIGHT, buff=0.03)
        seats.move_to(UP * 1.5)

        dir_arrow = Arrow(LEFT * 0.5, UP * 0.5, color=TEAL, stroke_width=2)
        dir_label = Text("Facing North", font_size=14, color=TEAL)
        dir_arrow.next_to(seats, RIGHT, buff=0.3)
        dir_label.next_to(dir_arrow, RIGHT, buff=0.1)

        self.play(*[FadeIn(s) for s in seats], FadeIn(dir_arrow), FadeIn(dir_label))

        # ── Highlight person at position 5 ──────────────────────
        hl = SurroundingRectangle(seats[4], color=CORAL, buff=0.04)
        p_label = Text("Person X at position 5", font_size=18, color=CORAL)
        p_label.next_to(hl, UP, buff=0.2)
        self.play(Create(hl), Write(p_label))
        self.wait(0.5)

        # ── k places to the LEFT (facing North) ────────────────
        # Left = decreasing positions
        k = 2
        target_pos = 5 - k  # = 3
        hl_target = SurroundingRectangle(seats[target_pos - 1], color=GREEN, buff=0.04)
        brace = BraceBetweenPoints(
            seats[target_pos - 1].get_top() + UP * 0.4,
            seats[4].get_top() + UP * 0.4,
            direction=UP, color=AMBER
        )
        brace_label = Text("k = 2 places", font_size=14, color=AMBER)
        brace_label.next_to(brace, UP, buff=0.1)

        formula1 = MathTex(
            r"\text{Position} = p - k = 5 - 2 = 3",
            font_size=28, color=GREEN
        )
        formula1.next_to(seats, DOWN, buff=0.8)

        self.play(Create(hl_target), Create(brace), Write(brace_label))
        self.play(Write(formula1))
        self.wait(1)

        # ── Clear and show "between" formula ────────────────────
        self.play(
            FadeOut(hl), FadeOut(hl_target), FadeOut(p_label),
            FadeOut(brace), FadeOut(brace_label), FadeOut(formula1)
        )

        # Highlight positions 2 and 6
        hl2 = SurroundingRectangle(seats[1], color=CORAL, buff=0.04)
        hl6 = SurroundingRectangle(seats[5], color=CORAL, buff=0.04)
        between_brace = BraceBetweenPoints(
            seats[2].get_bottom() + DOWN * 0.15,
            seats[4].get_bottom() + DOWN * 0.15,
            direction=DOWN, color=INDIGO
        )
        between_text = Text("3, 4, 5 are between 2 and 6", font_size=18, color=INDIGO)
        between_text.next_to(between_brace, DOWN, buff=0.15)

        formula2 = MathTex(
            r"\text{People between} = |p_1 - p_2| - 1 = |2 - 6| - 1 = 3",
            font_size=26, color=INDIGO
        )
        formula2.next_to(between_text, DOWN, buff=0.3)

        self.play(Create(hl2), Create(hl6))
        self.play(Create(between_brace), Write(between_text))
        self.play(Write(formula2))
        self.wait(1)

        # ── Formula summary ─────────────────────────────────────
        self.play(*[FadeOut(m) for m in self.mobjects if m != title])

        formulas = VGroup(
            MathTex(r"\text{Facing North, } k \text{ left: } p - k", font_size=26, color=TEAL),
            MathTex(r"\text{Facing North, } k \text{ right: } p + k", font_size=26, color=TEAL),
            MathTex(r"\text{Facing South, } k \text{ left: } p + k", font_size=26, color=CORAL),
            MathTex(r"\text{Facing South, } k \text{ right: } p - k", font_size=26, color=CORAL),
            MathTex(r"\text{People between: } |p_1 - p_2| - 1", font_size=26, color=INDIGO),
            MathTex(r"\text{Middle position: } \lceil n/2 \rceil \text{ (odd } n \text{)}", font_size=26, color=GREEN),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        formulas.move_to(ORIGIN)

        self.play(*[Write(f) for f in formulas], run_time=2)

        note = Text("South = flip the sign!", font_size=22, color=CORAL)
        note.to_edge(DOWN, buff=0.5)
        self.play(Write(note))
        self.wait(2)


# ====================================================================
# Scene 2.4 — Solved Example (GATE Style)
# ====================================================================
class LinearSolvedExample(Scene):
    """
    Animate the step-by-step solution of a 6-person linear problem.
    P, Q, R, S, T, U face North.
    Clues:
      1. P sits at position 2
      2. Q is immediately to the right of P
      3. S sits at an end
      4. R is 3rd from the right
      5. T is not adjacent to S
      6. U takes the remaining seat
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Solved Example: 6-Person Linear (GATE)", font_size=32, color=DARK)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))

        n = 6
        row = self._build_row(n)
        row.move_to(UP * 1.5)
        self.play(*[FadeIn(s) for s in row])

        clues_text = [
            "1. P sits at position 2",
            "2. Q is immediately right of P",
            "3. S sits at an end",
            "4. R is 3rd from the right",
            "5. T is not adjacent to S",
            "6. U takes the remaining seat",
        ]
        clue_group = VGroup(*[
            Text(c, font_size=16, color=DARK) for c in clues_text
        ]).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        clue_group.to_edge(LEFT, buff=0.5).shift(DOWN * 0.5)

        self.play(FadeIn(clue_group))

        # ── Step 1: Place P at position 2 ──────────────────────
        step_label = Text("Step 1: P at pos 2 (definite)", font_size=18, color=TEAL)
        step_label.to_edge(RIGHT, buff=0.5).shift(UP * 0.5)
        self.play(Write(step_label))

        p_text = Text("P", font_size=22, color=TEAL)
        p_text.move_to(row[1])  # position 2 = index 1
        self.play(FadeIn(p_text, scale=1.5))
        self.play(clue_group[0].animate.set_color(GREEN))
        self.wait(0.5)

        # ── Step 2: Q immediately right of P -> pos 3 ──────────
        self.play(FadeOut(step_label))
        step_label = Text("Step 2: Q right of P -> pos 3", font_size=18, color=CORAL)
        step_label.to_edge(RIGHT, buff=0.5).shift(UP * 0.5)
        self.play(Write(step_label))

        q_text = Text("Q", font_size=22, color=CORAL)
        q_text.move_to(row[2])  # position 3
        self.play(FadeIn(q_text, scale=1.5))
        self.play(clue_group[1].animate.set_color(GREEN))
        self.wait(0.5)

        # ── Step 3: R is 3rd from right -> pos 4 ───────────────
        # 3rd from right in 6 seats = position 6 - 3 + 1 = 4
        self.play(FadeOut(step_label))
        step_label = Text("Step 3: R 3rd from right -> pos 4", font_size=18, color=AMBER)
        step_label.to_edge(RIGHT, buff=0.5).shift(UP * 0.5)
        self.play(Write(step_label))

        formula = MathTex(
            r"L + R = n + 1 \Rightarrow L = 6 + 1 - 3 = 4",
            font_size=22, color=AMBER
        )
        formula.to_edge(RIGHT, buff=0.3).shift(DOWN * 0.2)
        self.play(Write(formula))

        r_text = Text("R", font_size=22, color=AMBER)
        r_text.move_to(row[3])  # position 4
        self.play(FadeIn(r_text, scale=1.5))
        self.play(clue_group[3].animate.set_color(GREEN))
        self.wait(0.5)

        # ── Step 4: S at an end -> pos 1 or 6 ──────────────────
        self.play(FadeOut(step_label), FadeOut(formula))
        step_label = Text("Step 4: S at end -> pos 1 or 6", font_size=18, color=INDIGO)
        step_label.to_edge(RIGHT, buff=0.5).shift(UP * 0.5)
        self.play(Write(step_label))

        # Highlight both ends
        hl1 = SurroundingRectangle(row[0], color=INDIGO, buff=0.04)
        hl6 = SurroundingRectangle(row[5], color=INDIGO, buff=0.04)
        self.play(Create(hl1), Create(hl6))
        self.play(clue_group[2].animate.set_color(GREEN))
        self.wait(0.5)

        # ── Step 5: T not adjacent to S ─────────────────────────
        # If S at pos 1: T cannot be at pos 2 (taken by P anyway). Remaining: 5, 6.
        # If S at pos 6: T cannot be at pos 5. Remaining: 1, 5.
        # Try S at pos 1: T and U fill 5, 6. T adj S? pos1 adj pos2 only, T at 5 or 6 -> not adj. OK.
        # Try S at pos 6: T cannot be at 5. So T at 1, U at 5. T adj S? No (pos 1 and 6 not adj). OK.
        # Both work, but let's go with S=1 for demonstration.
        self.play(FadeOut(step_label), FadeOut(hl1), FadeOut(hl6))
        step_label = Text("Step 5: Try S at pos 1", font_size=18, color=GREEN)
        step_label.to_edge(RIGHT, buff=0.5).shift(UP * 0.5)
        self.play(Write(step_label))

        s_text = Text("S", font_size=22, color=INDIGO)
        s_text.move_to(row[0])  # position 1
        self.play(FadeIn(s_text, scale=1.5))

        # T not adjacent to S (pos 1). T cannot be at pos 2 (P). Remaining: 5, 6.
        # T at 5 or 6 -> neither adjacent to 1. Both valid. Place T at 5.
        t_text = Text("T", font_size=22, color=GREEN)
        t_text.move_to(row[4])  # position 5
        self.play(FadeIn(t_text, scale=1.5))
        self.play(clue_group[4].animate.set_color(GREEN))

        # U fills position 6
        u_text = Text("U", font_size=22, color=DARK)
        u_text.move_to(row[5])  # position 6
        self.play(FadeIn(u_text, scale=1.5))
        self.play(clue_group[5].animate.set_color(GREEN))

        self.play(FadeOut(step_label))
        final = Text(
            "Final: S  P  Q  R  T  U",
            font_size=26, color=GREEN
        )
        final.to_edge(DOWN, buff=0.5)
        self.play(Write(final))
        self.wait(2)

    @staticmethod
    def _build_row(n):
        seats = VGroup()
        for i in range(n):
            sq = Square(side_length=0.75, stroke_color=TEAL, fill_color=WHITE, fill_opacity=1)
            idx = Text(str(i + 1), font_size=14, color=DARK)
            idx.next_to(sq, DOWN, buff=0.08)
            seats.add(VGroup(sq, idx))
        seats.arrange(RIGHT, buff=0.08)
        return seats


# ====================================================================
# Scene 2.6 — The L + R = n + 1 Identity
# ====================================================================
class LRIdentity(Scene):
    """
    Visual proof that position_from_left + position_from_right = n + 1.
    Analogy: a ruler read from both ends.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("The L + R = n + 1 Identity", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        n = 7
        seats = VGroup()
        for i in range(n):
            sq = Square(side_length=0.7, stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.06)
            seats.add(sq)
        seats.arrange(RIGHT, buff=0.03)
        seats.move_to(UP * 0.8)

        # Left-numbered labels
        left_labels = VGroup()
        for i, s in enumerate(seats):
            t = Text(str(i + 1), font_size=16, color=GREEN)
            t.next_to(s, UP, buff=0.1)
            left_labels.add(t)

        left_arrow = Arrow(seats[0].get_left() + LEFT * 0.3 + UP * 0.4,
                           seats[-1].get_right() + RIGHT * 0.3 + UP * 0.4,
                           color=GREEN, stroke_width=2)
        left_tag = Text("From Left (L)", font_size=14, color=GREEN)
        left_tag.next_to(left_arrow, UP, buff=0.05)

        # Right-numbered labels
        right_labels = VGroup()
        for i, s in enumerate(seats):
            t = Text(str(n - i), font_size=16, color=CORAL)
            t.next_to(s, DOWN, buff=0.1)
            right_labels.add(t)

        right_arrow = Arrow(seats[-1].get_right() + RIGHT * 0.3 + DOWN * 0.4,
                            seats[0].get_left() + LEFT * 0.3 + DOWN * 0.4,
                            color=CORAL, stroke_width=2)
        right_tag = Text("From Right (R)", font_size=14, color=CORAL)
        right_tag.next_to(right_arrow, DOWN, buff=0.05)

        self.play(*[FadeIn(s) for s in seats])
        self.play(
            *[Write(t) for t in left_labels],
            GrowArrow(left_arrow), Write(left_tag)
        )
        self.play(
            *[Write(t) for t in right_labels],
            GrowArrow(right_arrow), Write(right_tag)
        )
        self.wait(0.5)

        # ── Highlight position 3 ────────────────────────────────
        idx = 2  # position 3 from left
        hl = SurroundingRectangle(seats[idx], color=AMBER, buff=0.04, stroke_width=3)
        self.play(Create(hl))

        proof = MathTex(
            r"L = 3, \quad R = 5",
            font_size=28, color=AMBER
        )
        proof.next_to(seats, DOWN, buff=1.2)

        result = MathTex(
            r"L + R = 3 + 5 = 8 = 7 + 1 = n + 1 \quad \checkmark",
            font_size=28, color=AMBER
        )
        result.next_to(proof, DOWN, buff=0.3)

        self.play(Write(proof))
        self.play(Write(result))
        self.wait(1)

        # ── General formula ─────────────────────────────────────
        general = MathTex(
            r"\boxed{L + R = n + 1}",
            font_size=36, color=GREEN
        )
        general.to_edge(DOWN, buff=0.5)
        self.play(Write(general))

        use_case = Text(
            "Use case: Convert 'X is 3rd from right' to position from left instantly",
            font_size=18, color=INDIGO
        )
        use_case.next_to(general, UP, buff=0.3)
        self.play(Write(use_case))
        self.wait(2)


# ====================================================================
# Scene 2.7 — The Swap Trick
# ====================================================================
class SwapTrick(Scene):
    """
    When two arrangements are possible, draw both cases in parallel
    and test clues against each until one contradicts.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("The Swap Trick: Parallel Cases", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # ── Scenario: S could be at pos 1 or pos 6 ─────────────
        scenario = Text(
            "From earlier: S sits at an END. Two possibilities:",
            font_size=20, color=DARK
        )
        scenario.next_to(title, DOWN, buff=0.4)
        self.play(Write(scenario))

        # Case 1
        case1_label = Text("Case 1: S at position 1", font_size=18, color=TEAL)
        case1_row = self._build_labeled_row(["S", "P", "Q", "R", "?", "?"], TEAL)
        case1 = VGroup(case1_label, case1_row).arrange(DOWN, buff=0.2)
        case1.shift(LEFT * 0 + UP * 0.3)

        # Case 2
        case2_label = Text("Case 2: S at position 6", font_size=18, color=CORAL)
        case2_row = self._build_labeled_row(["?", "P", "Q", "R", "?", "S"], CORAL)
        case2 = VGroup(case2_label, case2_row).arrange(DOWN, buff=0.2)
        case2.next_to(case1, DOWN, buff=0.6)

        self.play(FadeIn(case1, shift=LEFT))
        self.play(FadeIn(case2, shift=LEFT))
        self.wait(0.5)

        # ── Apply clue: T not adjacent to S ─────────────────────
        clue = Text('Apply: "T is NOT adjacent to S"', font_size=20, color=AMBER)
        clue.next_to(case2, DOWN, buff=0.5)
        self.play(Write(clue))

        # Case 1: S at 1, adj = pos 2 (P). T can be at 5 or 6. Both valid.
        check1 = Text("Case 1: T at 5 or 6 (not adj to 1). Valid.", font_size=16, color=GREEN)
        check1.next_to(case1, RIGHT, buff=0.5)

        # Case 2: S at 6, adj = pos 5. T cannot be at 5. T at 1. Valid.
        check2 = Text("Case 2: T at 1 (not adj to 6). Valid.", font_size=16, color=GREEN)
        check2.next_to(case2, RIGHT, buff=0.5)

        self.play(Write(check1), Write(check2))
        self.wait(1)

        strategy = Text(
            "STRATEGY: Keep both cases alive until a clue eliminates one.\n"
            "This avoids backtracking and saves exam time.",
            font_size=18, color=INDIGO
        )
        strategy.to_edge(DOWN, buff=0.3)
        self.play(Write(strategy))
        self.wait(2)

    @staticmethod
    def _build_labeled_row(labels, color):
        seats = VGroup()
        for lbl in labels:
            sq = Square(side_length=0.6, stroke_color=color, fill_color=color, fill_opacity=0.06)
            t = Text(lbl, font_size=18, color=color)
            t.move_to(sq)
            seats.add(VGroup(sq, t))
        seats.arrange(RIGHT, buff=0.03)
        return seats


# ====================================================================
# Scene 2.8 — Edge Cases
# ====================================================================
class LinearEdgeCases(Scene):
    """
    Three critical edge cases:
    1. 'left of' vs 'immediately to the left of'
    2. Odd vs even middle
    3. 'From left' vs 'from right'
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Linear Edge Cases", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # ── Edge Case 1 ────────────────────────────────────────
        ec1_title = Text('1. "left of" vs "immediately to the left of"', font_size=22, color=CORAL)
        ec1_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ec1_title))

        row = VGroup()
        for i in range(6):
            sq = Square(side_length=0.55, stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.06)
            t = Text(str(i + 1), font_size=16, color=TEAL)
            t.move_to(sq)
            row.add(VGroup(sq, t))
        row.arrange(RIGHT, buff=0.03)
        row.next_to(ec1_title, DOWN, buff=0.4)
        self.play(FadeIn(row))

        # "A is to the left of B" — A can be ANYWHERE to B's left
        a_positions = VGroup(*[
            SurroundingRectangle(row[i], color=GREEN, buff=0.03)
            for i in range(3)  # positions 1,2,3 are all "left of" position 4
        ])
        b_hl = SurroundingRectangle(row[3], color=CORAL, buff=0.03)

        explain1 = Text(
            '"A to the left of B" -> A at ANY position left of B (range)',
            font_size=16, color=GREEN
        )
        explain1.next_to(row, DOWN, buff=0.3)

        self.play(Create(b_hl), *[Create(a) for a in a_positions], Write(explain1))
        self.wait(1)

        # "A is immediately to the left of B" — A is at position 3 exactly
        self.play(FadeOut(a_positions), FadeOut(explain1))
        a_imm = SurroundingRectangle(row[2], color=AMBER, buff=0.03, stroke_width=3)
        explain2 = Text(
            '"Immediately left" -> A at exactly ONE position (p - 1)',
            font_size=16, color=AMBER
        )
        explain2.next_to(row, DOWN, buff=0.3)
        self.play(Create(a_imm), Write(explain2))
        self.wait(1)

        # ── Edge Case 2 ────────────────────────────────────────
        self.play(*[FadeOut(m) for m in self.mobjects if m != title])

        ec2_title = Text("2. Odd vs Even: Middle Position", font_size=22, color=INDIGO)
        ec2_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ec2_title))

        # Odd: 7 seats -> middle = 4
        odd_row = VGroup(*[
            Square(side_length=0.5, stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.06)
            for _ in range(7)
        ]).arrange(RIGHT, buff=0.03)
        odd_row.next_to(ec2_title, DOWN, buff=0.4).shift(LEFT * 2)
        odd_label = Text("n=7 (odd): middle = position 4", font_size=16, color=TEAL)
        odd_label.next_to(odd_row, DOWN, buff=0.2)
        odd_hl = SurroundingRectangle(odd_row[3], color=GREEN, buff=0.03)

        # Even: 6 seats -> no unique middle
        even_row = VGroup(*[
            Square(side_length=0.5, stroke_color=CORAL, fill_color=CORAL, fill_opacity=0.06)
            for _ in range(6)
        ]).arrange(RIGHT, buff=0.03)
        even_row.next_to(odd_label, DOWN, buff=0.4)
        even_label = Text("n=6 (even): NO unique middle!", font_size=16, color=CORAL)
        even_label.next_to(even_row, DOWN, buff=0.2)

        self.play(FadeIn(odd_row), Write(odd_label), Create(odd_hl))
        self.play(FadeIn(even_row), Write(even_label))

        formula = MathTex(
            r"\text{Middle} = \lceil n/2 \rceil \text{ (only meaningful for odd } n \text{)}",
            font_size=22, color=INDIGO
        )
        formula.to_edge(DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(2)
