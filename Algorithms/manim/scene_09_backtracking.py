"""
Chapter 9: Backtracking & Branch and Bound
Manim CE animation scenes covering all concepts.

Render: manim -pqh scene_09_backtracking.py <SceneName>
"""

from manim import *
import numpy as np

TEAL = "#1a8a8a"
CORAL = "#d94f4f"
AMBER = "#e8a317"
INDIGO = "#4a5da8"
GREEN = "#2e8b57"


class Scene01_BacktrackingParadigm(Scene):
    """Backtracking template: explore, prune, undo."""

    def construct(self):
        title = Text("Backtracking", font_size=44, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        analogy = Text(
            "Like navigating a maze: go forward, dead end => backtrack",
            font_size=22, color=AMBER,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(analogy))

        template = VGroup(
            Text("Backtrack(state):", font_size=22, color=GREEN),
            Text("  if complete solution: process it", font_size=20),
            Text("  for each possible next choice:", font_size=20),
            Text("    if valid (prune!):", font_size=20, color=CORAL),
            Text("      make choice", font_size=20),
            Text("      Backtrack(new state)", font_size=20),
            Text("      UNDO choice  <-- backtrack", font_size=20, color=CORAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(analogy, DOWN, buff=0.4)
        box = SurroundingRectangle(template, buff=0.15, corner_radius=0.1, stroke_width=1, color=GREEN)
        self.play(FadeIn(template), Create(box))

        diff = Text(
            "Key vs brute force: backtracking PRUNES invalid branches",
            font_size=22, color=INDIGO,
        ).to_edge(DOWN)
        self.play(Write(diff))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene02_NQueens(Scene):
    """N-Queens: animate queen placement on 4x4 board."""

    def construct(self):
        title = Text("N-Queens Problem", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        N = 4
        board = VGroup()
        squares = {}
        for r in range(N):
            for c in range(N):
                color = WHITE if (r + c) % 2 == 0 else LIGHT_GRAY
                sq = Square(side_length=0.7, fill_color=color, fill_opacity=0.3, stroke_width=1)
                sq.move_to([c * 0.7 - 1.05, -r * 0.7 + 1.05, 0])
                squares[(r, c)] = sq
                board.add(sq)
        board.next_to(title, DOWN, buff=0.5).shift(LEFT * 2)
        self.play(FadeIn(board))

        # One valid solution for 4-Queens: columns [1, 3, 0, 2]
        solution = [1, 3, 0, 2]
        queens = VGroup()
        for r, c in enumerate(solution):
            q = Text("Q", font_size=22, color=CORAL, weight=BOLD)
            q.move_to(squares[(r, c)].get_center())
            queens.add(q)
            self.play(Write(q), squares[(r, c)].animate.set_fill(GREEN, opacity=0.3), run_time=0.5)

        # Safety check explanation
        rules = VGroup(
            Text("No two queens in same:", font_size=22, color=AMBER),
            Text("  Row | Column | Diagonal", font_size=22, color=CORAL),
            Text("Check: |col_i - col_j| != |i - j|", font_size=20, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(board, RIGHT, buff=0.5)
        self.play(Write(rules))

        # Solution counts
        counts = VGroup(
            Text("N=1: 1 | N=4: 2 | N=5: 10 | N=8: 92", font_size=20, color=INDIGO),
            Text("Time: ~O(N!) with pruning", font_size=20),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN)
        self.play(Write(counts))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene03_SubsetSum(Scene):
    """Subset sum with pruning."""

    def construct(self):
        title = Text("Subset Sum Problem", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        problem = Text(
            "Find subset of S whose sum = target T",
            font_size=24, color=AMBER,
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(problem))

        tree = VGroup(
            Text("Include S[n] or Exclude S[n]", font_size=22, color=GREEN),
            Text("Prune if:", font_size=22, color=CORAL),
            Text("  current element > remaining target", font_size=20),
            Text("  sum of remaining < target", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(problem, DOWN, buff=0.4)
        for t in tree:
            self.play(Write(t), run_time=0.4)

        fact = Text(
            "Subset Sum is NP-Complete — exponential worst case",
            font_size=22, color=CORAL,
        ).to_edge(DOWN)
        self.play(Write(fact))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene04_GraphColoring(Scene):
    """Graph coloring backtracking and chromatic number facts."""

    def construct(self):
        title = Text("Graph Coloring", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        facts = VGroup(
            Text("Complete K_n: χ(K_n) = n", font_size=22, color=CORAL),
            Text("Bipartite: χ = 2", font_size=22, color=GREEN),
            Text("Tree: χ = 2", font_size=22, color=GREEN),
            Text("Odd cycle: χ = 3", font_size=22, color=AMBER),
            Text("Planar: χ <= 4 (Four Color Theorem)", font_size=22, color=INDIGO),
            Text("Graph coloring is NP-Complete for m >= 3", font_size=22, color=CORAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.5)
        for f in facts:
            self.play(FadeIn(f, shift=LEFT), run_time=0.4)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene05_HamiltonianVsEuler(Scene):
    """Compare Hamiltonian (NP-Complete) vs Euler (polynomial)."""

    def construct(self):
        title = Text("Hamiltonian vs Euler", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["", "Eulerian", "Hamiltonian"],
            ["Visits", "Every edge once", "Every vertex once"],
            ["Easy check?", "Yes (degree)", "No (NPC)"],
            ["Complexity", "O(E)", "NP-Complete"],
        ]
        table = Table(
            [row[1:] for row in data[1:]],
            row_labels=[Text(row[0], font_size=20) for row in data[1:]],
            col_labels=[Text(h, font_size=20, weight=BOLD, color=AMBER) for h in data[0][1:]],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.6).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(table))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene06_BranchAndBound(Scene):
    """Branch and bound: bound-based pruning for optimisation."""

    def construct(self):
        title = Text("Branch and Bound", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        comparison = VGroup(
            VGroup(
                Text("Backtracking", font_size=24, color=AMBER, weight=BOLD),
                Text("Feasibility problems", font_size=20),
                Text("Prunes invalid paths", font_size=20),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("Branch & Bound", font_size=24, color=GREEN, weight=BOLD),
                Text("Optimisation problems", font_size=20),
                Text("Prunes suboptimal paths", font_size=20),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=1.5).next_to(title, DOWN, buff=0.5)
        for c in comparison:
            box = SurroundingRectangle(c, buff=0.15, corner_radius=0.1, stroke_width=1)
            self.play(FadeIn(c), Create(box), run_time=0.7)

        bb_idea = VGroup(
            Text("Compute upper/lower bound at each node", font_size=22, color=INDIGO),
            Text("If bound <= current best => prune entire subtree", font_size=22, color=CORAL),
            Text("Uses priority queue (best-first search)", font_size=22, color=GREEN),
        ).arrange(DOWN, buff=0.15).next_to(comparison, DOWN, buff=0.4)
        for b in bb_idea:
            self.play(Write(b), run_time=0.4)

        tsp = Text(
            "TSP with B&B: reduce cost matrix for lower bound",
            font_size=20, color=AMBER,
        ).to_edge(DOWN)
        self.play(Write(tsp))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene07_BacktrackVsBBVsDP(Scene):
    """Comparison: backtracking vs B&B vs DP."""

    def construct(self):
        title = Text("Backtracking vs B&B vs DP", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["Backtracking", "B&B", "DP"],
            ["Feasibility", "Optimisation", "Optimisation"],
            ["DFS", "BFS/Best-first", "Bottom-up"],
            ["Validity prune", "Bound prune", "Subproblems"],
            ["Can find all", "Usually one", "Usually one"],
        ]
        table = Table(
            data[1:],
            col_labels=[Text(h, font_size=20, weight=BOLD, color=AMBER) for h in data[0]],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.55).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(table))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
