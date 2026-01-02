# 🖥️ Operating System - Complete GATE & ESE Study Material

> **The Atomic Truth:** OS manages hardware resources for user programs.

[![GATE](https://img.shields.io/badge/GATE-CSE-blue)]()
[![ESE](https://img.shields.io/badge/ESE-IT-green)]()

---

## 📊 Weightage Analysis

| Topic | GATE Weightage | ESE Weightage | Difficulty |
|-------|---------------|---------------|------------|
| Process Management | 15-20% | 15% | Medium |
| CPU Scheduling | 10-15% | 12% | Medium-High |
| Process Synchronization | 15-20% | 15% | High |
| Deadlocks | 10-12% | 10% | Medium |
| Memory Management | 15-20% | 18% | High |
| Virtual Memory | 10-15% | 12% | High |
| File Systems | 8-10% | 10% | Medium |
| Disk Management | 5-8% | 8% | Medium |

---

## 📚 Chapter Index

| Chapter | Topic | Key Focus |
|---------|-------|-----------|
| [Chapter 1](./01-Introduction/README.md) | Introduction to OS | Types, Functions, System Calls |
| [Chapter 2](./02-Process-Management/README.md) | Process Management | PCB, States, Context Switching |
| [Chapter 3](./03-Threads/README.md) | Threads | User vs Kernel, Models |
| [Chapter 4](./04-CPU-Scheduling/README.md) | CPU Scheduling | FCFS, SJF, RR, Priority, MLFQ |
| [Chapter 5](./05-Process-Synchronization/README.md) | Process Synchronization | Critical Section, Semaphores, Monitors |
| [Chapter 6](./06-Deadlocks/README.md) | Deadlocks | Prevention, Avoidance, Detection |
| [Chapter 7](./07-Memory-Management/README.md) | Memory Management | Paging, Segmentation |
| [Chapter 8](./08-Virtual-Memory/README.md) | Virtual Memory | Page Replacement, Thrashing |
| [Chapter 9](./09-File-Systems/README.md) | File Systems | Allocation, Directory Structure |
| [Chapter 10](./10-Disk-Management/README.md) | Disk Management | Scheduling, RAID |

---

## 🎯 GATE 2026 Focus Areas (IIT-G Standards)

### High-Priority Topics
1. **Page Replacement Algorithms** - Optimal, LRU, FIFO, Belady's Anomaly
2. **Deadlock Detection** - RAG, Banker's Algorithm
3. **Semaphore Problems** - Producer-Consumer, Readers-Writers, Dining Philosophers
4. **CPU Scheduling Numericals** - Gantt Charts, Turnaround Time, Waiting Time
5. **Memory Allocation** - First Fit, Best Fit, Worst Fit, Fragmentation

### The Genius Traps (Common Mistakes)
- Confusing **Turnaround Time** with **Response Time**
- Wrong handling of **arrival time = 0** in scheduling
- Forgetting **overhead** in Context Switching calculations
- Misapplying **Banker's Algorithm** safe sequence detection
- Incorrect **TLB hit ratio** calculations

---

## 🧠 Quick Reference Formulas

### CPU Scheduling
$$\text{Turnaround Time (TAT)} = \text{Completion Time} - \text{Arrival Time}$$

$$\text{Waiting Time (WT)} = \text{Turnaround Time} - \text{Burst Time}$$

$$\text{Response Time} = \text{First Response} - \text{Arrival Time}$$

$$\text{CPU Utilization} = \frac{\text{Busy Time}}{\text{Total Time}} \times 100\%$$

### Memory Management
$$\text{Effective Access Time (EAT)} = h \times T_{TLB+M} + (1-h) \times T_{TLB+2M}$$

Where $h$ = TLB hit ratio, $T$ = memory access time

$$\text{Page Table Size} = \frac{\text{Virtual Address Space}}{\text{Page Size}} \times \text{Entry Size}$$

### Disk Scheduling
$$\text{Seek Time} = \text{Number of Cylinders} \times \text{Seek Time per Cylinder}$$

$$\text{Total Access Time} = \text{Seek Time} + \text{Rotational Latency} + \text{Transfer Time}$$

---

## 📖 How to Use This Material

1. **First Pass**: Read the concepts with examples
2. **Second Pass**: Solve the GATE PYQs at the end of each chapter
3. **Third Pass**: Focus on tricks and edge cases
4. **Final Pass**: Time-bound practice with NAT precision

---

## 🔥 5-Second Snap Checks

| Scenario | Quick Check |
|----------|-------------|
| Scheduling has preemption | Check if shorter jobs can interrupt |
| Deadlock possible | Check if all 4 conditions hold |
| Page fault occurs | Page not in main memory |
| Internal fragmentation | Fixed-size blocks (Paging) |
| External fragmentation | Variable-size blocks (Segmentation) |

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign]**

*Navigate to individual chapters for detailed explanations, solved examples, and GATE PYQs.*
