from brotli import compress, decompress

from ._base import BaseCodec


class BrotliCodec(BaseCodec):

    def __init__(self, quality=4, **kwargs):
        super(BrotliCodec, self).__init__(**kwargs)
        self.quality = quality

    def encode(self, data):
        return compress(data, quality=self.quality)

    decode = staticmethod(decompress)
