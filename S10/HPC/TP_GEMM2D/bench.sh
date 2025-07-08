source utils.sh
echo BENCHMARKING THE METHODS

export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1

traces="traces/bench_traces"
out="outputs/bench_outputs"
csv="csv/bench.csv"
echo m,n,k,b,p,q,algo,lookahead,gflops > $csv

# you can modify these values
p=2
q=2
P=$((p*q))
b=256
iter=5
platform="platforms/cluster_crossbar.xml"
hostfile="hostfiles/cluster_hostfile.txt"
mpi_options="-platform $platform -hostfile $hostfile -np $P"

#generate_hostfile $P

# proper benchmark <--- this could be a TODO for students ? (as in, show weak scaling and/or strong scaling)
#mpi_options="-hostfile hostfiles/hostfile.$P.txt"

for i in 4 8 12
do
  n=$((i*b))
  m=$n
  k=$n
  la=0
  options="-c"
  for algo in p2p bcast
  do
    	run
  done
  for la in $(seq 1 $((k/b)))
  do 
  	algo="p2p-i-la"
  	options="-c -l $la"
    	run
  done
done
