from lz4 import compress, decompress

from ._base import BaseCodec


class Lz4Codec(BaseCodec):

    # TODO: Unreleased version of lz4 support compression arguments.
    encode = staticmethod(compress)
    decode = staticmethod(decompress)
