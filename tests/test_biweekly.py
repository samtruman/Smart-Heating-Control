"""Tests for alternating schedule weeks."""

from datetime import date

from tests.pure import biweekly


def test_week_start_is_monday() -> None:
    assert biweekly.week_start(date(2026, 11, 25)) == date(2026, 11, 23)


def test_current_week_is_week_one() -> None:
    anchor = date(2026, 11, 25)
    assert biweekly.week_number(anchor, date(2026, 11, 25)) == 1
    assert biweekly.week_number(anchor, date(2026, 11, 30)) == 2
    assert biweekly.week_number(anchor, date(2026, 12, 7)) == 1


def test_dates_before_anchor_alternate_too() -> None:
    anchor = date(2026, 11, 23)
    assert biweekly.week_number(anchor, date(2026, 11, 16)) == 2
    assert biweekly.week_number(anchor, date(2026, 11, 9)) == 1
