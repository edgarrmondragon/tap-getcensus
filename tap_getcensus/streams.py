"""Stream type classes for tap-getcensus."""

from __future__ import annotations

from singer_sdk import typing as th

from tap_getcensus.client import CensusStream

__all__ = [
    "Syncs",
    "SyncRuns",
    "Destinations",
    "DestinationObjects",
    "Sources",
    "SourceObjects",
]


class Syncs(CensusStream):
    """Syncs stream."""

    name = "syncs"
    path = "/api/v1/syncs"
    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
            description="The sync's system ID",
        ),
        th.Property(
            "label",
            th.StringType,
            description="The sync's label",
        ),
        th.Property(
            "schedule_frequency",
            th.StringType,
            description="The sync's schedule frequency",
        ),
        th.Property(
            "schedule_day",
            th.IntegerType,
            description="The sync's schedule day",
        ),
        th.Property(
            "schedule_hour",
            th.IntegerType,
            description="The sync's schedule hour",
        ),
        th.Property(
            "schedule_minute",
            th.IntegerType,
            description="The sync's schedule minute",
        ),
        th.Property(
            "created_at",
            th.DateTimeType,
            description="The sync's creation date",
        ),
        th.Property(
            "updated_at",
            th.DateTimeType,
            description="The sync's last updated date",
        ),
        th.Property(
            "operation",
            th.StringType,
            description="The sync's operation type",
        ),
        th.Property(
            "paused",
            th.BooleanType,
            description="Whether the sync is paused",
        ),
        th.Property(
            "status",
            th.StringType,
            description="The sync's status",
        ),
        th.Property(
            "lead_union_insert_to",
            th.StringType,
            description="The sync's lead union insert to",
        ),
        th.Property(
            "trigger_on_dbt_cloud_rebuild",
            th.BooleanType,
            description="Whether the sync is triggered on dbt Cloud rebuild",
        ),
        th.Property(
            "field_behavior",
            th.StringType,
            description="The sync's field behavior type",
        ),
        th.Property(
            "field_normalization",
            th.StringType,
            description="The sync's field normalization type",
        ),
        th.Property(
            "mirror_strategy",
            th.StringType,
            description="The sync's mirror strategy type",
        ),
        # TODO: Add advanced_configuration when Census documentation is updated
        # th.Property(
        #     "advanced_configuration",
        #     th.ObjectType(),
        #     description="The sync's advanced configuration",
        # ),
        th.Property(
            "source_attributes",
            th.ObjectType(
                th.Property(
                    "connection_id",
                    th.IntegerType,
                    description="The sync's source connection ID",
                ),
                th.Property(
                    "object",
                    th.ObjectType(
                        th.Property(
                            "type",
                            th.StringType,
                            description="The sync's source object type",
                        ),
                        th.Property(
                            "id",
                            th.IntegerType,
                            description="The sync's source object ID",
                        ),
                        th.Property(
                            "name",
                            th.StringType,
                            description="The sync's source object name",
                        ),
                        th.Property(
                            "created_at",
                            th.DateTimeType,
                            description="The sync's source object creation date",
                        ),
                        th.Property(
                            "updated_at",
                            th.DateTimeType,
                            description="The sync's source object last updated date",
                        ),
                        th.Property(
                            "query",
                            th.StringType,
                            description="The sync's source object query",
                        ),
                    ),
                    description="The sync's source object",
                ),
            ),
            description="The sync's source attributes",
        ),
        th.Property(
            "destination_attributes",
            th.ObjectType(
                th.Property(
                    "connection_id",
                    th.IntegerType,
                    description="The sync's destination connection ID",
                ),
                th.Property(
                    "object",
                    th.StringType,
                    description="The sync's destination object",
                ),
            ),
            description="The sync's destination attributes",
        ),
        th.Property(
            "mappings",
            th.ArrayType(
                th.ObjectType(
                    th.Property(
                        "from",
                        th.ObjectType(
                            th.Property(
                                "type",
                                th.StringType,
                                description="The sync's mapping from type",
                            ),
                            th.Property(
                                "email",
                                th.StringType,
                                description="The sync's mapping from email",
                            ),
                        ),
                        description="The sync's mapping from",
                    ),
                    th.Property(
                        "to",
                        th.StringType,
                        description="The sync's mapping to",
                    ),
                    th.Property(
                        "is_primary_identifier",
                        th.BooleanType,
                        description="Whether the sync's mapping is primary identifier",
                    ),
                    th.Property(
                        "generate_field",
                        th.BooleanType,
                        description="Whether the sync's mapping generates field",
                    ),
                    th.Property(
                        "preserve_values",
                        th.BooleanType,
                        description="Whether the sync's mapping preserves values",
                    ),
                    th.Property(
                        "operation",
                        th.StringType,
                        description="The sync's mapping operation type",
                    ),
                ),
            ),
        ),
    ).to_dict()

    def get_child_context(self, record: dict, context: dict | None) -> dict:
        """Get child context.

        Args:
            record: The record.
            context: The context.

        Returns:
            The child context.
        """
        return {"sync_id": record["id"]}


class SyncRuns(CensusStream):
    """Sync runs stream."""

    name = "sync_runs"
    path = "/api/v1/syncs/{sync_id}/sync_runs"
    primary_keys = ["id"]
    replication_key = "updated_at"
    parent_stream_type = Syncs

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
            description="The sync run's system ID",
        ),
        th.Property(
            "sync_id",
            th.IntegerType,
            description="The sync run's sync ID",
        ),
        th.Property(
            "source_record_count",
            th.IntegerType,
            description="The sync run's source record count",
        ),
        th.Property(
            "records_processed",
            th.IntegerType,
            description="The count of records processed",
        ),
        th.Property(
            "records_updated",
            th.IntegerType,
            description="The count of records updated",
        ),
        th.Property(
            "records_failed",
            th.IntegerType,
            description="The count of records failed",
        ),
        th.Property(
            "records_invalid",
            th.IntegerType,
            description="The count of records invalid",
        ),
        th.Property(
            "created_at",
            th.DateTimeType,
            description="The sync run's creation date",
        ),
        th.Property(
            "updated_at",
            th.DateTimeType,
            description="The sync run's last updated date",
        ),
        th.Property(
            "completed_at",
            th.DateTimeType,
            description="The sync run's completion date",
        ),
        th.Property(
            "scheduled_execution_time",
            th.DateTimeType,
            description="The sync run's scheduled execution time",
        ),
        th.Property(
            "error_code",
            th.IntegerType,
            description="The sync run's error code",
        ),
        th.Property(
            "error_message",
            th.StringType,
            description="The sync run's error message",
        ),
        th.Property(
            "error_detail",
            th.StringType,
            description="The sync run's error detail",
        ),
        th.Property(
            "status",
            th.StringType,
            description="The sync run's status",
        ),
        th.Property(
            "canceled",
            th.BooleanType,
            description="Whether the sync run is canceled",
        ),
        th.Property(
            "full_sync",
            th.BooleanType,
            description="Whether the sync run is a full sync",
        ),
        th.Property(
            "sync_trigger_reason",
            th.ObjectType(additional_properties=th.StringType),
            description="The sync run's sync trigger reason",
        ),
    ).to_dict()


class Destinations(CensusStream):
    """Destinations stream."""

    name = "destinations"
    path = "/api/v1/destinations"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
            description="The destination's system ID",
        ),
        th.Property(
            "name",
            th.StringType,
            description="The destination's name",
        ),
        th.Property(
            "type",
            th.StringType,
            description="The destination's type",
        ),
        th.Property(
            "connection_details",
            th.ObjectType(),
            description="The destination's connection details",
        ),
    ).to_dict()

    def get_child_context(self, record: dict, context: dict | None) -> dict:
        """Get child context.

        Args:
            record: The record.
            context: The context.

        Returns:
            The child context.
        """
        return {"destination_id": record["id"]}


class DestinationObjects(CensusStream):
    """Destination objects stream."""

    name = "destination_objects"
    path = "/api/v1/destinations/{destination_id}/objects"
    primary_keys = ["full_name"]
    replication_key = None
    parent_stream_type = Destinations

    schema = th.PropertiesList(
        th.Property(
            "destination_id",
            th.IntegerType,
            description="The destination's system ID",
        ),
        th.Property(
            "label",
            th.StringType,
            description="The destination object's label",
        ),
        th.Property(
            "full_name",
            th.StringType,
            description="The destination object's full name",
        ),
        th.Property(
            "allow_custom_fields",
            th.BooleanType,
            description="Whether the destination object allows custom fields",
        ),
        th.Property(
            "allow_case_sensitive_field_names",
            th.BooleanType,
            description=(
                "Whether the destination object allows case sensitive field names"
            ),
        ),
        th.Property(
            "configurable_field_definitions",
            th.ObjectType(),
            description="The destination object's configurable field definitions",
        ),
        th.Property(
            "fields",
            th.ArrayType(
                th.ObjectType(
                    th.Property(
                        "label",
                        th.StringType,
                        description="The field's label",
                    ),
                    th.Property(
                        "full_name",
                        th.StringType,
                        description="The field's full name",
                    ),
                    th.Property(
                        "creatable",
                        th.BooleanType,
                        description=("Whether the field is creatable"),
                    ),
                    th.Property(
                        "updatable",
                        th.BooleanType,
                        description=("Whether the field is updatable"),
                    ),
                    th.Property(
                        "operations",
                        th.ArrayType(th.StringType),
                        description="The field's operations",
                    ),
                    th.Property(
                        "array",
                        th.BooleanType,
                        description="Whether the field is an array",
                    ),
                    th.Property(
                        "preserve_values_supported",
                        th.BooleanType,
                        description="Whether the field supports preserving values",
                    ),
                    th.Property(
                        "required_for_mapping",
                        th.BooleanType,
                        description="Whether the field is required for mapping",
                    ),
                    th.Property(
                        "can_be_upsert_key",
                        th.BooleanType,
                        description="Whether the field can be an upsert key",
                    ),
                    th.Property(
                        "can_be_update_key",
                        th.BooleanType,
                        description="Whether the field can be an update key",
                    ),
                    th.Property(
                        "can_be_insert_key",
                        th.BooleanType,
                        description="Whether the field can be an insert key",
                    ),
                    th.Property(
                        "can_be_reference_key",
                        th.BooleanType,
                        description="Whether the field can be a reference key",
                    ),
                    th.Property(
                        "lookup_object",
                        th.StringType,
                        description="The field's lookup object",
                    ),
                    th.Property(
                        "type",
                        th.StringType,
                        description="The field's type",
                    ),
                ),
            ),
            description="The destination object's fields",
        ),
    ).to_dict()


class Sources(CensusStream):
    """Sources stream."""

    name = "sources"
    path = "/api/v1/sources"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
            description="The source's system ID",
        ),
        th.Property(
            "name",
            th.StringType,
            description="The source's name",
        ),
        th.Property(
            "label",
            th.StringType,
            description="The source's label",
        ),
        th.Property(
            "type",
            th.StringType,
            description="The source's type",
        ),
        th.Property(
            "last_test_succeeded",
            th.BooleanType,
            description="Whether the last test succeeded",
        ),
        th.Property(
            "last_tested_at",
            th.DateTimeType,
            description="The last test's timestamp",
        ),
        th.Property(
            "connection_details",
            th.ObjectType(),
            description="The destination's connection details",
        ),
        th.Property(
            "read_only_connection",
            th.BooleanType,
            description="Whether the source is read-only",
        ),
    ).to_dict()

    def get_child_context(self, record: dict, context: dict | None) -> dict:
        """Get child context.

        Args:
            record: The record.
            context: The context.

        Returns:
            The child context.
        """
        return {"source_id": record["id"]}


class SourceObjects(CensusStream):
    """Source objects stream."""

    name = "source_objects"
    path = "/api/v1/sources/{source_id}/objects"
    primary_keys = ["id"]
    replication_key = None
    parent_stream_type = Sources

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
            description="The source object's ID",
        ),
        th.Property(
            "source_object_id",
            th.IntegerType,
            description="The source object's ID",
        ),
        th.Property(
            "source_id",
            th.IntegerType,
            description="The source object's source ID",
        ),
        th.Property(
            "columns",
            th.ArrayType(
                th.ObjectType(
                    th.Property(
                        "name",
                        th.StringType,
                        description="The column's name",
                    ),
                    th.Property(
                        "type",
                        th.StringType,
                        description="The column's type",
                    ),
                ),
            ),
            description="The source object's columns",
        ),
        th.Property(
            "name",
            th.StringType,
            description="The source object's name",
        ),
        th.Property(
            "description",
            th.StringType,
            description="The source object's description",
        ),
        th.Property(
            "approved",
            th.BooleanType,
            description="Whether the source object is approved",
        ),
        th.Property(
            "type",
            th.StringType,
            description="The source object's type",
        ),
        th.Property(
            "table_catalog",
            th.StringType,
            description="The source object's table catalog",
        ),
        th.Property(
            "table_schema",
            th.StringType,
            description="The source object's table schema",
        ),
        th.Property(
            "table_name",
            th.StringType,
            description="The source object's table name",
        ),
        th.Property(
            "created_at",
            th.DateTimeType,
            description="The source object's creation timestamp",
        ),
        th.Property(
            "updated_at",
            th.DateTimeType,
            description="The source object's update timestamp",
        ),
        th.Property(
            "query",
            th.StringType,
            description="The source object's query",
        ),
    ).to_dict()
