"""
Scene 05: Complex and Hybrid Arrangements
==========================================
Manim CE script — covers Chapter 5 concepts:
  5.1 Overview of complex types
  5.2 Rectangular / Square Table (corners vs sides)
  5.3 Floor / Multi-Level Puzzles
  5.4 Matrix / Grid Seating (adjacency rules)
  5.5 Hybrid Arrangements (combining types)
  5.6 Strategy: Divide-and-Conquer

Render all:  manim -pqh scene_05_complex.py
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
# Scene 5.1 — Overview of Complex Types
# ====================================================================
class ComplexOverview(Scene):
    """Shows the taxonomy of complex arrangement types."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("Complex & Hybrid Arrangements", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        types = [
            ("Rectangular / Square Table", TEAL,
             "Sides + corners. Corner has\n2 neighbours from different sides."),
            ("Floor / Multi-Level", CORAL,
             "Vertical linear. 'Above' = higher.\n"
             "Ground floor trap: 0 or 1?"),
            ("Matrix / Grid", AMBER,
             "2D layout. Corner: 2 neighbours.\n"
             "Edge: 3. Center: 4."),
            ("Hybrid", INDIGO,
             "Combine types. Solve each sub-type\n"
             "separately, then link with cross-clues."),
        ]

        cards = VGroup()
        for name, color, desc in types:
            box = RoundedRectangle(
                corner_radius=0.1, width=5.5, height=1.3,
                stroke_color=color, fill_color=color, fill_opacity=0.08
            )
            t = Text(name, font_size=18, color=color)
            t.next_to(box.get_top(), DOWN, buff=0.15)
            d = Text(desc, font_size=13, color=DARK)
            d.next_to(t, DOWN, buff=0.1)
            cards.add(VGroup(box, t, d))

        cards.arrange(DOWN, buff=0.15)
        cards.next_to(title, DOWN, buff=0.4)

        for card in cards:
            self.play(FadeIn(card, shift=LEFT), run_time=0.7)

        self.wait(2)


# ====================================================================
# Scene 5.2 — Rectangular Table
# ====================================================================
class RectangularTable(Scene):
    """
    Visual construction of a rectangular table:
    - 2 long sides (3 seats each)
    - 2 short sides (1 seat each)
    - Total: 8 seats
    Shows corner vs side adjacency.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Rectangular Table Layout", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # ── Draw the table ──────────────────────────────────────
        table = Rectangle(width=5, height=2, stroke_color=DARK, stroke_width=2,
                          fill_color="#f5f5f5", fill_opacity=0.5)
        table.move_to(ORIGIN)
        self.play(Create(table))

        # ── Place seats ─────────────────────────────────────────
        # Top side: 3 seats (facing South / inward)
        top_seats = self._side_seats(3, table.get_top(), DOWN, TEAL, start_num=1)
        # Bottom side: 3 seats (facing North / inward)
        bot_seats = self._side_seats(3, table.get_bottom(), UP, CORAL, start_num=4)
        # Left short side: 1 seat (facing Right / inward)
        left_seat = self._single_seat(table.get_left(), RIGHT, AMBER, 7)
        # Right short side: 1 seat (facing Left / inward)
        right_seat = self._single_seat(table.get_right(), LEFT, INDIGO, 8)

        all_seats = VGroup(top_seats, bot_seats, left_seat, right_seat)
        self.play(*[FadeIn(s, scale=0.8) for s in [top_seats, bot_seats, left_seat, right_seat]])
        self.wait(0.5)

        # ── Highlight corner seats ──────────────────────────────
        corner_label = Text(
            "CORNER seats (7, 8): neighbours from DIFFERENT sides",
            font_size=18, color=AMBER
        )
        corner_label.next_to(table, DOWN, buff=1.5)
        self.play(Write(corner_label))

        hl7 = SurroundingRectangle(left_seat, color=AMBER, buff=0.06, stroke_width=3)
        hl8 = SurroundingRectangle(right_seat, color=AMBER, buff=0.06, stroke_width=3)
        self.play(Create(hl7), Create(hl8))
        self.wait(0.5)

        # ── Highlight opposite concept ──────────────────────────
        self.play(FadeOut(hl7), FadeOut(hl8), FadeOut(corner_label))

        opp_label = Text(
            '"Opposite" depends on geometry — never assume!',
            font_size=18, color=CORAL
        )
        opp_label.next_to(table, DOWN, buff=1.5)

        # Draw line from seat 1 (top-left) to seat 4 (bottom-left)
        opp_line = DashedLine(
            top_seats[0].get_center(),
            bot_seats[0].get_center(),
            dash_length=0.1, color=CORAL, stroke_width=2
        )
        opp_note = Text("1 opposite 4?", font_size=14, color=CORAL)
        opp_note.next_to(opp_line, LEFT, buff=0.2)

        # Draw diagonal from seat 1 to seat 6 (bottom-right)
        diag_line = DashedLine(
            top_seats[0].get_center(),
            bot_seats[2].get_center(),
            dash_length=0.1, color=AMBER, stroke_width=2
        )
        diag_note = Text("1 diag-opposite 6?", font_size=14, color=AMBER)
        diag_note.next_to(diag_line, RIGHT, buff=0.2)

        self.play(Create(opp_line), Write(opp_note), Create(diag_line), Write(diag_note))
        self.play(Write(opp_label))
        self.wait(2)

    @staticmethod
    def _side_seats(n, anchor, direction, color, start_num):
        seats = VGroup()
        for i in range(n):
            c = Circle(radius=0.25, stroke_color=color, fill_color=color, fill_opacity=0.15)
            t = Text(str(start_num + i), font_size=14, color=color)
            t.move_to(c)
            seats.add(VGroup(c, t))
        seats.arrange(RIGHT, buff=0.6)
        seats.next_to(anchor, -direction, buff=0.35)  # outside the table
        return seats

    @staticmethod
    def _single_seat(anchor, direction, color, num):
        c = Circle(radius=0.25, stroke_color=color, fill_color=color, fill_opacity=0.15)
        t = Text(str(num), font_size=14, color=color)
        t.move_to(c)
        g = VGroup(c, t)
        g.next_to(anchor, -direction, buff=0.35)
        return g


# ====================================================================
# Scene 5.3 — Floor / Multi-Level Puzzle
# ====================================================================
class FloorPuzzle(Scene):
    """
    Vertical linear arrangement. Shows the 'ground floor' trap.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Floor / Multi-Level Puzzle", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        analogy = Text(
            "Analogy: A building with numbered floors.\n"
            "Same logic as LINEAR, but rotated 90 degrees.",
            font_size=18, color=INDIGO
        )
        analogy.next_to(title, DOWN, buff=0.3)
        self.play(Write(analogy))

        # ── Draw 7-floor building ───────────────────────────────
        n_floors = 7
        floors = VGroup()
        for i in range(n_floors):
            rect = Rectangle(
                width=2.5, height=0.55,
                stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.05 + i * 0.03
            )
            label = Text(f"Floor {i + 1}", font_size=14, color=TEAL)
            label.move_to(rect)
            floors.add(VGroup(rect, label))

        floors.arrange(UP, buff=0.03)
        floors.shift(LEFT * 3 + DOWN * 0.5)

        self.play(*[FadeIn(f, shift=RIGHT) for f in floors], run_time=1.5)

        # ── The formula ─────────────────────────────────────────
        formula_box = VGroup(
            Text("Floor from Bottom + Floor from Top = n + 1", font_size=18, color=GREEN),
            Text("", font_size=6),
            Text("'Above' = higher floor number", font_size=16, color=DARK),
            Text("'Below' = lower floor number", font_size=16, color=DARK),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        formula_box.shift(RIGHT * 2.5 + UP * 0.5)
        self.play(Write(formula_box))

        # ── The ground floor trap ───────────────────────────────
        trap = VGroup(
            Text("TRAP: Ground Floor Numbering", font_size=20, color=CORAL),
            Text("", font_size=4),
            Text("Some problems: Ground = Floor 0 (then 1st = Floor 1)", font_size=15, color=DARK),
            Text("Other problems: Ground = Floor 1", font_size=15, color=DARK),
            Text("ALWAYS check the problem statement!", font_size=16, color=CORAL),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        trap.to_edge(DOWN, buff=0.4)

        trap_box = SurroundingRectangle(trap, color=CORAL, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(trap_box), Write(trap))
        self.wait(2)


# ====================================================================
# Scene 5.4 — Grid / Matrix Seating
# ====================================================================
class GridSeating(Scene):
    """
    Shows a 3x3 grid and adjacency rules:
    - Corner: 2 neighbours
    - Edge: 3 neighbours
    - Center: 4 neighbours
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Grid / Matrix Seating", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # ── Build 3x3 grid ─────────────────────────────────────
        grid = VGroup()
        positions = {}
        num = 1
        for row in range(3):
            for col in range(3):
                sq = Square(side_length=0.9, stroke_color=TEAL,
                            fill_color=TEAL, fill_opacity=0.06)
                sq.move_to(RIGHT * (col - 1) * 1.0 + DOWN * (row - 1) * 1.0)
                t = Text(str(num), font_size=18, color=TEAL)
                t.move_to(sq)
                g = VGroup(sq, t)
                grid.add(g)
                positions[num] = (row, col)
                num += 1

        grid.move_to(LEFT * 2.5 + DOWN * 0.2)
        self.play(*[FadeIn(g) for g in grid], run_time=1)

        # ── Highlight corner (position 1) ───────────────────────
        hl_corner = SurroundingRectangle(grid[0], color=CORAL, buff=0.04, stroke_width=3)
        corner_label = Text("Corner: 2 neighbours", font_size=16, color=CORAL)
        corner_label.shift(RIGHT * 2 + UP * 1.5)

        # Highlight its neighbours (2 and 4)
        n2 = SurroundingRectangle(grid[1], color=AMBER, buff=0.03)
        n4 = SurroundingRectangle(grid[3], color=AMBER, buff=0.03)

        self.play(Create(hl_corner), Write(corner_label))
        self.play(Create(n2), Create(n4))
        self.wait(0.5)

        # ── Highlight edge (position 2) ─────────────────────────
        self.play(FadeOut(hl_corner), FadeOut(n2), FadeOut(n4), FadeOut(corner_label))

        hl_edge = SurroundingRectangle(grid[1], color=GREEN, buff=0.04, stroke_width=3)
        edge_label = Text("Edge: 3 neighbours", font_size=16, color=GREEN)
        edge_label.shift(RIGHT * 2 + UP * 1.5)

        ne1 = SurroundingRectangle(grid[0], color=AMBER, buff=0.03)
        ne3 = SurroundingRectangle(grid[2], color=AMBER, buff=0.03)
        ne5 = SurroundingRectangle(grid[4], color=AMBER, buff=0.03)

        self.play(Create(hl_edge), Write(edge_label))
        self.play(Create(ne1), Create(ne3), Create(ne5))
        self.wait(0.5)

        # ── Highlight center (position 5) ───────────────────────
        self.play(FadeOut(hl_edge), FadeOut(ne1), FadeOut(ne3), FadeOut(ne5), FadeOut(edge_label))

        hl_center = SurroundingRectangle(grid[4], color=INDIGO, buff=0.04, stroke_width=3)
        center_label = Text("Center: 4 neighbours", font_size=16, color=INDIGO)
        center_label.shift(RIGHT * 2 + UP * 1.5)

        nc2 = SurroundingRectangle(grid[1], color=AMBER, buff=0.03)
        nc4 = SurroundingRectangle(grid[3], color=AMBER, buff=0.03)
        nc6 = SurroundingRectangle(grid[5], color=AMBER, buff=0.03)
        nc8 = SurroundingRectangle(grid[7], color=AMBER, buff=0.03)

        self.play(Create(hl_center), Write(center_label))
        self.play(Create(nc2), Create(nc4), Create(nc6), Create(nc8))
        self.wait(0.5)

        # ── Summary ─────────────────────────────────────────────
        summary = VGroup(
            Text("Adjacency in Grid:", font_size=18, color=DARK),
            Text("Corner (1,3,7,9): 2 neighbours", font_size=15, color=CORAL),
            Text("Edge (2,4,6,8): 3 neighbours", font_size=15, color=GREEN),
            Text("Center (5): 4 neighbours", font_size=15, color=INDIGO),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        summary.shift(RIGHT * 3 + DOWN * 0.5)
        self.play(Write(summary))
        self.wait(2)


# ====================================================================
# Scene 5.5 — Hybrid Arrangements Strategy
# ====================================================================
class HybridStrategy(Scene):
    """
    Divide-and-conquer approach for hybrid problems.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Hybrid: Divide-and-Conquer Strategy", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # ── Pipeline ────────────────────────────────────────────
        steps = [
            ("1. Identify\nSub-Types", TEAL,
             "Is it row+circle?\nFloor+direction?"),
            ("2. Solve Each\nSeparately", CORAL,
             "Solve the spatial\nlayout for each type"),
            ("3. Link with\nCross-Clues", AMBER,
             "Chain constraints\nacross sub-types"),
            ("4. Validate\nAll Clues", GREEN,
             "Check every clue\nholds simultaneously"),
        ]

        boxes = VGroup()
        for label, color, desc in steps:
            box = RoundedRectangle(
                corner_radius=0.1, width=2.8, height=1.8,
                stroke_color=color, fill_color=color, fill_opacity=0.08
            )
            lbl = Text(label, font_size=14, color=color)
            lbl.move_to(box.get_center() + UP * 0.25)
            d = Text(desc, font_size=11, color=DARK)
            d.next_to(lbl, DOWN, buff=0.1)
            boxes.add(VGroup(box, lbl, d))

        boxes.arrange(RIGHT, buff=0.3)
        boxes.next_to(title, DOWN, buff=0.6)

        arrows = VGroup()
        for i in range(len(boxes) - 1):
            a = Arrow(
                boxes[i].get_right(), boxes[i + 1].get_left(),
                stroke_width=2, color=DARK, buff=0.05,
                max_tip_length_to_length_ratio=0.2
            )
            arrows.add(a)

        for i, box in enumerate(boxes):
            anims = [FadeIn(box, shift=UP)]
            if i > 0:
                anims.append(GrowArrow(arrows[i - 1]))
            self.play(*anims, run_time=0.6)

        # ── Example: Row + Circular hybrid ──────────────────────
        example = Text(
            "Example: 'Group A sits in a row, Group B sits around a table.\n"
            "Person X in Group A faces Person Y in Group B.'\n"
            "Solve the row arrangement and circular arrangement separately,\n"
            "then use 'faces' to link them.",
            font_size=16, color=INDIGO
        )
        example.to_edge(DOWN, buff=0.4)
        self.play(Write(example), run_time=2)
        self.wait(2)
