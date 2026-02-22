"""
Scene 06: Advanced Techniques and Shortcuts
=============================================
Manim CE script — covers Chapter 6 concepts:
  6.1 Overview of speed techniques
  6.2 Fixed-Point Cascade (BFS animation)
  6.3 Two-Case Split Method
  6.4 Negative Constraint (elimination matrix)
  6.5 Block Method (consecutive chains)
  6.6 Counting Shortcuts
  6.7 Option Elimination (MCQ)
  6.8 Symmetry Shortcut
  6.9 Time Management: 3-Minute Rule

Render all:  manim -pqh scene_06_advanced.py
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
# Scene 6.2 — Fixed-Point Cascade (BFS)
# ====================================================================
class FixedPointCascade(Scene):
    """
    Analogy: Dominoes — place one fixed piece, and the rest cascade.
    Animated BFS on the constraint graph.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Technique 1: Fixed-Point Cascade", font_size=32, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        analogy = Text(
            "Analogy: Domino chain reaction — one fixed piece topples the rest.",
            font_size=18, color=INDIGO
        )
        analogy.next_to(title, DOWN, buff=0.3)
        self.play(Write(analogy))

        # ── Constraint graph ────────────────────────────────────
        # Nodes: A,B,C,D,E. Fixed: A at pos 3. Edges show relative constraints.
        nodes_data = {
            "A": LEFT * 3 + DOWN * 0.5,
            "B": LEFT * 1 + UP * 0.5,
            "C": RIGHT * 1 + DOWN * 1,
            "D": RIGHT * 3 + UP * 0.5,
            "E": RIGHT * 1.5 + DOWN * 2,
        }
        edges_data = [("A", "B"), ("B", "C"), ("C", "D"), ("A", "E")]

        nodes = {}
        for name, pos in nodes_data.items():
            c = Circle(radius=0.35, stroke_color=DARK, fill_color=WHITE, fill_opacity=1)
            c.move_to(pos)
            t = Text(name, font_size=22, color=DARK)
            t.move_to(c)
            nodes[name] = VGroup(c, t)

        edges = {}
        edge_vgroup = VGroup()
        for n1, n2 in edges_data:
            line = Line(
                nodes[n1][0].get_center(), nodes[n2][0].get_center(),
                stroke_width=2, color=DARK
            )
            edges[(n1, n2)] = line
            edge_vgroup.add(line)

        all_nodes = VGroup(*nodes.values())
        graph = VGroup(edge_vgroup, all_nodes)

        self.play(FadeIn(graph))
        self.wait(0.5)

        # ── Step 1: Fix A (turn green) ──────────────────────────
        step1 = Text("Step 1: A is FIXED at position 3", font_size=18, color=GREEN)
        step1.to_edge(DOWN, buff=1.5)
        self.play(
            nodes["A"][0].animate.set_fill(GREEN, opacity=0.3).set_stroke(GREEN),
            nodes["A"][1].animate.set_color(GREEN),
            Write(step1)
        )
        self.wait(0.5)

        # ── Step 2: Cascade to B (A->B edge lights up) ─────────
        self.play(FadeOut(step1))
        step2 = Text("Step 2: B is '2 right of A' -> pos 5 (cascades from A)", font_size=18, color=TEAL)
        step2.to_edge(DOWN, buff=1.5)
        self.play(
            edges[("A", "B")].animate.set_color(AMBER).set_stroke(width=4),
            nodes["B"][0].animate.set_fill(TEAL, opacity=0.3).set_stroke(TEAL),
            nodes["B"][1].animate.set_color(TEAL),
            Write(step2)
        )
        self.wait(0.5)

        # ── Step 3: Cascade to C (B->C) ────────────────────────
        self.play(FadeOut(step2))
        step3 = Text("Step 3: C is 'opposite B' -> pos 2 (cascades from B)", font_size=18, color=TEAL)
        step3.to_edge(DOWN, buff=1.5)
        self.play(
            edges[("B", "C")].animate.set_color(AMBER).set_stroke(width=4),
            nodes["C"][0].animate.set_fill(TEAL, opacity=0.3).set_stroke(TEAL),
            nodes["C"][1].animate.set_color(TEAL),
            Write(step3)
        )
        self.wait(0.5)

        # ── Step 4: Cascade to D (C->D) and E (A->E) ───────────
        self.play(FadeOut(step3))
        step4 = Text("Step 4: D from C, E from A — all resolved!", font_size=18, color=GREEN)
        step4.to_edge(DOWN, buff=1.5)
        self.play(
            edges[("C", "D")].animate.set_color(AMBER).set_stroke(width=4),
            nodes["D"][0].animate.set_fill(TEAL, opacity=0.3).set_stroke(TEAL),
            nodes["D"][1].animate.set_color(TEAL),
            edges[("A", "E")].animate.set_color(AMBER).set_stroke(width=4),
            nodes["E"][0].animate.set_fill(TEAL, opacity=0.3).set_stroke(TEAL),
            nodes["E"][1].animate.set_color(TEAL),
            Write(step4)
        )

        # ── Summary ─────────────────────────────────────────────
        summary = Text(
            "One fixed point -> ALL positions determined via BFS on constraint graph",
            font_size=18, color=GREEN
        )
        summary.to_edge(DOWN, buff=0.4)
        self.play(FadeOut(step4), Write(summary))
        self.wait(2)


# ====================================================================
# Scene 6.3 — Two-Case Split
# ====================================================================
class TwoCaseSplit(Scene):
    """
    Animated parallel-worlds approach: when a branching occurs,
    maintain both cases and eliminate the contradicted one.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Technique 2: Two-Case Split", font_size=32, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        analogy = Text(
            "Analogy: Fork in the road — walk both paths simultaneously,\n"
            "one will hit a dead end.",
            font_size=18, color=INDIGO
        )
        analogy.next_to(title, DOWN, buff=0.3)
        self.play(Write(analogy))

        # ── The fork ────────────────────────────────────────────
        start = Dot(LEFT * 4 + DOWN * 0.5, color=DARK, radius=0.1)
        start_label = Text("Branching point:\nA at pos 2 OR pos 5", font_size=14, color=DARK)
        start_label.next_to(start, DOWN, buff=0.2)

        # Case 1 path
        case1_line = Arrow(start.get_center(), LEFT * 1 + UP * 1, color=TEAL, stroke_width=3)
        case1_box = RoundedRectangle(
            corner_radius=0.1, width=3.5, height=1.5,
            stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.08
        )
        case1_box.next_to(case1_line.get_end(), RIGHT, buff=0.2)
        case1_title = Text("Case 1: A at pos 2", font_size=16, color=TEAL)
        case1_detail = Text("Apply remaining clues...\nB at pos 4, C at pos 1...", font_size=12, color=DARK)
        case1_content = VGroup(case1_title, case1_detail).arrange(DOWN, buff=0.1)
        case1_content.move_to(case1_box)

        # Case 2 path
        case2_line = Arrow(start.get_center(), LEFT * 1 + DOWN * 2, color=CORAL, stroke_width=3)
        case2_box = RoundedRectangle(
            corner_radius=0.1, width=3.5, height=1.5,
            stroke_color=CORAL, fill_color=CORAL, fill_opacity=0.08
        )
        case2_box.next_to(case2_line.get_end(), RIGHT, buff=0.2)
        case2_title = Text("Case 2: A at pos 5", font_size=16, color=CORAL)
        case2_detail = Text("Apply remaining clues...\nB at pos 7 -> INVALID (n=6)!", font_size=12, color=DARK)
        case2_content = VGroup(case2_title, case2_detail).arrange(DOWN, buff=0.1)
        case2_content.move_to(case2_box)

        self.play(FadeIn(start), Write(start_label))
        self.play(GrowArrow(case1_line), FadeIn(case1_box), Write(case1_content))
        self.play(GrowArrow(case2_line), FadeIn(case2_box), Write(case2_content))
        self.wait(0.5)

        # ── Cross out Case 2 ───────────────────────────────────
        cross = Cross(case2_box, stroke_color=CORAL, stroke_width=4)
        contradiction = Text("CONTRADICTION!", font_size=18, color=CORAL)
        contradiction.next_to(case2_box, RIGHT, buff=0.3)

        valid = Text("VALID", font_size=18, color=GREEN)
        valid.next_to(case1_box, RIGHT, buff=0.3)

        self.play(Create(cross), Write(contradiction))
        self.play(
            case1_box.animate.set_stroke(GREEN, width=3),
            Write(valid)
        )
        self.wait(2)


# ====================================================================
# Scene 6.4 — Negative Constraint (Elimination Matrix)
# ====================================================================
class NegativeConstraint(Scene):
    """
    Track where people CANNOT sit.
    Shows the elimination matrix and 'naked single' technique.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Technique 3: Negative Constraint Matrix", font_size=30, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        analogy = Text(
            "Analogy: Sudoku — cross out impossibilities until only one option remains.",
            font_size=18, color=INDIGO
        )
        analogy.next_to(title, DOWN, buff=0.3)
        self.play(Write(analogy))

        # ── Build a 4x4 elimination matrix ──────────────────────
        people = ["A", "B", "C", "D"]
        positions = ["1", "2", "3", "4"]

        cell_size = 0.7
        matrix = VGroup()

        # Header row
        for j, pos in enumerate(positions):
            cell = Square(side_length=cell_size, stroke_color=DARK,
                          fill_color=TEAL, fill_opacity=0.1)
            cell.move_to(RIGHT * (j + 1) * cell_size + UP * 0 * cell_size)
            t = Text(f"Pos {pos}", font_size=11, color=TEAL)
            t.move_to(cell)
            matrix.add(VGroup(cell, t))

        # Header column
        for i, person in enumerate(people):
            cell = Square(side_length=cell_size, stroke_color=DARK,
                          fill_color=CORAL, fill_opacity=0.1)
            cell.move_to(RIGHT * 0 * cell_size + DOWN * (i + 1) * cell_size)
            t = Text(person, font_size=16, color=CORAL)
            t.move_to(cell)
            matrix.add(VGroup(cell, t))

        # Data cells (initially all '?')
        data_cells = {}
        for i in range(4):
            for j in range(4):
                cell = Square(side_length=cell_size, stroke_color=DARK,
                              fill_color=WHITE, fill_opacity=1)
                cell.move_to(RIGHT * (j + 1) * cell_size + DOWN * (i + 1) * cell_size)
                t = Text("?", font_size=16, color=DARK)
                t.move_to(cell)
                g = VGroup(cell, t)
                data_cells[(i, j)] = g
                matrix.add(g)

        matrix.move_to(LEFT * 1 + DOWN * 0.8)
        self.play(FadeIn(matrix), run_time=1)
        self.wait(0.5)

        # ── Apply constraints ───────────────────────────────────
        # Clue: A is NOT at pos 1 or 3
        clue1 = Text('Clue: "A not at pos 1 or 3"', font_size=16, color=AMBER)
        clue1.shift(RIGHT * 4 + UP * 0.5)
        self.play(Write(clue1))

        # Mark X at A-pos1 and A-pos3
        for j in [0, 2]:  # pos 1 and 3
            new_t = Text("X", font_size=18, color=CORAL)
            new_t.move_to(data_cells[(0, j)])
            self.play(
                Transform(data_cells[(0, j)][1], new_t),
                data_cells[(0, j)][0].animate.set_fill(CORAL, opacity=0.1),
                run_time=0.4
            )

        # Clue: B is at pos 1
        clue2 = Text('Clue: "B at pos 1"', font_size=16, color=GREEN)
        clue2.next_to(clue1, DOWN, buff=0.2)
        self.play(Write(clue2))

        # Mark checkmark at B-pos1, X at all others in row B and col 1
        check = Text("Y", font_size=18, color=GREEN)
        check.move_to(data_cells[(1, 0)])
        self.play(
            Transform(data_cells[(1, 0)][1], check),
            data_cells[(1, 0)][0].animate.set_fill(GREEN, opacity=0.15),
            run_time=0.4
        )
        for j in [1, 2, 3]:
            new_t = Text("X", font_size=18, color=CORAL)
            new_t.move_to(data_cells[(1, j)])
            self.play(
                Transform(data_cells[(1, j)][1], new_t),
                data_cells[(1, j)][0].animate.set_fill(CORAL, opacity=0.1),
                run_time=0.2
            )
        for i in [2, 3]:  # C and D can't be at pos 1
            new_t = Text("X", font_size=18, color=CORAL)
            new_t.move_to(data_cells[(i, 0)])
            self.play(
                Transform(data_cells[(i, 0)][1], new_t),
                data_cells[(i, 0)][0].animate.set_fill(CORAL, opacity=0.1),
                run_time=0.2
            )

        # ── Naked single ───────────────────────────────────────
        naked = Text(
            '"Naked Single": If only one ? remains\n'
            "in a row or column, that MUST be the answer.",
            font_size=16, color=GREEN
        )
        naked.shift(RIGHT * 4 + DOWN * 1.5)
        self.play(Write(naked))
        self.wait(2)


# ====================================================================
# Scene 6.5 — Block Method
# ====================================================================
class BlockMethod(Scene):
    """
    Treat consecutive people as a single block.
    Block of size m in row of n -> (n - m + 1) possible positions.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Technique 4: Block Method", font_size=32, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # ── A row of 6 seats ───────────────────────────────────
        n = 6
        seats = VGroup()
        for i in range(n):
            sq = Square(side_length=0.7, stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.06)
            t = Text(str(i + 1), font_size=18, color=TEAL)
            t.move_to(sq)
            seats.add(VGroup(sq, t))
        seats.arrange(RIGHT, buff=0.05)
        seats.move_to(UP * 1.2)
        self.play(*[FadeIn(s) for s in seats])

        # ── Define a block: A-B-C must sit together ─────────────
        block_label = Text('"A, B, C must sit together (in order)"', font_size=20, color=CORAL)
        block_label.next_to(seats, DOWN, buff=0.5)
        self.play(Write(block_label))

        block = RoundedRectangle(
            corner_radius=0.08, width=2.25, height=0.85,
            stroke_color=CORAL, fill_color=CORAL, fill_opacity=0.15, stroke_width=3
        )
        block.move_to(seats[0].get_center())
        block_text = Text("A B C", font_size=20, color=CORAL)
        block_text.move_to(block)
        self.play(FadeIn(block), Write(block_text))
        self.wait(0.5)

        # ── Animate sliding the block across positions ──────────
        # Block can start at positions 1, 2, 3, 4 (n - m + 1 = 6 - 3 + 1 = 4)
        for target_idx in [1, 2, 3]:
            target_pos = seats[target_idx].get_center()
            self.play(
                block.animate.move_to(target_pos),
                block_text.animate.move_to(target_pos),
                run_time=0.6
            )
            self.wait(0.2)

        # ── Formula ─────────────────────────────────────────────
        formula = MathTex(
            r"\text{Block of size } m \text{ in row of } n: \quad n - m + 1 \text{ positions}",
            font_size=24, color=INDIGO
        )
        formula.next_to(block_label, DOWN, buff=0.5)
        self.play(Write(formula))

        example = MathTex(
            r"m = 3, n = 6: \quad 6 - 3 + 1 = 4 \text{ sliding positions}",
            font_size=22, color=AMBER
        )
        example.next_to(formula, DOWN, buff=0.3)
        self.play(Write(example))
        self.wait(2)


# ====================================================================
# Scene 6.6 — Counting Shortcuts
# ====================================================================
class CountingShortcuts(Scene):
    """Quick formulas for common counting questions."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("Counting Shortcuts", font_size=34, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        formulas = VGroup(
            Text("Linear:", font_size=20, color=TEAL),
            MathTex(r"\text{People between } p_1, p_2 = |p_1 - p_2| - 1", font_size=22, color=TEAL),
            Text("", font_size=6),
            Text("Circular (shorter arc):", font_size=20, color=CORAL),
            MathTex(r"d = \min(|p_1 - p_2|, \; n - |p_1 - p_2|)", font_size=22, color=CORAL),
            MathTex(r"\text{People between} = d - 1", font_size=22, color=CORAL),
            Text("", font_size=6),
            Text("Arrangements:", font_size=20, color=INDIGO),
            MathTex(r"\text{Linear: } n!", font_size=22, color=INDIGO),
            MathTex(r"\text{Circular: } (n-1)!", font_size=22, color=INDIGO),
            MathTex(r"\text{Block of } m \text{ in } n \text{: } (n-m+1) \times m!",
                    font_size=22, color=INDIGO),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        formulas.next_to(title, DOWN, buff=0.4)

        for f in formulas:
            self.play(Write(f), run_time=0.4)

        self.wait(2)


# ====================================================================
# Scene 6.8 — Symmetry Shortcut
# ====================================================================
class SymmetryShortcut(Scene):
    """
    Mirror arrangements: if two valid arrangements exist (mirror images),
    questions about the SAME element give the SAME answer.
    """

    def construct(self):
        self.camera.background_color = BG

        title = Text("Technique 7: Symmetry Shortcut", font_size=32, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # ── Two mirror arrangements ─────────────────────────────
        arr1_label = Text("Arrangement 1", font_size=18, color=TEAL)
        arr1 = self._build_row(["A", "B", "C", "D", "E"], TEAL)
        g1 = VGroup(arr1_label, arr1).arrange(DOWN, buff=0.15)
        g1.shift(UP * 0.8)

        arr2_label = Text("Arrangement 2 (Mirror)", font_size=18, color=CORAL)
        arr2 = self._build_row(["E", "D", "C", "B", "A"], CORAL)
        g2 = VGroup(arr2_label, arr2).arrange(DOWN, buff=0.15)
        g2.shift(DOWN * 0.8)

        mirror_arrow = DoubleArrow(g1.get_bottom(), g2.get_top(), color=AMBER, stroke_width=2)
        mirror_text = Text("Mirror", font_size=14, color=AMBER)
        mirror_text.next_to(mirror_arrow, RIGHT, buff=0.1)

        self.play(FadeIn(g1), FadeIn(g2), GrowArrow(mirror_arrow), Write(mirror_text))
        self.wait(0.5)

        # ── Key insight ─────────────────────────────────────────
        insight = Text(
            'Q: "Who sits in the middle?"\n'
            "Arr1: C  |  Arr2: C  ->  SAME answer regardless!\n"
            "No need to determine which arrangement is correct.",
            font_size=18, color=GREEN
        )
        insight.to_edge(DOWN, buff=0.4)

        hl1 = SurroundingRectangle(arr1[2], color=GREEN, buff=0.03, stroke_width=3)
        hl2 = SurroundingRectangle(arr2[2], color=GREEN, buff=0.03, stroke_width=3)
        self.play(Create(hl1), Create(hl2), Write(insight))
        self.wait(2)

    @staticmethod
    def _build_row(labels, color):
        seats = VGroup()
        for lbl in labels:
            sq = Square(side_length=0.6, stroke_color=color, fill_color=color, fill_opacity=0.06)
            t = Text(lbl, font_size=18, color=color)
            t.move_to(sq)
            seats.add(VGroup(sq, t))
        seats.arrange(RIGHT, buff=0.03)
        return seats


# ====================================================================
# Scene 6.9 — Time Management
# ====================================================================
class TimeManagement(Scene):
    """3-minute rule for exams."""

    def construct(self):
        self.camera.background_color = BG

        title = Text("Time Management: The 3-Minute Rule", font_size=32, color=DARK)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # ── Banking timeline ────────────────────────────────────
        bank_title = Text("Banking Exam (6 min per set):", font_size=20, color=TEAL)
        bank_title.next_to(title, DOWN, buff=0.5).shift(LEFT * 2)

        phases_bank = [
            ("0-2 min", "Read + Skeleton", TEAL),
            ("2-4 min", "Place People", AMBER),
            ("4-6 min", "Answer Questions", GREEN),
        ]

        bank_timeline = VGroup()
        for phase, desc, color in phases_bank:
            box = RoundedRectangle(
                corner_radius=0.08, width=3, height=0.7,
                stroke_color=color, fill_color=color, fill_opacity=0.1
            )
            time_t = Text(phase, font_size=14, color=color)
            desc_t = Text(desc, font_size=14, color=DARK)
            content = VGroup(time_t, desc_t).arrange(RIGHT, buff=0.2)
            content.move_to(box)
            bank_timeline.add(VGroup(box, content))

        bank_timeline.arrange(RIGHT, buff=0.1)
        bank_timeline.next_to(bank_title, DOWN, buff=0.3)

        # ── GATE timeline ───────────────────────────────────────
        gate_title = Text("GATE (3 min per question):", font_size=20, color=CORAL)
        gate_title.next_to(bank_timeline, DOWN, buff=0.5).align_to(bank_title, LEFT)

        phases_gate = [
            ("0-1 min", "Read + Draw", CORAL),
            ("1-2 min", "Solve", AMBER),
            ("2-3 min", "Verify", GREEN),
        ]

        gate_timeline = VGroup()
        for phase, desc, color in phases_gate:
            box = RoundedRectangle(
                corner_radius=0.08, width=3, height=0.7,
                stroke_color=color, fill_color=color, fill_opacity=0.1
            )
            time_t = Text(phase, font_size=14, color=color)
            desc_t = Text(desc, font_size=14, color=DARK)
            content = VGroup(time_t, desc_t).arrange(RIGHT, buff=0.2)
            content.move_to(box)
            gate_timeline.add(VGroup(box, content))

        gate_timeline.arrange(RIGHT, buff=0.1)
        gate_timeline.next_to(gate_title, DOWN, buff=0.3)

        self.play(Write(bank_title))
        for box in bank_timeline:
            self.play(FadeIn(box, shift=RIGHT), run_time=0.5)
        self.play(Write(gate_title))
        for box in gate_timeline:
            self.play(FadeIn(box, shift=RIGHT), run_time=0.5)

        rule = Text(
            "RULE: If stuck after 3 minutes, mark and move on. Return if time permits.",
            font_size=18, color=CORAL
        )
        rule.to_edge(DOWN, buff=0.4)
        self.play(Write(rule))
        self.wait(2)
