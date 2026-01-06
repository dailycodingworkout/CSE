# Chapter 12: Distributed Databases

---

## 🎯 What is a Distributed Database?

A **Distributed Database (DDB)** is a collection of logically interrelated databases distributed over a computer network.

### Key Characteristics
- Data stored at multiple sites
- Sites connected by a network
- Appears as single database to users

### 🎭 Analogy
> Distributed Database = **Bank with multiple branches**
> - Each branch has local data
> - All branches connected
> - Customer sees one "bank"

---

## 📊 Centralized vs Distributed

| Aspect | Centralized | Distributed |
|--------|-------------|-------------|
| Data location | Single site | Multiple sites |
| Failure | Single point | Partial availability |
| Scalability | Limited | High |
| Complexity | Low | High |
| Query cost | Memory/disk | + Network |

---

## 🏗️ Distributed Database Architecture

### Types

```
                Distributed DB Architectures
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
   Homogeneous      Heterogeneous      Federated
        │                 │                 │
   Same DBMS        Different DBMS    Autonomous DBs
   Same Schema      Different Schema   Limited Integration
```

### Homogeneous DDBMS
- Same DBMS software at all sites
- Same data model and schema
- Easier to manage

### Heterogeneous DDBMS
- Different DBMS at different sites
- Translation/mapping needed
- More complex

---

## 📦 Data Fragmentation

### Types of Fragmentation

#### 1. Horizontal Fragmentation
Split table **by rows** (based on selection condition).

```
Student Table:
┌──────┬────────┬──────┐
│ Roll │  Name  │ Dept │
├──────┼────────┼──────┤
│  1   │ Alice  │  CS  │
│  2   │ Bob    │  EE  │
│  3   │ Carol  │  CS  │
│  4   │ Dave   │  EE  │
└──────┴────────┴──────┘

Fragment 1 (CS site): σ_Dept='CS'(Student)
┌──────┬────────┬──────┐
│  1   │ Alice  │  CS  │
│  3   │ Carol  │  CS  │
└──────┴────────┴──────┘

Fragment 2 (EE site): σ_Dept='EE'(Student)
┌──────┬────────┬──────┐
│  2   │ Bob    │  EE  │
│  4   │ Dave   │  EE  │
└──────┴────────┴──────┘
```

#### 2. Vertical Fragmentation
Split table **by columns** (based on projection).

```
Employee Table:
┌──────┬────────┬─────────┬────────┐
│ EmpID│  Name  │ Salary  │  Dept  │
├──────┼────────┼─────────┼────────┤
│  1   │ Alice  │  50000  │   CS   │
│  2   │ Bob    │  60000  │   EE   │
└──────┴────────┴─────────┴────────┘

Fragment 1 (HR site): π_EmpID,Name,Dept(Employee)
┌──────┬────────┬────────┐
│ EmpID│  Name  │  Dept  │
├──────┼────────┼────────┤
│  1   │ Alice  │   CS   │
│  2   │ Bob    │   EE   │
└──────┴────────┴────────┘

Fragment 2 (Finance site): π_EmpID,Salary(Employee)
┌──────┬─────────┐
│ EmpID│ Salary  │
├──────┼─────────┤
│  1   │  50000  │
│  2   │  60000  │
└──────┴─────────┘

Note: Include key (EmpID) in both for reconstruction!
```

#### 3. Mixed/Hybrid Fragmentation
Combination of horizontal and vertical.

```
First vertical, then horizontal on each fragment
OR
First horizontal, then vertical on each fragment
```

### Fragmentation Properties

| Property | Meaning |
|----------|---------|
| **Completeness** | All data preserved in fragments |
| **Reconstruction** | Can rebuild original from fragments |
| **Disjointness** | Fragments don't overlap (except keys) |

---

## 🔄 Data Replication

### Types

| Type | Description | Pros | Cons |
|------|-------------|------|------|
| **No Replication** | Data at one site only | Simple updates | Single point of failure |
| **Full Replication** | Complete copy at each site | High availability | Update overhead |
| **Partial Replication** | Some data replicated | Balance of both | Complex management |

### Replication Strategies

#### Synchronous (Eager)
- Update all replicas in same transaction
- Strong consistency
- Higher latency

#### Asynchronous (Lazy)
- Update primary, propagate later
- Better performance
- Temporary inconsistency

---

## 🌐 Transparency in DDBMS

### Types of Transparency

| Transparency | User Unaware Of |
|--------------|-----------------|
| **Location** | Where data is stored |
| **Fragmentation** | How data is divided |
| **Replication** | How many copies exist |
| **Network** | Network details |
| **Transaction** | Distributed nature of transactions |

### Example
```sql
-- User writes simple query
SELECT * FROM Student WHERE Dept = 'CS';

-- DDBMS handles:
-- 1. Finding which site has CS students
-- 2. Routing query to correct fragment
-- 3. Combining results if needed
```

---

## 📊 Distributed Query Processing

### Steps
```
1. Query decomposition (parse, normalize)
2. Data localization (find fragments)
3. Global optimization (choose sites, join order)
4. Local optimization (each site optimizes locally)
```

### Cost Factors
```
Total Cost = Local I/O Cost + Network Cost

Network Cost = Data Transfer + Message Overhead

Network is often the bottleneck!
```

### Semijoin Optimization

Reduce data transfer for distributed joins.

```
Normal Join: Ship R to S's site, join there

Semijoin:
1. Project join column from R, send to S's site
2. At S, find matching tuples
3. Send matching S tuples back
4. Join at R's site

Useful when |π_joinCol(R)| << |R|
```

---

## 🔐 Distributed Transaction Management

### Issues
1. Atomicity across sites
2. Concurrency control across sites
3. Recovery across sites

### Distributed ACID

| Property | Challenge |
|----------|-----------|
| Atomicity | All sites commit or all abort |
| Consistency | Constraints across fragments |
| Isolation | Distributed locking/timestamps |
| Durability | Recovery at multiple sites |

---

## ✅ Two-Phase Commit (2PC)

### The Protocol

Ensures atomicity across distributed sites.

### Participants
- **Coordinator**: Transaction manager at originating site
- **Participants**: Transaction managers at other sites

### Phase 1: Voting Phase
```
Coordinator → Participants: PREPARE?
Participants → Coordinator: VOTE (Yes/No)

If participant votes Yes: Enters "prepared" state
                          Can commit or abort
If participant votes No:  Unilaterally aborts
```

### Phase 2: Decision Phase
```
If ALL votes = Yes:
    Coordinator → Participants: COMMIT
    All participants commit

If ANY vote = No:
    Coordinator → Participants: ABORT
    All participants abort
```

### State Diagram

```
                    COORDINATOR
    ┌─────────────────────────────────────────┐
    │                                         │
    │    Initial → Waiting → Decided         │
    │                 │         │             │
    │            (collect    (commit/        │
    │             votes)      abort)         │
    └─────────────────────────────────────────┘

                    PARTICIPANT
    ┌─────────────────────────────────────────┐
    │                                         │
    │    Initial → Prepared → Decided        │
    │                 │          │            │
    │           (voted yes)  (received       │
    │                        decision)       │
    └─────────────────────────────────────────┘
```

### 2PC Problems

| Problem | Description |
|---------|-------------|
| **Blocking** | Participants wait if coordinator fails |
| **Performance** | Extra round-trip for prepare/commit |
| **Uncertainty Period** | After voting yes, before decision |

---

## 📊 Three-Phase Commit (3PC)

### Improvement over 2PC
- Adds "pre-commit" phase
- Non-blocking in most failure scenarios

### Phases
```
Phase 1: Voting (same as 2PC)
Phase 2: Pre-commit (prepare to commit)
Phase 3: Commit (actual commit)
```

### Trade-off
- More messages
- Better failure handling
- Still not perfect (network partitions)

---

## 🔒 Distributed Concurrency Control

### 1. Distributed Locking

#### Centralized Lock Manager
- One site manages all locks
- Simple but single point of failure

#### Primary Copy
- Each data item has primary site
- Lock requests go to primary

#### Distributed Lock Manager
- Lock at site where data resides
- More scalable

### 2. Distributed Timestamps

- Each site has local timestamp generator
- Combine with site ID for global uniqueness

```
Global Timestamp = (Local_Time, Site_ID)

(100, 1) < (100, 2) < (101, 1)
```

### 3. Distributed Optimistic Control

- Local validation at each site
- Global validation for distributed data

---

## 📱 CAP Theorem

### Statement
A distributed system can provide at most **2 of 3** guarantees:

| Property | Meaning |
|----------|---------|
| **C - Consistency** | All nodes see same data at same time |
| **A - Availability** | Every request gets a response |
| **P - Partition Tolerance** | System works despite network failures |

### The Trade-off

```
         Consistency
            /\
           /  \
          /    \
         /      \
        /   CA   \    ← Possible only if no partitions
       /    ▲     \       (not practical in distributed)
      /     │      \
     /      │       \
    /───────┼────────\
   /   CP   │   AP    \
  ▼─────────┴──────────▼
Availability   Partition Tolerance

In distributed systems, P is non-negotiable
So choice is between C and A during partitions
```

### Examples

| System | Choice | Trade-off |
|--------|--------|-----------|
| Traditional RDBMS | CA | Not partition tolerant |
| MongoDB, Redis | CP | May be unavailable |
| Cassandra, DynamoDB | AP | Eventually consistent |

---

## 🔄 Consistency Models

### Strong Consistency
- Read always returns latest write
- Expensive to implement

### Eventual Consistency
- Given enough time, all replicas converge
- Better availability

### Causal Consistency
- Causally related operations seen in order
- Non-causal operations can be concurrent

---

## 📐 NoSQL Basics (Brief)

### Types of NoSQL Databases

| Type | Structure | Example | Use Case |
|------|-----------|---------|----------|
| **Key-Value** | Key → Value | Redis, DynamoDB | Caching, sessions |
| **Document** | JSON-like docs | MongoDB, CouchDB | Content management |
| **Column-Family** | Column families | Cassandra, HBase | Analytics, time-series |
| **Graph** | Nodes + edges | Neo4j, Amazon Neptune | Social networks |

### BASE vs ACID

| ACID | BASE |
|------|------|
| Atomicity | **B**asically **A**vailable |
| Consistency | **S**oft state |
| Isolation | **E**ventual consistency |
| Durability | |

---

## ⚠️ Common GATE Traps

### Trap 1: 2PC Guarantee
```
2PC guarantees atomicity, NOT deadlock-freedom or availability
Coordinator failure → Blocking!
```

### Trap 2: CAP Theorem
```
Can't have all three in distributed system with partitions
Most systems choose AP or CP
CA only in single-site or always-connected systems
```

### Trap 3: Fragmentation Reconstruction
```
Horizontal: Union of fragments
Vertical: Natural join on key
Must preserve completeness!
```

### Trap 4: Semijoin Benefit
```
Semijoin reduces data transfer
NOT always better (overhead of extra messages)
Useful when projection is much smaller than table
```

---

## 🧪 Practice Problems

### Q1: Fragmentation
```
Student(Roll, Name, Dept, CGPA)
Horizontal fragmentation by Dept (3 departments)
Vertical fragmentation: (Roll, Name) and (Roll, Dept, CGPA)

How to reconstruct?
1. Each horizontal fragment: σ_Dept='X'(Student)
2. Combine: F1 ∪ F2 ∪ F3
3. Vertical: F1 ⋈ F2 on Roll
```

### Q2: 2PC Scenario
```
Coordinator sends PREPARE to 3 participants
P1 votes Yes, P2 votes Yes, P3 votes No

Decision: ABORT (any No → abort)
All participants abort (even P1, P2 who voted Yes)
```

### Q3: CAP Trade-off
```
During network partition:
- Choose Consistency: Some requests may fail
- Choose Availability: Some reads may return stale data

Can't have both during partition!
```

---

## 📌 Chapter Summary

| Concept | Key Points |
|---------|------------|
| **Fragmentation** | Horizontal (rows), Vertical (columns), Mixed |
| **Replication** | Full, Partial, None |
| **Transparency** | Location, Fragmentation, Replication |
| **2PC** | Voting → Decision, ensures atomicity |
| **CAP** | Choose 2 of 3 (Consistency, Availability, Partition) |
| **BASE** | Basically Available, Soft state, Eventually consistent |

---

## 🎓 Quick Revision Points

1. ✅ Horizontal = rows (selection), Vertical = columns (projection)
2. ✅ Vertical must include key for reconstruction
3. ✅ 2PC: All Yes → Commit, Any No → Abort
4. ✅ 2PC is blocking (coordinator failure)
5. ✅ CAP: Can only guarantee 2 of 3
6. ✅ Distributed needs P, so choose C or A
7. ✅ BASE trades consistency for availability

---

*Previous: [Recovery System](./11-Recovery-System.md) | Back to [Index](./README.md)*
