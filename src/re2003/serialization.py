"""Save and load utilities."""
from __future__ import annotations

import json
from dataclasses import asdict
from datetime import date
from pathlib import Path
from typing import Any, Dict

from .game_state import GameState


class SaveManager:
    def __init__(self, directory: str | Path = "saves") -> None:
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)

    def save(self, state: GameState, name: str = "autosave") -> Path:
        payload = asdict(state)
        path = self.directory / f"{name}.json"
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
        return path

    def load(self, name: str = "autosave") -> GameState:
        path = self.directory / f"{name}.json"
        data: Dict[str, Any] = json.loads(path.read_text())
        state = GameState()
        state.current_date = date.fromisoformat(data["current_date"])
        state.portfolio.cash = data["portfolio"]["cash"]
        state.quest_log = list(data.get("quest_log", []))
        state.journal = list(data.get("journal", []))
        return state


__all__ = ["SaveManager"]
