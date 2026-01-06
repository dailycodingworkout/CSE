# Chapter 2: Data Models & ER Diagrams

---

## 🎯 What is a Data Model?

A **Data Model** is a conceptual framework that defines:
- How data is **structured**
- What **operations** can be performed
- What **constraints** must be enforced

### 🎭 Analogy
> Data Model = **Language for describing data**
> 
> Just as English has grammar rules, a data model has rules for organizing data.

---

## 📊 Types of Data Models

### Classification Hierarchy

```
                    Data Models
                         │
    ┌────────────────────┼────────────────────┐
    │                    │                    │
Record-Based        Object-Based        Physical
    │                    │                    │
    ├── Hierarchical    ├── ER Model     (Low-level
    │                    │                storage)
    ├── Network         └── OO Model
    │
    └── Relational ← Most Important for GATE
```

---

## 🌳 Hierarchical Model

### Structure
- Tree structure (parent-child relationships)
- One parent, multiple children
- Root node has no parent

```
                    COMPANY (Root)
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
   DEPARTMENT-1    DEPARTMENT-2    DEPARTMENT-3
        │               │
    ┌───┴───┐       ┌───┴───┐
    ▼       ▼       ▼       ▼
  EMP-1   EMP-2   EMP-3   EMP-4
```

### Characteristics
| Feature | Description |
|---------|-------------|
| Structure | Tree (1:N relationships) |
| Navigation | Top-down, parent to child |
| Redundancy | High (data repeated for M:N) |
| Example | IBM's IMS (Information Management System) |

### ⚠️ Limitations
1. **No M:N relationships** directly (requires redundancy)
2. **No flexibility** – fixed navigation paths
3. **Deletion anomaly** – deleting parent deletes children

### 🎭 Real-World Analogy
> **File System on your computer**
> - C:\ is root
> - Folders are parents
> - Files/subfolders are children

---

## 🕸️ Network Model

### Structure
- Graph structure (records and sets)
- A child can have **multiple parents**
- More flexible than hierarchical

```
        SUPPLIER-1          SUPPLIER-2
             \                 /
              \               /
               ▼             ▼
               ┌─────────────┐
               │   PART-A    │
               └─────────────┘
                     │
                     ▼
               ┌─────────────┐
               │   ORDER-1   │
               └─────────────┘
```

### Characteristics
| Feature | Description |
|---------|-------------|
| Structure | Graph (M:N relationships) |
| Navigation | Via pointers/links |
| Complexity | High (pointer maintenance) |
| Example | CODASYL DBTG standard |

### ⚠️ Limitations
1. **Complex navigation** – must know access paths
2. **Pointer overhead** – maintenance complexity
3. **Schema changes** – expensive to modify

---

## 📐 Relational Model (Most Important!)

### Developed by: **E.F. Codd (1970)** ← GATE Favorite

### Structure
- Data stored in **tables (relations)**
- Each table has **rows (tuples)** and **columns (attributes)**
- Relationships via **values** (not pointers)

```
STUDENT Table:
┌──────┬────────┬─────────┬───────┐
│ Roll │  Name  │ Dept_ID │ CGPA  │
├──────┼────────┼─────────┼───────┤
│  1   │ Alice  │   CS    │  9.2  │
│  2   │ Bob    │   EE    │  8.5  │
│  3   │ Carol  │   CS    │  9.0  │
└──────┴────────┴─────────┴───────┘
```

### Key Terminology

| Term | Meaning | Also Called |
|------|---------|-------------|
| **Relation** | Table | File |
| **Tuple** | Row | Record |
| **Attribute** | Column | Field |
| **Domain** | Set of valid values | Data type + constraints |
| **Degree** | Number of attributes | Arity |
| **Cardinality** | Number of tuples | Number of rows |

### 🧠 Memory Trick
> **"RADD"** = Relation, Attribute, Degree, Domain
> 
> Degree = Columns (both have 'e' in second position)
> Cardinality = Rows (both relate to count)

### Properties of Relations
1. **Atomic values** – Each cell contains single value
2. **No duplicate tuples** – All rows unique
3. **Order doesn't matter** – Rows/columns unordered
4. **Unique attribute names** – No two columns same name

---

## 📊 ER Model (Entity-Relationship Model)

### Developed by: **Peter Chen (1976)**

### Purpose
- **Conceptual design** tool
- Visual representation before implementation
- Maps real-world to database structure

### 🎭 Analogy
> ER Diagram = **Blueprint before building a house**
> 
> You plan the layout before pouring concrete.

---

## 🔷 ER Model Components

### 1. Entity
- Real-world object with independent existence
- Can be physical (Student, Book) or conceptual (Course, Account)

#### Types:
| Type | Description | Example |
|------|-------------|---------|
| **Strong Entity** | Has its own key | Student (Roll No) |
| **Weak Entity** | No unique key, depends on strong entity | Dependent (of Employee) |

#### Representation:
```
Strong Entity:          Weak Entity:
┌──────────────┐       ╔══════════════╗
│   STUDENT    │       ║  DEPENDENT   ║
└──────────────┘       ╚══════════════╝
  (Rectangle)          (Double Rectangle)
```

### 2. Attributes
- Properties of entities

#### Types:
| Type | Description | Notation | Example |
|------|-------------|----------|---------|
| **Simple** | Atomic, indivisible | ○ | Roll_No |
| **Composite** | Divisible into sub-parts | ○─┬─○ | Name (First, Middle, Last) |
| **Single-valued** | One value per entity | ○ | DOB |
| **Multi-valued** | Multiple values | ◎ (double ellipse) | Phone_Numbers |
| **Derived** | Computed from others | ◦ (dashed ellipse) | Age (from DOB) |
| **Key** | Uniquely identifies entity | <u>○</u> (underlined) | Roll_No |

#### Visual Representation:
```
            ┌── First_Name
            │
Name ───────┼── Middle_Name     (Composite)
            │
            └── Last_Name

 Phone_Numbers                   (Multi-valued)
     ◎

  - - Age - -                   (Derived)
     ◦

   Roll_No                       (Key - Underlined)
   ───────
```

### 3. Relationships
- Association between entities

#### Representation:
```
┌──────────┐         ◇         ┌──────────┐
│ STUDENT  │─────ENROLLS───────│  COURSE  │
└──────────┘                   └──────────┘
              (Diamond shape)
```

#### Degree of Relationship:
| Degree | Entities Involved | Example |
|--------|-------------------|---------|
| Unary | 1 (self-referential) | Employee MANAGES Employee |
| Binary | 2 | Student ENROLLS Course |
| Ternary | 3 | Supplier SUPPLIES Part to Project |
| n-ary | n | Multiple entities |

---

## 🔢 Cardinality Ratios

### What It Means
How many entities of one type can be associated with how many of another.

### Types:

#### 1:1 (One-to-One)
```
PERSON ─────────── HAS ─────────── PASSPORT
  │                                    │
  └── One person has one passport ─────┘
```
**Real Example**: Country - Capital City

#### 1:N (One-to-Many)
```
DEPARTMENT ─────── HAS ─────── EMPLOYEE
     │                            │
     └── One dept has many emps ──┘
```
**Real Example**: Mother - Children

#### M:N (Many-to-Many)
```
STUDENT ─────── ENROLLS ─────── COURSE
    │                              │
    └── Many students, many courses┘
```
**Real Example**: Authors - Books

### 📊 Cardinality Notation Styles

#### Chen Notation:
```
      1        N
DEPT ────────────── EMP
```

#### Crow's Foot Notation:
```
DEPT ──────────┤├── EMP
      one    many
```

#### Min-Max (Participation) Notation:
```
DEPT ──(1,1)────(0,N)── EMP
         │         │
         │         └── An emp belongs to 0 or 1 dept (partial)
         └── A dept has 1 to N employees (total)
```

---

## 🔗 Participation Constraints

### Total Participation (Mandatory)
- **Every** entity must participate
- Denoted by **double line**

```
EMPLOYEE ═══════ WORKS_FOR ─────── DEPARTMENT
    │
    └── Every employee MUST work for a department
```

### Partial Participation (Optional)
- **Some** entities may not participate
- Denoted by **single line**

```
EMPLOYEE ─────── MANAGES ─────── DEPARTMENT
    │
    └── Not every employee manages a department
```

---

## 🔑 Keys in ER Model

### For Strong Entities

| Key Type | Definition | Example |
|----------|------------|---------|
| **Super Key** | Any set that uniquely identifies | {Roll}, {Roll, Name}, {Roll, Name, Dept} |
| **Candidate Key** | Minimal super key | {Roll}, {Email} |
| **Primary Key** | Chosen candidate key | Roll (underlined in ER) |

### For Weak Entities

| Key Type | Definition | Example |
|----------|------------|---------|
| **Partial Key/Discriminator** | Distinguishes weak entities under same owner | Dependent_Name (of an Employee) |

```
                    Partial Key
                        │
┌──────────┐      ╔═════▼═════╗
│ EMPLOYEE │══════║ DEPENDENT ║
└──────────┘      ╚═══════════╝
EmpID (PK)     Dep_Name (Discriminator)

Composite Key of Dependent = (EmpID, Dep_Name)
```

---

## 💪 Weak Entity Deep Dive

### Characteristics
1. **No primary key** on its own
2. **Existence dependent** on strong entity
3. **Identifying relationship** (double diamond)
4. **Double rectangle** notation

### Example:
```
┌──────────┐         ╔════════════════╗
│ BUILDING │◄════════╣     ROOM       ║
└──────────┘  HAS    ╚════════════════╝
    │         ◆◆         │
Building_ID          Room_Number (Partial Key)
(Owner Key)

Room's PK = Building_ID + Room_Number
```

### 🧠 GATE Trick
> **When is an entity weak?**
> 1. Cannot be uniquely identified by its own attributes
> 2. Must "borrow" the key from its owner entity
> 3. Examples: Room (in Building), Dependent (of Employee), Transaction (of Account)

---

## 🎨 Specialization & Generalization

### Generalization (Bottom-Up)
- Combine similar entities into a higher-level entity
- Extract **common attributes**

```
    PERSON (Generalized)
       △
      ╱ ╲
     ╱   ╲
STUDENT  EMPLOYEE
(Specialized entities)
```

### Specialization (Top-Down)
- Divide entity into sub-entities
- Add **specific attributes**

```
    EMPLOYEE
       △
      ╱|╲
     ╱ | ╲
ENGINEER MANAGER TECHNICIAN
   │        │        │
Technical Leadership Practical
  Skills   Role     Skills
```

### Attributes of Specialization

| Type | Description | Notation |
|------|-------------|----------|
| **Disjoint** | Entity can be in only ONE subclass | 'd' in circle |
| **Overlapping** | Entity can be in MULTIPLE subclasses | 'o' in circle |
| **Total** | Every superclass entity MUST be in a subclass | Double line |
| **Partial** | Superclass entity MAY NOT be in any subclass | Single line |

### Example:
```
                EMPLOYEE
                   │
              ┌────┴────┐
              │   (d)   │   ← Disjoint: Can't be both
              ├─────────┤
              ▼         ▼
         PERMANENT   CONTRACT
```

---

## 🔄 Aggregation

### Problem It Solves
Cannot have relationship between relationship and entity in basic ER.

### Solution
Treat a relationship as a **higher-level entity**.

```
Before (Invalid):
EMPLOYEE ── WORKS_ON ── PROJECT
                │
                │ manages (Can't do this!)
                ▼
            MANAGER

After (Aggregation):
┌─────────────────────────────────────┐
│                                     │
│  EMPLOYEE ── WORKS_ON ── PROJECT    │ ← Aggregated into one unit
│                                     │
└──────────────────┬──────────────────┘
                   │
                   │ MANAGES
                   ▼
               MANAGER
```

### 🎭 Real Example
- Employee works on Project (relationship)
- Manager manages this "working" (relationship with relationship)

---

## 📐 ER to Relational Mapping (CRITICAL FOR GATE!)

### Mapping Rules

#### 1. Strong Entity → Table
```
STUDENT(Roll, Name, Age)
   │
   ▼
CREATE TABLE Student (
    Roll INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT
);
```

#### 2. Weak Entity → Table with Owner's Key
```
DEPENDENT(Emp_ID, Dep_Name, DOB)
   │
   ▼
CREATE TABLE Dependent (
    Emp_ID INT,
    Dep_Name VARCHAR(50),
    DOB DATE,
    PRIMARY KEY (Emp_ID, Dep_Name),
    FOREIGN KEY (Emp_ID) REFERENCES Employee(Emp_ID)
);
```

#### 3. 1:1 Relationship → Foreign Key on Either Side (Prefer Total Participation Side)
```
PERSON ──(1,1)──── HAS ────(1,1)── PASSPORT
    │
    ▼
Option 1: Person(PID, Name, Passport_No)  ← FK in Person
Option 2: Passport(Pass_No, Issue_Date, PID) ← FK in Passport
```

#### 4. 1:N Relationship → Foreign Key on 'N' Side
```
DEPT ────(1)──── WORKS_FOR ────(N)── EMPLOYEE
    │
    ▼
Employee(EmpID, Name, Dept_ID)  ← FK in Employee (N side)
```

#### 5. M:N Relationship → New Table with Both PKs
```
STUDENT ──(M)── ENROLLS ──(N)── COURSE
    │
    ▼
Student(Roll, Name)
Course(CourseID, Title)
Enrolls(Roll, CourseID, Grade)  ← New junction table
       PK = (Roll, CourseID)
```

#### 6. Multi-valued Attribute → Separate Table
```
STUDENT with Phone_Numbers (multi-valued)
    │
    ▼
Student(Roll, Name)
Student_Phone(Roll, Phone_Number)  ← Separate table
              PK = (Roll, Phone_Number)
```

#### 7. Composite Attribute → Flatten into Simple Attributes
```
Name(First, Middle, Last)
    │
    ▼
Student(Roll, First_Name, Middle_Name, Last_Name, ...)
```

---

## 📊 Minimum Tables Calculation (GATE Favorite!)

### Formula for Minimum Tables

| Relationship Type | Minimum Tables | Reason |
|-------------------|----------------|--------|
| **1:1 (both total)** | 1 | Can merge all into one table |
| **1:1 (one partial)** | 2 | Can merge relationship with one entity |
| **1:N** | 2 | FK on N side, no extra table needed |
| **M:N** | 3 | Must create junction table |

### GATE Question Pattern:
> "What is the minimum number of tables required for this ER diagram?"

### Example Calculation:
```
ER Diagram:
- 3 Strong Entities: A, B, C
- 1 Weak Entity: D (depends on A)
- 1 Multi-valued attribute on B
- Relationships: A-B (1:N), B-C (M:N)

Calculation:
- A: 1 table
- B: 1 table  
- C: 1 table
- D: 1 table (weak entity needs table)
- Multi-valued attr: 1 table
- A-B (1:N): 0 extra tables (FK on N side)
- B-C (M:N): 1 table (junction table)

Total = 6 tables
```

---

## ⚠️ Common GATE Traps

### Trap 1: Weak Entity Primary Key
❌ Wrong: Weak entity has Partial Key as PK
✅ Right: Weak entity PK = Owner's PK + Partial Key

### Trap 2: Total vs Partial Participation
❌ Wrong: Double line means 1:1 relationship
✅ Right: Double line means total (mandatory) participation

### Trap 3: M:N Relationship Tables
❌ Wrong: M:N relationship needs 2 extra tables
✅ Right: M:N needs exactly 1 junction table

### Trap 4: Derived Attributes
❌ Wrong: Derived attributes stored in table
✅ Right: Derived attributes NOT stored (computed at runtime)

---

## 🔢 Important Formulas

### Maximum Tuples in Relationship

For relationship R between Entity A (with m tuples) and Entity B (with n tuples):

| Cardinality | Max Tuples in R |
|-------------|-----------------|
| 1:1 | min(m, n) |
| 1:N | n |
| M:N | m × n |

### Number of Keys

For n attributes (all candidate keys):
- Super Keys = 2ⁿ - 1 (all non-empty subsets)
- If k is size of candidate key: Super Keys = 2^(n-k) × (2^k - 1 + 1) - 1

---

## 🧪 Practice Problems

### Q1: Minimum Tables
> Given: Entity E1, E2 with M:N relationship and E1 has one multi-valued attribute.

**Answer**: 4 tables
- E1: 1 table
- E2: 1 table
- M:N junction: 1 table
- Multi-valued attribute: 1 table

### Q2: Weak Entity Key
> Weak entity ROOM with partial key Room_No, depending on BUILDING with PK Building_ID. What is ROOM's primary key?

**Answer**: (Building_ID, Room_No)
**Reason**: Weak entity borrows owner's PK

### Q3: Cardinality
> In university: A student can enroll in many courses, a course has many students. What is the cardinality?

**Answer**: M:N (Many-to-Many)

---

## 📌 Chapter Summary

| Concept | Key Points |
|---------|------------|
| **Data Models** | Hierarchical (tree) → Network (graph) → Relational (tables) |
| **ER Model** | Entities, Attributes, Relationships |
| **Weak Entity** | No own key, double rectangle, borrows owner's key |
| **Cardinality** | 1:1, 1:N, M:N |
| **Mapping to Tables** | 1:1/1:N → FK, M:N → junction table |
| **Specialization** | Top-down, add specific attributes |
| **Generalization** | Bottom-up, extract common attributes |

---

## 🎓 Quick Revision Points

1. ✅ Relational Model by **E.F. Codd (1970)**
2. ✅ ER Model by **Peter Chen (1976)**
3. ✅ Weak entity = Double rectangle + Double diamond
4. ✅ Derived attribute = Dashed ellipse (NOT stored)
5. ✅ M:N always needs junction table
6. ✅ 1:N → FK goes on N side
7. ✅ Minimum tables = Count carefully, don't over-count!

---

*Previous: [Introduction to DBMS](./01-Introduction-to-DBMS.md) | Next: [Relational Model](./03-Relational-Model.md)*
