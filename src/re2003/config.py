"""Global configuration for the Re:2003 prototype."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class WorldConfig:
    """Immutable configuration describing the simulation timeline."""

    start_date: date = date(2003, 9, 1)
    end_date: date = date(2004, 7, 1)
    start_capital: int = 10_000
    gpt_persona: str = (
        "Tu es R3-Mind, un mentor IA qui aide l'étudiant réincarné à tirer parti de ses"
        " connaissances de 2025. Reste positif, stratégique et cohérent avec le contexte"
        " de 2003."
    )


WORLD = WorldConfig()
