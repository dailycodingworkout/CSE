"""
Chapter 4: Sorting Algorithms
Manim CE animation scenes covering all concepts.

Render: manim -pqh scene_04_sorting.py <SceneName>
"""

from manim import *
import numpy as np

TEAL = "#1a8a8a"
CORAL = "#d94f4f"
AMBER = "#e8a317"
INDIGO = "#4a5da8"
GREEN = "#2e8b57"


def bar_chart(vals, color=INDIGO, bar_width=0.5):
    """Create a bar chart VGroup from a list of values."""
    bars = VGroup()
    for v in vals:
        bar = Rectangle(width=bar_width, height=v * 0.4, fill_color=color, fill_opacity=0.7, stroke_width=1)
        bar.align_to(ORIGIN, DOWN)
        lbl = Text(str(v), font_size=16).next_to(bar, UP, buff=0.05)
        bars.add(VGroup(bar, lbl))
    bars.arrange(RIGHT, buff=0.05, aligned_edge=DOWN)
    return bars


class Scene01_WhySorting(Scene):
    """Motivation: why sorting is the most tested topic."""

    def construct(self):
        title = Text("Why Study Sorting?", font_size=44, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        points = VGroup(
            Text("Most frequently tested in GATE", font_size=26, color=CORAL),
            Text("Teaches D&C, greedy, incremental paradigms", font_size=26, color=AMBER),
            Text("Time-space tradeoffs", font_size=26, color=GREEN),
            Text("Stability and in-place concepts", font_size=26, color=INDIGO),
            Text("Lower bound: Ω(n log n) for comparison sorts", font_size=26, color=CORAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.6)

        for p in points:
            self.play(FadeIn(p, shift=LEFT), run_time=0.5)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene02_BubbleSort(Scene):
    """Animate one pass of bubble sort."""

    def construct(self):
        title = Text("Bubble Sort", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        vals = [5, 3, 8, 1, 4]
        bars = bar_chart(vals, INDIGO).next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(bars))

        analogy = Text(
            "Larger elements 'bubble up' to the end",
            font_size=22, color=AMBER,
        ).next_to(bars, DOWN, buff=0.5)
        self.play(Write(analogy))

        # Animate one pass
        for i in range(len(vals) - 1):
            # Highlight pair
            bars[i][0].set_fill(CORAL, opacity=0.7)
            bars[i + 1][0].set_fill(CORAL, opacity=0.7)
            self.play(
                bars[i][0].animate.set_fill(CORAL, opacity=0.7),
                bars[i + 1][0].animate.set_fill(CORAL, opacity=0.7),
                run_time=0.3,
            )
            if vals[i] > vals[i + 1]:
                # Swap
                vals[i], vals[i + 1] = vals[i + 1], vals[i]
                self.play(
                    bars[i].animate.move_to(bars[i + 1].get_center()),
                    bars[i + 1].animate.move_to(bars[i].get_center()),
                    run_time=0.4,
                )
                bars[i], bars[i + 1] = bars[i + 1], bars[i]
            # Reset colors
            bars[i][0].set_fill(INDIGO, opacity=0.7)
            bars[i + 1][0].set_fill(INDIGO, opacity=0.7)

        complexity = VGroup(
            Text("Best: O(n)  |  Avg/Worst: O(n²)  |  Stable: Yes", font_size=22, color=GREEN),
            Text("Swaps = number of inversions", font_size=20, color=CORAL),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN)
        self.play(Write(complexity))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene03_SelectionSort(Scene):
    """Animate selection sort — finding minimum each pass."""

    def construct(self):
        title = Text("Selection Sort", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        info = VGroup(
            Text("Find the minimum, swap to front, repeat", font_size=24, color=AMBER),
            Text("Always O(n²) — not adaptive", font_size=22, color=CORAL),
            Text("Only n-1 swaps — minimum swaps of O(n²) sorts", font_size=22, color=GREEN),
            Text("NOT stable: [5a, 5b, 2] → [2, 5b, 5a]", font_size=22, color=CORAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.5)

        for i in info:
            self.play(FadeIn(i, shift=LEFT), run_time=0.5)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene04_InsertionSort(Scene):
    """Animate insertion sort — card-in-hand analogy."""

    def construct(self):
        title = Text("Insertion Sort", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        analogy = Text(
            "Like sorting cards in your hand — insert each into correct position",
            font_size=22, color=AMBER,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(analogy))

        props = VGroup(
            Text("Best: O(n) — already sorted", font_size=22, color=GREEN),
            Text("Worst: O(n²) — reverse sorted", font_size=22, color=CORAL),
            Text("Stable, In-place, Online, Adaptive", font_size=22, color=INDIGO),
            Text("Best for small arrays (n < 20-30)", font_size=22, color=AMBER),
            Text("Running time = O(n + inversions)", font_size=22, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(analogy, DOWN, buff=0.4)

        for p in props:
            self.play(FadeIn(p, shift=LEFT), run_time=0.5)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene05_MergeSort(Scene):
    """Visualise merge sort divide-and-merge process."""

    def construct(self):
        title = Text("Merge Sort", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Show splitting
        arr_text = lambda vals: Text(str(vals), font_size=20)
        level0 = arr_text([38, 27, 43, 3, 9, 82, 10])
        level0.next_to(title, DOWN, buff=0.5)
        self.play(Write(level0))

        l1a = arr_text([38, 27, 43])
        l1b = arr_text([3, 9, 82, 10])
        VGroup(l1a, l1b).arrange(RIGHT, buff=1).next_to(level0, DOWN, buff=0.4)
        self.play(TransformFromCopy(level0, l1a), TransformFromCopy(level0, l1b))

        l2a = arr_text([38])
        l2b = arr_text([27, 43])
        l2c = arr_text([3, 9])
        l2d = arr_text([82, 10])
        VGroup(l2a, l2b, l2c, l2d).arrange(RIGHT, buff=0.5).next_to(VGroup(l1a, l1b), DOWN, buff=0.4)
        self.play(
            TransformFromCopy(l1a, l2a), TransformFromCopy(l1a, l2b),
            TransformFromCopy(l1b, l2c), TransformFromCopy(l1b, l2d),
        )

        # Merged result
        merged = arr_text([3, 9, 10, 27, 38, 43, 82])
        merged.set_color(GREEN)
        merged.next_to(VGroup(l2a, l2b, l2c, l2d), DOWN, buff=0.6)
        merge_label = Text("Merge back up", font_size=20, color=AMBER).next_to(merged, UP, buff=0.1)
        self.play(Write(merge_label), Write(merged))

        complexity = VGroup(
            MathTex(r"T(n) = 2T(n/2) + \Theta(n) \;\Rightarrow\; \Theta(n\log n)", font_size=24, color=GREEN),
            Text("Space: O(n) | Stable: Yes | Best for linked lists", font_size=20, color=AMBER),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN)
        self.play(Write(complexity))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene06_QuickSort(Scene):
    """Visualise quick sort partition and pivot concept."""

    def construct(self):
        title = Text("Quick Sort", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Partition concept
        vals = [3, 7, 8, 5, 2, 1, 9, 5, 4]
        pivot_val = 4  # last element
        less = [v for v in vals[:-1] if v <= pivot_val]
        greater = [v for v in vals[:-1] if v > pivot_val]

        orig = Text(str(vals), font_size=22).next_to(title, DOWN, buff=0.5)
        pivot_txt = Text(f"Pivot = {pivot_val} (last element)", font_size=22, color=CORAL)
        pivot_txt.next_to(orig, DOWN, buff=0.3)
        self.play(Write(orig), Write(pivot_txt))

        less_txt = Text(f"<= pivot: {less}", font_size=22, color=GREEN)
        piv_mid = Text(f"[{pivot_val}]", font_size=22, color=AMBER)
        greater_txt = Text(f"> pivot: {greater}", font_size=22, color=CORAL)
        partitioned = VGroup(less_txt, piv_mid, greater_txt).arrange(RIGHT, buff=0.3)
        partitioned.next_to(pivot_txt, DOWN, buff=0.4)
        self.play(Write(partitioned))

        # Complexity
        info = VGroup(
            Text("Best/Avg: O(n log n) | Worst: O(n²) — sorted input", font_size=20, color=AMBER),
            Text("In-place, NOT stable, cache-friendly", font_size=20, color=GREEN),
            Text("Randomised pivot: expected O(n log n) for ALL inputs", font_size=20, color=INDIGO),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN)
        self.play(Write(info))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene07_HeapSort(Scene):
    """Build Heap O(n) proof and heap sort overview."""

    def construct(self):
        title = Text("Heap Sort", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        steps = VGroup(
            Text("1. Build max-heap (bottom-up)", font_size=24, color=AMBER),
            Text("2. Swap root (max) with last, reduce heap size", font_size=24, color=AMBER),
            Text("3. Heapify root, repeat", font_size=24, color=AMBER),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.5)
        for s in steps:
            self.play(FadeIn(s, shift=LEFT), run_time=0.4)

        # Build Heap O(n) proof
        proof = VGroup(
            Text("Build Heap is O(n), NOT O(n log n)!", font_size=24, color=CORAL, weight=BOLD),
            MathTex(
                r"\sum_{h=0}^{\lfloor\log n\rfloor} \left\lceil\frac{n}{2^{h+1}}\right\rceil \cdot O(h)"
                r"= O\!\left(n \sum \frac{h}{2^h}\right) = O(n)",
                font_size=22,
            ),
            MathTex(r"\sum_{h=0}^{\infty} \frac{h}{2^h} = 2 \;\text{(converges!)}", font_size=22, color=GREEN),
        ).arrange(DOWN, buff=0.2).next_to(steps, DOWN, buff=0.4)
        for p in proof:
            self.play(Write(p), run_time=0.7)

        props = Text(
            "All cases O(n log n) | O(1) space | In-place | NOT stable",
            font_size=20, color=AMBER,
        ).to_edge(DOWN)
        self.play(Write(props))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene08_CountingRadixBucket(Scene):
    """Non-comparison sorts: Counting, Radix, Bucket."""

    def construct(self):
        title = Text("Non-Comparison Sorts", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bypass = Text(
            "These bypass the Ω(n log n) lower bound!",
            font_size=24, color=CORAL,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(bypass))

        data = [
            ["Counting Sort", "O(n+k)", "O(n+k)", "Integer range [0,k]"],
            ["Radix Sort", "O(d(n+b))", "O(n+b)", "d digits, base b"],
            ["Bucket Sort", "O(n) avg", "O(n)", "Uniform distribution"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Algorithm", font_size=20, weight=BOLD),
                Text("Time", font_size=20, weight=BOLD),
                Text("Space", font_size=20, weight=BOLD),
                Text("Requirement", font_size=20, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.55).next_to(bypass, DOWN, buff=0.4)
        self.play(FadeIn(table))
        self.wait(1)

        facts = VGroup(
            Text("All three are stable (if implemented correctly)", font_size=20, color=GREEN),
            Text("Radix: intermediate sort MUST be stable!", font_size=20, color=CORAL),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN)
        self.play(Write(facts))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene09_LowerBound(Scene):
    """Decision tree lower bound Ω(n log n) proof."""

    def construct(self):
        title = Text("Lower Bound: Ω(n log n)", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        proof = VGroup(
            Text("Decision tree model:", font_size=24, color=AMBER),
            Text("Each internal node = comparison, each leaf = permutation", font_size=22),
            MathTex(r"\text{Leaves} \ge n!", font_size=26),
            MathTex(r"\text{Height } h: 2^h \ge n!", font_size=26),
            MathTex(r"h \ge \log_2(n!) = \Omega(n\log n)", font_size=28, color=GREEN),
        ).arrange(DOWN, buff=0.25).next_to(title, DOWN, buff=0.5)

        for p in proof:
            self.play(Write(p), run_time=0.6)
        self.wait(1)

        conclusion = VGroup(
            Text("Merge Sort & Heap Sort achieve this bound — optimal!", font_size=22, color=GREEN),
            Text("Counting, Radix, Bucket bypass by not comparing", font_size=22, color=AMBER),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene10_MasterComparison(Scene):
    """Master comparison table of all sorting algorithms."""

    def construct(self):
        title = Text("Sorting — Master Comparison", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["Bubble", "O(n)", "O(n²)", "O(1)", "Y", "Y"],
            ["Selection", "O(n²)", "O(n²)", "O(1)", "N", "Y"],
            ["Insertion", "O(n)", "O(n²)", "O(1)", "Y", "Y"],
            ["Merge", "O(n lg n)", "O(n lg n)", "O(n)", "Y", "N"],
            ["Quick", "O(n lg n)", "O(n²)", "O(lg n)", "N", "Y"],
            ["Heap", "O(n lg n)", "O(n lg n)", "O(1)", "N", "Y"],
            ["Counting", "O(n+k)", "O(n+k)", "O(n+k)", "Y", "N"],
            ["Radix", "O(d(n+b))", "O(d(n+b))", "O(n+b)", "Y", "N"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Sort", font_size=16, weight=BOLD),
                Text("Best", font_size=16, weight=BOLD),
                Text("Worst", font_size=16, weight=BOLD),
                Text("Space", font_size=16, weight=BOLD),
                Text("Stable", font_size=16, weight=BOLD),
                Text("In-Place", font_size=16, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.45).next_to(title, DOWN, buff=0.4)

        self.play(FadeIn(table))
        self.wait(1)

        tricks = VGroup(
            Text("In-place + O(n lg n): only Heap Sort", font_size=18, color=CORAL),
            Text("Stable + O(n lg n): only Merge Sort", font_size=18, color=GREEN),
            Text("Best practical general-purpose: Quick Sort (randomised)", font_size=18, color=AMBER),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN)
        self.play(Write(tricks))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])
