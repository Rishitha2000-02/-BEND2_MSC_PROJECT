# Bend2 Programming Language – MSc Project

## Project Overview

This project explores Bend2, a pure functional programming language designed for parallel computation.

The research is part of the MSc Cybersecurity and Data Science programme and focuses on Bend2's execution model, CPU parallelism, runtime architecture, memory management and GPU execution.

## Research Details

**Project:** Bend2 Programming Language

**Part:** Part B – Execution Model, Parallelism and Runtime Architecture

**Research Areas:**
- Bend2 execution model
- CPU parallelism and task scheduling
- BendRT runtime architecture
- Affine memory management
- GPU execution
- Historical HVM architecture
- Comparison between BendRT and CUDA
- CPU parallelism benchmarking

## Technologies Used

- Bend2 2.0.40
- Ubuntu Linux
- Python 3
- Bash scripting
- VirtualBox
- Git and GitHub
- CUDA (theoretical research; not installed in the experimental environment)

## Project Structure

```text
BEND2_MSC_PROJECT/
│
└── B_Execution_Model_Parallelism/
    │
    ├── B2_CPU_Benchmark_Results.txt
    ├── B2_Research_Summary.txt
    ├── BendRT.pdf
    ├── BendRT.txt
    ├── GUIDE.md
    ├── benchmark_parallel.sh
    ├── parallel_pow2.bend
    ├── parallel_pow2
    ├── precise_benchmark.py
    └── README.md
```

## Practical Experiments

### 1. Parallel Recursive Computation

Implemented a recursive power-of-two computation using Bend2.

```bash
bend parallel_pow2.bend --check-only
bend parallel_pow2.bend -o parallel_pow2
./parallel_pow2
```

Expected output:

```text
1048576
```

### 2. CPU Thread Configuration

Tested the program using one and six CPU worker threads.

```bash
./parallel_pow2 +RTS --threads 1 --gpu off
./parallel_pow2 +RTS --threads 6 --gpu off
```

Both configurations produced the correct result.

### 3. CPU Benchmark

Executed performance measurements using Python's `time.perf_counter()`.

| Metric | 1 Thread | 6 Threads |
|---|---:|---:|
| Median execution time | 9.1852 ms | 5.7759 ms |
| Number of runs | 20 | 20 |
| Output | 1048576 | 1048576 |

**Measured speedup:** 1.59×

**Performance improvement:** Approximately 37.1%.

### 4. BendRT Runtime Architecture

Studied the following architectural concepts:

- Flat evaluator
- Task-cube scheduler
- Grow and work phases
- Affine ownership
- Memory reclamation
- CPU and GPU execution

### 5. HVM and CUDA Comparison

Analysed the architectural differences between:

- Historical Higher-order Virtual Machine (HVM)
- BendRT runtime
- NVIDIA CUDA programming model

## Experimental Limitations

- Experiments were conducted inside an Ubuntu virtual machine.
- Six CPU workers were available.
- CUDA toolkit was not installed.
- GPU execution could not be experimentally tested.
- GPU and runtime analysis was based on the BendRT research paper.

## How to Run the Benchmark

```bash
chmod +x benchmark_parallel.sh
./benchmark_parallel.sh
```

For more precise measurements:

```bash
python3 precise_benchmark.py
```

## Learning Outcomes

- Understanding functional programming and parallel execution.
- Exploring CPU-based parallel computation.
- Understanding task scheduling and runtime architecture.
- Studying affine memory management.
- Analysing GPU execution concepts.
- Evaluating parallel performance through benchmarking.

## References

1. BendRT: A Parallel Runtime for CPUs and GPUs.
2. Official Bend2 Repository: https://github.com/bendlang/bend
3. Bend2 GUIDE.md.
4. NVIDIA CUDA C++ Programming Guide.

---

**Academic Project:** MSc Cybersecurity and Data Science

**Research Topic:** Bend2 Execution Model, Parallelism and Runtime Architecture
