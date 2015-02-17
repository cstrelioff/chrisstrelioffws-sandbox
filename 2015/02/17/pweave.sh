#! /bin/sh
#
# pweave.sh
# Copyright (C) 2014 Christopher C. Strelioff <chris.strelioff@gmail.com>
#
# Distributed under terms of the MIT license.
#
pweave -f sphinx --figure-directory figs using_python_to_query_data_from_socrata.Pnw
ptangle using_python_to_query_data_from_socrata.Pnw 
