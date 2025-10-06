from __future__ import annotations

from re2003.actions import available_actions
from re2003.game_state import GameState


def test_study_increases_knowledge_and_advances_time():
    state = GameState()
    actions = available_actions()
    baseline_date = state.current_date
    result = actions["study"](state)
    assert state.player.knowledge_level >= 93
    assert state.current_date > baseline_date
    assert "knowledge" in result.effects


def test_mentor_session_records_quest():
    state = GameState()
    actions = available_actions()
    result = actions["mentor"](state)
    assert state.quest_log, "Quest log should contain at least one quest"
    assert "Proposition" in result.message
