"""Charge Session model."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from datetime import datetime


@dataclass
class ChargeSession:
    """Object representing a Charge Session model response from the API."""

    session_id: int
    status: int
    start_time: datetime
    end_time: datetime
    duration_default: int

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> ChargeSession:
        """Return a new Charge Session instance based on the given JSON.

        Args:
        ----
            data: The JSON data from the API.

        Returns:
        -------
            A Charge Session Object.
        """
        return cls(
            session_id=data["variables"]["sessionId"]["value"],
            status=data["variables"]["sessionStatus"]["value"],
            start_time=data["variables"]["sessionStartTime"]["value"],
            end_time=data["variables"]["sessionEndTime"]["value"],
            duration_default=data["variables"]["sessionDurationDefault"]["value"],
        )
