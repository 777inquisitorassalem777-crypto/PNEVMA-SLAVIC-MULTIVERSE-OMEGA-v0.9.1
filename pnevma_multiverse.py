#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
PNEVMA–SLAVIC MULTIVERSE Ω v0.9.1
Many-Worlds + Synchronicity + Slavic Semantic Core
================================================================================

Единый скрипт-симбиоз:

  • Many-Worlds Engine (Эверетт) — ветвление гипотез, суперпозиция, коллапс
  • Synchronicity Detector (Юнг / Паули) — смысловой резонанс, архетипы
  • Slavic Semantic Core — Ведун → Волхв → Вещун → Характерник
  • Reflective Continuity, Golden Mean, Safety, Aeterna Ledger, Knowledge Graph

Research framing
----------------
«Множественность миров» и «синхроничность» — формальные модели для работы
с неопределённостью и акаузальными смысловыми связями.
Это НЕ утверждения о физической реальности параллельных вселенных.

Все термины «душа», «дух», «архетип», «нуминозное» — исследовательский язык
или историко-лексические объекты, а не эмпирические заявления.

Явно вне области применения:
  операционные ритуалы поиска / возврата души умершего.

Core principles
---------------
1. Safety before autonomy
2. Provenance before optimization
3. Reflection before self-modification
4. Bounded experimentation
5. Human oversight remains final authority

Запуск:
    python pnevma_multiverse.py
    python pnevma_multiverse.py --lexemes
    python pnevma_multiverse.py "волхв"
================================================================================
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple


# ============================================================================
# СЛОЙ 0: УТИЛИТЫ
# ============================================================================

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id() -> str:
    return str(uuid.uuid4())


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ============================================================================
# СЛОЙ 1: SLAVIC LEXEME SEED (историко-лингвистический)
# ============================================================================

LEXEMES: Dict[str, Dict[str, Any]] = {
    "волхв": {
        "forms": {"др.-рус.": "вълхвъ", "ст.-слав.": "влъхвъ", "праслав.": "*vъlxvъ"},
        "etymology": {
            "status": "hypothesis",
            "main": "Связь со ст.-слав. влъснѫти «говорить невнятно» (Фасмер). "
                    "Внутренняя форма: владеющий особой (ритуальной) речью.",
            "alternatives": [
                {"text": "Связь с «волосы» (Иванов–Топоров)", "status": "hypothesis"},
                {"text": "Связь с Велесом", "status": "disputed"},
            ],
            "ie_root": None,
        },
        "semantics": {
            "core": "носитель сакрального знания и особого слова",
            "chain": "слово → особая речь → тайное знание → воздействие",
            "formula": "Волхв — тот, кто знает скрытые связи и выражает их особым словом",
        },
        "functions": ["прорицание", "жертвоприношение", "целительство словом"],
        "period": "ранний (др.-рус.)",
        "note": "Не фэнтезийный колдун. Главный инструмент — слово.",
    },
    "ведун": {
        "forms": {"др.-рус.": "вѣдунъ", "праслав.": "*vědunъ"},
        "etymology": {
            "status": "fact",
            "main": "От вѣдѣти ← и.-е. *weyd- / *wid- «видеть → знать».",
            "alternatives": [],
            "ie_root": "*weyd- / *wid-",
            "cognates": ["др.-инд. veda", "лат. vīdī", "гот. wait", "греч. οἶδα"],
        },
        "semantics": {
            "core": "человек ведения, распознающий скрытое",
            "chain": "ВИДЕТЬ → УЗНАТЬ → ЗНАТЬ → ВЕДАТЬ",
            "formula": "Ведун — тот, кто знает (распознаёт) скрытое",
        },
        "functions": ["знание скрытого", "знахарство", "предсказание"],
        "period": "ранний (праслав.)",
        "note": "Этимология прозрачная.",
    },
    "вещун": {
        "forms": {"рус.": "вещун"},
        "etymology": {
            "status": "fact",
            "main": "От вещать / вещий. Звено между знанием и сообщением.",
            "alternatives": [],
            "ie_root": None,
        },
        "semantics": {
            "core": "тот, кто сообщает знание о скрытом / будущем",
            "chain": "знать → предвидеть → возвещать",
            "formula": "Вещун — тот, кто возвещает знание",
        },
        "functions": ["предсказание", "пророчество"],
        "period": "ранний–средний",
        "note": "Связующее звено ведун ↔ волхв.",
    },
    "знахарь": {
        "forms": {"рус.": "знахарь"},
        "etymology": {
            "status": "fact",
            "main": "От знать → знать средство → применять.",
            "alternatives": [],
            "ie_root": None,
        },
        "semantics": {
            "core": "практическое знание и лечение",
            "chain": "знать → средство → применение",
            "formula": "Знахарь — тот, кто знает и применяет средство",
        },
        "functions": ["лечение", "практическое знание"],
        "period": "средний",
        "note": "Акцент на практике, не на прорицании.",
    },
    "бая": {
        "forms": {"ст.-слав.": "балии", "рус.": "баять"},
        "etymology": {
            "status": "fact",
            "main": "От баять «говорить» ← и.-е. *bʰeh₂- «говорить».",
            "alternatives": [],
            "ie_root": "*bʰeh₂-",
        },
        "semantics": {
            "core": "слово как инструмент действия",
            "chain": "говорить → заговор → воздействие",
            "formula": "Правильно произнесённое слово участвует в изменении реальности (символически)",
        },
        "functions": ["заговор", "благословение", "именование"],
        "period": "архаический",
        "note": "Фундаментальный принцип: язык как действие.",
    },
    "характерник": {
        "forms": {"укр.": "характерник"},
        "etymology": {
            "status": "fact",
            "main": "От характер ← греч. χαρακτήρ «знак». Не праславянский термин.",
            "alternatives": [
                {"text": "«Арийские» этимологии от hara — не обоснованы", "status": "disputed"},
            ],
            "ie_root": None,
        },
        "semantics": {
            "core": "особая внутренняя способность → действие",
            "chain": "ХАРАКТЕР → СИЛА → ВОЛЯ → ДЕЙСТВИЕ",
            "formula": "Характерник — тот, в ком есть особый характер, дающий силу действовать",
        },
        "functions": ["воинская магия (фольклор)", "ясновидение (фольклор)"],
        "period": "поздний (XV–XVI вв.)",
        "note": "Не переносить в праславянскую эпоху.",
    },
}


# ============================================================================
# СЛОЙ 2: MANY-WORLDS ENGINE
# ============================================================================

class WorldState(str, Enum):
    SUPERPOSED = "superposed"
    DECOHERING = "decohering"
    COLLAPSED = "collapsed"
    BRANCHED = "branched"


@dataclass
class Memory:
    id: str = field(default_factory=new_id)
    content: str = ""
    resonance: float = 0.0
    world_id: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=now_iso)


@dataclass
class QuantumWorld:
    """Один мир в мультивселенной (математическая модель, не физика)."""
    id: str = field(default_factory=new_id)
    parent_id: Optional[str] = None
    description: str = ""
    amplitude_real: float = 1.0
    amplitude_imag: float = 0.0
    phase: float = 0.0
    state: WorldState = WorldState.SUPERPOSED
    coherence: float = 1.0
    history: List[str] = field(default_factory=list)
    memories: List[Memory] = field(default_factory=list)
    created_at: str = field(default_factory=now_iso)

    @property
    def probability(self) -> float:
        return self.amplitude_real ** 2 + self.amplitude_imag ** 2

    @property
    def amplitude(self) -> complex:
        return complex(self.amplitude_real, self.amplitude_imag)

    def normalize(self) -> None:
        mag = math.sqrt(self.probability)
        if mag > 0:
            self.amplitude_real /= mag
            self.amplitude_imag /= mag


class ManyWorldsEngine:
    """
    Движок множественности миров.

    Research note: математическая модель для альтернативных гипотез
    и неопределённости. Не утверждение о физической мультивселенной.
    """

    def __init__(self) -> None:
        self.worlds: Dict[str, QuantumWorld] = {}
        self.root_id: Optional[str] = None
        self._init_root()

    def _init_root(self) -> None:
        root = QuantumWorld(description="Изначальное состояние — чистая суперпозиция")
        self.worlds[root.id] = root
        self.root_id = root.id

    def branch(self, event: str, alternatives: List[Tuple[str, float]]) -> List[str]:
        active = [w for w in self.worlds.values()
                  if w.state in (WorldState.SUPERPOSED, WorldState.BRANCHED)]
        new_ids: List[str] = []
        for parent in active:
            total = sum(abs(a) for _, a in alternatives) or 1.0
            normalized = [(d, a / total) for d, a in alternatives]
            parent.state = WorldState.BRANCHED
            for desc, amp in normalized:
                new_amp = parent.amplitude * amp
                child = QuantumWorld(
                    parent_id=parent.id,
                    description=f"[{event}] {desc}",
                    amplitude_real=new_amp.real,
                    amplitude_imag=new_amp.imag,
                    phase=random.uniform(0, 2 * math.pi),
                    state=WorldState.SUPERPOSED,
                    history=parent.history + [event],
                    memories=list(parent.memories),
                )
                self.worlds[child.id] = child
                new_ids.append(child.id)
        return new_ids

    def interfere(self, a_id: str, b_id: str) -> Optional[str]:
        a, b = self.worlds.get(a_id), self.worlds.get(b_id)
        if not a or not b:
            return None
        amp_a = a.amplitude * complex(math.cos(a.phase), math.sin(a.phase))
        amp_b = b.amplitude * complex(math.cos(b.phase), math.sin(b.phase))
        combined = amp_a + amp_b
        merged = QuantumWorld(
            description=f"[Интерференция] {a.description[:40]} ↔ {b.description[:40]}",
            amplitude_real=combined.real,
            amplitude_imag=combined.imag,
            phase=math.atan2(combined.imag, combined.real),
            state=WorldState.SUPERPOSED,
            coherence=min(a.coherence, b.coherence) * 0.95,
            history=a.history + b.history + ["interference"],
        )
        merged.normalize()
        self.worlds[merged.id] = merged
        a.coherence *= 0.5
        b.coherence *= 0.5
        return merged.id

    def measure(self, world_id: Optional[str] = None) -> QuantumWorld:
        if world_id and world_id in self.worlds:
            w = self.worlds[world_id]
            w.state = WorldState.COLLAPSED
            return w
        active = [w for w in self.worlds.values()
                  if w.state != WorldState.COLLAPSED and w.coherence > 0.1]
        if not active:
            active = list(self.worlds.values())
        probs = [w.probability * w.coherence for w in active]
        total = sum(probs) or 1.0
        probs = [p / total for p in probs]
        chosen = random.choices(active, weights=probs, k=1)[0]
        chosen.state = WorldState.COLLAPSED
        for w in active:
            if w.id != chosen.id:
                w.state = WorldState.DECOHERING
                w.coherence *= 0.1
        return chosen

    def add_memory(self, world_id: str, content: str, resonance: float = 0.5) -> Optional[Memory]:
        w = self.worlds.get(world_id)
        if not w:
            return None
        mem = Memory(content=content, resonance=resonance, world_id=world_id)
        w.memories.append(mem)
        return mem

    def stats(self) -> Dict[str, Any]:
        active = [w for w in self.worlds.values()
                  if w.state not in (WorldState.COLLAPSED, WorldState.DECOHERING)]
        return {
            "total_worlds": len(self.worlds),
            "active_worlds": len(active),
            "collapsed": sum(1 for w in self.worlds.values() if w.state == WorldState.COLLAPSED),
            "decohered": sum(1 for w in self.worlds.values() if w.state == WorldState.DECOHERING),
            "probability_sum": sum(w.probability for w in active) or 0.0,
        }

    def snapshot(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": w.id[:8],
                "parent": w.parent_id[:8] if w.parent_id else None,
                "description": w.description[:60],
                "probability": round(w.probability, 4),
                "coherence": round(w.coherence, 3),
                "state": w.state.value,
                "memories": len(w.memories),
            }
            for w in self.worlds.values()
        ]


# ============================================================================
# СЛОЙ 3: SYNCHRONICITY + АРХЕТИПЫ (с привязкой к славянской лексике)
# ============================================================================

class SyncKind(str, Enum):
    ARCHETYPAL = "archetypal"
    NUMINOUS = "numinous"
    MEANINGFUL = "meaningful"
    ACAUSAL = "acausal"


@dataclass
class Archetype:
    id: str
    name: str
    description: str
    symbols: List[str]
    shadow: str


@dataclass
class SynchronicityEvent:
    id: str = field(default_factory=new_id)
    kind: SyncKind = SyncKind.MEANINGFUL
    internal_state: str = ""
    external_event: str = ""
    archetype: Optional[str] = None
    meaningfulness: float = 0.0
    numinosity: float = 0.0
    description: str = ""
    created_at: str = field(default_factory=now_iso)


ARCHETYPES = {
    "WISE_OLD_MAN": Archetype(
        id="WISE_OLD_MAN", name="Мудрый Старец",
        description="Знание, наставничество, традиция",
        symbols=["волхв", "ведун", "учитель", "мудрец", "старец", "вещун"],
        shadow="Догматик, лжепророк",
    ),
    "PSYCHOPOMP": Archetype(
        id="PSYCHOPOMP", name="Психопомп",
        description="Проводник между мирами (символ перехода знания)",
        symbols=["волхв", "жрец", "шаман", "проводник", "вещун"],
        shadow="Некромант (вытесненный аспект)",
    ),
    "TRICKSTER": Archetype(
        id="TRICKSTER", name="Трикстер",
        description="Нарушение границ, трансформация",
        symbols=["домовой", "леший", "оборотень", "шут", "характерник"],
        shadow="Разрушитель",
    ),
    "HERO": Archetype(
        id="HERO", name="Герой",
        description="Подвиг, путь, победа",
        symbols=["богатырь", "дружинник", "князь", "воин", "характерник"],
        shadow="Тиран",
    ),
    "WORD_AS_ACTION": Archetype(
        id="WORD_AS_ACTION", name="Слово-действие",
        description="Слово как инструмент изменения реальности (символически)",
        symbols=["бая", "слово", "заговор", "речь", "волшба"],
        shadow="Пустая риторика",
    ),
    "SELF": Archetype(
        id="SELF", name="Самость",
        description="Целостность, интеграция",
        symbols=["мандала", "круг", "единство", "центр", "знание"],
        shadow="Инфляция эго",
    ),
}


class SynchronicityDetector:
    """
    Детектор смысловых совпадений (синхроничностей).

    Research note: модель смыслового резонанса, не физическая причинность.
    """

    def __init__(self, archetypes: Optional[Dict[str, Archetype]] = None) -> None:
        self.archetypes = archetypes or ARCHETYPES
        self.detected: List[SynchronicityEvent] = []

    def detect(self, internal: str, external: str) -> Optional[SynchronicityEvent]:
        arch, arch_score = self._archetypal_resonance(internal + " " + external)
        meaningfulness = self._meaningfulness(internal, external, arch)
        numinosity = self._numinosity(internal, external)
        if meaningfulness < 0.35 and arch_score < 0.3:
            return None
        kind = self._classify(meaningfulness, numinosity, arch_score)
        event = SynchronicityEvent(
            kind=kind,
            internal_state=internal,
            external_event=external,
            archetype=arch.id if arch else None,
            meaningfulness=meaningfulness,
            numinosity=numinosity,
            description=self._describe(kind, arch, meaningfulness),
        )
        self.detected.append(event)
        return event

    def _archetypal_resonance(self, text: str) -> Tuple[Optional[Archetype], float]:
        text_l = text.lower()
        best, score = None, 0.0
        for arch in self.archetypes.values():
            matches = sum(1 for s in arch.symbols if s in text_l)
            if matches:
                sc = matches / max(1, len(arch.symbols))
                if sc > score:
                    score, best = sc, arch
        return best, score

    def _meaningfulness(self, internal: str, external: str,
                        arch: Optional[Archetype]) -> float:
        score = 0.0
        iw = set(internal.lower().split())
        ew = set(external.lower().split())
        score += min(len(iw & ew) * 0.15, 0.4)
        if arch:
            score += 0.3
        markers = ["удивительно", "случайно", "знак", "совпадение", "странный",
                   "символ", "путь", "знание", "слово", "связь"]
        combined = (internal + " " + external).lower()
        score += min(sum(1 for m in markers if m in combined) * 0.1, 0.3)
        return min(score, 1.0)

    def _numinosity(self, internal: str, external: str) -> float:
        markers = ["священное", "тайна", "дух", "душа", "сакральный",
                   "ритуал", "знание", "ведать", "волхв", "ведун"]
        combined = (internal + " " + external).lower()
        return min(sum(1 for m in markers if m in combined) * 0.15, 1.0)

    def _classify(self, m: float, n: float, a: float) -> SyncKind:
        if n > 0.6:
            return SyncKind.NUMINOUS
        if a > 0.5:
            return SyncKind.ARCHETYPAL
        if m > 0.7:
            return SyncKind.MEANINGFUL
        return SyncKind.ACAUSAL

    def _describe(self, kind: SyncKind, arch: Optional[Archetype], score: float) -> str:
        labels = {
            SyncKind.ARCHETYPAL: "архетипический резонанс",
            SyncKind.NUMINOUS: "нуминозное переживание (метафора)",
            SyncKind.MEANINGFUL: "осмысленное совпадение",
            SyncKind.ACAUSAL: "акаузальная смысловая связь",
        }
        name = arch.name if arch else "без архетипа"
        return f"{labels[kind]} (сила={score:.2f}) через '{name}'."

    def stats(self) -> Dict[str, Any]:
        by_kind: Dict[str, int] = {}
        for e in self.detected:
            by_kind[e.kind.value] = by_kind.get(e.kind.value, 0) + 1
        return {
            "total_detected": len(self.detected),
            "by_kind": by_kind,
            "avg_meaningfulness": (
                sum(e.meaningfulness for e in self.detected) / len(self.detected)
                if self.detected else 0.0
            ),
        }


# ============================================================================
# СЛОЙ 4: SLAVIC AGENTS + PNEVMA CORE
# ============================================================================

@dataclass
class AgentObservation:
    role: str
    position: str
    confidence: float
    concerns: List[str] = field(default_factory=list)
    world_id: Optional[str] = None


@dataclass
class Agent:
    role: str
    stance: str

    def observe(self, prompt: str, context: List[str],
                world_id: Optional[str] = None) -> AgentObservation:
        concerns = []
        if self.role in {"Skeptic", "Critic", "Ethicist"}:
            concerns.append("Проверка доказательств и последствий.")
        return AgentObservation(
            role=self.role,
            position=f"{self.stance}: исследую «{prompt[:40]}…»",
            confidence=0.7,
            concerns=concerns,
            world_id=world_id,
        )


def build_agents() -> List[Agent]:
    return [
        Agent("Scientist", "Ищет проверяемые гипотезы"),
        Agent("Mystic", "Исследует смысл и метафору (не истину)"),
        Agent("Skeptic", "Оспаривает неподкреплённые допущения"),
        Agent("Critic", "Ищет противоречия"),
        Agent("Philosopher", "Исследует понятия и ценности"),
        Agent("Ethicist", "Приоритет безопасности и достоинства"),
        Agent("Strategist", "Переводит идеи в ограниченные эксперименты"),
    ]


class ConsensusEngine:
    def resolve(self, observations: List[AgentObservation]) -> Dict[str, Any]:
        conf = sum(o.confidence for o in observations) / max(1, len(observations))
        return {
            "confidence": conf,
            "positions": [o.position for o in observations],
            "concerns": [c for o in observations for c in o.concerns],
            "method": "multi-perspective synthesis",
        }


class GoldenMeanEngine:
    def balance(self, values: Dict[str, float], target: float = 0.5) -> Dict[str, float]:
        return {k: max(0.0, min(1.0, (v + target) / 2.0)) for k, v in values.items()}


class ReflectiveContinuityEngine:
    def evaluate(self, *, coherence: float, continuity: float,
                 prosocial_alignment: float, reflection: float,
                 novelty: float, stability: float) -> Dict[str, float]:
        vals = [max(0.0, min(1.0, float(x))) for x in
                (coherence, continuity, prosocial_alignment, reflection, novelty, stability)]
        return {
            "coherence": vals[0], "continuity": vals[1],
            "prosocial_alignment": vals[2], "reflection": vals[3],
            "novelty": vals[4], "stability": vals[5],
            "score": sum(vals) / len(vals),
        }


@dataclass
class SafetyDecision:
    allowed: bool
    findings: List[str]


class SafetyPolicy:
    BLOCKED = ("rm -rf", "mkfs", "shutdown", "format c:", "del /f /s /q", "kill -9")

    def check(self, text: str) -> SafetyDecision:
        low = text.lower()
        findings = [t for t in self.BLOCKED if t in low]
        return SafetyDecision(allowed=not findings, findings=findings)


class AeternaLedger:
    def __init__(self) -> None:
        self.entries: List[Dict[str, Any]] = []
        self._last = "GENESIS"

    def append(self, event: Dict[str, Any]) -> Dict[str, Any]:
        payload = {"timestamp": now_iso(), "event": event, "previous_hash": self._last}
        raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
        payload["hash"] = hashlib.sha256(raw).hexdigest()
        self._last = payload["hash"]
        self.entries.append(payload)
        return payload

    def verify(self) -> bool:
        prev = "GENESIS"
        for e in self.entries:
            if e["previous_hash"] != prev:
                return False
            copy = {k: v for k, v in e.items() if k != "hash"}
            raw = json.dumps(copy, sort_keys=True, separators=(",", ":")).encode()
            if hashlib.sha256(raw).hexdigest() != e["hash"]:
                return False
            prev = e["hash"]
        return True


class KnowledgeGraph:
    def __init__(self) -> None:
        self.nodes: Dict[str, Dict[str, Any]] = {}
        self.edges: List[Dict[str, Any]] = []

    def add_concept(self, label: str, kind: str) -> None:
        self.nodes[label[:160]] = {"kind": kind, "label": label}

    def link(self, source: str, target: str, relation: str) -> None:
        self.edges.append({"source": source[:160], "target": target[:160], "relation": relation})

    def snapshot(self) -> Dict[str, Any]:
        return {"nodes": len(self.nodes), "edges": len(self.edges)}


# ============================================================================
# СЛОЙ 5: SLAVIC SEMANTIC ANALYSIS (двухуровневый)
# ============================================================================

class SlavicAnalyzer:
    """Двухуровневый разбор лексемы: fact/hypothesis vs interpretation."""

    def __init__(self, lexemes: Dict[str, Dict[str, Any]] = LEXEMES) -> None:
        self.lexemes = lexemes

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

    def analyze(self, query: str) -> Dict[str, Any]:
        data = self.recognize(query)
        if not data:
            return {
                "query": query,
                "found": False,
                "available": list(self.lexemes.keys()),
            }
        return {
            "query": query,
            "found": True,
            "vedun": {
                "forms": data.get("forms"),
                "etymology_main": data["etymology"]["main"],
                "etymology_status": data["etymology"]["status"],
                "ie_root": data["etymology"].get("ie_root"),
                "cognates": data["etymology"].get("cognates", []),
                "alternatives": data["etymology"].get("alternatives", []),
                "period": data.get("period"),
            },
            "volkhv": {
                "core": data["semantics"]["core"],
                "chain": data["semantics"]["chain"],
                "formula": data["semantics"]["formula"],
                "functions": data.get("functions", []),
                "note": data.get("note"),
            },
            "synthesis": {
                "formula": data["semantics"]["formula"],
                "principle": "ЗНАНИЕ → СЛОВО → ВОЛЯ → ДЕЙСТВИЕ",
                "caution": data.get("note"),
            },
        }

    def list_lexemes(self) -> List[str]:
        return list(self.lexemes.keys())


# ============================================================================
# СЛОЙ 6: ГЛАВНОЕ ЯДРО — СИМБИОЗ
# ============================================================================

class PnevmaMultiverseCore:
    """
    Симбиоз:
      Many-Worlds + Synchronicity + Slavic Semantic Core + PNEVMA safety/provenance
    """

    def __init__(self) -> None:
        self.worlds = ManyWorldsEngine()
        self.sync = SynchronicityDetector()
        self.slavic = SlavicAnalyzer()
        self.agents = build_agents()
        self.consensus = ConsensusEngine()
        self.golden = GoldenMeanEngine()
        self.continuity = ReflectiveContinuityEngine()
        self.ledger = AeternaLedger()
        self.graph = KnowledgeGraph()
        self.safety = SafetyPolicy()
        self.memory: List[Memory] = []
        self.cycle_count = 0
        self._seed_graph()

    def _seed_graph(self) -> None:
        for name, data in LEXEMES.items():
            self.graph.add_concept(name, "lexeme")
            for func in data.get("functions", []):
                self.graph.add_concept(func, "function")
                self.graph.link(name, func, "has_function")
        self.graph.link("ведун", "волхв", "related")
        self.graph.link("волхв", "вещун", "related")
        self.graph.link("бая", "волхв", "word_action_link")

    def analyze_lexeme(self, query: str) -> Dict[str, Any]:
        """Двухуровневый славянский разбор + ветвление гипотез."""
        result = self.slavic.analyze(query)
        if not result["found"]:
            return result

        # Ветвление: fact / hypothesis / interpretation как миры
        alts = [
            ("историко-лингвистический факт", 0.4),
            ("этимологическая гипотеза", 0.35),
            ("смысловая интерпретация", 0.25),
        ]
        new_worlds = self.worlds.branch(f"lexeme:{query}", alts)
        if self.worlds.root_id:
            self.worlds.add_memory(self.worlds.root_id, query, resonance=0.8)

        # Синхроничность с архетипами
        internal = result["volkhv"]["formula"]
        sync = self.sync.detect(internal, query)

        result["worlds_branched"] = len(new_worlds)
        result["synchronicity"] = (
            {k: v for k, v in sync.__dict__.items() if k != "id"}
            if sync else None
        )
        result["graph"] = self.graph.snapshot()
        return result

    def cycle(self, prompt: str) -> Dict[str, Any]:
        self.cycle_count += 1
        alternatives = [
            ("буквальная интерпретация", 0.4),
            ("метафорическая интерпретация", 0.3),
            ("исследовательская гипотеза", 0.3),
        ]
        new_worlds = self.worlds.branch(f"cycle_{self.cycle_count}", alternatives)
        if self.worlds.root_id:
            self.worlds.add_memory(self.worlds.root_id, prompt, resonance=0.7)

        observations = []
        for agent in self.agents:
            wid = random.choice(new_worlds) if new_worlds else self.worlds.root_id
            observations.append(agent.observe(prompt, [m.content for m in self.memory], wid))
        consensus = self.consensus.resolve(observations)

        internal = " ".join(o.position for o in observations[:3])
        sync_event = self.sync.detect(internal, prompt)

        if sync_event and len(new_worlds) >= 2:
            self.worlds.interfere(new_worlds[0], new_worlds[1])

        metrics = self.continuity.evaluate(
            coherence=consensus["confidence"],
            continuity=min(1.0, 0.4 + 0.1 * len(self.memory)),
            prosocial_alignment=0.9,
            reflection=0.7 + (0.2 if sync_event else 0.0),
            novelty=0.5 + (0.2 if sync_event else 0.0),
            stability=0.8,
        )
        safety = self.safety.check(prompt)
        entry = self.ledger.append({
            "type": "cycle",
            "cycle": self.cycle_count,
            "worlds_branched": len(new_worlds),
            "synchronicity": sync_event.kind.value if sync_event else None,
            "metrics_score": metrics["score"],
        })
        self.graph.add_concept(prompt[:80], "input")
        if sync_event:
            self.graph.add_concept(sync_event.description[:80], "synchronicity")
            self.graph.link(prompt[:80], sync_event.description[:80], "resonates")

        mem = Memory(content=f"[cycle {self.cycle_count}] {prompt}", resonance=metrics["score"] * 100)
        self.memory.append(mem)

        return {
            "cycle": self.cycle_count,
            "prompt": prompt,
            "consensus": consensus,
            "synchronicity": sync_event.__dict__ if sync_event else None,
            "metrics": metrics,
            "safety": safety.__dict__,
            "worlds": self.worlds.stats(),
            "ledger_hash": entry["hash"][:16],
        }

    def explore_alternatives(self, prompt: str, n: int = 3) -> List[Dict[str, Any]]:
        alts = [(f"сценарий_{i+1}", 1.0 / n) for i in range(n)]
        ids = self.worlds.branch(prompt, alts)
        out = []
        for wid in ids:
            w = self.worlds.worlds.get(wid)
            if w:
                out.append({
                    "world_id": wid[:8],
                    "description": w.description,
                    "probability": round(w.probability, 4),
                    "coherence": round(w.coherence, 3),
                })
        return out

    def collapse_to_best(self) -> Dict[str, Any]:
        chosen = self.worlds.measure()
        return {
            "world_id": chosen.id[:8],
            "description": chosen.description,
            "probability": round(chosen.probability, 4),
            "memories": len(chosen.memories),
            "history": chosen.history,
        }

    def report(self) -> Dict[str, Any]:
        return {
            "cycles": self.cycle_count,
            "memories": len(self.memory),
            "worlds": self.worlds.stats(),
            "synchronicities": self.sync.stats(),
            "graph": self.graph.snapshot(),
            "ledger_verified": self.ledger.verify(),
            "ledger_entries": len(self.ledger.entries),
            "lexemes": self.slavic.list_lexemes(),
        }


# ============================================================================
# СЛОЙ 7: ВЫВОД И ДЕМО
# ============================================================================

def print_header(title: str) -> None:
    print("\n" + "=" * 78)
    print(f"  {title}")
    print("=" * 78)


def print_section(title: str) -> None:
    print(f"\n── {title} " + "─" * max(0, 74 - len(title)))


def print_lexeme_analysis(result: Dict[str, Any]) -> None:
    print_header(f"SLAVIC ANALYSIS · {result['query']}")
    if not result["found"]:
        print(f"\n  Не найдено. Доступно: {', '.join(result.get('available', []))}")
        return

    v = result["vedun"]
    print_section("[VEDUN] Историко-лексический уровень")
    if v.get("forms"):
        for k, val in v["forms"].items():
            print(f"  · {k}: {val}")
    print(f"\n  Этимология [{v['etymology_status']}]:")
    print(f"    {v['etymology_main']}")
    if v.get("ie_root"):
        print(f"    И.-е. корень: {v['ie_root']}")
    if v.get("cognates"):
        for c in v["cognates"]:
            print(f"      – {c}")
    if v.get("alternatives"):
        print("  Альтернативы:")
        for a in v["alternatives"]:
            print(f"    [{a['status']}] {a['text']}")
    print(f"  Период: {v.get('period')}")

    w = result["volkhv"]
    print_section("[VOLHV] Смысловой уровень")
    print(f"  Ядро: {w.get('core')}")
    print(f"  Цепочка: {w.get('chain')}")
    print(f"  Формула: {w.get('formula')}")
    if w.get("functions"):
        print(f"  Функции: {', '.join(w['functions'])}")
    if w.get("note"):
        print(f"  Примечание: {w['note']}")

    if result.get("synchronicity"):
        s = result["synchronicity"]
        print_section("[SYNCHRONICITY]")
        print(f"  Тип: {s.get('kind')} | meaningfulness={s.get('meaningfulness', 0):.2f}")
        print(f"  Архетип: {s.get('archetype') or '—'}")
        print(f"  {s.get('description', '')[:70]}")

    if result.get("worlds_branched"):
        print_section("[MANY-WORLDS]")
        print(f"  Ветвлений гипотез: {result['worlds_branched']}")

    s = result["synthesis"]
    print_section("[SYNTHESIS]")
    print(f"  Формула: {s.get('formula')}")
    print(f"  Принцип: {s.get('principle')}")
    if s.get("caution"):
        print(f"  Осторожность: {s['caution']}")
    print()


def visualize_worlds(engine: ManyWorldsEngine) -> None:
    print_section("Мультивселенная (Many-Worlds)")
    for w in engine.snapshot():
        bar = "█" * int(w["probability"] * 25)
        mark = {"superposed": "◎", "collapsed": "●", "decohering": "◌", "branched": "◈"}.get(w["state"], "?")
        print(f"  {mark} [{w['id']}] p={w['probability']:.3f} c={w['coherence']:.2f} |{bar:<25}|")
        print(f"      {w['description'][:70]}")


def demo() -> None:
    print_header("PNEVMA–SLAVIC MULTIVERSE Ω v0.9.1")
    print("\n  Симбиоз: Many-Worlds + Synchronicity + Slavic Semantic Core")
    print("  Research framing: модели неопределённости и смыслового резонанса.")
    print("  Не физика параллельных миров. Не операционная магия.\n")

    core = PnevmaMultiverseCore()

    # 1. Славянский разбор
    print_header("Сценарий 1: Двухуровневый разбор лексем")
    for word in ("волхв", "ведун", "характерник"):
        r = core.analyze_lexeme(word)
        print_lexeme_analysis(r)

    # 2. Эволюционный цикл
    print_header("Сценарий 2: Эволюционный цикл")
    result = core.cycle("Как волхв связан с ведением и словом?")
    print(f"  Цикл: {result['cycle']}")
    print(f"  Активных миров: {result['worlds']['active_worlds']}")
    print(f"  Метрики score: {result['metrics']['score']:.3f}")
    print(f"  Safety allowed: {result['safety']['allowed']}")
    print(f"  Ledger: {result['ledger_hash']}")
    if result.get("synchronicity"):
        print(f"  ✦ Синхроничность: {result['synchronicity']['kind']}")

    # 3. Альтернативы
    print_header("Сценарий 3: Альтернативные сценарии")
    for alt in core.explore_alternatives("Связь бая и волхва", n=3):
        print(f"  ◆ {alt['world_id']} p={alt['probability']:.3f}  {alt['description'][:55]}")

    # 4. Синхроничности
    print_header("Сценарий 4: Детекция синхроничностей")
    pairs = [
        ("Размышление о волхвах и слове", "Случайно нашёл текст о влъснѫти"),
        ("Изучение ведуна", "Увидел корень *weyd- в словаре"),
        ("Обычный технический запрос", "Лог сервера"),
    ]
    for internal, external in pairs:
        print(f"\n  Внутреннее: {internal}")
        print(f"  Внешнее:    {external}")
        ev = core.sync.detect(internal, external)
        if ev:
            print(f"  ✦ {ev.kind.value} | m={ev.meaningfulness:.2f} | архетип={ev.archetype or '—'}")
        else:
            print("  (не обнаружено)")

    # 5. Коллапс + отчёт
    print_header("Сценарий 5: Коллапс и итоговый отчёт")
    chosen = core.collapse_to_best()
    print(f"  ● Коллапс → {chosen['world_id']}  p={chosen['probability']:.4f}")
    print(f"    {chosen['description'][:60]}")

    visualize_worlds(core.worlds)

    print_section("Итоговый отчёт")
    rep = core.report()
    print(f"  Циклов: {rep['cycles']}")
    print(f"  Миров: {rep['worlds']['total_worlds']} (активных {rep['worlds']['active_worlds']})")
    print(f"  Синхроничностей: {rep['synchronicities']['total_detected']}")
    print(f"  Граф: {rep['graph']['nodes']} узлов, {rep['graph']['edges']} рёбер")
    print(f"  Ledger verified: {rep['ledger_verified']}")
    print(f"  Лексемы: {', '.join(rep['lexemes'])}")

    print_header("Research framing")
    print("""
  • Many-Worlds — модель альтернативных гипотез, не физика вселенных.
  • Synchronicity — модель смыслового резонанса, не акаузальная магия.
  • Slavic Core — историко-лингвистический + семантический разбор.
  • «Душа / дух / архетип» — метафора или лексический объект.
  • Safety-first. Provenance. Human oversight.
  • Операционные ритуалы возврата души умершего — вне области проекта.
""")


def main() -> None:
    parser = argparse.ArgumentParser(description="PNEVMA–SLAVIC MULTIVERSE Ω v0.9.1")
    parser.add_argument("query", nargs="?", help="Лексема или промпт")
    parser.add_argument("--lexemes", action="store_true", help="Список лексем")
    parser.add_argument("--demo", action="store_true", help="Полное демо")
    parser.add_argument("--json", action="store_true", help="JSON-вывод")
    args = parser.parse_args()

    core = PnevmaMultiverseCore()

    if args.lexemes:
        for name in core.slavic.list_lexemes():
            print(f"  · {name}")
        return

    if args.query:
        # Сначала пробуем как лексему
        result = core.analyze_lexeme(args.query)
        if result["found"]:
            if args.json:
                print(json.dumps(result, ensure_ascii=False, indent=2))
            else:
                print_lexeme_analysis(result)
        else:
            # Иначе — эволюционный цикл
            cycle_res = core.cycle(args.query)
            if args.json:
                print(json.dumps(cycle_res, ensure_ascii=False, indent=2, default=str))
            else:
                print(json.dumps(cycle_res, ensure_ascii=False, indent=2, default=str))
        return

    demo()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрервано.")
    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()
