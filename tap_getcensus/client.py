"""REST client handling, including CensusStream base class."""

from __future__ import annotations

from typing import Any

from singer_sdk import RESTStream
from singer_sdk.authenticators import BasicAuthenticator


class CensusStream(RESTStream):
    """Census stream class."""

    url_base = "https://app.getcensus.com"
    records_jsonpath = "$.data[*]"

    @property
    def authenticator(self) -> BasicAuthenticator:
        """Get an authenticator object.

        Returns:
            The authenticator instance for this REST stream.
        """
        api_token = self.config["api_token"]

        return BasicAuthenticator.create_for_stream(
            self,
            username="bearer",
            password=api_token,
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        headers["User-Agent"] = f"{self.tap_name}/{self._tap.plugin_version}"
        return headers

    def get_url_params(
        self,
        context: dict | None,
        next_page_token: Any | None,
    ) -> dict[str, Any]:
        """Get URL query parameters.

        Args:
            context: Stream sync context.
            next_page_token: Next offset.

        Returns:
            Mapping of URL query parameters.
        """
        return {
            "order": "asc",
            "page": next_page_token,
            "per_page": 100,
        }
