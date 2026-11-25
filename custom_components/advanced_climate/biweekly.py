"""Helpers for the optional alternating two-week schedule."""

from __future__ import annotations

from datetime import date, timedelta
from typing import Any


def week_start(day: date) -> date:
    """Return the Monday containing ``day``."""
    return day - timedelta(days=day.weekday())


def week_number(anchor: date, day: date) -> int:
    """Return the 1-based alternating week number for ``day``.

    ``anchor`` is the Monday that was current when rotation was enabled and is
    therefore Week 1. Dates before it are handled symmetrically.
    """
    anchor = week_start(anchor)
    current = week_start(day)
    return 1 if ((current - anchor).days // 7) % 2 == 0 else 2


def rotation_week(rotation: dict[str, Any] | None, day: date) -> int | None:
    """Return the active rotation week, or ``None`` for a normal schedule."""
    if not isinstance(rotation, dict) or not rotation.get("enabled"):
        return None
    try:
        anchor = date.fromisoformat(str(rotation["anchor"]))
    except (KeyError, TypeError, ValueError):
        return None
    return week_number(anchor, day)

