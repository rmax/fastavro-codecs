from lzma import compress, decompress

from ._base import BaseCodec


class LzmaCodec(BaseCodec):

    def __init__(self, preset=3, **kwargs):
        super(LzmaCodec, self).__init__(**kwargs)
        self.preset = preset

    def encode(self, data):
        return compress(data, preset=self.preset)

    decode = staticmethod(decompress)
