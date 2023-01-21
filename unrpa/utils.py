from typing import Union, Tuple, Dict, cast, Iterable


# Offset, Length
SimpleIndexPart = Tuple[int, int]
SimpleIndexEntry = Iterable[SimpleIndexPart]
# Offset, Length, Prefix
ComplexIndexPart = Tuple[int, int, bytes]
ComplexIndexEntry = Iterable[ComplexIndexPart]
IndexPart = Union[SimpleIndexPart, ComplexIndexPart]
IndexEntry = Iterable[IndexPart]


class Utils:
    """Deobfuscate Utils"""

    @staticmethod
    def deobfuscate_entry(key: int, entry: IndexEntry) -> ComplexIndexEntry:
        return [
            (offset ^ key, length ^ key, start)
            for offset, length, start in Utils.normalise_entry(entry)
        ]

    @staticmethod
    def normalise_index(
        index: Dict[bytes, IndexEntry]
    ) -> Dict[bytes, ComplexIndexEntry]:
        return {path: Utils.normalise_entry(entry) for path, entry in index.items()}

    @staticmethod
    def normalise_entry(entry: IndexEntry) -> ComplexIndexEntry:
        return [
            (*cast(SimpleIndexPart, part), b"")
            if len(part) == 2
            else cast(ComplexIndexPart, part)
            for part in entry
        ]
