"""
Chapter 14: GATE Exam Strategy & PYQ Patterns
Manim CE animation scenes covering all concepts.

Render: manim -pqh scene_14_gate_strategy.py <SceneName>
"""

from manim import *
import numpy as np

TEAL = "#1a8a8a"
CORAL = "#d94f4f"
AMBER = "#e8a317"
INDIGO = "#4a5da8"
GREEN = "#2e8b57"


class Scene01_TopicWeightage(Scene):
    """Topic-wise weightage in GATE as an animated bar chart."""

    def construct(self):
        title = Text("GATE Topic Weightage", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        topics = [
            ("Graph Algo", 8, CORAL),
            ("DP", 6, CORAL),
            ("Sorting", 4, AMBER),
            ("Asymptotic", 4, GREEN),
            ("Recurrences", 4, GREEN),
            ("Greedy", 4, AMBER),
            ("NP-Complete", 4, INDIGO),
            ("Searching", 2, GREEN),
            ("Hashing", 2, GREEN),
            ("String Match", 2, TEAL),
        ]

        bars = VGroup()
        for name, marks, color in topics:
            bar = Rectangle(
                width=marks * 0.4, height=0.4,
                fill_color=color, fill_opacity=0.7, stroke_width=1,
            )
            lbl = Text(f"{name} ({marks})", font_size=14).next_to(bar, RIGHT, buff=0.1)
            bars.add(VGroup(bar, lbl))
        bars.arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(title, DOWN, buff=0.4).shift(LEFT * 2)

        for b in bars:
            self.play(FadeIn(b, shift=RIGHT), run_time=0.3)

        strategy = Text(
            "Master Graph Algorithms + DP = ~50% of questions!",
            font_size=22, color=CORAL,
        ).to_edge(DOWN)
        self.play(Write(strategy))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene02_QuestionPatterns(Scene):
    """Common GATE question patterns and strategies."""

    def construct(self):
        title = Text("Common GATE Question Patterns", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        patterns = VGroup(
            VGroup(
                Text("P1: Find time complexity", font_size=22, color=AMBER, weight=BOLD),
                Text("Identify loops, write recurrence, apply Master Thm", font_size=18),
            ).arrange(DOWN, buff=0.05),
            VGroup(
                Text("P2: Apply algorithm X to input", font_size=22, color=GREEN, weight=BOLD),
                Text("Trace step by step — FREE marks!", font_size=18),
            ).arrange(DOWN, buff=0.05),
            VGroup(
                Text("P3: Which statement is true?", font_size=22, color=INDIGO, weight=BOLD),
                Text("Know properties deeply", font_size=18),
            ).arrange(DOWN, buff=0.05),
            VGroup(
                Text("P4: Minimum comparisons to...", font_size=22, color=CORAL, weight=BOLD),
                Text("Know lower bounds from Ch.13", font_size=18),
            ).arrange(DOWN, buff=0.05),
            VGroup(
                Text("P5: Solve recurrence", font_size=22, color=TEAL, weight=BOLD),
                Text("Try Master Thm first, then recursion tree", font_size=18),
            ).arrange(DOWN, buff=0.05),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.4)

        for p in patterns:
            self.play(FadeIn(p, shift=LEFT), run_time=0.4)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene03_TimeManagement(Scene):
    """Time allocation per question type."""

    def construct(self):
        title = Text("Time Management Strategy", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["1-mark MCQ", "1-2 min", "Quick recall"],
            ["2-mark MCQ", "3-4 min", "Work systematically"],
            ["1-mark NAT", "2-3 min", "Careful calculation"],
            ["2-mark NAT", "4-5 min", "Double-check"],
            ["MSQ", "3-5 min", "Verify each option"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Type", font_size=20, weight=BOLD),
                Text("Time", font_size=20, weight=BOLD),
                Text("Strategy", font_size=20, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.6).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(table))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene04_CommonMistakes(Scene):
    """Top 10 mistakes to avoid in GATE."""

    def construct(self):
        title = Text("Common Mistakes to Avoid", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        mistakes = VGroup(
            Text("1. Confusing O and Θ (O is upper, Θ is tight)", font_size=20, color=CORAL),
            Text("2. Wrong direction of NPC reduction", font_size=20, color=CORAL),
            Text("3. Forgetting base cases in recurrences", font_size=20, color=CORAL),
            Text("4. Dijkstra with negative edges (use Bellman-Ford!)", font_size=20, color=CORAL),
            Text("5. Quick Sort worst case IS O(n²)", font_size=20, color=CORAL),
            Text("6. Selection Sort is NOT stable", font_size=20, color=CORAL),
            Text("7. MST != Shortest Path Tree", font_size=20, color=CORAL),
            Text("8. Build Heap is O(n), NOT O(n log n)", font_size=20, color=CORAL),
            Text("9. NP doesn't mean 'hard' — P is subset of NP", font_size=20, color=CORAL),
            Text("10. Amortised != Average case", font_size=20, color=CORAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).next_to(title, DOWN, buff=0.3)

        for m in mistakes:
            self.play(FadeIn(m, shift=LEFT), run_time=0.3)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene05_SortingQuickRef(Scene):
    """Quick reference: sorting algorithm complexities."""

    def construct(self):
        title = Text("Quick Reference — Sorting", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["Insertion", "n", "n²", "1", "Y"],
            ["Merge", "n lg n", "n lg n", "n", "Y"],
            ["Quick", "n lg n", "n²", "lg n", "N"],
            ["Heap", "n lg n", "n lg n", "1", "N"],
            ["Counting", "n+k", "n+k", "n+k", "Y"],
            ["Radix", "d(n+b)", "d(n+b)", "n+b", "Y"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Sort", font_size=18, weight=BOLD),
                Text("Best", font_size=18, weight=BOLD),
                Text("Worst", font_size=18, weight=BOLD),
                Text("Space", font_size=18, weight=BOLD),
                Text("Stable", font_size=18, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.5).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(table))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene06_GraphQuickRef(Scene):
    """Quick reference: graph algorithm complexities."""

    def construct(self):
        title = Text("Quick Reference — Graph Algorithms", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["BFS", "O(V+E)", "SSSP unweighted"],
            ["DFS", "O(V+E)", "Cycles, SCC, TopoSort"],
            ["Dijkstra", "O((V+E)lgV)", "SSSP non-neg"],
            ["Bellman-Ford", "O(VE)", "SSSP neg edges"],
            ["Floyd-Warshall", "O(V³)", "APSP"],
            ["Kruskal", "O(E lg E)", "MST"],
            ["Prim", "O((V+E)lgV)", "MST"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Algorithm", font_size=18, weight=BOLD),
                Text("Time", font_size=18, weight=BOLD),
                Text("Purpose", font_size=18, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.5).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(table))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene07_DPQuickRef(Scene):
    """Quick reference: DP problem complexities."""

    def construct(self):
        title = Text("Quick Reference — Dynamic Programming", font_size=36, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["LCS", "O(mn)", "O(mn)"],
            ["LIS", "O(n²) / O(n lg n)", "O(n)"],
            ["MCM", "O(n³)", "O(n²)"],
            ["0/1 Knapsack", "O(nW)", "O(nW)"],
            ["Edit Distance", "O(mn)", "O(mn)"],
            ["Floyd-Warshall", "O(V³)", "O(V²)"],
            ["Coin Change", "O(nV)", "O(V)"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Problem", font_size=18, weight=BOLD),
                Text("Time", font_size=18, weight=BOLD),
                Text("Space", font_size=18, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.5).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(table))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene08_FinalChecklist(Scene):
    """The final exam readiness checklist."""

    def construct(self):
        title = Text("Final Checklist Before Exam", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        items = [
            "Master Theorem in under 30 seconds?",
            "Trace BFS, DFS, Dijkstra, Prim, Kruskal?",
            "All sorting complexities by heart?",
            "Write recurrence for LCS, MCM, Knapsack?",
            "P vs NP-Complete classification?",
            "Build KMP failure function?",
            "When does Dijkstra fail?",
            "Why Build Heap is O(n)?",
            "Lower bounds (max, sort, merge)?",
            "Amortised O(1) vs Average O(1)?",
        ]

        checklist = VGroup()
        for item in items:
            check = Text(f"[ ] {item}", font_size=18, color=GREEN)
            checklist.add(check)
        checklist.arrange(DOWN, aligned_edge=LEFT, buff=0.12).next_to(title, DOWN, buff=0.3)

        for c in checklist:
            self.play(FadeIn(c, shift=LEFT), run_time=0.25)

        self.wait(1)

        # Check all boxes
        for i, c in enumerate(checklist):
            new_text = c.text.replace("[ ]", "[x]", 1)
            new_c = Text(new_text, font_size=18, color=AMBER).move_to(c.get_center()).align_to(c, LEFT)
            self.play(Transform(c, new_c), run_time=0.15)

        ready = Text(
            "You're ready to ace the Algorithms section!",
            font_size=24, color=CORAL, weight=BOLD,
        ).to_edge(DOWN)
        self.play(Write(ready))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
