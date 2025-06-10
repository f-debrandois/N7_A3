#!/bin/bash

SIMGRID=/mnt/n7fs/ens/tp_guivarch/opt2023/simgrid-3.32

export PATH=${SIMGRID}/bin:${PATH}

alias Smpirun="smpirun -hostfile ${SIMGRID}/archis/cluster_hostfile.txt -platform ${SIMGRID}/archis/cluster_crossbar.xml"
