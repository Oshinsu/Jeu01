"""Lightweight GPT-inspired agent used for quests and dialogues."""
from __future__ import annotations

from dataclasses import dataclass
from textwrap import dedent
from typing import Iterable

from . import config


@dataclass
class DialogueTurn:
    speaker: str
    text: str


class QuestAgent:
    """Rules-based agent that emulates GPT driven responses."""

    def __init__(self, persona: str | None = None) -> None:
        self.persona = persona or config.WORLD.gpt_persona

    def build_context(self, state_summary: str, goals: Iterable[str]) -> str:
        goals_block = "\n".join(f"- {goal}" for goal in goals) or "- Explorer"
        return dedent(
            f"""
            Persona: {self.persona}
            Résumé du joueur: {state_summary}
            Objectifs actuels:\n{goals_block}
            """
        ).strip()

    def propose_quest(self, state_summary: str, goals: Iterable[str]) -> DialogueTurn:
        context = self.build_context(state_summary, goals)
        suggestion = (
            "Je recommande de capitaliser sur tes connaissances futures : lance un blog tech"
            " détaillant les innovations qui sortiront prochainement. Prépare un calendrier"
            " éditorial et profite des revenus publicitaires avant la concurrence."
        )
        text = dedent(
            f"""
            {context}

            Proposition : {suggestion}
            Étapes clés :
            1. Planifier trois articles sur des sujets visionnaires.
            2. Utiliser ton réseau scolaire pour promouvoir le blog.
            3. Réinvestir les gains dans de nouvelles opportunités.
            """
        ).strip()
        return DialogueTurn(speaker="R3-Mind", text=text)

    def reactive_dialogue(self, player_input: str, state_summary: str) -> DialogueTurn:
        if "argent" in player_input.lower():
            response = (
                "Diversifie tes investissements : combine immobilier abordable en 2003,"
                " paris sportifs maîtrisés et capital-risque sur les services web naissants."
            )
        elif "ami" in player_input.lower():
            response = (
                "Entretiens tes relations : propose des LAN parties, partage des astuces tech"
                " et construis un réseau qui te suivra dans tes futures entreprises."
            )
        else:
            response = (
                "Continue d'équilibrer études, business et bien-être. Profite de ta seconde"
                " chance pour bâtir un empire tout en restant un lycéen exemplaire."
            )
        text = dedent(
            f"""
            Contexte joueur : {state_summary}
            Réponse : {response}
            """
        ).strip()
        return DialogueTurn(speaker="R3-Mind", text=text)

    def render_turn(self, turn: DialogueTurn) -> None:
        separator = "=" * 12
        print(f"{separator} {turn.speaker} {separator}")
        print(turn.text)


__all__ = ["QuestAgent", "DialogueTurn"]
