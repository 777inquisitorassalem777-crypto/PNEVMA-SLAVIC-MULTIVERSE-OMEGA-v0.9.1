"""CLI / API оркестратор: Vedun → Volkhv → Veshchun → Kharakternik + Graph"""

from __future__ import annotations
from typing import Any, Dict, Optional
from datetime import datetime

from .vedun import Vedun
from .volkhv import Volkhv
from .veshchun import Veshchun
from .kharakternik import Kharakternik
from ..graph.knowledge_graph import SemanticGraph


class SlavicCognitiveAgent:
    def __init__(self):
        self.vedun = Vedun()
        self.volkhv = Volkhv()
        self.veshchun = Veshchun()
        self.kharakternik = Kharakternik()
        self.graph = SemanticGraph()
        # обогащаем граф лексемами
        for name, data in self.vedun.get_all().items():
            self.graph.add_lexeme(name, data)

    def analyze(self, query: str) -> Dict[str, Any]:
        data = self.vedun.recognize(query)
        interpretation = self.volkhv.interpret(data) if data else {}
        proclamation = self.veshchun.proclaim(query, data, interpretation)
        action = self.kharakternik.suggest_action(query, data, interpretation)

        result: Dict[str, Any] = {
            "query": query,
            "found": data is not None,
            "timestamp": datetime.now().isoformat(),
        }

        if data:
            result["vedun"] = {
                "forms": data.get("forms"),
                "etymology_main": data["etymology"]["main"],
                "etymology_status": data["etymology"]["status"],
                "ie_root": data["etymology"].get("ie_root"),
                "cognates": data["etymology"].get("cognates", []),
                "alternatives": data["etymology"].get("alternatives", []),
                "sources": data.get("sources", []),
                "period": data.get("period"),
            }
            result["volkhv"] = interpretation
            result["veshchun"] = proclamation
            result["kharakternik"] = action
            result["graph"] = {
                "neighbors": self.graph.neighbors(query.lower()),
                "summary": self.graph.summary(),
            }
            result["synthesis"] = {
                "formula": interpretation.get("formula"),
                "principle": "ЗНАНИЕ → СЛОВО → ВОЛЯ → ДЕЙСТВИЕ",
                "caution": data.get("note"),
            }
        else:
            result["message"] = f"Лексема «{query}» отсутствует в seed-базе."
            result["available"] = self.vedun.list_lexemes()

        return result

    def print_analysis(self, result: Dict[str, Any]) -> None:
        q = result["query"]
        print("=" * 70)
        print("  PNEVMA–SLAVIC COGNITIVE AGENT Ω")
        print(f"  Запрос: {q}")
        print("=" * 70)

        if not result["found"]:
            print(f"\n[!] {result.get('message')}")
            print("Доступные лексемы:", ", ".join(result.get("available", [])))
            return

        v = result["vedun"]
        print("\n[VEDUN]  Историко-лексический уровень (FACT / HYPOTHESIS)")
        print("-" * 50)
        if v.get("forms"):
            print("Формы:")
            for k, val in v["forms"].items():
                print(f"  · {k}: {val}")
        print(f"\nЭтимология [{v['etymology_status']}]:")
        print(f"  {v['etymology_main']}")
        if v.get("ie_root"):
            print(f"  И.-е. корень: {v['ie_root']}")
        if v.get("cognates"):
            print("  Когнаты:")
            for c in v["cognates"]:
                print(f"    – {c}")
        if v.get("alternatives"):
            print("  Альтернативы / спорные версии:")
            for alt in v["alternatives"]:
                print(f"    [{alt['status']}] {alt['text']}")
        print(f"\nПериод: {v.get('period')}")
        print("Источники:")
        for s in v.get("sources", []):
            print(f"  · {s}")

        w = result["volkhv"]
        print("\n[VOLHV]  Смысловой уровень (INTERPRETATION)")
        print("-" * 50)
        print(f"Ядро: {w.get('core')}")
        print(f"Цепочка: {w.get('chain')}")
        print(f"Формула: {w.get('formula')}")
        if w.get("functions"):
            print("Функции:", ", ".join(w["functions"]))
        if w.get("note"):
            print(f"Примечание: {w['note']}")

        print("\n[VESHCHUN]  Возвещение / синтез")
        print("-" * 50)
        print(result["veshchun"])

        print("\n[KHARAKTERNIK]  Исследовательское действие")
        print("-" * 50)
        print(result["kharakternik"])

        if "graph" in result:
            print("\n[GRAPH]  Связи в семантическом графе")
            print("-" * 50)
            neigh = result["graph"].get("neighbors", [])
            if neigh:
                print("Соседи:", ", ".join(neigh))
            print(result["graph"].get("summary", ""))

        s = result["synthesis"]
        print("\n[SYNTHESIS]")
        print("-" * 50)
        print(f"Формула: {s.get('formula')}")
        print(f"Принцип: {s.get('principle')}")
        if s.get("caution"):
            print(f"Осторожность: {s['caution']}")
        print()

    def list_lexemes(self) -> None:
        print("=" * 50)
        print("  Лексемы в seed-базе")
        print("=" * 50)
        for name in self.vedun.list_lexemes():
            data = self.vedun.lexemes[name]
            print(f"  · {name:15} [{data.get('period', '—')}]")
        print()

    def show_graph(self) -> None:
        print("=" * 50)
        print("  Semantic Knowledge Graph")
        print("=" * 50)
        print(self.graph.summary())
        print()
