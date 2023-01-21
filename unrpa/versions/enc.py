from typing import BinaryIO, Tuple, Optional, Type

from unrpa.versions.version import HeaderBasedVersion, Version


class ENC1(HeaderBasedVersion):
    """The third official version of the RPA format from GrandNesting-demo-1.0."""

    name = "ENC-1.0"
    header = b"ENC-1.0"

    def find_offset_and_key(self, archive: BinaryIO) -> Tuple[int, Optional[int]]:
        line = archive.readline()

        # Encryption Branch
        caesar = {
            "0": "a",
            "5": "b",
            "b": "c",
            "2": "d",
            "a": "e",
            "4": "f",
            "c": "0",
            "8": "1",
            "e": "2",
            "3": "3",
            "d": "4",
            "6": "5",
            "f": "6",
            "7": "7",
            "1": "8",
            "9": "9",
            "g": " ",
        }
        offset_and_key = line[8:33].decode("utf-8")
        offset_and_key = "".join([caesar[c] for c in offset_and_key])

        parts = offset_and_key.split()
        offset = int(parts[0], 16)
        key = int(parts[1], 16)
        return offset, key


versions: Tuple[Type[Version], ...] = (ENC1,)
