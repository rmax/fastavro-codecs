# -*- coding: utf-8 -*-
import contextlib
import fastavro

__author__ = 'Rolando Espinoza'
__email__ = 'rolando at rmax.io'
__version__ = '0.1.0-dev'


AVAILABLE_CODECS = {}


def install_codec(name, override=True, codec_cls=None, **codec_kwargs):
    BLOCK_READERS = fastavro._reader.BLOCK_READERS
    BLOCK_WRITERS = fastavro._writer.BLOCK_WRITERS
    if (name in BLOCK_READERS or name in BLOCK_WRITERS) and not override:
        raise ValueError("Codec already available in fastavro: %s" % name)

    if codec_cls is None:
        try:
            codec_cls = AVAILABLE_CODECS[name]
        except KeyError:
            raise ValueError("Codec not available: %s" % name)

    codec = codec_cls(**codec_kwargs)
    BLOCK_READERS[name] = codec.read_block
    BLOCK_WRITERS[name] = codec.write_block


def install_all(*names):
    names = names or AVAILABLE_CODECS.keys()
    for name in names:
        install_codec(name)


def list_codecs():
    return list(AVAILABLE_CODECS.keys())


@contextlib.contextmanager
def ignoring(*exceptions):
    try:
        yield
    except exceptions:
        pass


with ignoring(ImportError):
    from ._brotli import BrotliCodec
    AVAILABLE_CODECS['brotli'] = BrotliCodec

with ignoring(ImportError):
    from ._lz4 import Lz4Codec
    AVAILABLE_CODECS['lz4'] = Lz4Codec

with ignoring(ImportError):
    from ._lzma import LzmaCodec
    AVAILABLE_CODECS['lzma'] = LzmaCodec
    AVAILABLE_CODECS['xz'] = AVAILABLE_CODECS['lzma']  # alias

with ignoring(ImportError):
    from ._lzo import LzoCodec
    AVAILABLE_CODECS['lzo'] = LzoCodec

with ignoring(ImportError):
    from ._snappy import SnappyCodec
    AVAILABLE_CODECS['snappy'] = SnappyCodec

with ignoring(ImportError):
    from ._zstd import ZstdCodec
    AVAILABLE_CODECS['zstd'] = ZstdCodec
