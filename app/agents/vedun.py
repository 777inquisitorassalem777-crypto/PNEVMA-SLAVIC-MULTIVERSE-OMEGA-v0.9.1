"""ВЕДУН — Knowledge / Memory. «Я ЗНАЮ»"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List, Optional


class Vedun:
    def __init__(self, data_path: Optional[str] = None):
        if data_path is None:
            data_path = Path(__file__).resolve().parents[2] / "data" / "lexemes.json"
        self.data_path = Path(data_path)
        self.lexemes: Dict[str, Any] = {}
        self._load()

    def _load(self) -> None:
        if self.data_path.exists():
            with open(self.data_path, encoding="utf-8") as f:
                self.lexemes = json.load(f)
        else:
            self.lexemes = {}

    def recognize(self, query: str) -> Optional[Dict[str, Any]]:
        q = query.lower().strip()
        if q in self.lexemes:
            return self.lexemes[q]
        for key, data in self.lexemes.items():
            if q in key or key in q:
                return data
            for form in data.get("forms", {}).values():
                if isinstance(form, str) and q in form.lower():
                    return data
        return None

    def list_lexemes(self) -> List[str]:
        return list(self.lexemes.keys())

    def get_all(self) -> Dict[str, Any]:
        return self.lexemes
