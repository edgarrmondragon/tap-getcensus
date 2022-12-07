"""Census tap class."""

from __future__ import annotations

from singer_sdk import Stream, Tap
from singer_sdk import typing as th
from singer_sdk.streams import RESTStream

from tap_getcensus.streams import (
    DestinationObjects,
    Destinations,
    SourceObjects,
    Sources,
    SyncRuns,
    Syncs,
)

__all__ = ["TapCensus"]

STREAM_TYPES: list[type[RESTStream]] = [
    Syncs,
    SyncRuns,
    Destinations,
    DestinationObjects,
    Sources,
    SourceObjects,
]


class TapCensus(Tap):
    """Singer tap for Census."""

    name = "tap-getcensus"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_token",
            th.StringType,
            required=True,
            description="Auth token for getcensus.com API",
        ),
    ).to_dict()

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of Census streams.
        """
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
