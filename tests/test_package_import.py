import fastavro_codecs


def test_package_metadata():
    assert fastavro_codecs.__author__
    assert fastavro_codecs.__email__
    assert fastavro_codecs.__version__
