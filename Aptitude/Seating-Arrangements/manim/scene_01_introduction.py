"""
Scene 01: Introduction and Fundamentals of Seating Arrangements
================================================================
Manim CE script — covers Chapter 1 concepts:
  1.1 What is a Seating Arrangement Problem?
  1.2 Classification of Types (Linear / Circular / Complex)
  1.3 Core Terminology (positional & directional)
  1.4 Universal 5-Step Solving Framework
  1.5 Notation System
  1.6 Constraint Density Principle
  1.7 Common Mistake Patterns (perspective trap)

Render:
  manim -pqh scene_01_introduction.py
  (renders all scenes at 1080p)

Individual scenes:
  manim -pqh scene_01_introduction.py WhatIsSeatingArrangement
  manim -pqh scene_01_introduction.py ClassificationTree
  manim -pqh scene_01_introduction.py CoreTerminology
  manim -pqh scene_01_introduction.py FiveStepFramework
  manim -pqh scene_01_introduction.py NotationSystem
  manim -pqh scene_01_introduction.py ConstraintDensityPrinciple
  manim -pqh scene_01_introduction.py PerspectiveTrap
"""

from manim import *
import numpy as np

# ── Colour palette (matches the website theme) ──────────────────────
TEAL    = "#1a8a8a"
CORAL   = "#d94f4f"
AMBER   = "#e8a317"
INDIGO  = "#4a5da8"
GREEN   = "#2e8b57"
BG      = "#ffffff"
DARK    = "#1a1a2e"


# ====================================================================
# Scene 1.1 — What Is a Seating Arrangement Problem?
# ====================================================================
class WhatIsSeatingArrangement(Scene):
    """
    Analogy: a jigsaw puzzle where each piece (person) must fit
    into exactly one slot (position) obeying the picture (clues).
    """

    def construct(self):
        self.camera.background_color = BG

        # ── Title ───────────────────────────────────────────────
        title = Text("What is a Seating Arrangement?", font_size=40, color=DARK)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # ── Three ingredients ───────────────────────────────────
        people_label = Text("People", font_size=28, color=TEAL)
        positions_label = Text("Positions", font_size=28, color=CORAL)
        constraints_label = Text("Constraints", font_size=28, color=AMBER)
        arrow1 = Text("+", font_size=32, color=DARK)
        arrow2 = Text("+", font_size=32, color=DARK)
        eq = Text("=", font_size=32, color=DARK)
        result_label = Text("Unique Valid Arrangement", font_size=28, color=GREEN)

        row = VGroup(
            people_label, arrow1, positions_label, arrow2,
            constraints_label, eq, result_label
        ).arrange(RIGHT, buff=0.3)
        row.next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP), run_time=1.5)
        self.wait(0.5)

        # ── Jigsaw analogy ──────────────────────────────────────
        analogy_box = RoundedRectangle(
            corner_radius=0.15, width=10, height=2.2,
            stroke_color=INDIGO, fill_color=WHITE, fill_opacity=0.9
        )
        analogy_box.next_to(row, DOWN, buff=0.7)

        analogy_title = Text("Analogy: Jigsaw Puzzle", font_size=24, color=INDIGO)
        analogy_title.next_to(analogy_box.get_top(), DOWN, buff=0.2)

        analogy_text = Text(
            "Each person = puzzle piece\n"
            "Each position = slot on the board\n"
            "Each clue = shape constraint on the piece",
            font_size=20, color=DARK, line_spacing=1.3
        )
        analogy_text.next_to(analogy_title, DOWN, buff=0.2)

        self.play(FadeIn(analogy_box), Write(analogy_title))
        self.play(Write(analogy_text), run_time=2)
        self.wait(1)

        # ── Visual: 5 people mapped to 5 chairs ────────────────
        self.play(FadeOut(analogy_box), FadeOut(analogy_title), FadeOut(analogy_text))

        persons = VGroup()
        chairs = VGroup()
        for i in range(5):
            p = Circle(radius=0.3, stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.2)
            label = Text(chr(65 + i), font_size=20, color=TEAL)
            label.move_to(p)
            pg = VGroup(p, label)
            persons.add(pg)

            c = Square(side_length=0.6, stroke_color=CORAL, fill_color=CORAL, fill_opacity=0.1)
            clabel = Text(str(i + 1), font_size=18, color=CORAL)
            clabel.move_to(c)
            cg = VGroup(c, clabel)
            chairs.add(cg)

        persons.arrange(RIGHT, buff=0.4).shift(DOWN * 0.3 + LEFT * 3)
        chairs.arrange(RIGHT, buff=0.4).shift(DOWN * 0.3 + RIGHT * 3)

        people_heading = Text("People", font_size=22, color=TEAL)
        people_heading.next_to(persons, UP, buff=0.3)
        chairs_heading = Text("Positions", font_size=22, color=CORAL)
        chairs_heading.next_to(chairs, UP, buff=0.3)

        self.play(
            FadeIn(people_heading), FadeIn(chairs_heading),
            *[FadeIn(p, shift=DOWN) for p in persons],
            *[FadeIn(c, shift=DOWN) for c in chairs],
        )
        self.wait(0.5)

        # ── Arrows mapping people to chairs ─────────────────────
        mapping = [0, 2, 4, 1, 3]  # A->1, B->3, C->5, D->2, E->4
        arrows = VGroup()
        for i, j in enumerate(mapping):
            a = Arrow(
                persons[i].get_right(), chairs[j].get_left(),
                stroke_width=2, color=AMBER, buff=0.1,
                max_tip_length_to_length_ratio=0.15
            )
            arrows.add(a)

        self.play(*[GrowArrow(a) for a in arrows], run_time=1.5)

        goal = Text(
            "Goal: Deduce this mapping using ONLY the given clues",
            font_size=22, color=GREEN
        )
        goal.to_edge(DOWN, buff=0.5)
        self.play(Write(goal))
        self.wait(2)


# ====================================================================
# Scene 1.2 — Classification Tree
# ====================================================================
class ClassificationTree(Scene):
    """
    Animated tree: Seating Arrangements -> Linear / Circular / Complex
    each branch fans out into sub-types.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Classification of Seating Arrangements", font_size=36, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # ── Root node ───────────────────────────────────────────
        root = self._node("Seating\nArrangements", DARK)
        root.move_to(UP * 2)

        # ── Level-1 children ────────────────────────────────────
        linear = self._node("LINEAR", TEAL)
        circular = self._node("CIRCULAR", CORAL)
        complex_node = self._node("COMPLEX", INDIGO)
        level1 = VGroup(linear, circular, complex_node).arrange(RIGHT, buff=1.8)
        level1.next_to(root, DOWN, buff=1.0)

        # ── Level-2 children ────────────────────────────────────
        lin_sub1 = self._leaf("Single Row", TEAL)
        lin_sub2 = self._leaf("Double Row", TEAL)
        lin_subs = VGroup(lin_sub1, lin_sub2).arrange(DOWN, buff=0.3)
        lin_subs.next_to(linear, DOWN, buff=0.7)

        circ_sub1 = self._leaf("Round Table", CORAL)
        circ_sub2 = self._leaf("Square Table", CORAL)
        circ_subs = VGroup(circ_sub1, circ_sub2).arrange(DOWN, buff=0.3)
        circ_subs.next_to(circular, DOWN, buff=0.7)

        comp_sub1 = self._leaf("Rectangular", INDIGO)
        comp_sub2 = self._leaf("Floor-based", INDIGO)
        comp_sub3 = self._leaf("Hybrid", INDIGO)
        comp_subs = VGroup(comp_sub1, comp_sub2, comp_sub3).arrange(DOWN, buff=0.3)
        comp_subs.next_to(complex_node, DOWN, buff=0.7)

        # ── Edges ───────────────────────────────────────────────
        edges_l1 = VGroup(
            self._edge(root, linear),
            self._edge(root, circular),
            self._edge(root, complex_node),
        )
        edges_l2 = VGroup(
            self._edge(linear, lin_sub1),
            self._edge(linear, lin_sub2),
            self._edge(circular, circ_sub1),
            self._edge(circular, circ_sub2),
            self._edge(complex_node, comp_sub1),
            self._edge(complex_node, comp_sub2),
            self._edge(complex_node, comp_sub3),
        )

        # ── Animate ─────────────────────────────────────────────
        self.play(FadeIn(root, scale=0.8))
        self.wait(0.3)
        self.play(
            *[Create(e) for e in edges_l1],
            *[FadeIn(n, shift=DOWN) for n in [linear, circular, complex_node]],
            run_time=1.5
        )
        self.wait(0.3)
        self.play(
            *[Create(e) for e in edges_l2],
            *[FadeIn(n, shift=DOWN) for n in
              [lin_sub1, lin_sub2, circ_sub1, circ_sub2,
               comp_sub1, comp_sub2, comp_sub3]],
            run_time=1.5
        )

        # ── Exam frequency badges ──────────────────────────────
        gate_badge = self._badge("GATE: Linear + Circular dominate", GREEN)
        gate_badge.to_edge(DOWN, buff=0.6)
        bank_badge = self._badge("Banking: Double-Row + Circular mixed facing", AMBER)
        bank_badge.next_to(gate_badge, UP, buff=0.2)

        self.play(FadeIn(bank_badge, shift=LEFT), FadeIn(gate_badge, shift=LEFT))
        self.wait(2)

    # ── helpers ─────────────────────────────────────────────────
    @staticmethod
    def _node(label, color):
        box = RoundedRectangle(
            corner_radius=0.12, width=2.2, height=0.9,
            stroke_color=color, fill_color=color, fill_opacity=0.12
        )
        txt = Text(label, font_size=18, color=color)
        txt.move_to(box)
        return VGroup(box, txt)

    @staticmethod
    def _leaf(label, color):
        txt = Text(label, font_size=16, color=color)
        dot = Dot(radius=0.06, color=color).next_to(txt, LEFT, buff=0.1)
        return VGroup(dot, txt)

    @staticmethod
    def _edge(parent, child):
        return Line(
            parent.get_bottom(), child.get_top(),
            stroke_width=1.5, color=DARK
        )

    @staticmethod
    def _badge(text, color):
        t = Text(text, font_size=18, color=color)
        box = SurroundingRectangle(t, corner_radius=0.1, color=color, buff=0.15)
        return VGroup(box, t)


# ====================================================================
# Scene 1.3 — Core Terminology
# ====================================================================
class CoreTerminology(Scene):
    """
    Visual dictionary of positional and directional terms.
    Shows the critical LEFT / RIGHT perspective trap.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Core Terminology", font_size=36, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # ── Build a row of 7 seats ──────────────────────────────
        seats = VGroup()
        labels = "ABCDEFG"
        for i, ch in enumerate(labels):
            sq = Square(side_length=0.7, stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.08)
            t = Text(ch, font_size=22, color=TEAL)
            t.move_to(sq)
            g = VGroup(sq, t)
            seats.add(g)
        seats.arrange(RIGHT, buff=0.05)
        seats.move_to(UP * 0.5)

        pos_nums = VGroup()
        for i, s in enumerate(seats):
            n = Text(str(i + 1), font_size=14, color=DARK)
            n.next_to(s, DOWN, buff=0.1)
            pos_nums.add(n)

        self.play(*[FadeIn(s) for s in seats], *[FadeIn(n) for n in pos_nums])
        self.wait(0.5)

        # ── Immediate left / right ──────────────────────────────
        hl_d = SurroundingRectangle(seats[3], color=CORAL, buff=0.05)  # D
        hl_c = SurroundingRectangle(seats[2], color=GREEN, buff=0.05)  # C
        hl_e = SurroundingRectangle(seats[4], color=GREEN, buff=0.05)  # E

        note1 = Text("C is immediately LEFT of D", font_size=20, color=GREEN)
        note2 = Text("E is immediately RIGHT of D", font_size=20, color=GREEN)
        notes = VGroup(note1, note2).arrange(DOWN, buff=0.15)
        notes.next_to(seats, DOWN, buff=0.7)

        self.play(Create(hl_d))
        self.play(Create(hl_c), Write(note1))
        self.play(Create(hl_e), Write(note2))
        self.wait(1)

        # ── "Second to left" ────────────────────────────────────
        self.play(FadeOut(hl_c), FadeOut(hl_e), FadeOut(notes))
        hl_b = SurroundingRectangle(seats[1], color=AMBER, buff=0.05)
        note3 = Text("B is SECOND to the left of D", font_size=20, color=AMBER)
        note3.next_to(seats, DOWN, buff=0.7)
        brace = BraceBetweenPoints(
            seats[1].get_top() + UP * 0.15,
            seats[3].get_top() + UP * 0.15,
            direction=UP, color=AMBER
        )
        brace_label = Text("2 places", font_size=16, color=AMBER)
        brace_label.next_to(brace, UP, buff=0.1)
        self.play(Create(hl_b), Write(note3), Create(brace), Write(brace_label))
        self.wait(1)

        # ── "Between" ──────────────────────────────────────────
        self.play(
            FadeOut(hl_b), FadeOut(hl_d), FadeOut(note3),
            FadeOut(brace), FadeOut(brace_label)
        )
        hl_b2 = SurroundingRectangle(seats[1], color=CORAL, buff=0.05)
        hl_f = SurroundingRectangle(seats[5], color=CORAL, buff=0.05)
        between_brace = BraceBetweenPoints(
            seats[2].get_bottom() + DOWN * 0.15,
            seats[4].get_bottom() + DOWN * 0.15,
            direction=DOWN, color=INDIGO
        )
        between_label = Text(
            "C, D, E are BETWEEN B and F\n|p1 - p2| - 1 = |2 - 6| - 1 = 3",
            font_size=18, color=INDIGO
        )
        between_label.next_to(between_brace, DOWN, buff=0.15)
        self.play(Create(hl_b2), Create(hl_f), Create(between_brace), Write(between_label))
        self.wait(1)

        # ── End / Extreme positions ─────────────────────────────
        self.play(
            FadeOut(hl_b2), FadeOut(hl_f),
            FadeOut(between_brace), FadeOut(between_label)
        )
        hl_a = SurroundingRectangle(seats[0], color=AMBER, buff=0.05)
        hl_g = SurroundingRectangle(seats[6], color=AMBER, buff=0.05)
        end_note = Text(
            "A and G sit at EXTREME / END positions (1 neighbour only)",
            font_size=18, color=AMBER
        )
        end_note.next_to(seats, DOWN, buff=0.7)
        self.play(Create(hl_a), Create(hl_g), Write(end_note))
        self.wait(1)

        # ── The critical perspective trap ───────────────────────
        self.play(*[FadeOut(m) for m in self.mobjects if m != title])

        trap_title = Text(
            "CRITICAL TRAP: Left/Right is from the PERSON's perspective",
            font_size=24, color=CORAL
        )
        trap_title.next_to(title, DOWN, buff=0.6)
        self.play(Write(trap_title))

        # Person facing NORTH
        person_n = self._person("X", TEAL, "Facing North")
        person_n.shift(LEFT * 3 + DOWN * 0.5)
        arrow_n = Arrow(
            person_n.get_top() + UP * 0.1,
            person_n.get_top() + UP * 0.7,
            color=TEAL, buff=0
        )
        l_n = Text("Left", font_size=16, color=GREEN).next_to(person_n, LEFT, buff=0.5)
        r_n = Text("Right", font_size=16, color=CORAL).next_to(person_n, RIGHT, buff=0.5)
        arr_l_n = Arrow(person_n.get_left(), l_n.get_right(), color=GREEN, buff=0.1,
                        max_tip_length_to_length_ratio=0.2)
        arr_r_n = Arrow(person_n.get_right(), r_n.get_left(), color=CORAL, buff=0.1,
                        max_tip_length_to_length_ratio=0.2)

        # Person facing SOUTH
        person_s = self._person("Y", INDIGO, "Facing South")
        person_s.shift(RIGHT * 3 + DOWN * 0.5)
        arrow_s = Arrow(
            person_s.get_bottom() + DOWN * 0.1,
            person_s.get_bottom() + DOWN * 0.7,
            color=INDIGO, buff=0
        )
        l_s = Text("Left", font_size=16, color=GREEN).next_to(person_s, RIGHT, buff=0.5)
        r_s = Text("Right", font_size=16, color=CORAL).next_to(person_s, LEFT, buff=0.5)
        arr_l_s = Arrow(person_s.get_right(), l_s.get_left(), color=GREEN, buff=0.1,
                        max_tip_length_to_length_ratio=0.2)
        arr_r_s = Arrow(person_s.get_left(), r_s.get_right(), color=CORAL, buff=0.1,
                        max_tip_length_to_length_ratio=0.2)

        self.play(
            FadeIn(person_n), GrowArrow(arrow_n),
            FadeIn(person_s), GrowArrow(arrow_s),
        )
        self.play(
            GrowArrow(arr_l_n), Write(l_n),
            GrowArrow(arr_r_n), Write(r_n),
            GrowArrow(arr_l_s), Write(l_s),
            GrowArrow(arr_r_s), Write(r_s),
        )

        flip_note = Text(
            "Facing South FLIPS left/right on paper!",
            font_size=22, color=CORAL
        )
        flip_note.to_edge(DOWN, buff=0.5)
        self.play(Write(flip_note))
        self.wait(2)

    @staticmethod
    def _person(label, color, subtitle):
        c = Circle(radius=0.35, stroke_color=color, fill_color=color, fill_opacity=0.15)
        t = Text(label, font_size=24, color=color)
        t.move_to(c)
        s = Text(subtitle, font_size=14, color=color)
        s.next_to(c, DOWN, buff=0.15)
        return VGroup(c, t, s)


# ====================================================================
# Scene 1.4 — Universal 5-Step Solving Framework
# ====================================================================
class FiveStepFramework(Scene):
    """
    Pipeline animation: each step lights up in sequence.
    Analogy: assembly line in a factory.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("The 5-Step Solving Framework", font_size=36, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # ── Analogy ─────────────────────────────────────────────
        analogy = Text(
            "Think of it as an assembly line: raw material (clues) enters,\n"
            "finished product (arrangement) exits.",
            font_size=18, color=INDIGO
        )
        analogy.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(analogy))
        self.wait(1)

        # ── Steps as pipeline boxes ─────────────────────────────
        steps_data = [
            ("1. Draw\nSkeleton", TEAL,   "Empty row / circle\nwith position numbers"),
            ("2. Find\nDefinite Clues", CORAL,  "Absolute positions:\n'A sits at position 3'"),
            ("3. Place\nAnchor", AMBER,  "Most constrained\nperson goes first"),
            ("4. Apply\nRelative Clues", INDIGO, "'B is 2 to the left\nof A' — chain outward"),
            ("5. Eliminate\n& Verify", GREEN,  "Fill remaining slots,\ncheck ALL clues hold"),
        ]

        boxes = VGroup()
        arrows = VGroup()
        for i, (label, color, desc) in enumerate(steps_data):
            box = RoundedRectangle(
                corner_radius=0.1, width=2.0, height=1.5,
                stroke_color=color, fill_color=color, fill_opacity=0.08
            )
            lbl = Text(label, font_size=14, color=color)
            lbl.move_to(box.get_center() + UP * 0.15)
            d = Text(desc, font_size=10, color=DARK)
            d.next_to(lbl, DOWN, buff=0.1)
            g = VGroup(box, lbl, d)
            boxes.add(g)

        boxes.arrange(RIGHT, buff=0.35)
        boxes.next_to(analogy, DOWN, buff=0.6)

        # Scale to fit
        if boxes.width > 13:
            boxes.scale_to_fit_width(13)

        for i in range(len(boxes) - 1):
            a = Arrow(
                boxes[i].get_right(), boxes[i + 1].get_left(),
                stroke_width=2, color=DARK, buff=0.05,
                max_tip_length_to_length_ratio=0.2
            )
            arrows.add(a)

        # ── Animate step by step ────────────────────────────────
        for i, box in enumerate(boxes):
            anims = [FadeIn(box, shift=UP)]
            if i > 0:
                anims.append(GrowArrow(arrows[i - 1]))
            self.play(*anims, run_time=0.8)
            self.wait(0.3)

        # ── Highlight the key insight ───────────────────────────
        key = Text(
            "KEY: Step 3 (Anchor) determines solving speed.\n"
            "Pick the person mentioned in the MOST clues.",
            font_size=20, color=CORAL
        )
        key.to_edge(DOWN, buff=0.4)
        self.play(Write(key))
        self.wait(2)


# ====================================================================
# Scene 1.5 — Notation System
# ====================================================================
class NotationSystem(Scene):
    """Visual legend for the shorthand notation used throughout."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("Notation System", font_size=36, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        notations = [
            ("A --- B",      "A and B are adjacent",              TEAL),
            ("A _ B",        "A is immediately LEFT of B",        CORAL),
            ("A __ B",       "A is two places LEFT of B",         AMBER),
            ("A  x  B",      "A and B are NOT adjacent",          CORAL),
            ("A <-> B",      "A and B sit OPPOSITE each other",   INDIGO),
            ("A [end]",      "A sits at an END / CORNER",         GREEN),
        ]

        rows = VGroup()
        for sym, meaning, color in notations:
            sym_text = Text(sym, font_size=22, color=color, font="Monospace")
            sym_text.set_width(2.5, stretch=True) if sym_text.width > 2.5 else None
            meaning_text = Text(meaning, font_size=20, color=DARK)
            r = VGroup(sym_text, meaning_text).arrange(RIGHT, buff=1.0)
            rows.add(r)

        rows.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        rows.next_to(title, DOWN, buff=0.6)

        for r in rows:
            self.play(FadeIn(r, shift=RIGHT), run_time=0.5)
        self.wait(0.5)

        tip = Text(
            "Use this notation on rough paper to save time during exams.",
            font_size=20, color=GREEN
        )
        tip.to_edge(DOWN, buff=0.5)
        self.play(Write(tip))
        self.wait(2)


# ====================================================================
# Scene 1.6 — Constraint Density Principle
# ====================================================================
class ConstraintDensityPrinciple(Scene):
    """
    Analogy: social network — the person with the most connections
    (mentions in clues) gives the most information when placed first.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Constraint Density Principle", font_size=36, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        subtitle = Text(
            "Place the person mentioned in the MOST clues first.",
            font_size=22, color=INDIGO
        )
        subtitle.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle))

        # ── Network graph: nodes = people, edges = clue mentions ─
        positions = {
            "A": LEFT * 2 + DOWN * 0.5,
            "B": LEFT * 0.5 + UP * 0.8,
            "C": RIGHT * 1.5 + UP * 0.5,
            "D": RIGHT * 2.5 + DOWN * 0.5,
            "E": ORIGIN + DOWN * 1.5,
        }

        # B appears in clues with A, C, D, E (4 connections = most constrained)
        edges_data = [
            ("A", "B"), ("B", "C"), ("B", "D"), ("B", "E"), ("A", "E"),
        ]

        nodes = {}
        for name, pos in positions.items():
            c = Circle(radius=0.35, stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.1)
            c.move_to(pos)
            t = Text(name, font_size=22, color=TEAL)
            t.move_to(c)
            g = VGroup(c, t)
            nodes[name] = g

        edges = VGroup()
        for n1, n2 in edges_data:
            e = Line(
                nodes[n1][0].get_center(), nodes[n2][0].get_center(),
                stroke_width=2, color=DARK
            )
            edges.add(e)

        all_nodes = VGroup(*nodes.values())
        graph = VGroup(edges, all_nodes)
        graph.move_to(DOWN * 0.5)

        self.play(*[FadeIn(n) for n in nodes.values()])
        self.play(*[Create(e) for e in edges], run_time=1)
        self.wait(0.5)

        # ── Highlight B as the most connected ───────────────────
        b_highlight = Circle(
            radius=0.45, stroke_color=CORAL, stroke_width=4
        ).move_to(nodes["B"][0])

        count_label = Text(
            "B has 4 connections\n= Place B FIRST",
            font_size=20, color=CORAL
        )
        count_label.next_to(b_highlight, RIGHT, buff=0.8)

        self.play(Create(b_highlight), Write(count_label))
        self.wait(1)

        # ── Cascade animation ───────────────────────────────────
        cascade_text = Text(
            "Once B is placed, A, C, D, E positions cascade automatically",
            font_size=20, color=GREEN
        )
        cascade_text.to_edge(DOWN, buff=0.5)

        # Highlight edges emanating from B in sequence
        for e in [edges[0], edges[1], edges[2], edges[3]]:
            self.play(e.animate.set_color(AMBER), run_time=0.3)

        self.play(Write(cascade_text))
        self.wait(2)


# ====================================================================
# Scene 1.7 — Perspective Trap (Common Mistake)
# ====================================================================
class PerspectiveTrap(Scene):
    """
    Shows the number-one mistake: confusing the reader's left/right
    with the person's left/right.
    Two-panel animation: wrong vs right interpretation.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Common Mistake: The Perspective Trap", font_size=34, color=CORAL)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        clue = Text(
            'Clue: "B sits to the LEFT of A"',
            font_size=24, color=DARK
        )
        clue.next_to(title, DOWN, buff=0.5)
        self.play(Write(clue))

        # ── WRONG interpretation (reader's left) ────────────────
        wrong_title = Text("WRONG (reader's left)", font_size=20, color=CORAL)
        wrong_row = self._build_row(["B", "A", "_", "_"], CORAL)
        wrong_group = VGroup(wrong_title, wrong_row).arrange(DOWN, buff=0.2)
        wrong_group.shift(LEFT * 3 + DOWN * 1)

        cross = Cross(wrong_group, stroke_color=CORAL, stroke_width=4)

        # ── RIGHT interpretation (person's left) ────────────────
        right_title = Text("CORRECT (A's perspective)", font_size=20, color=GREEN)

        # When all face North: A's left = lower position = paper-left
        # So B is to A's left = B sits in lower position
        right_row = self._build_row(["B", "A", "_", "_"], GREEN)
        note = Text("All face North: person's left = paper left", font_size=14, color=DARK)
        right_group = VGroup(right_title, right_row, note).arrange(DOWN, buff=0.2)
        right_group.shift(RIGHT * 3 + DOWN * 1)

        check = Text("Correct", font_size=20, color=GREEN)
        check.next_to(right_group, DOWN, buff=0.2)

        self.play(FadeIn(wrong_group, shift=DOWN))
        self.wait(0.5)
        self.play(Create(cross))
        self.wait(0.5)
        self.play(FadeIn(right_group, shift=DOWN), Write(check))
        self.wait(1)

        # ── South-facing reversal ───────────────────────────────
        south_note = Text(
            "But if all face SOUTH: person's left = paper RIGHT\n"
            "Then B sits to the RIGHT of A on paper!",
            font_size=20, color=AMBER
        )
        south_note.to_edge(DOWN, buff=0.4)
        self.play(Write(south_note))
        self.wait(2)

    @staticmethod
    def _build_row(labels, color):
        seats = VGroup()
        for lbl in labels:
            sq = Square(side_length=0.6, stroke_color=color, fill_color=color, fill_opacity=0.08)
            t = Text(lbl, font_size=20, color=color)
            t.move_to(sq)
            seats.add(VGroup(sq, t))
        seats.arrange(RIGHT, buff=0.05)
        return seats
