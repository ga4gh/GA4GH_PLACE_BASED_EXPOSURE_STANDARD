"""Data model package for exposure-linkage."""

from pathlib import Path
from .exposure_linkage import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "exposure_linkage.yaml"
