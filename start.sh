#!/bin/bash

BINPATH=$(readlink $BASH_SOURCE)

if [ -n "$BINPATH" ]
then
    BINDIR=$(dirname $BINPATH)
else
    BINDIR=$(dirname $BASH_SOURCE)
fi

cd $BINDIR
source $BINDIR/venv/bin/activate
python3 $BINDIR/main.py $@ &> $BINDIR/output.txt
