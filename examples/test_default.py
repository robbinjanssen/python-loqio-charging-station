# pylint: disable=redefined-outer-name,too-many-statements
"""Asynchronous Python client for OJ Microline Thermostat."""
import asyncio

from loqio_charging_station import Loqio


async def main() -> None:
    """Show example on using the Loqio client."""
    async with Loqio(
        scheme="http",
        host="xxx",
        port=12354,
        api_token="xxx",
    ) as client:
        # fmt: off
        thermostats = await client.get_charge_points()
        for resource in thermostats:
            print("####################")
            print(f"# {resource.name}")
            print("####################")
            print("- Details:")
            print(f"   ID: {resource.charge_point_id}")
            print(f"   Username: {resource.username}")
            print(f"   Claimed: {resource.claimed}")
            print(f"   Active Power: {resource.active_power}")
            print(f"   Power Instruction: {resource.power_instruction}")
            print(f"   Power Minimum: {resource.power_minimum}")
            print(f"   Power Minimum Default: {resource.power_minimum_default}")
            print(f"   Phase Usage Capability: {resource.phase_usage_capability}")
            print(f"   Current Minimum Capability: {resource.current_minimum_capability}")
            print(f"   Current Maximum Capability: {resource.current_maximum_capability}")
            print(f"   Energy Charge Target: {resource.energy_charge_target}")
            print(f"   Energy Charge Target Default: {resource.energy_charge_target_default}")
            print(f"   Charge Strategy: {resource.charge_strategy}")
            print(f"   Charge Strategy Default: {resource.charge_strategy_default}")
            print(f"   Departure Time: {resource.departure_time}")
            print(f"   Energy Charged: {resource.energy_charged}")
            print(f"   Measured vs Instructed Current Ratio: {resource.measured_vs_instructed_current_ratio}")
            print(f"   Departure Time: {resource.departure_time}")
        # fmt: on


if __name__ == "__main__":
    asyncio.run(main())
