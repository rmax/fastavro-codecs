#!/bin/bash
#
# This script builds manylinux wheels. Run this script from top directory:
#
#   docker run --rm -v $PWD:/io quay.io/pypa/manylinux1_x86_64 /io/scripts/build-wheels.sh
#
set -eux

SRC=/io
PIP_WHEEL_DIR=$SRC/wheels
PIP_FIND_LINKS=$SRC/wheels

PYTHON_BINS=$(echo /opt/python/{cp27*,cp34*,cp35*}/bin)

yum install -y python-devel lzo lzo-devel snappy snappy-devel

export PIP_WHEEL_DIR PIP_FIND_LINKS

# Compile wheels
for PYBIN in $PYTHON_BINS; do
    ${PYBIN}/pip wheel -r $SRC/requirements.txt -w $PIP_WHEEL_DIR
    ${PYBIN}/pip wheel $SRC -w $PIP_WHEEL_DIR
done

# Bundle external shared libraries into the wheels
for whl in $PIP_WHEEL_DIR/*-cp*-linux_*.whl; do
    auditwheel repair $whl -w $PIP_WHEEL_DIR
done

# Install packages and test
for PYBIN in $PYTHON_BINS; do
    ${PYBIN}/pip install fastavro-codecs --no-index -f $PIP_WHEEL_DIR
    ${PYBIN}/pip install -r $SRC/requirements-tests.txt
    ${PYBIN}/py.test $SRC/tests
done
