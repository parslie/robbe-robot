#!/bin/bash

BINPATH=$(readlink $BASH_SOURCE)
BINDIR=$(dirname $BINPATH)

cd $BINDIR
source $BINDIR/venv/bin/activate
python3 $BINDIR/main.py $@