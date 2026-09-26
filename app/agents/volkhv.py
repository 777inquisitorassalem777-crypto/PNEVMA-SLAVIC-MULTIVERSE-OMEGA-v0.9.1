"""ВОЛХВ — Interpretation / Symbolism. «Я ПОНИМАЮ»"""

from __future__ import annotations
from typing import Any, Dict


class Volkhv:
    def interpret(self, lexeme_data: Dict[str, Any] | None) -> Dict[str, Any]:
        if not lexeme_data:
            return {"meaning": "пустота", "level": "none"}

        sem = lexeme_data.get("semantics", {})
        return {
            "core": sem.get("core"),
            "chain": sem.get("chain"),
            "formula": sem.get("formula"),
            "functions": lexeme_data.get("functions", []),
            "period": lexeme_data.get("period"),
            "note": lexeme_data.get("note"),
        }
