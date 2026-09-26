#!/usr/bin/env python3
"""
PNEVMA–SLAVIC SEMANTIC CORE Ω  ·  CLI-оркестратор
=================================================

Запуск:
  python slavic_cognitive_agent.py "волхв"
  python slavic_cognitive_agent.py --interactive
  python slavic_cognitive_agent.py --lexemes
  python slavic_cognitive_agent.py --graph
  python slavic_cognitive_agent.py --demo
"""

from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

# добавляем корень проекта в path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.agents.orchestrator import SlavicCognitiveAgent


def interactive_mode(agent: SlavicCognitiveAgent) -> None:
    print("=" * 70)
    print("  PNEVMA–SLAVIC COGNITIVE AGENT Ω  ·  Интерактивный режим")
    print("=" * 70)
    print("Введите слово, понятие или вопрос.")
    print("Команды: /lexemes  /graph  /quit  /help")
    print()

    while True:
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nДо свидания.")
            break

        if not user_input:
            continue
        if user_input in ("/quit", "/exit", "выход"):
            print("До свидания.")
            break
        if user_input in ("/lexemes", "/слова"):
            agent.list_lexemes()
            continue
        if user_input in ("/graph", "/граф"):
            agent.show_graph()
            continue
        if user_input in ("/help", "/помощь"):
            print("Примеры: волхв, ведун, вещун, знахарь, бая, характерник")
            print("Команды: /lexemes /graph /quit")
            continue

        result = agent.analyze(user_input)
        agent.print_analysis(result)


def demo(agent: SlavicCognitiveAgent) -> None:
    print("=" * 70)
    print("  ДЕМО: двухуровневый разбор ключевых лексем")
    print("=" * 70)
    for word in ["волхв", "ведун", "характерник"]:
        result = agent.analyze(word)
        agent.print_analysis(result)
        print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="PNEVMA–SLAVIC SEMANTIC CORE Ω — когнитивный оркестратор"
    )
    parser.add_argument("query", nargs="?", help="Слово или понятие для разбора")
    parser.add_argument("--interactive", "-i", action="store_true", help="Интерактивный режим")
    parser.add_argument("--lexemes", "-l", action="store_true", help="Список лексем")
    parser.add_argument("--graph", "-g", action="store_true", help="Семантический граф")
    parser.add_argument("--demo", "-d", action="store_true", help="Демонстрация")
    parser.add_argument("--json", action="store_true", help="Вывод в JSON")

    args = parser.parse_args()
    agent = SlavicCognitiveAgent()

    if args.interactive:
        interactive_mode(agent)
    elif args.lexemes:
        agent.list_lexemes()
    elif args.graph:
        agent.show_graph()
    elif args.demo:
        demo(agent)
    elif args.query:
        result = agent.analyze(args.query)
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            agent.print_analysis(result)
    else:
        demo(agent)


if __name__ == "__main__":
    main()
