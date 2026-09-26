"""Knowledge Graph на NetworkX для славянской сакральной лексики."""

from __future__ import annotations
from typing import Any, Dict, List, Optional
import networkx as nx


class SemanticGraph:
    def __init__(self):
        self.G = nx.DiGraph()
        self._build_core()

    def _build_core(self) -> None:
        """Базовый семантический граф ролей и связей."""
        nodes = {
            "ведун": {"role": "knowledge", "label": "Ведун"},
            "волхв": {"role": "interpretation", "label": "Волхв"},
            "вещун": {"role": "communication", "label": "Вещун"},
            "знахарь": {"role": "practice", "label": "Знахарь"},
            "бая": {"role": "word_action", "label": "Бая"},
            "характерник": {"role": "agency", "label": "Характерник"},
            "знание": {"role": "concept", "label": "Знание"},
            "слово": {"role": "concept", "label": "Слово"},
            "воля": {"role": "concept", "label": "Воля"},
            "действие": {"role": "concept", "label": "Действие"},
        }
        for n, attrs in nodes.items():
            self.G.add_node(n, **attrs)

        edges = [
            ("ведун", "знание", {"relation": "обладает"}),
            ("ведун", "волхв", {"relation": "передаёт"}),
            ("волхв", "слово", {"relation": "использует"}),
            ("волхв", "вещун", {"relation": "передаёт"}),
            ("вещун", "знание", {"relation": "возвещает"}),
            ("бая", "слово", {"relation": "действует_через"}),
            ("знахарь", "знание", {"relation": "применяет"}),
            ("характерник", "воля", {"relation": "обладает"}),
            ("характерник", "действие", {"relation": "совершает"}),
            ("знание", "слово", {"relation": "выражается_в"}),
            ("слово", "воля", {"relation": "формирует"}),
            ("воля", "действие", {"relation": "ведёт_к"}),
            ("ведун", "вещун", {"relation": "связан"}),
            ("волхв", "бая", {"relation": "родственный_принцип"}),
        ]
        for u, v, attrs in edges:
            self.G.add_edge(u, v, **attrs)

    def add_lexeme(self, name: str, data: Dict[str, Any]) -> None:
        self.G.add_node(name, role="lexeme", period=data.get("period"), **data.get("semantics", {}))
        # связи по функциям
        for func in data.get("functions", []):
            if not self.G.has_node(func):
                self.G.add_node(func, role="function")
            self.G.add_edge(name, func, relation="имеет_функцию")

    def neighbors(self, node: str) -> List[str]:
        if node not in self.G:
            return []
        return list(self.G.successors(node)) + list(self.G.predecessors(node))

    def path(self, source: str, target: str) -> Optional[List[str]]:
        try:
            return nx.shortest_path(self.G, source, target)
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "nodes": [{"id": n, **self.G.nodes[n]} for n in self.G.nodes],
            "edges": [
                {"source": u, "target": v, **d}
                for u, v, d in self.G.edges(data=True)
            ],
        }

    def summary(self) -> str:
        lines = [f"Узлов: {self.G.number_of_nodes()}, рёбер: {self.G.number_of_edges()}"]
        lines.append("Ключевые связи:")
        for u, v, d in list(self.G.edges(data=True))[:12]:
            lines.append(f"  {u} —[{d.get('relation', '')}]→ {v}")
        return "\n".join(lines)
