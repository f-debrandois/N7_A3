#!/bin/bash
source utils.sh
echo "LOOKAHEAD TUNING BENCHMARK"

export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1

traces="traces/bench_traces_lookahead"
out="outputs/bench_outputs_lookahead"
csv="csv/bench_lookahead.csv"
echo m,n,k,b,p,q,algo,lookahead,gflops > $csv

b=256
p=4
q=4
P=$((p*q))
m=2048
n=2048
k=2048
iter=5
platform="platforms/cluster_crossbar.xml"
hostfile="hostfiles/cluster_hostfile.txt"
mpi_options="-platform $platform -hostfile $hostfile -np $P"

for la in $(seq 1 $((k / b)))
do
    algo="p2p-i-la"
    options="-c -l $la"
    run
done
