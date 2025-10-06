"""Command line interface for Re:2003 prototype."""
from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import Dict

from .actions import ActionResult, available_actions
from .agents import QuestAgent
from .events import EventDeck
from .game_state import GameState
from .serialization import SaveManager


@dataclass
class GameContext:
    state: GameState
    agent: QuestAgent
    actions: Dict[str, callable]
    deck: EventDeck
    saves: SaveManager


def render_dashboard(context: GameContext) -> None:
    state = context.state
    print("\n" + "#" * 60)
    print(f"Re:2003 — {state.current_date.isoformat()}")
    print("-" * 60)
    print(f"Énergie     : {state.player.energy}/100")
    print(f"Stress      : {state.player.stress}/100")
    print(f"Cash        : {state.portfolio.cash:,.0f}€")
    print(f"Réseau      : {state.relationship_summary()}")
    print(f"Quêtes act. : {len(state.quest_log)}")
    if state.journal[-3:]:
        print("\nDerniers événements :")
        for line in state.journal[-3:]:
            print(f"  • {line}")
    print("#" * 60)


def execute_action(context: GameContext, choice: str) -> None:
    state = context.state
    if choice not in context.actions:
        print(f"Action inconnue : {choice}")
        return
    result: ActionResult = context.actions[choice](state)
    print("\nRésultat :")
    print(result.message)
    if result.effects:
        print("Effets:")
        for key, value in result.effects.items():
            print(f"  - {key}: {value:+}")
    due_events = context.deck.draw_due_events(state)
    if due_events:
        print("\nÉvénements débloqués :")
        for evt in due_events:
            print(f"  - {evt.description} — {evt.impact}")
    context.saves.save(state)


def run() -> int:
    state = GameState()
    agent = QuestAgent()
    deck = EventDeck()
    deck.prime_events(state)
    context = GameContext(
        state=state,
        agent=agent,
        actions=available_actions(agent),
        deck=deck,
        saves=SaveManager(),
    )

    print("=" * 60)
    print("Bienvenue dans Re:2003 — Prototype CLI")
    print("Tu es projeté en 2003 avec toutes tes connaissances de 2025. Construis ta légende !")
    print("=" * 60)

    while True:
        render_dashboard(context)
        choices = ", ".join(list(context.actions.keys()) + ["quit"])
        choice = input(f"Actions disponibles [{choices}] : ").strip().lower()
        if choice == "quit":
            print("Sauvegarde automatique effectuée. À bientôt !")
            context.saves.save(context.state)
            break
        execute_action(context, choice)

    return 0


if __name__ == "__main__":
    sys.exit(run())
