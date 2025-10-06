"""Procedural events triggered as the timeline advances."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from random import Random
from typing import Iterable, List

from .game_state import GameState


@dataclass
class TimelineEvent:
    date: date
    description: str
    impact: str


class EventDeck:
    """Deterministic event generator based on seed for reproducibility."""

    def __init__(self, seed: int = 2003) -> None:
        self.random = Random(seed)
        self.future_events: List[TimelineEvent] = []

    def prime_events(self, state: GameState) -> None:
        anchors = [
            (9, 22, "Lancement de Steam en France", "Opportunité d'investir dans le digital."),
            (11, 18, "Sortie de Call of Duty", "Organisation de tournois e-sport."),
            (2, 4, "Facebook en bêta", "Prépare un réseau social local."),
        ]
        year = state.current_date.year
        events = [
            TimelineEvent(date=date(year, month, day), description=desc, impact=impact)
            for month, day, desc, impact in anchors
        ]
        self.random.shuffle(events)
        self.future_events = events

    def draw_due_events(self, state: GameState) -> List[TimelineEvent]:
        due = [evt for evt in self.future_events if evt.date <= state.current_date]
        self.future_events = [evt for evt in self.future_events if evt.date > state.current_date]
        for evt in due:
            state.journal.append(f"{evt.date.isoformat()} : {evt.description} — {evt.impact}")
        return due


__all__ = ["TimelineEvent", "EventDeck"]
