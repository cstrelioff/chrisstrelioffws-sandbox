#! /bin/sh
#
# pweave.sh
# Copyright (C) 2014 Christopher C. Strelioff <chris.strelioff@gmail.com>
#
# Distributed under terms of the MIT license.
#
if [ "$#" -ne 1 ]
then
    echo "usage: ./pweave.sh <filename.Pnw>"
    exit 1
else
    echo "running pweave..."
    pweave -f sphinx --figure-directory figs $1
    ptangle $1
fi

