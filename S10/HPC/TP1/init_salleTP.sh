#!/bin/bash

# à modifier en indiquant où est installé simgrid
SIMGRID=/mnt/n7fs/ens/tp_guivarch/opt2023/simgrid-3.32

export PATH=${SIMGRID}/bin:${PATH}

alias Smpirun="smpirun -hostfile ${PWD}/archis/cluster_hostfile.txt -platform ${PWD}/archis/cluster_crossbar.xml"
