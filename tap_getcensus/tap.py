"""Census tap class."""

from __future__ import annotations

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_getcensus import streams

__all__ = ["TapCensus"]


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
        return [
            streams.Syncs(tap=self),
            streams.SyncRuns(tap=self),
            streams.Destinations(tap=self),
            streams.DestinationObjects(tap=self),
            streams.Sources(tap=self),
            streams.SourceObjects(tap=self),
        ]
