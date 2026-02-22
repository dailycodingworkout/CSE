"""
Chapter 6: Greedy Algorithms
Manim CE animation scenes covering all concepts.

Render: manim -pqh scene_06_greedy.py <SceneName>
"""

from manim import *
import numpy as np

TEAL = "#1a8a8a"
CORAL = "#d94f4f"
AMBER = "#e8a317"
INDIGO = "#4a5da8"
GREEN = "#2e8b57"


class Scene01_GreedyParadigm(Scene):
    """Greedy choice property + optimal substructure."""

    def construct(self):
        title = Text("Greedy Algorithms", font_size=44, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        analogy = Text(
            "Like a buffet: always pick the best dish available NOW",
            font_size=24, color=AMBER,
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(analogy))

        props = VGroup(
            VGroup(
                Text("Greedy Choice Property", font_size=24, color=GREEN, weight=BOLD),
                Text("Local optimal => Global optimal", font_size=20),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("Optimal Substructure", font_size=24, color=INDIGO, weight=BOLD),
                Text("Optimal solution contains optimal sub-solutions", font_size=20),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=1).next_to(analogy, DOWN, buff=0.6)

        for p in props:
            box = SurroundingRectangle(p, buff=0.15, corner_radius=0.1, stroke_width=1)
            self.play(FadeIn(p), Create(box), run_time=0.7)

        proof_methods = VGroup(
            Text("Prove correctness via:", font_size=22, color=CORAL),
            Text("1. Exchange argument", font_size=20),
            Text("2. Greedy stays ahead", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_edge(DOWN)
        self.play(Write(proof_methods))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene02_ActivitySelection(Scene):
    """Activity selection: sort by finish time, select greedily."""

    def construct(self):
        title = Text("Activity Selection", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Timeline
        activities = [
            ("A1", 1, 2), ("A2", 3, 4), ("A3", 0, 6),
            ("A4", 5, 7), ("A5", 3, 9), ("A6", 5, 9),
        ]
        # Sorted by finish time already

        timeline = NumberLine(x_range=[0, 10, 1], length=10, include_numbers=True)
        timeline.next_to(title, DOWN, buff=0.5)
        self.play(Create(timeline))

        bars = VGroup()
        colors = [GREEN, GREEN, CORAL, GREEN, CORAL, CORAL]
        for i, (name, s, f) in enumerate(activities):
            bar = Line(
                timeline.n2p(s), timeline.n2p(f),
                stroke_width=8, color=colors[i],
            ).shift(DOWN * (0.4 + i * 0.35))
            label = Text(name, font_size=16, color=colors[i]).next_to(bar, LEFT, buff=0.1)
            bars.add(VGroup(bar, label))

        for b in bars:
            self.play(Create(b), run_time=0.4)

        result = Text(
            "Selected: {A1, A2, A4} = 3 activities (earliest finish time)",
            font_size=22, color=GREEN,
        ).to_edge(DOWN).shift(UP * 0.3)
        self.play(Write(result))

        trap = Text(
            "Sorting by start time or duration does NOT work!",
            font_size=20, color=CORAL,
        ).to_edge(DOWN)
        self.play(Write(trap))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene03_FractionalKnapsack(Scene):
    """Fractional knapsack by value/weight ratio."""

    def construct(self):
        title = Text("Fractional Knapsack", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        items = [
            ("Item 1", 60, 10, 6.0),
            ("Item 2", 100, 20, 5.0),
            ("Item 3", 120, 30, 4.0),
        ]
        header = Text("Sort by value/weight ratio (decreasing)", font_size=22, color=AMBER)
        header.next_to(title, DOWN, buff=0.4)
        self.play(Write(header))

        table_data = [[name, str(v), str(w), f"{r:.1f}"] for name, v, w, r in items]
        table = Table(
            table_data,
            col_labels=[Text(h, font_size=20, weight=BOLD) for h in ["Item", "Value", "Weight", "Ratio"]],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.55).next_to(header, DOWN, buff=0.3)
        self.play(FadeIn(table))

        # W = 50
        steps = VGroup(
            Text("W=50: Take Item 1 fully (w=10) -> W=40, V=60", font_size=20, color=GREEN),
            Text("Take Item 2 fully (w=20) -> W=20, V=160", font_size=20, color=GREEN),
            Text("Take 20/30 of Item 3 -> V=160+80=240", font_size=20, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(table, DOWN, buff=0.3)
        for s in steps:
            self.play(Write(s), run_time=0.5)

        result = Text("Maximum value = 240", font_size=26, color=CORAL, weight=BOLD).to_edge(DOWN)
        self.play(Write(result))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene04_HuffmanCoding(Scene):
    """Build Huffman tree step by step."""

    def construct(self):
        title = Text("Huffman Coding", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Show frequencies
        chars = [("a", 5), ("b", 9), ("c", 12), ("d", 13), ("e", 16), ("f", 45)]
        freq_txt = Text(
            "Frequencies: a(5) b(9) c(12) d(13) e(16) f(45)",
            font_size=22, color=AMBER,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(freq_txt))

        # Build tree (show steps as text)
        steps = VGroup(
            Text("Step 1: Merge a(5)+b(9) = [14]", font_size=20),
            Text("Step 2: Merge c(12)+d(13) = [25]", font_size=20),
            Text("Step 3: Merge [14]+e(16) = [30]", font_size=20),
            Text("Step 4: Merge [25]+[30] = [55]", font_size=20),
            Text("Step 5: Merge f(45)+[55] = [100]", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(freq_txt, DOWN, buff=0.3)
        for s in steps:
            self.play(Write(s), run_time=0.5)

        # Final codes
        codes = Text(
            "f=0  c=100  d=101  a=1100  b=1101  e=111",
            font_size=22, color=GREEN,
        ).next_to(steps, DOWN, buff=0.3)
        self.play(Write(codes))

        total = MathTex(
            r"\text{Total bits} = 45(1)+12(3)+13(3)+5(4)+9(4)+16(3) = 224",
            font_size=22, color=CORAL,
        ).to_edge(DOWN)
        self.play(Write(total))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene05_JobSequencing(Scene):
    """Job sequencing with deadlines."""

    def construct(self):
        title = Text("Job Sequencing with Deadlines", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["J1", "2", "100"],
            ["J3", "2", "27"],
            ["J4", "1", "25"],
            ["J2", "1", "19"],
            ["J5", "3", "15"],
        ]
        table = Table(
            data,
            col_labels=[Text(h, font_size=20, weight=BOLD) for h in ["Job", "Deadline", "Profit"]],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.55).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(table))

        # Scheduling slots
        slots = VGroup()
        for i in range(3):
            sq = Square(side_length=0.8, stroke_color=INDIGO)
            lbl = Text(f"Slot {i + 1}", font_size=16).next_to(sq, DOWN, buff=0.05)
            slots.add(VGroup(sq, lbl))
        slots.arrange(RIGHT, buff=0.3).next_to(table, DOWN, buff=0.4)
        self.play(FadeIn(slots))

        # Fill slots
        assignments = [("J3", 0, GREEN), ("J1", 1, GREEN), ("J5", 2, AMBER)]
        for job, idx, color in assignments:
            txt = Text(job, font_size=22, color=color)
            txt.move_to(slots[idx][0].get_center())
            self.play(Write(txt), slots[idx][0].animate.set_fill(color, opacity=0.2), run_time=0.5)

        result = Text("Total profit = 27+100+15 = 142", font_size=24, color=CORAL).to_edge(DOWN)
        self.play(Write(result))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene06_KruskalMST(Scene):
    """Kruskal's MST: sort edges, union-find."""

    def construct(self):
        title = Text("Kruskal's MST", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        info = VGroup(
            Text("Strategy: Sort edges by weight, add if no cycle", font_size=22, color=AMBER),
            Text("Uses Union-Find (disjoint set)", font_size=22),
            MathTex(r"\text{Time: } O(E\log E) = O(E\log V)", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).next_to(title, DOWN, buff=0.5)
        for i in info:
            self.play(Write(i), run_time=0.5)

        props = VGroup(
            Text("Cut Property: min edge crossing any cut is in MST", font_size=20, color=INDIGO),
            Text("Cycle Property: max edge in any cycle is NOT in MST", font_size=20, color=CORAL),
            Text("Unique MST if all edge weights distinct", font_size=20, color=GREEN),
            Text("MST has exactly V-1 edges", font_size=20, color=AMBER),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(info, DOWN, buff=0.4)
        for p in props:
            self.play(FadeIn(p, shift=LEFT), run_time=0.4)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene07_PrimAndDijkstra(Scene):
    """Prim's MST and Dijkstra's SSSP side by side."""

    def construct(self):
        title = Text("Prim's MST vs Dijkstra's SSSP", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["", "Kruskal", "Prim", "Dijkstra"],
            ["Type", "MST (edge)", "MST (vertex)", "SSSP"],
            ["DS", "Union-Find", "Priority Queue", "Priority Queue"],
            ["Sparse", "Better", "—", "—"],
            ["Dense", "—", "Better", "Better"],
            ["Neg edges", "N/A", "N/A", "FAILS!"],
        ]
        table = Table(
            [row[1:] for row in data[1:]],
            row_labels=[Text(row[0], font_size=18) for row in data[1:]],
            col_labels=[Text(h, font_size=18, weight=BOLD, color=AMBER) for h in data[0][1:]],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.55).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(table))
        self.wait(1)

        trap = Text(
            "Dijkstra FAILS with negative edges! Use Bellman-Ford instead.",
            font_size=22, color=CORAL,
        ).to_edge(DOWN)
        box = SurroundingRectangle(trap, color=CORAL, buff=0.1)
        self.play(Write(trap), Create(box))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene08_GreedyVsDP(Scene):
    """When to use greedy vs dynamic programming."""

    def construct(self):
        title = Text("Greedy vs Dynamic Programming", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["Greedy", "DP"],
            ["One choice per step", "All choices considered"],
            ["No backtracking", "Builds on all subproblems"],
            ["Faster (generally)", "More versatile"],
            ["Fractional Knapsack", "0/1 Knapsack"],
            ["Activity Selection", "Matrix Chain"],
            ["Huffman Coding", "LCS"],
        ]
        table = Table(
            data[1:],
            col_labels=[Text(h, font_size=22, weight=BOLD, color=AMBER) for h in data[0]],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.55).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(table))

        rule = Text(
            "Can you prove greedy choice property? Yes => Greedy. No => DP.",
            font_size=22, color=GREEN,
        ).to_edge(DOWN)
        self.play(Write(rule))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
