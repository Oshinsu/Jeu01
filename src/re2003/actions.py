"""Domain actions that drive the simulation."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict

from .agents import QuestAgent
from .game_state import GameState


@dataclass
class ActionResult:
    message: str
    effects: Dict[str, float]


Action = Callable[[GameState], ActionResult]


def study_for_exam(state: GameState) -> ActionResult:
    state.player.study()
    state.advance_day()
    message = "Tu révises intensément les sujets clés de 2005 et prends une longueur d'avance."
    return ActionResult(message=message, effects={"knowledge": +3, "stress": +4})


def launch_startup(state: GameState) -> ActionResult:
    investment = 1500
    if state.portfolio.cash < investment:
        return ActionResult("Tu manques de liquidités pour lancer cette start-up.", effects={})
    state.portfolio.adjust_cash(-investment)
    company_name = f"Skylink Labs {len(state.portfolio.businesses) + 1}"
    state.portfolio.businesses.append(
        Business(name=company_name, capital=investment, revenue_per_week=420, expenses_per_week=120)
    )
    state.player.reputation = min(100, state.player.reputation + 6)
    state.player.stress = min(100, state.player.stress + 5)
    state.advance_day()
    message = (
        f"Tu immatricules {company_name} en utilisant tes connaissances du Web 2.0,"
        " prêt à capturer le marché avant l'heure."
    )
    return ActionResult(message=message, effects={"cash": -investment, "reputation": +6})


def day_trading(state: GameState) -> ActionResult:
    stake = min(1000, state.portfolio.cash * 0.1)
    if stake <= 0:
        return ActionResult("Impossible de trader sans capital disponible.", effects={})
    state.portfolio.adjust_cash(-stake)
    gain = stake * 0.35  # leveraging future knowledge
    state.portfolio.adjust_cash(stake + gain)
    state.player.stress = min(100, state.player.stress + 3)
    state.advance_day()
    return ActionResult(
        message="Tu profites d'informations sur les prochains succès boursiers et réalises un coup d'éclat.",
        effects={"cash": gain, "stress": +3},
    )


def host_lan_party(state: GameState) -> ActionResult:
    cost = 120
    state.portfolio.adjust_cash(-cost)
    for rel in state.relationships.values():
        if "gamer" in rel.tags:
            rel.adjust(+8)
        else:
            rel.adjust(+2)
    state.player.energy = max(0, state.player.energy - 8)
    state.player.reputation = min(100, state.player.reputation + 5)
    state.advance_day()
    return ActionResult(
        message="La LAN party rassemble tout le lycée et renforce ton aura d'innovateur.",
        effects={"cash": -cost, "reputation": +5},
    )


def mentor_session(state: GameState, agent: QuestAgent | None = None) -> ActionResult:
    agent = agent or QuestAgent()
    turn = agent.propose_quest(state.snapshot(), state.quest_log[-3:])
    state.register_quest(turn.text.split("Proposition : ")[-1].split("\n")[0])
    return ActionResult(message=turn.text, effects={})


def available_actions(agent: QuestAgent | None = None) -> Dict[str, Callable[[GameState], ActionResult]]:
    agent = agent or QuestAgent()
    return {
        "study": study_for_exam,
        "startup": launch_startup,
        "trade": day_trading,
        "lan": host_lan_party,
        "mentor": lambda state: mentor_session(state, agent=agent),
    }


from .game_state import Business  # placed at end to avoid circular import

__all__ = [
    "Action",
    "ActionResult",
    "available_actions",
    "study_for_exam",
    "launch_startup",
    "day_trading",
    "host_lan_party",
    "mentor_session",
]
