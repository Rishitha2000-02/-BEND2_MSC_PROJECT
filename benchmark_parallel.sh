#!/bin/bash

echo "Bend2 Parallel Execution Benchmark"
echo "Workload: pow2(20)"
echo "GPU: Disabled"
echo "Runs: 10"
echo

for THREADS in 1 6
do
    echo "Testing with $THREADS thread(s):"

    for RUN in {1..10}
    do
        /usr/bin/time -f "%e" ./parallel_pow2 +RTS --threads "$THREADS" --gpu off >/dev/null
    done

    echo
done
