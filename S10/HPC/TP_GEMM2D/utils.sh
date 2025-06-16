# to modify according to where you install simgrid on your computer
TOOLS_DIR=/home/guivarch/opt
SIMGRID_DIR=$TOOLS_DIR/simgrid-4.0

export PATH=${SIMGRID_DIR}/bin:${PATH}

# to modify according to the value given by --cfg=smpi/host-speed:auto
COMPUTER=6.691Gf

# for check and bench

tmp=$HOME/tmp_simgrid
mkdir -p $tmp
my_mpirun="$SIMGRID_DIR/bin/smpirun -trace --cfg=smpi/tmpdir:$tmp --cfg=smpi/host-speed:$COMPUTER"
traces="traces"
exec=build/bin/main

generate_hostfile() {
 	N=${1:-4}
	mkdir -p hostfiles
	rm -f hostfiles/hostfile.$N.txt
 	for i in $(seq 1 $N)
	do
		echo node-${i}.simgrid.org >> hostfiles/hostfile.$N.txt
	done
}

run() {
        human=${1:-0}
	mkdir -p $out
 	echo $my_mpirun $mpi_options ${exec:-build/bin/main} -m $m -k $k -n $n -b $b -a $algo -p $p -q $q -i $iter $options
 	$my_mpirun $mpi_options ${exec:-build/bin/main} -m $m -k $k -n $n -b $b -a $algo -p $p -q $q -i $iter $options &> $out/$algo.out
	echo reading $out/$algo.out
	correct=$(grep -i "gemm is correct" "$out/$algo.out" | wc -l)
	trial=$(grep "Gflop/s" $out/$algo.out | grep $algo | wc -l)
	echo Found $correct correct GEMM out of $trial
        while read line ; do
	  # [0] (p2p) measured_wtime = 0.000058s (la=0) | 0.002195 Gflop/s
	  gflops=$( echo $line | grep -o "| .* Gflop/s" | grep -o "[0-9]\\+.[0-9]\\+" )
	  if [ $human -eq 0 ]; then
	    echo "$m,$k,$n,$b,$p,$q,$algo,$la,$gflops"
	  else
	    echo "mxnxk=${m}x${n}x${k},b=$b,p x q = $p x $q | using $algo, (lookahead:$la) => $gflops Gflop/s"
	  fi
	  echo "$m,$k,$n,$b,$p,$q,$algo,$la,$gflops" >> $csv
	done < <(grep "Gflop/s" $out/$algo.out | grep $algo)
	if [ $la -gt 0 ]; then
	  	algo=$algo-$la
	fi
	mkdir -p $traces
	mv -f smpi_simgrid.trace $traces/$algo.trace
	#echo You can open $traces/$algo.trace with $VITE_DIR/bin/vite
	echo
}
