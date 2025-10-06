"""Calendar utilities for the simulation."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

from .config import WORLD


@dataclass
class Timekeeper:
    current_date: date = WORLD.start_date

    def advance(self, days: int = 1) -> date:
        self.current_date += timedelta(days=days)
        return self.current_date

    def rewind(self, days: int = 1) -> date:
        self.current_date -= timedelta(days=days)
        return self.current_date

    def until_graduation(self) -> int:
        return (WORLD.end_date - self.current_date).days


__all__ = ["Timekeeper"]
