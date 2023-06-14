# pylint: disable=too-many-arguments
"""Asynchronous Python client communicating with the Loqio Charging Station API."""
from __future__ import annotations

import asyncio
import json
import socket
from dataclasses import dataclass
from typing import Any

import async_timeout
from aiohttp import ClientError, ClientSession, hdrs
from yarl import URL

from .exceptions import (
    LoqioConnectionError,
    LoqioError,
    LoqioTimeoutError,
)
from .models import ChargePoint


@dataclass
class Loqio:
    """Main class for handling data from Loqio Charging Station API."""

    __host: str
    __api_token: str
    __port: int = 443
    __scheme: str = "https"
    __ssl: bool = True

    __request_timeout: float = 30.0
    __http_session: ClientSession | None = None
    __close_http_session: bool = False

    def __init__(  # noqa: PLR0913
        self,
        host: str,
        api_token: str,
        port: int = 443,
        session: ClientSession | None = None,
        scheme: str = "https",
        ssl: bool = True,  # noqa: FBT001, FBT002
    ) -> None:
        """Create a new Loqio instance.

        Args:
        ----
            host: The HOST (without protocol) to use for API requests.
            api_token: The API key to use in requests.
            session: The session to use, or a new session will be created.
        """
        self.__host = host
        self.__api_token = api_token
        self.__port = port
        self.__scheme = scheme
        self.__ssl = ssl
        self.__http_session = session

    async def _request(
        self,
        uri: str,
        *,
        method: str = hdrs.METH_GET,
        params: dict[str, Any] | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Handle a request to the Loqio Charging API.

        Args:
        ----
            uri: Request URI, without '/', for example, 'status'
            method: HTTP method to use, for example, 'GET'
            params: Extra options to improve or limit the response.
            body: Data can be used in a POST and PATCH request.

        Returns:
        -------
            A Python dictionary (text) with the response from
            the API.

        Raises:
        ------
            LoqioTimeoutError: A timeout occurred.
            LoqioConnectionError: An error occurred.
            LoqioError: Received an unexpected response from the API.
        """
        try:
            if self.__http_session is None:
                self.__http_session = ClientSession()
                self.__close_http_session = True

            url = URL.build(
                scheme=self.__scheme,
                host=self.__host,
                port=self.__port,
                path="/",
            ).join(URL(uri))

            async with async_timeout.timeout(self.__request_timeout):
                response = await self.__http_session.request(
                    method,
                    url,
                    params=params,
                    headers={
                        "Content-Type": "application/json; charset=utf-8",
                        "Authorization": f"Bearer {self.__api_token}",
                    },
                    json=body,
                    ssl=self.__ssl,
                )
                response.raise_for_status()
        except asyncio.TimeoutError as exception:
            msg = "Timeout occurred while connecting to the Loqio API."
            raise LoqioTimeoutError(
                msg,
            ) from exception
        except (ClientError, socket.gaierror) as exception:
            msg = "Error occurred while communicating with the Loqio API."
            raise LoqioConnectionError(
                msg,
            ) from exception

        content_type = response.headers.get("Content-Type", "")
        if not any(item in content_type for item in ["application/json"]):
            text = await response.text()
            msg = "Unexpected content type response from the Loqio API"
            raise LoqioError(
                msg,
                {"Content-Type": content_type, "response": text},
            )

        return json.loads(await response.text())

    async def get_charge_points(self) -> list[ChargePoint]:
        """Get all the charge points.

        Returns
        -------
            A list of ChargePoint objects.

        Raises
        ------
            LoqioResultsError: An error occurred while getting thermostats.
        """
        results: list[ChargePoint] = []
        data = await self._request(
            "hook/api/objectdata-alt?model=ChargePointResourceModel",
            method=hdrs.METH_GET,
        )

        for item in data:
            results.append(ChargePoint.from_json(item))

        return results

    async def close(self) -> None:
        """Close open client session."""
        if self.__http_session and self.__close_http_session:
            self.__close_http_session = False
            await self.__http_session.close()

    async def __aenter__(self) -> Loqio:
        """Async enter.

        Returns
        -------
            The API object.
        """
        return self

    async def __aexit__(self, *_exc_info: str) -> None:
        """Async exit.

        Args:
        ----
            _exc_info: Exec type.
        """
        await self.close()
