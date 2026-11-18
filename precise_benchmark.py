import subprocess
import time
import statistics

runs = 20
results = {}

for threads in [1, 6]:
    timings = []

    # Warm-up
    subprocess.run(
        ["./parallel_pow2", "+RTS", "--threads", str(threads), "--gpu", "off"],
        stdout=subprocess.DEVNULL,
        check=True
    )

    for _ in range(runs):
        start = time.perf_counter()

        subprocess.run(
            ["./parallel_pow2", "+RTS", "--threads", str(threads), "--gpu", "off"],
            stdout=subprocess.DEVNULL,
            check=True
        )

        end = time.perf_counter()
        timings.append((end - start) * 1000)

    results[threads] = statistics.median(timings)

    print(f"{threads} thread(s):")
    print(f"  Runs: {runs}")
    print(f"  Median: {results[threads]:.4f} ms")

if results[6] > 0:
    speedup = results[1] / results[6]
    print(f"\nSpeedup (1 thread / 6 threads): {speedup:.2f}x")
