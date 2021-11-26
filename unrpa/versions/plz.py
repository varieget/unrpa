from typing import Tuple, Type

from unrpa.versions.version import Version
from unrpa.versions.official_rpa import RPA3, RPA2


class PLZ3(RPA3):
    """A slightly custom variant of RPA-3.0."""

    name = "PLZ-3.0"
    header = b"PLZ-3.0"


class PLZ2(RPA2):
    """A slightly custom variant of RPA-2.0."""

    name = "PLZ-2.0"
    header = b"PLZ-2.0"


versions: Tuple[Type[Version], ...] = (
    PLZ3,
    PLZ2,
)
