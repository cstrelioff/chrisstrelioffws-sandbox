#! /bin/sh
#
# pweave.sh
# Copyright (C) 2014 Christopher C. Strelioff <chris.strelioff@gmail.com>
#
# Distributed under terms of the MIT license.
#
Pweave -f sphinx --figure-directory figs getting_started_with_latent_dirichlet_allocation_in_python.PnW
Ptangle getting_started_with_latent_dirichlet_allocation_in_python.PnW
