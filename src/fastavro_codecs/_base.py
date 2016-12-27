try:
    from fastavro._writer import write_long, write_crc32
except ImportError:
    from fastavro.writer import write_long, write_crc32

try:
    from fastavro._reader import read_long
except ImportError:
    from fastavro.reader import read_long

try:
    from fastavro._six import MemoryIO
except ImportError:
    from fastavro.six import MemoryIO


class BaseCodec(object):

    def __init__(self, strict=False):
        self.strict = strict

    def read_block(self, fo):
        length = read_long(fo, None)
        data = fo.read(length - 4)
        crc = fo.read(4)
        # Optionally check CRC for speed purposes.
        if self.strict:
            self.assert_crc(data, crc)
        return MemoryIO(self.decode(data))

    def write_block(self, fo, block_bytes):
        data = self.encode(block_bytes)
        # Always write CRC code.
        write_long(fo, len(data) + 4)
        fo.write(data)
        write_crc32(fo, block_bytes)

    def assert_crc(self, data, expected):
        crc = MemoryIO()
        # Check using same generator function.
        write_crc32(crc, data)
        if crc.getvalue() != expected:
            raise IOError("Checksum failed")

    def encode(self, data):
        raise NotImplementedError

    def decode(self, data):
        raise NotImplementedError
