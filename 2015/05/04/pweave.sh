#! /bin/sh
#
# pweave.sh
# Copyright (C) 2014 Christopher C. Strelioff <chris.strelioff@gmail.com>
#
# Distributed under terms of the MIT license.
#
#pweave -f sphinx --figure-directory figs probabilistic_programming_with_python_and_lea.Pnw 
pweave -f sphinx probabilistic_programming_with_python_and_lea.Pnw 
ptangle probabilistic_programming_with_python_and_lea.Pnw
