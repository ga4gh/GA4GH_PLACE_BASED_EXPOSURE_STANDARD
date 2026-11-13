"""exposure-linkage.

GA4GH Place-Based Exposure Metadata Standard: a LinkML schema describing how environmental exposure datasets are linked to cohort participants.
"""

try:
    from exposure_linkage._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
