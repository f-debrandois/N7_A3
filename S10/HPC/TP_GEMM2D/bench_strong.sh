#!/bin/bash
source utils.sh
echo "STRONG SCALING BENCHMARK"

export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1

traces="traces/bench_traces_strong"
out="outputs/bench_outputs_strong"
csv="csv/bench_strong.csv"
echo m,n,k,b,p,q,algo,lookahead,gflops > $csv

b=256
m=2048
n=2048
k=2048
iter=5
platform="platforms/cluster_crossbar.xml"
hostfile="hostfiles/cluster_hostfile.txt"

for scale in 1 2 4 8
do
    p=$scale
    q=$scale
    P=$((p*q))
    mpi_options="-platform $platform -hostfile $hostfile -np $P"
    
    for algo in p2p bcast
    do
        la=0
        options="-c"
        run
    done

    for la in $(seq 1 $((k / b)))
    do
        algo="p2p-i-la"
        options="-c -l $la"
        run
    done
done
