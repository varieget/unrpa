from abc import ABCMeta, abstractmethod
from typing import Tuple, Optional, BinaryIO, Dict

from unrpa.view import ArchiveView
from unrpa.utils import Utils, IndexEntry, ComplexIndexEntry


class Version(metaclass=ABCMeta):
    """An abstract base class for parsing different versions of RPA archive."""

    name: str

    @abstractmethod
    def detect(self, extension: str, first_line: bytes) -> bool:
        """Detect if an archive is of this version."""
        raise NotImplementedError()

    @abstractmethod
    def find_offset_and_key(self, archive: BinaryIO) -> Tuple[int, Optional[int]]:
        """Find the offset and key values for the archive."""
        raise NotImplementedError()

    def postprocess(self, source: ArchiveView, sink: BinaryIO) -> None:
        """Allows postprocessing over the data extracted from the archive."""
        for segment in iter(source.read1, b""):
            sink.write(segment)

    def deobfuscate_index(
        self, key: int, index: Dict[bytes, IndexEntry]
    ) -> Dict[bytes, ComplexIndexEntry]:
        return {
            path: Utils.deobfuscate_entry(key, entry) for path, entry in index.items()
        }

    def __str__(self) -> str:
        return self.name


class ExtensionBasedVersion(Version, metaclass=ABCMeta):
    """A helper for versions where detection is based on the file extension."""

    extension: str

    def detect(self, extension: str, first_line: bytes) -> bool:
        return extension == self.extension


class HeaderBasedVersion(Version, metaclass=ABCMeta):
    """A helper for versions where detection is based on an in-file header."""

    header: bytes

    def detect(self, extension: str, first_line: bytes) -> bool:
        return first_line.startswith(self.header)
