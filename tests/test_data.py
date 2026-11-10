"""Conformance tests: every valid example must pass, every invalid example must fail.

Invalid examples declare the error they are meant to trigger in a header line,
``# expected_error: <substring>``. The test checks that this error is among the
reported ones, so an example cannot pass by failing for an unrelated reason.

Examples under ``data/problem/invalid`` document rules the schema states but the
generated JSON Schema does not yet enforce. They are strict xfails: once the
rule is enforced the test fails, and the example should move to ``data/invalid``.
"""

import re
from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.loaders import yaml_loader

import exposure_linkage.datamodel.exposure_linkage as datamodel

DATA_DIR = Path(__file__).parent / "data"
SCHEMA = (
    Path(__file__).parent.parent
    / "src"
    / "exposure_linkage"
    / "schema"
    / "exposure_linkage.yaml"
)

VALID_EXAMPLE_FILES = sorted((DATA_DIR / "valid").glob("*.yaml"))
INVALID_EXAMPLE_FILES = sorted((DATA_DIR / "invalid").glob("*.yaml"))
PROBLEM_INVALID_FILES = sorted((DATA_DIR / "problem" / "invalid").glob("*.yaml"))

EXPECTED_ERROR = re.compile(r"^# expected_error: (.+)$", re.MULTILINE)


@pytest.fixture(scope="module")
def validator():
    return Validator(
        str(SCHEMA), validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )


def target_class(filepath: Path) -> str:
    return filepath.stem.split("-")[0]


def errors_for(validator, filepath: Path) -> list[str]:
    instance = yaml.safe_load(filepath.read_text())
    report = validator.validate(instance, target_class(filepath))
    return [r.message for r in report.results]


def expected_error(filepath: Path) -> str:
    match = EXPECTED_ERROR.search(filepath.read_text())
    assert match, f"{filepath.name} has no '# expected_error:' header"
    return match.group(1).strip()


def test_example_dirs_not_empty():
    assert VALID_EXAMPLE_FILES
    assert INVALID_EXAMPLE_FILES


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES, ids=lambda p: p.stem)
def test_valid_data_files(validator, filepath):
    """Valid examples pass schema validation."""
    assert errors_for(validator, filepath) == []


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES, ids=lambda p: p.stem)
def test_valid_data_files_load(filepath):
    """Valid examples load into the generated Python datamodel."""
    tgt_class = getattr(datamodel, target_class(filepath))
    assert yaml_loader.load(str(filepath), target_class=tgt_class)


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES, ids=lambda p: p.stem)
def test_invalid_data_files(validator, filepath):
    """Invalid examples fail, and fail for the documented reason."""
    errors = errors_for(validator, filepath)
    expected = expected_error(filepath)
    assert errors, f"{filepath.name} unexpectedly passed validation"
    assert any(expected in e for e in errors), f"expected {expected!r}, got {errors}"


@pytest.mark.parametrize("filepath", PROBLEM_INVALID_FILES, ids=lambda p: p.stem)
@pytest.mark.xfail(
    strict=True,
    reason="rule stated in the schema but not enforced by the generated JSON Schema",
)
def test_problem_invalid_data_files(validator, filepath):
    expected = expected_error(filepath)
    assert any(expected in e for e in errors_for(validator, filepath))
