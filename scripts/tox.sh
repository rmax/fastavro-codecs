#!/bin/bash
set -eux

which tox || pip install tox

exec tox -v
