<div align="center">

# tap-getcensus

<div>
  <a href="https://results.pre-commit.ci/latest/github/edgarrmondragon/tap-getcensus/main">
    <img alt="pre-commit.ci status" src="https://results.pre-commit.ci/badge/github/edgarrmondragon/tap-getcensus/main.svg"/>
  </a>
  <a href="https://github.com/edgarrmondragon/tap-getcensus/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/edgarrmondragon/tap-getcensus"/>
  </a>
</div>

Singer Tap for the [Census Operational Analytics Platform](https://www.getcensus.com/). Built with the [Meltano Singer SDK](https://sdk.meltano.com).

</div>

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`

## Settings

| Setting             | Required | Default | Description |
|:--------------------|:--------:|:-------:|:------------|
| api_token           | True     | None    | Auth token for getcensus.com API |
| stream_maps         | False    | None    | Config object for stream maps capability. |
| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. |
| flattening_enabled  | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth| False    | None    | The max depth to flatten schemas. |

A full list of supported settings and capabilities is available by running: `tap-getcensus --about`

## Streams

| Stream                | Replication Method | Replication Key | Primary Key | Documentation |
|:----------------------|:------------------:|:---------------:|:-----------:|:-------------:|
| `syncs`               | Full Table         | None            | id          | https://docs.getcensus.com/basics/api/syncs#get-syncs |
| `sync_runs`           | Full Table         | None            | id          | https://docs.getcensus.com/basics/api/sync-runs#get-syncs-id-sync_runs |
| `destinations`        | Full Table         | None            | id          | https://docs.getcensus.com/basics/api/destinations#get-destinations |
| `destination_objects` | Full Table         | None            | id          | https://docs.getcensus.com/basics/api/destination-objects#get-destinations-id-objects |
| `sources`             | Full Table         | None            | id          | https://docs.getcensus.com/basics/api/sources#get-sources |
| `source_objects`      | Full Table         | None            | id          | https://docs.getcensus.com/basics/api/source-objects#get-sources-id-objects |

The full catalog is available by running: `tap-getcensus --discover`

### Source Authentication and Authorization

See the [API docs](https://docs.getcensus.com/basics/api#getting-api-access).

## Usage

You can easily run `tap-getcensus` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-getcensus --version
tap-getcensus --help
tap-getcensus --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and then run:

```bash
poetry run pytest
```

You can also test the `tap-getcensus` CLI interface directly using `poetry run`:

```bash
poetry run tap-getcensus --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano

# Update all plugin definitions
meltano lock --update --all

# Initialize meltano within this directory
cd tap-getcensus
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-getcensus --version

# OR run a pipeline:
meltano run tap-getcensus target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
