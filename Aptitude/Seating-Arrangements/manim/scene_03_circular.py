"""
Scene 03: Circular Seating Arrangements
========================================
Manim CE script — covers Chapter 3 concepts:
  3.1 What is a Circular Arrangement (no endpoints)
  3.2 Rotation Principle (n! vs (n-1)!)
  3.3 Clockwise / Anticlockwise convention
  3.4 The "Opposite" Concept and formula
  3.5 Facing Center vs Facing Outward (left/right flip)
  3.6 Solved Example — Basic Circular (GATE Style)
  3.7 Mixed Facing variant
  3.8 Linear vs Circular comparison

Render all:  manim -pqh scene_03_circular.py
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
# Scene 3.1 — What Is a Circular Arrangement?
# ====================================================================
class CircularBasics(Scene):
    """Shows a round table with n seats, no endpoints."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("Circular Arrangement — No Endpoints", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        n = 8
        positions = circle_positions(n, radius=1.8)

        table = Circle(radius=1.0, stroke_color=DARK, stroke_width=1, fill_color="#f5f5f5", fill_opacity=0.5)
        table.move_to(ORIGIN)
        self.play(Create(table))

        seats = VGroup()
        for i, pos in enumerate(positions):
            c = Circle(radius=0.28, stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.1)
            c.move_to(pos)
            t = Text(str(i + 1), font_size=16, color=TEAL)
            t.move_to(c)
            seats.add(VGroup(c, t))

        self.play(*[FadeIn(s, scale=0.5) for s in seats], run_time=1.5)
        self.wait(0.5)

        note = Text(
            "Every seat has exactly 2 neighbours.\n"
            "No 'first' or 'last' — only RELATIVE positions matter.",
            font_size=20, color=INDIGO
        )
        note.to_edge(DOWN, buff=0.5)
        self.play(Write(note))
        self.wait(2)


# ====================================================================
# Scene 3.2 — Rotation Principle
# ====================================================================
class RotationPrinciple(Scene):
    """
    Shows why we fix one person: rotating all n people gives
    the same arrangement.  n! -> (n-1)!
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Rotation Principle: Fix One Person", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        n = 4
        labels = ["A", "B", "C", "D"]
        radius = 1.4

        # ── Show two "different" rotations that are really the same ─
        grp1 = self._circle_arrangement(labels, radius, TEAL)
        grp1.shift(LEFT * 3)
        grp1_title = Text("Rotation 1", font_size=18, color=TEAL)
        grp1_title.next_to(grp1, UP, buff=0.2)

        labels_rot = ["D", "A", "B", "C"]  # rotated by 1
        grp2 = self._circle_arrangement(labels_rot, radius, CORAL)
        grp2.shift(RIGHT * 3)
        grp2_title = Text("Rotation 2", font_size=18, color=CORAL)
        grp2_title.next_to(grp2, UP, buff=0.2)

        self.play(FadeIn(grp1), Write(grp1_title), FadeIn(grp2), Write(grp2_title))
        self.wait(0.5)

        eq = Text("= SAME arrangement!", font_size=24, color=AMBER)
        eq.move_to(ORIGIN)
        self.play(Write(eq))
        self.wait(0.5)

        # ── Formula ─────────────────────────────────────────────
        formula = MathTex(
            r"\text{Linear: } n! \quad \text{Circular: } \frac{n!}{n} = (n-1)!",
            font_size=28, color=INDIGO
        )
        formula.next_to(eq, DOWN, buff=0.6)
        self.play(Write(formula))

        fix_note = Text(
            "FIX one person at the top. Then arrange the remaining (n-1).",
            font_size=20, color=GREEN
        )
        fix_note.to_edge(DOWN, buff=0.5)
        self.play(Write(fix_note))
        self.wait(2)

    def _circle_arrangement(self, labels, radius, color):
        positions = circle_positions(len(labels), radius=radius)
        table = Circle(radius=radius * 0.55, stroke_color=DARK, stroke_width=1,
                       fill_color="#f5f5f5", fill_opacity=0.3)
        seats = VGroup()
        for lbl, pos in zip(labels, positions):
            c = Circle(radius=0.25, stroke_color=color, fill_color=color, fill_opacity=0.1)
            c.move_to(pos)
            t = Text(lbl, font_size=18, color=color)
            t.move_to(c)
            seats.add(VGroup(c, t))
        return VGroup(table, seats)


# ====================================================================
# Scene 3.3 — Clockwise / Anticlockwise
# ====================================================================
class ClockwiseAnticlockwise(Scene):
    """
    Animated clock-hand analogy for CW/ACW direction.
    Shows position numbering in both directions.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Clockwise (CW) vs Anticlockwise (ACW)", font_size=32, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        n = 8
        radius = 1.8
        positions = circle_positions(n, radius=radius)

        table = Circle(radius=1.0, stroke_color=DARK, stroke_width=1,
                       fill_color="#f5f5f5", fill_opacity=0.3)

        seats = VGroup()
        for i, pos in enumerate(positions):
            c = Circle(radius=0.25, stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.1)
            c.move_to(pos)
            t = Text(str(i + 1), font_size=16, color=TEAL)
            t.move_to(c)
            seats.add(VGroup(c, t))

        self.play(Create(table), *[FadeIn(s) for s in seats])
        self.wait(0.3)

        # ── CW arrow arc ────────────────────────────────────────
        cw_arc = Arc(
            radius=radius + 0.3, start_angle=PI / 2, angle=-PI * 1.2,
            color=CORAL, stroke_width=3
        )
        cw_tip = Triangle(fill_color=CORAL, fill_opacity=1, stroke_width=0)
        cw_tip.scale(0.12)
        cw_tip.move_to(cw_arc.get_end())
        cw_tip.rotate(cw_arc.get_end() - cw_arc.point_from_proportion(0.95))
        cw_label = Text("CW", font_size=20, color=CORAL)
        cw_label.next_to(cw_arc.point_from_proportion(0.5), RIGHT, buff=0.15)

        self.play(Create(cw_arc), FadeIn(cw_tip), Write(cw_label))
        self.wait(0.5)

        # ── ACW arrow arc ───────────────────────────────────────
        acw_arc = Arc(
            radius=radius + 0.6, start_angle=PI / 2, angle=PI * 1.2,
            color=GREEN, stroke_width=3
        )
        acw_label = Text("ACW", font_size=20, color=GREEN)
        acw_label.next_to(acw_arc.point_from_proportion(0.5), LEFT, buff=0.15)

        self.play(Create(acw_arc), Write(acw_label))
        self.wait(0.5)

        # ── Position formula ────────────────────────────────────
        formula = MathTex(
            r"k \text{ places CW from pos } p = (p + k - 1) \bmod n + 1",
            font_size=24, color=INDIGO
        )
        formula.to_edge(DOWN, buff=0.8)
        self.play(Write(formula))

        # ── Demo: 3 places CW from position 1 ──────────────────
        demo = Text(
            "Example: 3 places CW from pos 1 = (1+3-1) mod 8 + 1 = 4",
            font_size=18, color=AMBER
        )
        demo.next_to(formula, UP, buff=0.3)
        hl_start = SurroundingRectangle(seats[0], color=AMBER, buff=0.04)
        hl_end = SurroundingRectangle(seats[3], color=AMBER, buff=0.04)
        self.play(Create(hl_start), Create(hl_end), Write(demo))
        self.wait(2)


# ====================================================================
# Scene 3.4 — The "Opposite" Concept
# ====================================================================
class OppositeFormula(Scene):
    """
    Visual proof: opposite in a circle of n = position + n/2.
    Only works for even n. Odd n has no exact opposite.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text('The "Opposite" in Circular', font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        n = 8
        radius = 1.8
        positions = circle_positions(n, radius=radius)

        table = Circle(radius=1.0, stroke_color=DARK, stroke_width=1,
                       fill_color="#f5f5f5", fill_opacity=0.3)

        seats = VGroup()
        for i, pos in enumerate(positions):
            c = Circle(radius=0.25, stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.1)
            c.move_to(pos)
            t = Text(str(i + 1), font_size=16, color=TEAL)
            t.move_to(c)
            seats.add(VGroup(c, t))

        self.play(Create(table), *[FadeIn(s) for s in seats])

        # ── Draw diameter lines for opposite pairs ──────────────
        pairs = [(0, 4), (1, 5), (2, 6), (3, 7)]
        colors = [CORAL, AMBER, INDIGO, GREEN]
        lines = VGroup()
        for (i, j), color in zip(pairs, colors):
            line = DashedLine(
                positions[i], positions[j],
                dash_length=0.1, color=color, stroke_width=2
            )
            lines.add(line)

        self.play(*[Create(l) for l in lines], run_time=1.5)

        # ── Formula ─────────────────────────────────────────────
        formula = MathTex(
            r"\text{Opposite of pos } p = \left(p + \frac{n}{2} - 1\right) \bmod n + 1",
            font_size=24, color=INDIGO
        )
        formula.next_to(table, DOWN, buff=1.8)
        self.play(Write(formula))

        # ── Example ─────────────────────────────────────────────
        example = Text(
            "Opposite of 3 = (3 + 4 - 1) mod 8 + 1 = 7",
            font_size=20, color=AMBER
        )
        example.next_to(formula, DOWN, buff=0.3)
        self.play(Write(example))

        # ── Odd n warning ───────────────────────────────────────
        warning = Text(
            "WARNING: For ODD n, there is NO exact opposite! (Exam trap)",
            font_size=20, color=CORAL
        )
        warning.to_edge(DOWN, buff=0.3)
        self.play(Write(warning))
        self.wait(2)


# ====================================================================
# Scene 3.5 — Facing Center vs Facing Outward
# ====================================================================
class FacingCenterVsOutward(Scene):
    """
    The KEY rule:
      Facing CENTER  -> Left = CW,  Right = ACW
      Facing OUTWARD -> Left = ACW, Right = CW
    Visual proof via hand-pointing at each position.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Facing Center vs Facing Outward", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        n = 6
        radius = 1.5

        # ── Facing Center (left panel) ──────────────────────────
        center_label = Text("Facing CENTER", font_size=22, color=TEAL)
        center_circle = self._build_circle(n, radius, TEAL, facing_in=True)
        center_group = VGroup(center_label, center_circle).arrange(DOWN, buff=0.3)
        center_group.shift(LEFT * 3.5)

        # ── Facing Outward (right panel) ────────────────────────
        out_label = Text("Facing OUTWARD", font_size=22, color=CORAL)
        out_circle = self._build_circle(n, radius, CORAL, facing_in=False)
        out_group = VGroup(out_label, out_circle).arrange(DOWN, buff=0.3)
        out_group.shift(RIGHT * 3.5)

        self.play(FadeIn(center_group), FadeIn(out_group))
        self.wait(0.5)

        # ── Rules ───────────────────────────────────────────────
        rule_center = Text("Left = CW, Right = ACW", font_size=18, color=TEAL)
        rule_center.next_to(center_group, DOWN, buff=0.3)

        rule_out = Text("Left = ACW, Right = CW", font_size=18, color=CORAL)
        rule_out.next_to(out_group, DOWN, buff=0.3)

        self.play(Write(rule_center), Write(rule_out))

        # ── Physical proof ──────────────────────────────────────
        proof = Text(
            "PROOF: Sit at position 1 (top). Face center (look DOWN).\n"
            "Your left hand points RIGHT on paper = CLOCKWISE direction.\n"
            "Face outward (look UP): left hand points LEFT = ANTICLOCKWISE.",
            font_size=16, color=DARK
        )
        proof.to_edge(DOWN, buff=0.3)
        self.play(Write(proof), run_time=2)
        self.wait(2)

    def _build_circle(self, n, radius, color, facing_in):
        positions = circle_positions(n, radius=radius)
        table = Circle(radius=radius * 0.4, stroke_color=DARK, stroke_width=1,
                       fill_color="#f5f5f5", fill_opacity=0.3)
        seats = VGroup()
        for i, pos in enumerate(positions):
            c = Circle(radius=0.22, stroke_color=color, fill_color=color, fill_opacity=0.1)
            c.move_to(pos)
            t = Text(str(i + 1), font_size=14, color=color)
            t.move_to(c)

            # Direction arrow
            direction = -pos / np.linalg.norm(pos) if facing_in else pos / np.linalg.norm(pos)
            arrow = Arrow(
                pos, pos + direction * 0.35,
                stroke_width=2, color=color, buff=0,
                max_tip_length_to_length_ratio=0.3
            )
            seats.add(VGroup(c, t, arrow))

        return VGroup(table, seats)


# ====================================================================
# Scene 3.6 — Solved Example (GATE Circular)
# ====================================================================
class CircularSolvedExample(Scene):
    """
    8 people around a round table, all facing center.
    Clues:
      1. A sits at position 1 (top, fixed anchor)
      2. B is 3rd to the LEFT of A  (left = CW -> pos 4)
      3. C sits opposite A           (pos 5)
      4. D is immediately right of C (right = ACW -> pos 4... wait, pos 4 is B)
         Actually: right of C = ACW from C = pos 4 is taken, so re-read:
         Let's use clear clues:
      Revised clues for clean demo:
      1. A sits at position 1
      2. B is 3 places CW from A -> pos 4
      3. C is opposite A -> pos 5
      4. D is immediately ACW from C -> pos 6
      5. E is opposite B -> pos 8
      6. F is immediately CW from A -> pos 2
      7. G is opposite D -> pos 2 (conflict!)... let's use pos opposite 6 = pos 2... taken.
    
    Simplify: use 6-person table for clean demo.
      1. Fix A at top (pos 1)
      2. B is opposite A -> pos 4
      3. C is immediately CW from A -> pos 2
      4. D is immediately CW from B -> pos 5
      5. E is opposite C -> pos 5... conflict.
    
    Final clean 6-person:
      1. Fix A at pos 1
      2. B opposite A -> pos 4
      3. C immediately CW from A -> pos 2
      4. D immediately ACW from B -> pos 3
      5. E opposite D -> pos 6
      6. F remaining -> pos 5
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Solved Example: 6-Person Circular (GATE)", font_size=30, color=DARK)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))

        n = 6
        radius = 1.6
        positions = circle_positions(n, radius=radius)

        table = Circle(radius=0.8, stroke_color=DARK, stroke_width=1,
                       fill_color="#f5f5f5", fill_opacity=0.3)
        table.move_to(LEFT * 2.5)

        seats = VGroup()
        seat_labels = VGroup()
        for i, pos in enumerate(positions):
            shifted = pos + LEFT * 2.5
            c = Circle(radius=0.28, stroke_color=TEAL, fill_color=WHITE, fill_opacity=1)
            c.move_to(shifted)
            num = Text(str(i + 1), font_size=12, color=DARK)
            num.move_to(shifted)
            seats.add(VGroup(c, num))

        self.play(Create(table), *[FadeIn(s) for s in seats])

        # Clues panel
        clues = [
            "1. A at top (pos 1)",
            "2. B opposite A -> pos 4",
            "3. C immediately CW from A -> pos 2",
            "4. D immediately ACW from B -> pos 3",
            "5. E opposite D -> pos 6",
            "6. F remaining -> pos 5",
        ]
        clue_texts = VGroup(*[
            Text(c, font_size=14, color=DARK) for c in clues
        ]).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        clue_texts.to_edge(RIGHT, buff=0.3).shift(UP * 0.5)
        self.play(FadeIn(clue_texts))

        # ── Step-by-step placement ──────────────────────────────
        placement = [
            (0, "A", TEAL),    # pos 1
            (3, "B", CORAL),   # pos 4
            (1, "C", AMBER),   # pos 2
            (2, "D", INDIGO),  # pos 3
            (5, "E", GREEN),   # pos 6
            (4, "F", DARK),    # pos 5
        ]

        for step, (idx, name, color) in enumerate(placement):
            person = Text(name, font_size=22, color=color)
            person.move_to(seats[idx])
            self.play(
                FadeIn(person, scale=1.5),
                seats[idx][0].animate.set_stroke(color=color, width=3),
                clue_texts[step].animate.set_color(GREEN),
                run_time=0.7
            )
            self.wait(0.3)

        result = Text("A C D B F E (CW from top)", font_size=22, color=GREEN)
        result.to_edge(DOWN, buff=0.4)
        self.play(Write(result))
        self.wait(2)


# ====================================================================
# Scene 3.7 — Linear vs Circular Comparison
# ====================================================================
class LinearVsCircular(Scene):
    """Side-by-side comparison table."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("Linear vs Circular: Key Differences", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        headers = ["Property", "Linear", "Circular"]
        rows_data = [
            ["Endpoints", "YES (2 ends)", "NONE"],
            ["Arrangements", "n!", "(n-1)!"],
            ["Opposite", "Not defined", "p + n/2"],
            ["Left/Right", "Fixed by direction", "Depends on facing"],
            ["'Between'", "One path only", "Two arcs (shorter)"],
            ["Wrapping", "No wrap", "Wraps around"],
        ]

        # Build table manually
        cell_w, cell_h = 3.2, 0.45
        table = VGroup()

        for col_idx, h in enumerate(headers):
            cell = Rectangle(width=cell_w, height=cell_h,
                             stroke_color=DARK, fill_color=INDIGO, fill_opacity=0.15)
            cell.shift(RIGHT * col_idx * cell_w)
            txt = Text(h, font_size=16, color=DARK)
            txt.move_to(cell)
            table.add(VGroup(cell, txt))

        for row_idx, row in enumerate(rows_data):
            for col_idx, val in enumerate(row):
                cell = Rectangle(width=cell_w, height=cell_h,
                                 stroke_color=DARK, fill_color=WHITE, fill_opacity=1)
                cell.shift(RIGHT * col_idx * cell_w + DOWN * (row_idx + 1) * cell_h)
                color = TEAL if col_idx == 1 else CORAL if col_idx == 2 else DARK
                txt = Text(val, font_size=14, color=color)
                txt.move_to(cell)
                table.add(VGroup(cell, txt))

        table.move_to(ORIGIN)
        if table.width > 12:
            table.scale_to_fit_width(12)

        self.play(FadeIn(table), run_time=2)
        self.wait(3)
