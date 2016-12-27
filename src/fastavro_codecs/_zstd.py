# zstandard package.
import zstd

from ._base import BaseCodec


class ZstdCodec(BaseCodec):

    Compressor = zstd.ZstdCompressor
    Decompressor = zstd.ZstdDecompressor

    def __init__(self, level=3, **kwargs):
        super(ZstdCodec, self).__init__(**kwargs)
        self.level = level

    def encode(self, data):
        # Without explicit content size the decompressor fails.
        compressor = self.Compressor(level=self.level,
                                     write_content_size=True)
        return compressor.compress(data)

    def decode(self, data):
        decompressor = self.Decompressor()
        return decompressor.decompress(data)
