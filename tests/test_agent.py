"""Базовые тесты оркестратора."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.agents.orchestrator import SlavicCognitiveAgent


def test_analyze_volkhv():
    agent = SlavicCognitiveAgent()
    result = agent.analyze("волхв")
    assert result["found"] is True
    assert result["vedun"]["etymology_status"] in ("fact", "hypothesis", "disputed")
    assert "formula" in result["volkhv"]
    assert result["synthesis"]["principle"] == "ЗНАНИЕ → СЛОВО → ВОЛЯ → ДЕЙСТВИЕ"


def test_analyze_vedun():
    agent = SlavicCognitiveAgent()
    result = agent.analyze("ведун")
    assert result["found"] is True
    assert result["vedun"]["etymology_status"] == "fact"
    assert result["vedun"]["ie_root"] is not None


def test_analyze_kharakternik():
    agent = SlavicCognitiveAgent()
    result = agent.analyze("характерник")
    assert result["found"] is True
    assert "поздний" in result["vedun"]["period"]


def test_unknown():
    agent = SlavicCognitiveAgent()
    result = agent.analyze("несуществующее_слово_xyz")
    assert result["found"] is False
    assert "available" in result


def test_graph():
    agent = SlavicCognitiveAgent()
    g = agent.graph.to_dict()
    assert len(g["nodes"]) > 5
    assert len(g["edges"]) > 5


def test_lexemes_list():
    agent = SlavicCognitiveAgent()
    lexemes = agent.vedun.list_lexemes()
    assert "волхв" in lexemes
    assert "ведун" in lexemes
    assert "характерник" in lexemes
