"""ХАРАКТЕРНИК — Agency / Will / Action. «Я ДЕЙСТВУЮ»"""

from __future__ import annotations
from typing import Any, Dict, Optional


class Kharakternik:
    def suggest_action(self, query: str, vedun_data: Optional[Dict], volkhv_data: Dict) -> str:
        if not vedun_data:
            return "Расширить лексическую базу и источники по данному термину."

        period = vedun_data.get("period", "")
        if "поздний" in period:
            return (
                "Отделить поздний культурный слой от праславянского. "
                "Не проецировать казацкие функции на древний период. "
                "Искать параллели в функциях, а не в этимологии."
            )
        return (
            "Развести уровни: 1) засвидетельствованные формы и источники; "
            "2) этимологические гипотезы; 3) смысловую реконструкцию. "
            "Строить семантический граф связей с соседними лексемами."
        )
