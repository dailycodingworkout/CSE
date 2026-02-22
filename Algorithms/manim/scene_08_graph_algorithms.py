"""
Chapter 8: Graph Algorithms
Manim CE animation scenes covering all concepts.

Render: manim -pqh scene_08_graph_algorithms.py <SceneName>
"""

from manim import *
import numpy as np

TEAL = "#1a8a8a"
CORAL = "#d94f4f"
AMBER = "#e8a317"
INDIGO = "#4a5da8"
GREEN = "#2e8b57"


class Scene01_GraphRepresentations(Scene):
    """Adjacency matrix vs adjacency list."""

    def construct(self):
        title = Text("Graph Representations", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["", "Matrix", "List"],
            ["Space", "O(V²)", "O(V+E)"],
            ["Edge check", "O(1)", "O(deg)"],
            ["Neighbors", "O(V)", "O(deg)"],
            ["Best for", "Dense", "Sparse"],
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


class Scene02_BFS(Scene):
    """BFS: level-by-level exploration using a queue."""

    def construct(self):
        title = Text("Breadth-First Search (BFS)", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        analogy = Text(
            "Like a stone in water: explore in expanding circles",
            font_size=22, color=AMBER,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(analogy))

        # Simple graph
        positions = {
            "0": LEFT * 2 + UP, "1": ORIGIN + UP, "2": RIGHT * 2 + UP,
            "3": LEFT * 2 + DOWN, "4": ORIGIN + DOWN, "5": RIGHT * 2 + DOWN,
        }
        edges_list = [("0", "1"), ("0", "3"), ("1", "2"), ("1", "4"), ("2", "5"), ("3", "4"), ("4", "5")]

        nodes = {}
        node_grp = VGroup()
        for name, pos in positions.items():
            c = Circle(radius=0.3, stroke_color=INDIGO, fill_color=INDIGO, fill_opacity=0.1)
            t = Text(name, font_size=20)
            n = VGroup(c, t).move_to(pos + DOWN * 0.5)
            nodes[name] = n
            node_grp.add(n)

        edge_grp = VGroup()
        for u, v in edges_list:
            line = Line(nodes[u].get_center(), nodes[v].get_center(), stroke_width=1.5)
            edge_grp.add(line)

        self.play(FadeIn(node_grp), Create(edge_grp))

        # BFS from 0
        bfs_order = ["0", "1", "3", "2", "4", "5"]
        level_colors = {0: GREEN, 1: AMBER, 2: CORAL}
        levels = {"0": 0, "1": 1, "3": 1, "2": 2, "4": 2, "5": 2}
        for name in bfs_order:
            color = level_colors.get(levels[name], WHITE)
            self.play(
                nodes[name][0].animate.set_fill(color, opacity=0.5),
                run_time=0.4,
            )

        info = VGroup(
            Text("Time: O(V+E) | Uses Queue (FIFO)", font_size=20, color=GREEN),
            Text("Gives shortest path in unweighted graphs", font_size=20, color=AMBER),
            Text("Only tree edges + cross edges (undirected)", font_size=20, color=CORAL),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN)
        self.play(Write(info))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene03_DFS(Scene):
    """DFS: deep exploration with timestamps and edge classification."""

    def construct(self):
        title = Text("Depth-First Search (DFS)", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        analogy = Text("Like exploring a maze: go deep, then backtrack", font_size=22, color=AMBER)
        analogy.next_to(title, DOWN, buff=0.4)
        self.play(Write(analogy))

        # Edge classification table
        data = [
            ["Tree edge", "Part of DFS tree"],
            ["Back edge", "To ancestor => CYCLE!"],
            ["Forward edge", "To descendant (not tree)"],
            ["Cross edge", "No ancestor relation"],
        ]
        table = Table(
            data,
            col_labels=[Text("Edge Type", font_size=20, weight=BOLD), Text("Meaning", font_size=20, weight=BOLD)],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.55).next_to(analogy, DOWN, buff=0.3)
        self.play(FadeIn(table))

        facts = VGroup(
            Text("Undirected: only tree + back edges", font_size=20, color=GREEN),
            Text("Directed: all four types possible", font_size=20, color=AMBER),
            Text("Back edge <=> cycle exists", font_size=20, color=CORAL),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN)
        self.play(Write(facts))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene04_TopologicalSort(Scene):
    """Topological sort: DFS-based and Kahn's BFS-based."""

    def construct(self):
        title = Text("Topological Sort", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        analogy = Text(
            "Course prerequisites: CS201 before CS301",
            font_size=22, color=AMBER,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(analogy))

        methods = VGroup(
            VGroup(
                Text("Method 1: DFS", font_size=24, color=GREEN, weight=BOLD),
                Text("Decreasing order of finish times", font_size=20),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("Method 2: Kahn's (BFS)", font_size=24, color=INDIGO, weight=BOLD),
                Text("Remove vertices with in-degree 0", font_size=20),
                Text("Also detects cycles!", font_size=20, color=CORAL),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=1).next_to(analogy, DOWN, buff=0.5)

        for m in methods:
            box = SurroundingRectangle(m, buff=0.15, corner_radius=0.1, stroke_width=1)
            self.play(FadeIn(m), Create(box), run_time=0.7)

        facts = VGroup(
            Text("Exists iff graph is a DAG", font_size=20, color=AMBER),
            Text("Not unique — multiple valid orderings", font_size=20, color=GREEN),
            MathTex(r"\text{Time: } O(V+E)", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN)
        self.play(Write(facts))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene05_SCC(Scene):
    """Strongly connected components: Kosaraju and Tarjan."""

    def construct(self):
        title = Text("Strongly Connected Components", font_size=38, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        defn = Text(
            "SCC: maximal set where every vertex reaches every other",
            font_size=22, color=AMBER,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(defn))

        kosaraju = VGroup(
            Text("Kosaraju's Algorithm", font_size=24, color=GREEN, weight=BOLD),
            Text("1. DFS on G, record finish times", font_size=20),
            Text("2. Compute transpose G^T", font_size=20),
            Text("3. DFS on G^T in decreasing finish order", font_size=20),
            Text("4. Each DFS tree = one SCC", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(defn, DOWN, buff=0.3)
        for k in kosaraju:
            self.play(FadeIn(k, shift=LEFT), run_time=0.3)

        tarjan = VGroup(
            Text("Tarjan's: Single DFS with low-link values", font_size=22, color=INDIGO),
            MathTex(r"\text{Both: } O(V+E)", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN)
        self.play(Write(tarjan))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene06_ShortestPathSummary(Scene):
    """Master comparison of all shortest path algorithms."""

    def construct(self):
        title = Text("Shortest Path Algorithms — Summary", font_size=36, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        data = [
            ["BFS", "O(V+E)", "SSSP", "N/A"],
            ["Dijkstra", "O((V+E)logV)", "SSSP", "No neg"],
            ["Bellman-Ford", "O(VE)", "SSSP", "Yes"],
            ["DAG SP", "O(V+E)", "SSSP", "Yes (DAG)"],
            ["Floyd-Warshall", "O(V³)", "APSP", "Yes"],
        ]
        table = Table(
            data,
            col_labels=[
                Text("Algorithm", font_size=18, weight=BOLD),
                Text("Time", font_size=18, weight=BOLD),
                Text("Type", font_size=18, weight=BOLD),
                Text("Neg Edges", font_size=18, weight=BOLD),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        ).scale(0.55).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(table))

        decision = VGroup(
            Text("Unweighted => BFS", font_size=18, color=GREEN),
            Text("DAG => DAG SP", font_size=18, color=AMBER),
            Text("Non-negative => Dijkstra", font_size=18, color=INDIGO),
            Text("Negative edges => Bellman-Ford", font_size=18, color=CORAL),
            Text("All pairs => Floyd-Warshall", font_size=18, color=TEAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_edge(DOWN)
        self.play(Write(decision))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene07_ArticulationBridges(Scene):
    """Articulation points and bridges using Tarjan's low-link."""

    def construct(self):
        title = Text("Articulation Points & Bridges", font_size=40, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        defns = VGroup(
            Text("Articulation Point: removal disconnects graph", font_size=22, color=CORAL),
            Text("Bridge: edge removal disconnects graph", font_size=22, color=INDIGO),
        ).arrange(DOWN, buff=0.2).next_to(title, DOWN, buff=0.4)
        self.play(Write(defns))

        rules = VGroup(
            Text("Articulation (non-root): low[v] >= disc[u]", font_size=22, color=AMBER),
            Text("Articulation (root): >= 2 DFS children", font_size=22, color=AMBER),
            Text("Bridge: low[v] > disc[u] (strict)", font_size=22, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(defns, DOWN, buff=0.4)
        for r in rules:
            self.play(Write(r), run_time=0.5)

        facts = VGroup(
            Text("Time: O(V+E)", font_size=20, color=GREEN),
            Text("Tree has V-1 bridges and V-2 articulation points", font_size=20, color=CORAL),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN)
        self.play(Write(facts))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Scene08_Bipartite(Scene):
    """Bipartite graph: 2-coloring check."""

    def construct(self):
        title = Text("Bipartite Graph Checking", font_size=42, color=TEAL)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        defn = Text(
            "Bipartite: vertices split into two sets, edges only between sets",
            font_size=22, color=AMBER,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(defn))

        method = VGroup(
            Text("Algorithm: BFS/DFS 2-coloring", font_size=22, color=GREEN),
            Text("Color source 0, neighbors 1, their neighbors 0, ...", font_size=20),
            Text("Conflict => NOT bipartite", font_size=20, color=CORAL),
        ).arrange(DOWN, buff=0.15).next_to(defn, DOWN, buff=0.4)
        for m in method:
            self.play(Write(m), run_time=0.5)

        theorem = Text(
            "Bipartite <=> no odd-length cycle",
            font_size=26, color=GREEN, weight=BOLD,
        ).to_edge(DOWN)
        box = SurroundingRectangle(theorem, color=GREEN, buff=0.1)
        self.play(Write(theorem), Create(box))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
