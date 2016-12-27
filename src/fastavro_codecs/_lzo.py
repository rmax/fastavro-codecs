from lzo import compress, decompress

from ._base import BaseCodec


class LzoCodec(BaseCodec):

    def __init__(self, level=6, **kwargs):
        super(LzoCodec, self).__init__(**kwargs)
        self.level = level

    def encode(self, data):
        return compress(data, self.level)

    decode = staticmethod(decompress)
