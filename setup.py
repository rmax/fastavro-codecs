# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


def read_file(filename):
    with open(filename) as fp:
        return fp.read().strip()


def read_rst(filename):
    # Ignore unsupported directives by pypi.
    return ''.join(line for line in read_file(filename).splitlines()
                   if not line.startswith('.. comment::'))

EXTRAS_REQUIRE = {
    'brotli': ['brotli>=0.5'],
    'lz4': ['lz4>=0.8'],
    'lzo': ['python-lzo>=1.09'],
    'snappy': ['pysnappy>=0.6'],
    'zstd': ['zstandard>=0.5'],
}
EXTRAS_REQUIRE['all'] = list(dep for deps in EXTRAS_REQUIRE.values() for dep in deps)

setup_attrs = dict(
    name='fastavro-codecs',
    version=read_file('VERSION'),
    description="Fastavro codecs.",
    long_description=read_rst('README.rst') + '\n\n' + read_rst('HISTORY.rst'),
    author="Rolando Espinoza",
    author_email='rolando@rmax.io',
    url='https://github.com/rolando/fastavro-codecs',
    packages=list(find_packages('src')),
    package_dir={'': 'src'},
    install_requires=[
        'fastavro>=0.9.6',
    ],
    extras_require=EXTRAS_REQUIRE,
    license="MIT",
    keywords='fastavro-codecs',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)


if __name__ == "__main__":
    setup(**setup_attrs)
