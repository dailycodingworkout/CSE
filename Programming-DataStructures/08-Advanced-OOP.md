# Chapter 8: Advanced OOP and Design Concepts

## The Singularity | First Principles

> **The Atomic Truth:** "Good design = Low coupling, high cohesion."

---

## 8.1 Composition vs Inheritance

### Inheritance: IS-A

```cpp
class Dog : public Animal {
    // Dog IS-A Animal
};
```

### Composition: HAS-A

```cpp
class Car {
    Engine engine;    // Car HAS-A Engine
    Wheel wheels[4];  // Car HAS-A set of Wheels
};
```

### When to Use Which?

| Use Inheritance When | Use Composition When |
|---------------------|---------------------|
| True IS-A relationship | HAS-A relationship |
| Need polymorphism | Need to change behavior at runtime |
| Derived is a specialization | Relationship can change |
| Interface reuse | Implementation reuse |

### The Composition Over Inheritance Principle

**"Favor composition over inheritance"** - Gang of Four

**Why?**
1. **Flexibility**: Can change composed objects at runtime
2. **Encapsulation**: No exposure of base class internals
3. **Reuse**: Can compose any compatible object

---

## 8.2 Aggregation vs Composition

### Composition (Strong HAS-A)

Parts **cannot exist** without the whole.

```cpp
class House {
    Room rooms[5];  // Rooms are part of House
    // When House is destroyed, Rooms are destroyed
};
```

**Lifetime**: Same as container.

### Aggregation (Weak HAS-A)

Parts **can exist** independently.

```cpp
class Team {
    vector<Player*> players;  // Players exist independently
    // Players can belong to other teams
};
```

**Lifetime**: Independent.

### UML Representation

```
Composition:   [Container]◆─────────[Part]
                          (filled diamond)

Aggregation:   [Container]◇─────────[Part]
                          (empty diamond)

Association:   [Class A]────────────[Class B]
                          (plain line)
```

---

## 8.3 Shallow Copy vs Deep Copy

### Shallow Copy

Copies the values of data members directly. Pointers are copied, not what they point to.

```cpp
class Shallow {
    int* data;
public:
    Shallow(int val) {
        data = new int(val);
    }
    
    // Default copy constructor does shallow copy
    // Shallow(const Shallow& s) { data = s.data; }  // Just copies pointer!
};

Shallow s1(10);
Shallow s2 = s1;  // Both point to SAME memory!
```

**Problem**: Both objects point to same memory → Double delete!

### Deep Copy

Creates independent copies of all dynamically allocated memory.

```cpp
class Deep {
    int* data;
public:
    Deep(int val) {
        data = new int(val);
    }
    
    // Deep copy constructor
    Deep(const Deep& d) {
        data = new int(*d.data);  // Allocate new memory
    }
    
    // Deep copy assignment
    Deep& operator=(const Deep& d) {
        if(this != &d) {
            delete data;           // Free old memory
            data = new int(*d.data); // Allocate new
        }
        return *this;
    }
    
    ~Deep() {
        delete data;
    }
};
```

### The Rule of Three/Five

**Rule of Three (C++98)**: If you define one, define all three:
1. Destructor
2. Copy constructor
3. Copy assignment operator

**Rule of Five (C++11)**: Add:
4. Move constructor
5. Move assignment operator

---

## 8.4 Move Semantics (C++11)

### The Problem with Copies

```cpp
vector<int> createVector() {
    vector<int> v = {1, 2, 3, 4, 5};
    return v;  // Copy of entire vector? Expensive!
}
```

### Move Constructor

```cpp
class Buffer {
    int* data;
    size_t size;
public:
    // Move constructor
    Buffer(Buffer&& other) noexcept 
        : data(other.data), size(other.size) {
        other.data = nullptr;  // Leave source in valid state
        other.size = 0;
    }
    
    // Move assignment
    Buffer& operator=(Buffer&& other) noexcept {
        if(this != &other) {
            delete[] data;
            data = other.data;
            size = other.size;
            other.data = nullptr;
            other.size = 0;
        }
        return *this;
    }
};
```

### lvalue vs rvalue

| lvalue | rvalue |
|--------|--------|
| Has address | Temporary |
| Can appear on left of = | Cannot appear on left of = |
| Named variable | Expression result |

```cpp
int x = 10;       // x is lvalue, 10 is rvalue
int y = x + 5;    // y is lvalue, x+5 is rvalue
```

### std::move

Casts lvalue to rvalue reference.

```cpp
Buffer b1;
Buffer b2 = std::move(b1);  // Forces move instead of copy
// b1 is now in "moved-from" state
```

---

## 8.5 Smart Pointers

### The Problem with Raw Pointers

```cpp
void func() {
    int* p = new int(10);
    // ... some code ...
    if(condition) return;  // Memory leak!
    delete p;
}
```

### unique_ptr (C++11)

Exclusive ownership - only one owner.

```cpp
#include <memory>

unique_ptr<int> p1 = make_unique<int>(10);  // C++14
// unique_ptr<int> p2 = p1;  // ERROR! Cannot copy
unique_ptr<int> p2 = std::move(p1);  // OK, transfers ownership
// p1 is now nullptr
```

**Use when**: Single ownership, no sharing needed.

### shared_ptr (C++11)

Reference-counted shared ownership.

```cpp
shared_ptr<int> p1 = make_shared<int>(10);
shared_ptr<int> p2 = p1;  // Both own the resource
cout << p1.use_count();   // 2

p1.reset();  // p1 releases ownership
cout << p2.use_count();   // 1
// Resource deleted when last shared_ptr destroyed
```

**Use when**: Multiple owners needed.

### weak_ptr (C++11)

Non-owning observer, breaks circular references.

```cpp
shared_ptr<int> sp = make_shared<int>(10);
weak_ptr<int> wp = sp;  // Doesn't increase ref count

if(auto p = wp.lock()) {  // Get shared_ptr if still exists
    cout << *p;
}
```

**Use when**: Observing without ownership, breaking cycles.

---

## 8.6 Object-Oriented Design Principles (SOLID)

### S - Single Responsibility Principle

A class should have only ONE reason to change.

```cpp
// BAD: Multiple responsibilities
class Employee {
    void calculatePay();     // Accounting
    void save();             // Database
    void generateReport();   // Reporting
};

// GOOD: Separated responsibilities
class Employee { /* core data */ };
class PayCalculator { void calculate(Employee&); };
class EmployeeRepository { void save(Employee&); };
class ReportGenerator { void generate(Employee&); };
```

### O - Open/Closed Principle

Open for extension, closed for modification.

```cpp
// BAD: Modify class for new shapes
class AreaCalculator {
    double calculate(Object obj) {
        if(obj.type == "circle") { ... }
        else if(obj.type == "rectangle") { ... }
        // Must modify for new shapes!
    }
};

// GOOD: Extend through inheritance
class Shape { virtual double area() = 0; };
class Circle : public Shape { double area() override; };
class Rectangle : public Shape { double area() override; };
// New shapes don't require modifying existing code
```

### L - Liskov Substitution Principle

Derived classes must be substitutable for base classes.

```cpp
// BAD: Square violates LSP for Rectangle
class Rectangle {
    virtual void setWidth(int w) { width = w; }
    virtual void setHeight(int h) { height = h; }
};

class Square : public Rectangle {
    void setWidth(int w) override { width = height = w; }
    void setHeight(int h) override { width = height = h; }
    // Changing width changes height - unexpected!
};
```

### I - Interface Segregation Principle

Clients shouldn't depend on interfaces they don't use.

```cpp
// BAD: Fat interface
class Worker {
    virtual void work() = 0;
    virtual void eat() = 0;
};
// Robot can't eat!

// GOOD: Segregated interfaces
class Workable { virtual void work() = 0; };
class Eatable { virtual void eat() = 0; };

class Human : public Workable, public Eatable { ... };
class Robot : public Workable { ... };  // Only implements what it needs
```

### D - Dependency Inversion Principle

High-level modules shouldn't depend on low-level modules. Both should depend on abstractions.

```cpp
// BAD: High-level depends on low-level
class MySQLDatabase { void save(); };
class UserService {
    MySQLDatabase db;  // Tight coupling!
};

// GOOD: Both depend on abstraction
class Database { virtual void save() = 0; };
class MySQLDatabase : public Database { void save() override; };
class MongoDatabase : public Database { void save() override; };

class UserService {
    Database* db;  // Abstraction - can be any database!
};
```

---

## 8.7 Common Design Patterns | GATE Focus

### 1. Singleton Pattern

Ensure only one instance of a class exists.

```cpp
class Singleton {
    static Singleton* instance;
    Singleton() {}  // Private constructor
    
public:
    static Singleton* getInstance() {
        if(!instance)
            instance = new Singleton();
        return instance;
    }
    
    // Delete copy and assignment
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;
};

Singleton* Singleton::instance = nullptr;
```

**Use case**: Database connection, logger, configuration.

### 2. Factory Pattern

Create objects without specifying exact class.

```cpp
class Shape { virtual void draw() = 0; };
class Circle : public Shape { void draw() override; };
class Rectangle : public Shape { void draw() override; };

class ShapeFactory {
public:
    static Shape* create(string type) {
        if(type == "circle") return new Circle();
        if(type == "rectangle") return new Rectangle();
        return nullptr;
    }
};

Shape* s = ShapeFactory::create("circle");
```

### 3. Observer Pattern

One-to-many dependency; when one changes, all dependents notified.

```cpp
class Observer {
public:
    virtual void update(int value) = 0;
};

class Subject {
    vector<Observer*> observers;
    int state;
public:
    void attach(Observer* o) { observers.push_back(o); }
    void setState(int s) {
        state = s;
        for(auto o : observers)
            o->update(state);
    }
};
```

**Use case**: Event handling, UI updates.

### 4. Strategy Pattern

Define family of algorithms, make them interchangeable.

```cpp
class SortStrategy {
public:
    virtual void sort(vector<int>&) = 0;
};

class BubbleSort : public SortStrategy {
    void sort(vector<int>& arr) override { /* bubble sort */ }
};

class QuickSort : public SortStrategy {
    void sort(vector<int>& arr) override { /* quick sort */ }
};

class Sorter {
    SortStrategy* strategy;
public:
    void setStrategy(SortStrategy* s) { strategy = s; }
    void sort(vector<int>& arr) { strategy->sort(arr); }
};
```

---

## 8.8 Templates | Generic Programming

### Function Templates

```cpp
template<typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

int m1 = maximum(10, 20);        // T = int
double m2 = maximum(3.14, 2.71); // T = double
```

### Class Templates

```cpp
template<typename T>
class Stack {
    T arr[100];
    int top;
public:
    Stack() : top(-1) {}
    void push(T val) { arr[++top] = val; }
    T pop() { return arr[top--]; }
};

Stack<int> intStack;
Stack<string> stringStack;
```

### Template Specialization

```cpp
template<typename T>
class Printer {
public:
    void print(T val) { cout << val; }
};

// Specialization for bool
template<>
class Printer<bool> {
public:
    void print(bool val) { cout << (val ? "true" : "false"); }
};
```

---

## 8.9 Exception Handling

### Basic Syntax

```cpp
try {
    // Code that might throw
    if(error_condition)
        throw exception();
}
catch(const exception& e) {
    // Handle exception
    cout << e.what();
}
catch(...) {
    // Catch all exceptions
}
```

### Custom Exceptions

```cpp
class InvalidAgeException : public exception {
    string message;
public:
    InvalidAgeException(int age) {
        message = "Invalid age: " + to_string(age);
    }
    const char* what() const noexcept override {
        return message.c_str();
    }
};

void setAge(int age) {
    if(age < 0 || age > 150)
        throw InvalidAgeException(age);
}
```

### Exception Safety Guarantees

| Level | Guarantee |
|-------|-----------|
| No-throw | Operation never throws |
| Strong | If exception, state unchanged |
| Basic | If exception, no resources leaked |
| No guarantee | Anything can happen |

---

## 8.10 Memory Management Best Practices

### RAII (Resource Acquisition Is Initialization)

```cpp
class FileHandler {
    FILE* file;
public:
    FileHandler(const char* name) {
        file = fopen(name, "r");
        if(!file) throw runtime_error("Cannot open file");
    }
    
    ~FileHandler() {
        if(file) fclose(file);  // Always cleaned up
    }
};

void process() {
    FileHandler fh("data.txt");  // Opened
    // ... work with file ...
}  // Automatically closed, even if exception thrown
```

### Common Memory Errors

| Error | Cause | Prevention |
|-------|-------|------------|
| Memory leak | Not freeing allocated memory | Use smart pointers, RAII |
| Double free | Freeing same memory twice | Set to nullptr after free |
| Dangling pointer | Using freed memory | Smart pointers, careful lifetime management |
| Buffer overflow | Writing beyond allocated | Bounds checking, safe functions |

---

## 8.11 GATE-Focused Concepts

### Virtual Table Questions

```cpp
class A {
public:
    virtual void f1() { cout << "A::f1"; }
    virtual void f2() { cout << "A::f2"; }
};

class B : public A {
public:
    void f1() override { cout << "B::f1"; }
    void f3() { cout << "B::f3"; }
};
```

**Question**: How many entries in B's vtable?
**Answer**: 3 (f1 → B::f1, f2 → A::f2, f3 → B::f3)

### Template Instantiation

```cpp
template<typename T>
class Container {
    T data;
};

Container<int> c1;     // Instantiates Container<int>
Container<double> c2;  // Instantiates Container<double>
```

**Question**: How many class definitions generated?
**Answer**: 2 (one for each type)

### Exception Handling Flow

```cpp
void f3() { throw runtime_error("Error"); }
void f2() { f3(); }
void f1() {
    try { f2(); }
    catch(exception& e) { cout << "Caught"; }
}
```

**Execution**: f3 throws → f2 propagates → f1 catches

---

## 8.12 Practice Problems

### Q1 (Output)

```cpp
class Base {
public:
    Base() { cout << "B "; }
    virtual ~Base() { cout << "~B "; }
};

class Derived : public Base {
public:
    Derived() { cout << "D "; }
    ~Derived() { cout << "~D "; }
};

int main() {
    Base* p = new Derived();
    delete p;
    return 0;
}
```

**Answer**: `B D ~D ~B `

### Q2 (Smart Pointer)

```cpp
shared_ptr<int> p1 = make_shared<int>(10);
shared_ptr<int> p2 = p1;
shared_ptr<int> p3 = p1;
cout << p1.use_count();
```

**Answer**: 3

### Q3 (Template)

```cpp
template<typename T>
T add(T a, T b) { return a + b; }

int main() {
    cout << add(5, 3) << " ";
    cout << add(2.5, 1.5);
    return 0;
}
```

**Answer**: `8 4` (or `8 4.0` depending on output format)

### Q4 (Exception)

```cpp
int main() {
    try {
        cout << "1 ";
        throw 42;
        cout << "2 ";
    }
    catch(int e) {
        cout << "3 ";
    }
    cout << "4";
    return 0;
}
```

**Answer**: `1 3 4`

---

## 8.13 Quick Reference

### Design Principles Summary

| Principle | Meaning |
|-----------|---------|
| SRP | One reason to change |
| OCP | Extend, don't modify |
| LSP | Subtypes substitutable |
| ISP | Small, specific interfaces |
| DIP | Depend on abstractions |

### Smart Pointer Comparison

| Type | Ownership | Copyable | Use Case |
|------|-----------|----------|----------|
| unique_ptr | Exclusive | No (move only) | Single owner |
| shared_ptr | Shared | Yes | Multiple owners |
| weak_ptr | Observer | N/A | Break cycles |

### Memory Management Rules

1. **Match new with delete** (new[] with delete[])
2. **RAII for all resources**
3. **Prefer smart pointers over raw**
4. **Virtual destructor for polymorphic classes**
5. **Rule of Three/Five for custom resource management**

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Advanced]**

*Next: [Chapter 9: Problem Solving Techniques for GATE →](09-Problem-Solving-Techniques.md)*
