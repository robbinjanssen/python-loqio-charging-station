"""Charge Point model."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from .charge_session import ChargeSession

if TYPE_CHECKING:
    from datetime import datetime


@dataclass
class ChargePoint:
    """Object representing a Charge Point model response from the API."""

    charge_point_id: int
    name: str
    power_instruction: int
    active_power: float
    power_minimum: float
    power_minimum_default: float
    session: ChargeSession
    phase_usage_capability: int
    current_minimum_capability: float
    current_maximum_capability: float
    energy_charge_target: int
    energy_charge_target_default: int
    charge_strategy: int
    charge_strategy_default: int
    departure_time: datetime
    energy_charged: int
    measured_vs_instructed_current_ratio: float
    username: str
    claimed: bool

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> ChargePoint:
        """Return a new Charge Point instance based on the given JSON.

        Args:
        ----
            data: The JSON data from the API.

        Returns:
        -------
            A Charge Point Object.
        """
        session = ChargeSession.from_json(data)

        return cls(
            charge_point_id=data["id"],
            name=f'{data["humanUsablePrimaryIdentifier"]} - {data["humanUsableSecondaryIdentifier"]}',  # noqa: E501
            username=data["variables"]["username"]["value"],
            claimed=data["variables"]["isClaimed"]["value"],
            active_power=data["variables"]["activePower"]["value"],
            power_instruction=data["variables"]["powerInstruction"]["value"],
            power_minimum=data["variables"]["powerMinimum"]["value"],
            power_minimum_default=data["variables"]["powerMinimumDefault"]["value"],
            session=session,
            phase_usage_capability=data["variables"]["phaseUsageCapability"]["value"],
            current_minimum_capability=data["variables"]["currentMinimumCapability"][
                "value"
            ],
            current_maximum_capability=data["variables"]["currentMaximumCapability"][
                "value"
            ],
            energy_charge_target=data["variables"]["energyChargeTarget"]["value"],
            energy_charge_target_default=data["variables"]["energyChargeTargetDefault"][
                "value"
            ],
            charge_strategy=data["variables"]["chargeStrategy"]["value"],
            charge_strategy_default=data["variables"]["chargeStrategyDefault"]["value"],
            departure_time=data["variables"]["departureTime"]["value"],
            energy_charged=data["variables"]["energyCharged"]["value"] * 1000,
            measured_vs_instructed_current_ratio=data["variables"][
                "measuredVersusInstructedCurrentRatio"
            ]["value"],
        )


# def parse_date(value: str, offset: int) -> datetime:
#     """
#     Parse a given value and offset into a datetime object.

#     Args:
#         value: The date time string.
#         offset: The time zone offset in seconds.

#     Returns:
#         The parsed datetime.
#     """
