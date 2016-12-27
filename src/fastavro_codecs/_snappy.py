import pysnappy

from ._base import BaseCodec


class SnappyCodec(BaseCodec):

    encode = staticmethod(pysnappy.compress)
    decode = staticmethod(pysnappy.uncompress)
