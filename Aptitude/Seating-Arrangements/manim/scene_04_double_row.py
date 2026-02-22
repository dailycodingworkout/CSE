"""
Scene 04: Double-Row Seating Arrangements
==========================================
Manim CE script — covers Chapter 4 concepts:
  4.1 What is a Double-Row Arrangement (two rows facing each other)
  4.2 The Direction Convention — The Master Trap
  4.3 The "Faces" / "Opposite" Concept
  4.4 Position Mathematics
  4.5 Solved Example — Standard Double Row
  4.6 Facing Pair Technique
  4.7 Common Traps

Render all:  manim -pqh scene_04_double_row.py
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
# Scene 4.1 — Double Row Basics
# ====================================================================
class DoubleRowBasics(Scene):
    """
    Two parallel rows facing each other.
    Row 1 faces South, Row 2 faces North.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Double-Row Arrangement", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        subtitle = Text(
            "Two rows facing each other — Most tested in Banking exams",
            font_size=20, color=INDIGO
        )
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))

        n = 5  # people per row

        # ── Row 1 (top, faces South) ────────────────────────────
        row1_label = Text("Row 1: Faces SOUTH", font_size=18, color=TEAL)
        row1 = self._build_row(n, TEAL)
        face_arrows_1 = VGroup()
        for seat in row1:
            a = Arrow(seat.get_bottom(), seat.get_bottom() + DOWN * 0.4,
                      stroke_width=2, color=TEAL, buff=0,
                      max_tip_length_to_length_ratio=0.3)
            face_arrows_1.add(a)

        row1_group = VGroup(row1_label, row1).arrange(DOWN, buff=0.2)
        row1_group.shift(UP * 1.0)

        # ── Row 2 (bottom, faces North) ─────────────────────────
        row2_label = Text("Row 2: Faces NORTH", font_size=18, color=CORAL)
        row2 = self._build_row(n, CORAL)
        face_arrows_2 = VGroup()
        for seat in row2:
            a = Arrow(seat.get_top(), seat.get_top() + UP * 0.4,
                      stroke_width=2, color=CORAL, buff=0,
                      max_tip_length_to_length_ratio=0.3)
            face_arrows_2.add(a)

        row2_group = VGroup(row2, row2_label).arrange(DOWN, buff=0.2)
        row2_group.shift(DOWN * 1.2)

        # Position them so rows face each other
        self.play(FadeIn(row1_group), *[GrowArrow(a) for a in face_arrows_1])
        self.play(FadeIn(row2_group), *[GrowArrow(a) for a in face_arrows_2])

        # ── Facing pairs ────────────────────────────────────────
        facing_lines = VGroup()
        for i in range(n):
            line = DashedLine(
                row1[i].get_bottom() + DOWN * 0.45,
                row2[i].get_top() + UP * 0.45,
                dash_length=0.08, color=AMBER, stroke_width=1.5
            )
            facing_lines.add(line)

        facing_label = Text("Position k in Row 1 FACES position k in Row 2",
                            font_size=18, color=AMBER)
        facing_label.to_edge(DOWN, buff=0.5)

        self.play(*[Create(l) for l in facing_lines], Write(facing_label))
        self.wait(2)

    @staticmethod
    def _build_row(n, color):
        seats = VGroup()
        for i in range(n):
            sq = Square(side_length=0.65, stroke_color=color, fill_color=color, fill_opacity=0.08)
            t = Text(str(i + 1), font_size=18, color=color)
            t.move_to(sq)
            seats.add(VGroup(sq, t))
        seats.arrange(RIGHT, buff=0.05)
        return seats


# ====================================================================
# Scene 4.2 — The Direction Convention (Master Trap)
# ====================================================================
class DirectionTrap(Scene):
    """
    The MOST important rule in double-row:
    Directions are OPPOSITE between the two rows on paper.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("The Master Trap: Opposite Directions", font_size=32, color=CORAL)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        n = 5

        # ── Row 1 (faces South) ─────────────────────────────────
        row1 = self._labeled_row(n, TEAL)
        row1.shift(UP * 1.2)
        r1_label = Text("Row 1: Facing South", font_size=16, color=TEAL)
        r1_label.next_to(row1, LEFT, buff=0.3)

        # South-facing: left = paper-right, right = paper-left
        r1_left = Text("Left (person's)", font_size=14, color=GREEN)
        r1_right = Text("Right (person's)", font_size=14, color=CORAL)
        r1_arrow = Arrow(row1.get_left() + LEFT * 0.2, row1.get_right() + RIGHT * 0.2,
                         color=GREEN, stroke_width=2)
        r1_left.next_to(r1_arrow.get_end(), RIGHT, buff=0.1)
        r1_right_arr = Arrow(row1.get_right() + RIGHT * 0.2, row1.get_left() + LEFT * 0.2,
                             color=CORAL, stroke_width=2)
        r1_right.next_to(r1_right_arr.get_end(), LEFT, buff=0.1)

        r1_left.next_to(row1, UP, buff=0.15).shift(RIGHT * 2)
        r1_right.next_to(row1, UP, buff=0.15).shift(LEFT * 2)
        r1_lr_arrow = Arrow(LEFT * 2.5, RIGHT * 2.5, color=GREEN, stroke_width=2)
        r1_lr_arrow.next_to(row1, UP, buff=0.5)
        r1_left_end = Text("Right", font_size=12, color=CORAL).next_to(r1_lr_arrow, LEFT, buff=0.1)
        r1_right_end = Text("Left", font_size=12, color=GREEN).next_to(r1_lr_arrow, RIGHT, buff=0.1)

        # ── Row 2 (faces North) ─────────────────────────────────
        row2 = self._labeled_row(n, CORAL)
        row2.shift(DOWN * 1.2)
        r2_label = Text("Row 2: Facing North", font_size=16, color=CORAL)
        r2_label.next_to(row2, LEFT, buff=0.3)

        # North-facing: left = paper-left, right = paper-right
        r2_lr_arrow = Arrow(RIGHT * 2.5, LEFT * 2.5, color=GREEN, stroke_width=2)
        r2_lr_arrow.next_to(row2, DOWN, buff=0.5)
        r2_left_end = Text("Left", font_size=12, color=GREEN).next_to(r2_lr_arrow, LEFT, buff=0.1)
        r2_right_end = Text("Right", font_size=12, color=CORAL).next_to(r2_lr_arrow, RIGHT, buff=0.1)

        # ── Animate ─────────────────────────────────────────────
        self.play(FadeIn(row1), Write(r1_label))
        self.play(
            GrowArrow(r1_lr_arrow), Write(r1_left_end), Write(r1_right_end)
        )
        self.play(FadeIn(row2), Write(r2_label))
        self.play(
            GrowArrow(r2_lr_arrow), Write(r2_left_end), Write(r2_right_end)
        )

        # ── The rule ────────────────────────────────────────────
        rule_box = RoundedRectangle(
            corner_radius=0.1, width=9, height=1.2,
            stroke_color=AMBER, fill_color=AMBER, fill_opacity=0.1
        )
        rule_text = Text(
            "Row 1 (South): left = +position  |  Row 2 (North): left = -position\n"
            "DIRECTIONS ARE OPPOSITE ON PAPER!",
            font_size=16, color=DARK
        )
        rule_text.move_to(rule_box)
        rule_group = VGroup(rule_box, rule_text)
        rule_group.to_edge(DOWN, buff=0.3)

        self.play(FadeIn(rule_group))

        # ── Mnemonic ────────────────────────────────────────────
        mnemonic = Text(
            'Mnemonic: "North-Left-West" — Facing North, Left is West (paper-left)',
            font_size=16, color=INDIGO
        )
        mnemonic.next_to(rule_group, UP, buff=0.2)
        self.play(Write(mnemonic))
        self.wait(2)

    @staticmethod
    def _labeled_row(n, color):
        seats = VGroup()
        for i in range(n):
            sq = Square(side_length=0.6, stroke_color=color, fill_color=color, fill_opacity=0.06)
            t = Text(str(i + 1), font_size=16, color=color)
            t.move_to(sq)
            seats.add(VGroup(sq, t))
        seats.arrange(RIGHT, buff=0.03)
        return seats


# ====================================================================
# Scene 4.3 — Position Mathematics
# ====================================================================
class DoubleRowFormulas(Scene):
    """Position formulas for double-row with visual derivation."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("Double-Row Position Formulas", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        formulas = VGroup(
            Text("Row 1 (Facing South):", font_size=20, color=TEAL),
            MathTex(r"k \text{ to LEFT: position} = p + k", font_size=24, color=TEAL),
            MathTex(r"k \text{ to RIGHT: position} = p - k", font_size=24, color=TEAL),
            Text("", font_size=10),
            Text("Row 2 (Facing North):", font_size=20, color=CORAL),
            MathTex(r"k \text{ to LEFT: position} = p - k", font_size=24, color=CORAL),
            MathTex(r"k \text{ to RIGHT: position} = p + k", font_size=24, color=CORAL),
            Text("", font_size=10),
            Text("Cross-row:", font_size=20, color=AMBER),
            MathTex(r"\text{Person at pos } k \text{ in Row 1 FACES pos } k \text{ in Row 2}",
                    font_size=22, color=AMBER),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        formulas.next_to(title, DOWN, buff=0.5)

        for f in formulas:
            self.play(Write(f), run_time=0.5)

        insight = Text(
            "KEY INSIGHT: South swaps the sign! Compare with linear:\n"
            "North: left = -k | South: left = +k",
            font_size=18, color=INDIGO
        )
        insight.to_edge(DOWN, buff=0.4)
        self.play(Write(insight))
        self.wait(2)


# ====================================================================
# Scene 4.5 — Solved Example
# ====================================================================
class DoubleRowSolvedExample(Scene):
    """
    8 people (A-D in Row 1 facing South, P-S in Row 2 facing North).
    Clues:
      1. A sits at 2nd position from the left end of Row 1
      2. P faces A
      3. B is immediately to the left of A (Row 1, South: left = +pos -> B at pos 3)
      4. Q is immediately to the right of P (Row 2, North: right = +pos -> Q at pos 3)
      5. C sits at an end of Row 1
      6. S faces C
      7. D takes remaining in Row 1, R takes remaining in Row 2
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Solved Example: 4+4 Double Row", font_size=30, color=DARK)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))

        n = 4

        # ── Build rows ─────────────────────────────────────────
        row1 = self._build_row(n, TEAL, "Row 1 (South)")
        row1.shift(UP * 1.0)
        row2 = self._build_row(n, CORAL, "Row 2 (North)")
        row2.shift(DOWN * 1.0)

        self.play(FadeIn(row1), FadeIn(row2))

        # Clues panel
        clues = [
            "1. A at 2nd from left of Row 1",
            "2. P faces A",
            "3. B imm. left of A (South: pos+1=3)",
            "4. Q imm. right of P (North: pos+1=3)",
            "5. C at end of Row 1",
            "6. S faces C",
            "7. D, R fill remaining",
        ]
        clue_panel = VGroup(*[
            Text(c, font_size=12, color=DARK) for c in clues
        ]).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        clue_panel.to_edge(RIGHT, buff=0.2).shift(UP * 0.2)
        self.play(FadeIn(clue_panel))

        # ── Step 1: A at pos 2 in Row 1 ────────────────────────
        # Row 1 facing South: "2nd from left" = left is +pos direction
        # So "2nd from left end" = position 2 (standard numbering)
        # Wait — facing South, left = increasing position on paper.
        # "from the left end" means from position that is "left" from person's view.
        # Facing South: person's left = paper-right. Left end = rightmost on paper.
        # So "2nd from the left end" of Row 1 = 2nd from paper-right = position n-1 = 3.
        #
        # ACTUALLY, in exam convention, "left end" typically refers to the
        # left end of the row as drawn, not from person's perspective.
        # So position 2 from the left end = position 2.
        # Let's use the simpler convention for clarity.

        a_label = Text("A", font_size=20, color=TEAL)
        a_label.move_to(row1[0][1])  # seats are (label, row_group)
        # row1 structure: [label_text, seats_group]
        # Let me restructure. The _build_row returns VGroup(label, seats).
        # seats = row1[1], seat[1] = position 2 = index 1
        a_label.move_to(row1[1][1])
        self.play(FadeIn(a_label, scale=1.5), clue_panel[0].animate.set_color(GREEN), run_time=0.6)

        # ── Step 2: P faces A -> P at pos 2 in Row 2 ───────────
        p_label = Text("P", font_size=20, color=CORAL)
        p_label.move_to(row2[1][1])
        facing_line = DashedLine(
            row1[1][1].get_bottom() + DOWN * 0.1,
            row2[1][1].get_top() + UP * 0.1,
            color=AMBER, dash_length=0.08
        )
        self.play(
            FadeIn(p_label, scale=1.5), Create(facing_line),
            clue_panel[1].animate.set_color(GREEN), run_time=0.6
        )

        # ── Step 3: B immediately left of A in Row 1 ───────────
        # Row 1 faces South. "Left of A" (person's left) = +position = pos 3
        b_label = Text("B", font_size=20, color=TEAL)
        b_label.move_to(row1[1][2])  # pos 3 = index 2
        self.play(FadeIn(b_label, scale=1.5), clue_panel[2].animate.set_color(GREEN), run_time=0.6)

        # ── Step 4: Q immediately right of P in Row 2 ──────────
        # Row 2 faces North. "Right of P" (person's right) = +position = pos 3
        q_label = Text("Q", font_size=20, color=CORAL)
        q_label.move_to(row2[1][2])  # pos 3 = index 2
        self.play(FadeIn(q_label, scale=1.5), clue_panel[3].animate.set_color(GREEN), run_time=0.6)

        # ── Step 5: C at end of Row 1 -> pos 1 or 4 ────────────
        # pos 2 and 3 are taken. Ends = 1, 4. Try C at 1.
        c_label = Text("C", font_size=20, color=TEAL)
        c_label.move_to(row1[1][0])  # pos 1 = index 0
        self.play(FadeIn(c_label, scale=1.5), clue_panel[4].animate.set_color(GREEN), run_time=0.6)

        # ── Step 6: S faces C -> S at pos 1 in Row 2 ───────────
        s_label = Text("S", font_size=20, color=CORAL)
        s_label.move_to(row2[1][0])
        facing_line2 = DashedLine(
            row1[1][0].get_bottom() + DOWN * 0.1,
            row2[1][0].get_top() + UP * 0.1,
            color=AMBER, dash_length=0.08
        )
        self.play(
            FadeIn(s_label, scale=1.5), Create(facing_line2),
            clue_panel[5].animate.set_color(GREEN), run_time=0.6
        )

        # ── Step 7: D at pos 4 Row 1, R at pos 4 Row 2 ─────────
        d_label = Text("D", font_size=20, color=TEAL)
        d_label.move_to(row1[1][3])
        r_label = Text("R", font_size=20, color=CORAL)
        r_label.move_to(row2[1][3])
        self.play(
            FadeIn(d_label, scale=1.5), FadeIn(r_label, scale=1.5),
            clue_panel[6].animate.set_color(GREEN), run_time=0.6
        )

        # ── Final result ────────────────────────────────────────
        result = Text(
            "Row 1: C  A  B  D  (facing South)\n"
            "Row 2: S  P  Q  R  (facing North)",
            font_size=20, color=GREEN
        )
        result.to_edge(DOWN, buff=0.3)
        self.play(Write(result))
        self.wait(2)

    @staticmethod
    def _build_row(n, color, label_text):
        label = Text(label_text, font_size=16, color=color)
        seats = VGroup()
        for i in range(n):
            sq = Square(side_length=0.65, stroke_color=color, fill_color=WHITE, fill_opacity=1)
            t = Text(str(i + 1), font_size=14, color=DARK)
            t.move_to(sq)
            seats.add(VGroup(sq, t))
        seats.arrange(RIGHT, buff=0.05)
        label.next_to(seats, LEFT, buff=0.3)
        return VGroup(label, seats)


# ====================================================================
# Scene 4.7 — Common Traps
# ====================================================================
class DoubleRowTraps(Scene):
    """Visual catalogue of the most common double-row mistakes."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("Double-Row: Common Traps", font_size=34, color=CORAL)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        traps = [
            ("Trap 1", "Left/Right confusion between rows",
             "Facing South: left = +pos (paper-right)\n"
             "Facing North: left = -pos (paper-left)"),
            ("Trap 2", "'Faces' vs 'Adjacent'",
             "'Faces' = same position in opposite row\n"
             "'Adjacent' = next position in SAME row"),
            ("Trap 3", "'From left end' ambiguity",
             "Usually means from the left end as drawn,\n"
             "NOT from the person's left perspective"),
        ]

        y_offset = 1.5
        for trap_title, trap_desc, trap_detail in traps:
            t_title = Text(trap_title, font_size=22, color=CORAL)
            t_desc = Text(trap_desc, font_size=18, color=DARK)
            t_detail = Text(trap_detail, font_size=14, color=INDIGO)

            group = VGroup(t_title, t_desc, t_detail).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            group.move_to(UP * y_offset)
            y_offset -= 2.0

            box = SurroundingRectangle(group, color=CORAL, buff=0.15, corner_radius=0.1)
            self.play(FadeIn(box), Write(t_title), Write(t_desc), Write(t_detail), run_time=1)
            self.wait(0.5)

        self.wait(1)
