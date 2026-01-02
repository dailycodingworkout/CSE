# 📚 Chapter 02: Entity-Relationship (ER) Model & Enhanced ER (EER)

> **The Atomic Truth**: *Real-world entities mapped to database structure through relationships.*

---

## 🎯 GATE Relevance

| Aspect | Details |
|--------|---------|
| Weightage | 2-4 marks |
| Frequency | 80% years |
| Type | MCQ (conceptual), NAT (counting relationships) |
| Difficulty | Easy to Medium |
| Hot Topics | Participation constraints, Weak entities, Cardinality ratios |

---

## 1. Introduction to ER Model

### What is the ER Model?
The **Entity-Relationship (ER) Model** is a high-level data model that describes the structure of a database using:
- **Entities**: Objects in the real world
- **Attributes**: Properties of entities
- **Relationships**: Associations between entities

### Why ER Model?
1. **Communication Tool**: Between stakeholders and developers
2. **Design Phase**: Before creating actual tables
3. **Abstract View**: Independent of physical storage
4. **Standard Notation**: Universal understanding

### The Mental Model
Think of ER diagrams as a **map of a company**:
- **Entities** = Departments, Employees, Projects (things that exist)
- **Attributes** = Names, IDs, Dates (properties of things)
- **Relationships** = "Works in", "Manages", "Assigned to" (connections)

---

## 2. Entities and Entity Sets

### Entity
An **entity** is a "thing" or "object" in the real world that is distinguishable from other objects.

**Examples:**
- A specific person (John Doe)
- A specific bank account (Account #12345)
- A specific course (CS101)

### Entity Set
An **entity set** is a collection of entities of the same type.

**Examples:**
- All employees in a company
- All bank accounts in a bank
- All courses in a university

### Entity Representation in ER Diagram

```
    ┌────────────────────┐
    │      ENTITY        │     ← Rectangle
    │     (Strong)       │
    └────────────────────┘
    
    ╔════════════════════╗
    ║   WEAK ENTITY      ║     ← Double Rectangle
    ╚════════════════════╝
```

### Strong Entity vs Weak Entity

| Strong Entity | Weak Entity |
|---------------|-------------|
| Has its own primary key | No primary key of its own |
| Exists independently | Depends on owner entity |
| Single rectangle | Double rectangle |
| Example: Employee | Example: Dependent (of Employee) |

### Weak Entity Deep Dive

A **weak entity** is identified by:
1. **Partial Key (Discriminator)**: Attribute that distinguishes among weak entities of same owner
2. **Owner Entity's Primary Key**: From the identifying relationship

```
┌──────────────┐           ╔══════════════╗
│   EMPLOYEE   │═══════════║  DEPENDENT   ║
│   (Strong)   │    Has    ║   (Weak)     ║
│   emp_id(PK) │ (1:N)     ║ dep_name(PK*)║
└──────────────┘           ╚══════════════╝

* Partial Key (Discriminator) - Underlined with dashed line
* Full Key = emp_id + dep_name
```

### GATE Trap Alert! 🚨
**Q**: How many tables for a weak entity?
- **Answer**: Usually 1 table (not 2!)
- The weak entity table includes the owner's primary key as part of its primary key
- Example: `Dependent(emp_id, dep_name, ...)` where (emp_id, dep_name) is the composite PK

---

## 3. Attributes

### Types of Attributes

```
                              ATTRIBUTES
                                  │
        ┌──────────┬──────────────┼────────────────┬───────────┐
        ▼          ▼              ▼                ▼           ▼
     Simple    Composite    Single-valued    Multi-valued   Derived
     (Atomic)                                                
        │          │              │                │           │
        ▼          ▼              ▼                ▼           ▼
    ○ Name     ○─┬─○          ○ DOB          ● Phone      ○- - - Age
               │ └─○                         Numbers      (from DOB)
              Address
             ├─Street
             ├─City
             └─Zip
```

### Attribute Classification Table

| Type | Description | ER Symbol | Example |
|------|-------------|-----------|---------|
| **Simple (Atomic)** | Cannot be divided | ○ (oval) | Roll Number |
| **Composite** | Can be divided into sub-parts | ○ with branches | Name (First + Last) |
| **Single-valued** | One value per entity | ○ | Date of Birth |
| **Multi-valued** | Multiple values per entity | ● (double oval) | Phone Numbers |
| **Derived** | Computed from other attributes | ○--- (dashed oval) | Age (from DOB) |
| **Key Attribute** | Uniquely identifies entity | ○ (underlined) | emp_id |
| **Partial Key** | Identifies weak entity | ○ (dashed underline) | dependent_name |

### Composite Attribute Example

```
                    ○ Name
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
     ○ First     ○ Middle     ○ Last
       Name        Name        Name
```

### Multi-valued Attribute Example

```
        ●══════════╗
        ║ Phone    ║    ← Double oval
        ║ Numbers  ║
        ╚══════════╝
        
Entity: John
Phone Numbers: {9876543210, 9123456789, 8765432190}
```

### GATE Trap Alert! 🚨
**Multi-valued attributes create separate tables!**

If Employee has multi-valued attribute `phone_numbers`:
```sql
-- Main table
Employee(emp_id, name, ...)

-- Separate table for multi-valued attribute
Employee_Phone(emp_id, phone_number)
-- Primary Key: (emp_id, phone_number)
```

**Number of additional tables = Number of multi-valued attributes**

---

## 4. Relationships

### What is a Relationship?
A **relationship** is an association among several entities.

### Relationship Set
A **relationship set** is a set of relationships of the same type.

### Degree of Relationship

| Degree | Name | Description | Example |
|--------|------|-------------|---------|
| 1 | Unary | Entity related to itself | Employee MANAGES Employee |
| 2 | Binary | Two entity sets | Employee WORKS_IN Department |
| 3 | Ternary | Three entity sets | Supplier SUPPLIES Part TO Project |
| n | n-ary | n entity sets | Complex associations |

### Binary Relationship Examples

```
┌──────────────┐              ┌──────────────┐
│   EMPLOYEE   │──────────────│  DEPARTMENT  │
└──────────────┘   Works_In   └──────────────┘
```

### Unary (Recursive) Relationship

```
┌──────────────┐
│   EMPLOYEE   │◄─────┐
└──────────────┘      │ Manages
        │             │
        └─────────────┘
        
One employee manages other employees
Manager is also an employee
```

### Ternary Relationship

```
         ┌──────────────┐
         │   SUPPLIER   │
         └──────┬───────┘
                │
                ▼
         ◇ SUPPLIES ◇
        ╱            ╲
       ▼              ▼
┌──────────┐    ┌──────────┐
│   PART   │    │ PROJECT  │
└──────────┘    └──────────┘
```

---

## 5. Cardinality Ratios (Mapping Cardinalities)

### The Four Cardinality Types

| Type | Meaning | Example |
|------|---------|---------|
| **1:1** (One-to-One) | Each A relates to at most one B, and vice versa | Person HAS Passport |
| **1:N** (One-to-Many) | Each A relates to many B, but each B relates to one A | Department HAS Employees |
| **N:1** (Many-to-One) | Each A relates to one B, but each B relates to many A | Employees WORK_IN Department |
| **M:N** (Many-to-Many) | Each A relates to many B, and vice versa | Students ENROLL Courses |

### Visual Representation

```
1:1 (One-to-One)
┌─────────┐         ┌─────────┐
│ PERSON  │────1───1│PASSPORT │
└─────────┘         └─────────┘
One person has one passport; One passport belongs to one person

1:N (One-to-Many)
┌─────────┐         ┌─────────┐
│  DEPT   │────1───N│EMPLOYEE │
└─────────┘         └─────────┘
One department has many employees; Each employee belongs to one department

M:N (Many-to-Many)
┌─────────┐         ┌─────────┐
│ STUDENT │────M───N│ COURSE  │
└─────────┘         └─────────┘
One student enrolls in many courses; One course has many students
```

### Cardinality and Table Count (Critical for GATE!)

| Cardinality | Tables Needed | Foreign Key Placement |
|-------------|---------------|----------------------|
| **1:1** | 2 or 3 tables | FK on either side (prefer total participation side) |
| **1:N** | 2 tables | FK on the N side |
| **M:N** | 3 tables | Separate junction table with both FKs |

### GATE NAT Pattern: Counting Minimum Tables

**Formula**: 
$$\text{Min Tables} = E + M_{M:N} + M_{multi} - M_{weak}$$

Where:
- $E$ = Number of entity sets
- $M_{M:N}$ = Number of M:N relationships
- $M_{multi}$ = Number of multi-valued attributes
- $M_{weak}$ = Number of weak entity sets (they merge with relationship)

### Example Calculation

```
Entities: Employee, Department, Project (3)
Relationships: 
  - Works_In (Employee-Department, N:1)
  - Works_On (Employee-Project, M:N)
Multi-valued: Phone_Numbers in Employee (1)
Weak Entities: None (0)

Minimum Tables = 3 + 1 + 1 - 0 = 5 tables

Tables:
1. Employee(emp_id, name, dept_id)
2. Department(dept_id, name)
3. Project(proj_id, name)
4. Works_On(emp_id, proj_id)  -- For M:N
5. Emp_Phones(emp_id, phone)  -- For multi-valued
```

---

## 6. Participation Constraints

### Total vs Partial Participation

| Type | Meaning | Symbol | Example |
|------|---------|--------|---------|
| **Total** | Every entity must participate | Double line (═══) | Every employee MUST work in a department |
| **Partial** | Some entities may not participate | Single line (───) | Not every employee manages a department |

### Visual Representation

```
Total Participation (Every employee must be in a department):
┌──────────────┐              ┌──────────────┐
│   EMPLOYEE   │═══════○══════│  DEPARTMENT  │
└──────────────┘   Works_In   └──────────────┘
        ▲
        │
  Double line = Total

Partial Participation (Not every employee manages):
┌──────────────┐              ┌──────────────┐
│   EMPLOYEE   │───────○──────│  DEPARTMENT  │
└──────────────┘   Manages    └──────────────┘
        ▲
        │
  Single line = Partial
```

### Participation Constraints in Relational Schema

| Participation | Constraint in Table |
|---------------|---------------------|
| **Total** | Foreign key is NOT NULL |
| **Partial** | Foreign key can be NULL |

```sql
-- Total participation: Employee MUST be in a department
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    dept_id INT NOT NULL,  -- NOT NULL enforces total participation
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- Partial participation: Employee MAY manage a department
CREATE TABLE Department (
    dept_id INT PRIMARY KEY,
    name VARCHAR(100),
    manager_id INT,  -- Can be NULL (partial participation)
    FOREIGN KEY (manager_id) REFERENCES Employee(emp_id)
);
```

---

## 7. (min, max) Notation

### Alternative to Cardinality Ratios

The **(min, max)** notation specifies:
- **min**: Minimum number of times an entity participates
- **max**: Maximum number of times an entity participates
- **max = *** means unlimited (N)

### Converting Cardinality to (min, max)

```
1:N Relationship with Total Participation on N side:

                  (1,1)              (0,N)
┌──────────────┐────────────◇────────────┌──────────────┐
│   EMPLOYEE   │         Works_In        │  DEPARTMENT  │
└──────────────┘                         └──────────────┘

Employee side (1,1): Each employee works in minimum 1, maximum 1 department
Department side (0,N): Each department has minimum 0, maximum N employees
```

### (min, max) Quick Reference

| Notation | Meaning |
|----------|---------|
| (0, 1) | Optional, at most one |
| (1, 1) | Mandatory, exactly one |
| (0, N) or (0, *) | Optional, any number |
| (1, N) or (1, *) | Mandatory, any number |
| (2, 5) | Between 2 and 5 |

### GATE Trap Alert! 🚨
**(min, max) is placed on the OPPOSITE side in some notations!**

In Chen notation (common in GATE):
- Numbers are placed near the entity they describe
- (1,1) near Employee means each employee participates once

In Crow's Foot notation:
- Symbols are placed at the opposite end
- This causes confusion - always check the convention!

---

## 8. ER to Relational Mapping Algorithm

### Step-by-Step Conversion Rules

#### Step 1: Map Strong Entity Sets
- Create a table for each strong entity
- Simple attributes become columns
- Choose one candidate key as primary key
- Composite attributes: Include only leaf attributes

```
Entity: EMPLOYEE(emp_id, name(first, last), address)
Table:  Employee(emp_id, first_name, last_name, address)
```

#### Step 2: Map Weak Entity Sets
- Create table with all simple attributes
- Include primary key of owner entity
- Primary key = Owner PK + Partial Key

```
Weak Entity: DEPENDENT(name, birth_date) of EMPLOYEE
Table: Dependent(emp_id, name, birth_date)
       Primary Key: (emp_id, name)
```

#### Step 3: Map Binary 1:1 Relationships
**Option A**: Foreign key approach (preferred)
- Add primary key of one entity to the other as foreign key
- Prefer the side with total participation

**Option B**: Merged table (if both have total participation)
- Merge both entities into single table

```
EMPLOYEE ──1───1── PASSPORT
Option A: Passport(passport_id, ..., emp_id FK)
```

#### Step 4: Map Binary 1:N Relationships
- Add primary key of "1" side to "N" side as foreign key
- Include relationship attributes in "N" side table

```
DEPARTMENT ──1───N── EMPLOYEE
Table: Employee(..., dept_id FK)
```

#### Step 5: Map Binary M:N Relationships
- Create a new junction/association table
- Include primary keys of both entities (composite PK)
- Include relationship attributes

```
STUDENT ──M───N── COURSE with attribute "grade"
New Table: Enrollment(student_id, course_id, grade)
           Primary Key: (student_id, course_id)
```

#### Step 6: Map Multi-valued Attributes
- Create separate table
- Include primary key of entity + multi-valued attribute

```
EMPLOYEE with Phone_Numbers (multi-valued)
New Table: Emp_Phone(emp_id, phone_number)
           Primary Key: (emp_id, phone_number)
```

#### Step 7: Map n-ary Relationships (n > 2)
- Create relationship table with PKs of all participating entities
- Primary key depends on cardinality constraints

```
SUPPLIER ──── SUPPLIES ──── PART ──── PROJECT
Table: Supplies(supplier_id, part_id, project_id, quantity)
       Primary Key: Depends on functional dependencies
```

---

## 9. Enhanced ER (EER) Model

### Specialization (Top-Down)
**Definition**: Defining subclasses based on distinguishing characteristics

```
                    ┌───────────────┐
                    │    PERSON     │
                    │   (General)   │
                    └───────┬───────┘
                            │
                           ◯ d    ← Disjoint constraint
                          ╱ ╲
                         ╱   ╲
           ┌────────────┐     ┌────────────┐
           │  EMPLOYEE  │     │  CUSTOMER  │
           │(Specialized)│     │(Specialized)│
           └────────────┘     └────────────┘
```

### Generalization (Bottom-Up)
**Definition**: Abstracting common features from multiple entity sets

```
           ┌────────────┐     ┌────────────┐
           │    CAR     │     │   TRUCK    │
           └──────┬─────┘     └─────┬──────┘
                  │                 │
                  └────────┬────────┘
                           │
                          ◯ ← Generalization
                           │
                    ┌──────┴──────┐
                    │   VEHICLE   │
                    │  (General)  │
                    └─────────────┘
```

### Disjoint vs Overlapping Constraints

| Constraint | Meaning | Symbol | Example |
|------------|---------|--------|---------|
| **Disjoint (d)** | Entity can be in only one subclass | d in circle | Person is either Employee OR Customer |
| **Overlapping (o)** | Entity can be in multiple subclasses | o in circle | Person can be both Student AND Employee |

### Total vs Partial Specialization

| Constraint | Meaning | Symbol | Example |
|------------|---------|--------|---------|
| **Total** | Every superclass entity must be in at least one subclass | Double line | Every person MUST be employee or customer |
| **Partial** | Superclass entity may not be in any subclass | Single line | Some vehicles may not be car or truck |

### EER to Relational Mapping Options

#### Option 1: Single Table with Type
```sql
CREATE TABLE Person (
    person_id INT PRIMARY KEY,
    name VARCHAR(100),
    type ENUM('EMPLOYEE', 'CUSTOMER'),
    -- Employee-specific attributes (NULL for customers)
    salary DECIMAL(10,2),
    -- Customer-specific attributes (NULL for employees)
    credit_limit DECIMAL(10,2)
);
```
- **Pros**: Simple, single table
- **Cons**: Many NULL values, constraint enforcement difficult

#### Option 2: Separate Tables (Most Common)
```sql
CREATE TABLE Person (
    person_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Employee (
    person_id INT PRIMARY KEY,
    salary DECIMAL(10,2),
    FOREIGN KEY (person_id) REFERENCES Person(person_id)
);

CREATE TABLE Customer (
    person_id INT PRIMARY KEY,
    credit_limit DECIMAL(10,2),
    FOREIGN KEY (person_id) REFERENCES Person(person_id)
);
```
- **Pros**: No NULL values, clean design
- **Cons**: Requires joins to get complete info

#### Option 3: Subclass Tables Only (for Total Specialization)
```sql
CREATE TABLE Employee (
    person_id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2)
);

CREATE TABLE Customer (
    person_id INT PRIMARY KEY,
    name VARCHAR(100),
    credit_limit DECIMAL(10,2)
);
```
- **Pros**: No superclass table needed
- **Cons**: Duplicate attributes, harder to enforce across subclasses

---

## 10. Aggregation

### What is Aggregation?
**Aggregation** is an abstraction that treats a relationship as an entity, allowing relationships between relationships.

### When to Use Aggregation?
When you need to express a relationship between:
1. An entity set
2. A relationship set (not just entities)

### Example: Sponsorship of Employee-Project Work

```
Without Aggregation (Cannot express properly):
Employee ─── Works_On ─── Project
                ↑
                │ Sponsored_By?
                ↓
            Sponsor

With Aggregation:
┌─────────────────────────────────────────┐
│         ┌─────────────────────────┐     │
│         │      Works_On           │     │
│   ┌─────┤                         ├───┐ │
│   │ EMP └─────────────────────────┘PRJ│ │
│   └───────────────────────────────────┘ │
│              (Aggregated)               │
└────────────────────┬────────────────────┘
                     │
                     │ Sponsored_By
                     ▼
              ┌───────────┐
              │  SPONSOR  │
              └───────────┘
```

### Aggregation to Relational Mapping
- Create table for the inner relationship as usual
- Create table for outer relationship including:
  - Primary key of aggregated relationship
  - Primary key of other entity
  - Relationship attributes

```sql
-- Inner relationship
Works_On(emp_id, proj_id, hours)
Primary Key: (emp_id, proj_id)

-- Outer relationship using aggregation
Sponsorship(emp_id, proj_id, sponsor_id, amount)
Primary Key: (emp_id, proj_id, sponsor_id)
Foreign Key: (emp_id, proj_id) REFERENCES Works_On
Foreign Key: (sponsor_id) REFERENCES Sponsor
```

---

## 11. Minimum Tables Formula (GATE NAT Favorite!)

### The Master Formula

$$\text{Minimum Tables} = E - W - 1:1_{merged} + R_{M:N} + R_{ternary+} + M$$

Where:
- $E$ = Number of entity sets
- $W$ = Number of weak entity sets (merged with identifying relationship)
- $1:1_{merged}$ = Number of 1:1 relationships where entities can merge
- $R_{M:N}$ = Number of M:N relationships
- $R_{ternary+}$ = Number of n-ary relationships (n ≥ 3)
- $M$ = Number of multi-valued attributes

### Quick Counting Rules

| Element | Effect on Table Count |
|---------|----------------------|
| Strong Entity | +1 table |
| Weak Entity | +1 table (includes identifying relationship) |
| 1:1 Relationship | +0 tables (FK approach) or -1 if merged |
| 1:N Relationship | +0 tables (FK in N side) |
| M:N Relationship | +1 table (junction table) |
| Ternary Relationship | +1 table |
| Multi-valued Attribute | +1 table per attribute |
| Composite Attribute | +0 tables (flattened) |
| Derived Attribute | +0 tables (not stored) |

### GATE Example Problem

**Given ER Diagram:**
- 3 Strong entities: E1, E2, E3
- 1 Weak entity: W1 (depends on E1)
- Relationships:
  - R1(E1, E2): 1:1
  - R2(E2, E3): M:N
  - R3(E1, W1): Identifying (1:N)
- Multi-valued: E1 has "phones"

**Solution:**
```
Entities: 3 + 1 = 4

Tables:
- E1: 1 table
- E2: 1 table  
- E3: 1 table
- W1: 1 table (includes E1's PK from R3)
- R1: 0 additional (FK in E1 or E2)
- R2: 1 additional (M:N junction)
- R3: 0 additional (absorbed in W1)
- phones: 1 additional (multi-valued)

Total = 4 + 1 + 1 = 6 tables
```

---

## 12. ER Diagram Symbols Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                    ER DIAGRAM SYMBOLS                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ENTITIES                                                        │
│  ┌───────────┐  Strong Entity                                   │
│  └───────────┘                                                   │
│                                                                  │
│  ╔═══════════╗  Weak Entity                                     │
│  ╚═══════════╝                                                   │
│                                                                  │
│  RELATIONSHIPS                                                   │
│       ◇         Binary Relationship                             │
│      ◇◇         Identifying Relationship (for weak entity)      │
│                                                                  │
│  ATTRIBUTES                                                      │
│      ○         Simple Attribute                                 │
│      ○         Key Attribute (with underline)                   │
│     ●          Multi-valued Attribute (double oval)             │
│    ○---        Derived Attribute (dashed oval)                  │
│     ○─┬─○      Composite Attribute                              │
│       └─○                                                        │
│                                                                  │
│  CARDINALITY                                                     │
│    ──1──1──    One-to-One                                       │
│    ──1──N──    One-to-Many                                      │
│    ──M──N──    Many-to-Many                                     │
│                                                                  │
│  PARTICIPATION                                                   │
│    ────────    Partial Participation                            │
│    ════════    Total Participation                              │
│                                                                  │
│  EER CONSTRAINTS                                                 │
│      ◯ d       Disjoint Specialization                          │
│      ◯ o       Overlapping Specialization                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 13. Common GATE Questions & Patterns

### Pattern 1: Counting Minimum Tables
**Q**: Given an ER diagram with 4 entities, 2 M:N relationships, 1 multi-valued attribute, and 1 weak entity, find minimum tables.
**A**: 4 + 2 + 1 = 7 (weak entity is counted in the 4)

### Pattern 2: Weak Entity Identification
**Q**: Which of the following is true about weak entities?
- They always have total participation in identifying relationship ✓
- They cannot have their own attributes ✗
- They can exist without owner entity ✗
- They need partial key (discriminator) ✓

### Pattern 3: Cardinality from Business Rules
**Q**: "Each student can enroll in many courses. Each course can have many students enrolled."
**A**: M:N relationship

### Pattern 4: EER Constraints
**Q**: A person can be both a student and an employee. Which constraint applies?
**A**: Overlapping (o)

---

## 14. Edge Cases & Tricky Scenarios

### Edge Case 1: Self-Referencing M:N
```
Employee ──M:N── Employee (Collaboration)

Table: Collaboration(emp_id1, emp_id2, project)
Both columns reference Employee.emp_id
Need to ensure emp_id1 ≠ emp_id2 (or allow it based on semantics)
```

### Edge Case 2: Multiple Relationships Between Same Entities
```
Employee ──Works_In── Department
Employee ──Manages── Department

Two separate relationships = Two FK considerations
```

### Edge Case 3: Ternary vs Three Binary
```
Ternary: Supplier-Part-Project (single relationship)
- Captures: "Supplier S supplies Part P to Project J"

Three Binary:
- Supplier-Part: S can supply P
- Part-Project: P is used in J  
- Supplier-Project: S works with J

NOT EQUIVALENT! Ternary captures specific combination
```

### Edge Case 4: Total Participation on Both Sides of 1:1
```
A ══1══1══ B (Both total)

Can merge into single table if semantically one entity
```

---

## 15. Practice Problems

### Problem 1: ER to Tables
Convert the following to relational schema:
- Entity: STUDENT (roll_no, name, phones)
- Entity: COURSE (code, title)
- Relationship: ENROLLS (M:N) with attribute grade

**Solution:**
```sql
Student(roll_no, name)
Student_Phones(roll_no, phone)
Course(code, title)
Enrollment(roll_no, code, grade)
```
Total: 4 tables

### Problem 2: Identify Weak Entity
In a hospital system:
- PATIENT (patient_id, name)
- ADMISSION (admission_date, diagnosis)

Is ADMISSION weak?

**Solution:** Yes, if admission is identified by patient_id + admission_date
- Full key: (patient_id, admission_date)
- Partial key: admission_date

### Problem 3: Cardinality Determination
"A book is written by one or more authors. An author can write many books."

**Solution:** M:N (Many-to-Many)
- Each book: 1 or more authors (min 1, max N)
- Each author: 0 or more books (min 0, max N)

---

## 🧠 Memory Techniques

### Weak Entity Mnemonic: "WEAK = Without External Attributes for Keys"
- **W**ithout own primary key
- **E**xistentially dependent
- **A**lways has identifying relationship
- **K**ey = Owner's key + Discriminator

### Cardinality Mnemonic: "1 is Lonely, N is iNfinite"
- 1:1 = One lonely partner each
- 1:N = One has iNfinite partners
- M:N = Multiple choose Multiple

### EER Mnemonic: "DOT" for constraints
- **D**isjoint = Different categories (either/or)
- **O**verlapping = Overlapping categories (both/and)
- **T**otal = Take all (everyone must specialize)

---

## 🔑 Key Takeaways for GATE

1. **Table Counting**: Master the formula - it appears almost every year
2. **Weak Entity**: Understand discriminator vs full key
3. **M:N Always Needs Junction Table**: No exceptions
4. **Multi-valued = New Table**: One per multi-valued attribute
5. **Participation → NOT NULL**: Total participation means NOT NULL FK
6. **EER Mapping**: Know all three options for specialization

---

## 📚 Related Chapters
- [← Previous: Chapter 01 - Introduction](../01-Introduction-to-DBMS/README.md)
- [Next: Chapter 03 - Relational Model →](../03-Relational-Model/README.md)

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**
