from typing import Tuple, Type, Dict

from unrpa.versions.version import Version
from unrpa.versions.official_rpa import RPA3
from unrpa.utils import Utils, IndexEntry, ComplexIndexEntry


class TMOZ02(RPA3):
    """The third official version of RPA-3.0 from Once Upon a Breeze (Demo)."""

    name = "TMOZ-02"
    header = b"TMOZ-02"

    def deobfuscate_index(
        self, key: int, index: Dict[bytes, IndexEntry]
    ) -> Dict[bytes, ComplexIndexEntry]:
        return {
            path: TMOZ02.deobfuscate_entry(key, entry) for path, entry in index.items()
        }

    @staticmethod
    def deobfuscate_entry(key: int, entry: IndexEntry) -> ComplexIndexEntry:
        return [
            (offset ^ key, length ^ key, start)
            for length, offset, start in Utils.normalise_entry(entry)
        ]


versions: Tuple[Type[Version], ...] = (TMOZ02,)
