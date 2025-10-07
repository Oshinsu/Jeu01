"""Game state primitives for Re:2003."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List

from .config import WORLD


@dataclass
class Relationship:
    name: str
    affinity: int = 50
    tags: List[str] = field(default_factory=list)

    def adjust(self, delta: int) -> None:
        self.affinity = max(0, min(100, self.affinity + delta))


@dataclass
class Business:
    name: str
    capital: float
    revenue_per_week: float
    expenses_per_week: float

    def settle_week(self) -> float:
        profit = self.revenue_per_week - self.expenses_per_week
        self.capital += profit
        return profit


@dataclass
class Portfolio:
    cash: float = float(WORLD.start_capital)
    holdings: Dict[str, float] = field(default_factory=dict)
    businesses: List[Business] = field(default_factory=list)

    def net_worth(self) -> float:
        return self.cash + sum(self.holdings.values()) + sum(b.capital for b in self.businesses)

    def adjust_cash(self, delta: float) -> None:
        self.cash = max(0.0, self.cash + delta)


@dataclass
class Player:
    name: str
    knowledge_level: int = 90
    energy: int = 80
    reputation: int = 40
    stress: int = 20
    focus: int = 70

    def apply_day(self, energy_delta: int = -5, stress_delta: int = 2) -> None:
        self.energy = max(0, min(100, self.energy + energy_delta))
        self.stress = max(0, min(100, self.stress + stress_delta))

    def study(self) -> None:
        self.focus = min(100, self.focus + 5)
        self.knowledge_level = min(100, self.knowledge_level + 3)
        self.stress = min(100, self.stress + 4)

    def rest(self) -> None:
        self.energy = min(100, self.energy + 12)
        self.stress = max(0, self.stress - 6)

    def socialize(self) -> None:
        self.reputation = min(100, self.reputation + 4)
        self.stress = max(0, self.stress - 3)
        self.energy = max(0, self.energy - 2)


@dataclass
class GameState:
    current_date: date = WORLD.start_date
    player: Player = field(default_factory=lambda: Player(name="Alex"))
    portfolio: Portfolio = field(default_factory=Portfolio)
    relationships: Dict[str, Relationship] = field(
        default_factory=lambda: {
            "Emma": Relationship(name="Emma", affinity=60, tags=["ami", "gamer"]),
            "Prof. Martin": Relationship(name="Prof. Martin", affinity=45, tags=["professeur", "maths"]),
            "Léo": Relationship(name="Léo", affinity=35, tags=["entrepreneur"]),
        }
    )
    quest_log: List[str] = field(default_factory=list)
    journal: List[str] = field(default_factory=list)

    def advance_day(self, days: int = 1) -> None:
        self.current_date = date.fromordinal(self.current_date.toordinal() + days)
        self.player.apply_day()
        if self.current_date.weekday() == 6:  # settle weekly every Sunday
            self.settle_weekly_business()

    def settle_weekly_business(self) -> None:
        for business in self.portfolio.businesses:
            profit = business.settle_week()
            self.portfolio.adjust_cash(profit)
            self.journal.append(
                f"{self.current_date.isoformat()} : {business.name} génère {profit:.0f}€ de profit cumulatif."
            )

    def register_quest(self, quest: str) -> None:
        self.quest_log.append(quest)
        self.journal.append(f"{self.current_date.isoformat()} : Nouvelle quête - {quest}")

    def snapshot(self) -> str:
        return (
            f"Date: {self.current_date.isoformat()} | Énergie: {self.player.energy}/100 | "
            f"Cash: {self.portfolio.cash:.0f}€ | Réputation: {self.player.reputation}/100 | "
            f"Stress: {self.player.stress}/100"
        )

    def relationship_summary(self) -> str:
        return ", ".join(f"{rel.name}:{rel.affinity}" for rel in self.relationships.values())


__all__ = [
    "Relationship",
    "Business",
    "Portfolio",
    "Player",
    "GameState",
]
