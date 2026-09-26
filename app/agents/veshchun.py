"""ВЕЩУН — Communication / Prediction. «Я ВЕЩАЮ»"""

from __future__ import annotations
from typing import Any, Dict, Optional


class Veshchun:
    def proclaim(self, query: str, vedun_data: Optional[Dict], volkhv_data: Dict) -> str:
        if not vedun_data:
            return f"Не нашёл устойчивых данных по «{query}». Требуется расширение базы."

        lines = [
            f"Формула: {volkhv_data.get('formula', '—')}",
            f"Цепочка: {volkhv_data.get('chain', '—')}",
        ]
        if volkhv_data.get("functions"):
            lines.append("Функции: " + ", ".join(volkhv_data["functions"]))
        return "\n".join(lines)
