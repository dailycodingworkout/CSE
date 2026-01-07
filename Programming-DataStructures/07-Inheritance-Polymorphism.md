# Chapter 7: Inheritance and Polymorphism

## The Singularity | First Principles

> **The Atomic Truth:** "Inheritance = IS-A relationship. Polymorphism = Same interface, different behavior."

---

## 7.1 Inheritance | The Foundation

### What is Inheritance?

Inheritance is a mechanism where a **derived class** (child) acquires properties and behaviors from a **base class** (parent).

```cpp
class Animal {           // Base class
public:
    void eat() { cout << "Eating..." << endl; }
};

class Dog : public Animal {   // Derived class
public:
    void bark() { cout << "Barking..." << endl; }
};

Dog d;
d.eat();   // Inherited from Animal
d.bark();  // Dog's own method
```

### The IS-A Relationship

- Dog **IS-A** Animal ✅
- Car **IS-A** Vehicle ✅
- Engine **IS-A** Car ❌ (Engine is PART-OF Car → Composition)

---

## 7.2 Types of Inheritance

### 1. Single Inheritance

One derived class inherits from one base class.

```
    ┌─────────┐
    │  Base   │
    └────┬────┘
         │
    ┌────┴────┐
    │ Derived │
    └─────────┘
```

```cpp
class Animal { };
class Dog : public Animal { };
```

### 2. Multiple Inheritance

One class inherits from multiple base classes.

```
┌─────────┐   ┌─────────┐
│ Base1   │   │ Base2   │
└────┬────┘   └────┬────┘
     │             │
     └──────┬──────┘
       ┌────┴────┐
       │ Derived │
       └─────────┘
```

```cpp
class Printable { 
    void print() { }
};
class Serializable { 
    void save() { }
};
class Document : public Printable, public Serializable { };
```

### 3. Multilevel Inheritance

Chain of inheritance.

```
    ┌─────────┐
    │ Animal  │
    └────┬────┘
         │
    ┌────┴────┐
    │ Mammal  │
    └────┬────┘
         │
    ┌────┴────┐
    │   Dog   │
    └─────────┘
```

```cpp
class Animal { };
class Mammal : public Animal { };
class Dog : public Mammal { };
```

### 4. Hierarchical Inheritance

Multiple classes inherit from one base class.

```
         ┌─────────┐
         │ Animal  │
         └────┬────┘
     ┌────────┼────────┐
┌────┴────┐ ┌─┴─┐ ┌────┴────┐
│   Dog   │ │Cat│ │  Bird   │
└─────────┘ └───┘ └─────────┘
```

```cpp
class Animal { };
class Dog : public Animal { };
class Cat : public Animal { };
class Bird : public Animal { };
```

### 5. Hybrid Inheritance

Combination of multiple types.

```
         ┌─────────┐
         │ Animal  │
         └────┬────┘
     ┌────────┴────────┐
┌────┴────┐      ┌────┴────┐
│ Mammal  │      │  Bird   │
└────┬────┘      └────┬────┘
     │                │
     └────────┬───────┘
         ┌────┴────┐
         │   Bat   │   (Mammal + Bird-like features)
         └─────────┘
```

**Warning**: Can lead to Diamond Problem.

---

## 7.3 Access Specifiers in Inheritance

### Inheritance Modes

```cpp
class Derived : public Base { };     // Public inheritance
class Derived : protected Base { };  // Protected inheritance
class Derived : private Base { };    // Private inheritance (default)
```

### Access Table

| Base Member | public inheritance | protected inheritance | private inheritance |
|-------------|-------------------|----------------------|---------------------|
| public | public | protected | private |
| protected | protected | protected | private |
| private | not accessible | not accessible | not accessible |

### The Rule

**Inheritance mode sets the maximum accessibility in derived class.**

### Practical Example

```cpp
class Base {
public:
    int x;
protected:
    int y;
private:
    int z;
};

class PublicDerived : public Base {
    // x is public, y is protected, z is NOT accessible
};

class ProtectedDerived : protected Base {
    // x is protected, y is protected, z is NOT accessible
};

class PrivateDerived : private Base {
    // x is private, y is private, z is NOT accessible
};
```

---

## 7.4 Constructors and Destructors in Inheritance

### Order of Execution

```
Construction: Base first, then Derived
Destruction: Derived first, then Base
```

```cpp
class Base {
public:
    Base() { cout << "Base Constructor" << endl; }
    ~Base() { cout << "Base Destructor" << endl; }
};

class Derived : public Base {
public:
    Derived() { cout << "Derived Constructor" << endl; }
    ~Derived() { cout << "Derived Destructor" << endl; }
};

int main() {
    Derived d;
    return 0;
}
```

**Output**:
```
Base Constructor
Derived Constructor
Derived Destructor
Base Destructor
```

### Passing Arguments to Base Constructor

```cpp
class Base {
    int x;
public:
    Base(int a) : x(a) { }
};

class Derived : public Base {
    int y;
public:
    Derived(int a, int b) : Base(a), y(b) { }  // Base initializer
};
```

---

## 7.5 Function Overriding

### Concept

Derived class provides its own implementation of a base class method.

```cpp
class Animal {
public:
    void speak() { cout << "Some sound" << endl; }
};

class Dog : public Animal {
public:
    void speak() { cout << "Bark!" << endl; }  // Override
};

Dog d;
d.speak();  // "Bark!"
```

### Calling Base Class Method

```cpp
class Dog : public Animal {
public:
    void speak() {
        Animal::speak();    // Call base version
        cout << "Bark!" << endl;
    }
};
```

### Overloading vs Overriding

| Overloading | Overriding |
|-------------|------------|
| Same name, different parameters | Same name and parameters |
| Same class | Different classes (inheritance) |
| Compile-time | Run-time (with virtual) |
| Return type can differ | Return type must match (or covariant) |

---

## 7.6 The Diamond Problem

### What is It?

When a class inherits from two classes that have a common base.

```
       ┌───────────┐
       │  Animal   │
       └─────┬─────┘
     ┌───────┴───────┐
┌────┴────┐    ┌────┴────┐
│ Mammal  │    │  Bird   │
└────┬────┘    └────┬────┘
     └───────┬───────┘
        ┌────┴────┐
        │   Bat   │
        └─────────┘
```

### The Problem

```cpp
class Animal { public: int age; };
class Mammal : public Animal { };
class Bird : public Animal { };
class Bat : public Mammal, public Bird { };

Bat b;
b.age = 5;  // ERROR! Ambiguous - which age?
```

**Bat has TWO copies of Animal's members!**

### The Solution: Virtual Inheritance

```cpp
class Animal { public: int age; };
class Mammal : virtual public Animal { };  // Virtual
class Bird : virtual public Animal { };     // Virtual
class Bat : public Mammal, public Bird { };

Bat b;
b.age = 5;  // OK - only ONE copy of age
```

---

## 7.7 Polymorphism | One Interface, Many Forms

### Types of Polymorphism

```
                Polymorphism
                     │
    ┌────────────────┴────────────────┐
    │                                  │
Compile-time                       Run-time
(Static)                           (Dynamic)
    │                                  │
┌───┴───┐                         ┌───┴───┐
│Overload│                        │Virtual│
│Operator│                        │Functions│
│Templates│                       │Override│
└───────┘                         └───────┘
```

### Compile-Time Polymorphism

Resolved at compile time.

**1. Function Overloading**
```cpp
int add(int a, int b) { return a + b; }
double add(double a, double b) { return a + b; }

add(1, 2);      // Calls int version
add(1.5, 2.5);  // Calls double version
```

**2. Operator Overloading**
```cpp
Complex c1, c2;
Complex c3 = c1 + c2;  // Overloaded +
```

### Run-Time Polymorphism

Resolved at run time using virtual functions.

```cpp
class Animal {
public:
    virtual void speak() { cout << "Animal sound" << endl; }
};

class Dog : public Animal {
public:
    void speak() override { cout << "Bark!" << endl; }
};

class Cat : public Animal {
public:
    void speak() override { cout << "Meow!" << endl; }
};

void makeSound(Animal* a) {
    a->speak();  // Which speak() is called? Depends on actual object!
}

Dog d;
Cat c;
makeSound(&d);  // "Bark!"
makeSound(&c);  // "Meow!"
```

---

## 7.8 Virtual Functions | The Key to Polymorphism

### What is a Virtual Function?

A function declared with `virtual` keyword in base class that can be overridden in derived classes with **dynamic binding**.

```cpp
class Base {
public:
    virtual void show() { cout << "Base" << endl; }
};

class Derived : public Base {
public:
    void show() override { cout << "Derived" << endl; }
};

Base* ptr = new Derived();
ptr->show();  // "Derived" - dynamic binding
```

### Without Virtual (Static Binding)

```cpp
class Base {
public:
    void show() { cout << "Base" << endl; }  // Non-virtual
};

class Derived : public Base {
public:
    void show() { cout << "Derived" << endl; }
};

Base* ptr = new Derived();
ptr->show();  // "Base" - static binding (based on pointer type)
```

### How Virtual Functions Work: vtable

```
┌─────────────────────┐
│   Base Object       │
│ ┌─────────────────┐ │
│ │ vptr ───────────┼─┼──→ Base vtable
│ ├─────────────────┤ │    ┌──────────────┐
│ │ data members    │ │    │ show() → Base│
│ └─────────────────┘ │    └──────────────┘
└─────────────────────┘

┌─────────────────────┐
│   Derived Object    │
│ ┌─────────────────┐ │
│ │ vptr ───────────┼─┼──→ Derived vtable
│ ├─────────────────┤ │    ┌────────────────┐
│ │ base data       │ │    │ show() → Derived│
│ ├─────────────────┤ │    └────────────────┘
│ │ derived data    │ │
│ └─────────────────┘ │
└─────────────────────┘
```

### Virtual Destructor

**CRITICAL for proper cleanup with polymorphism!**

```cpp
class Base {
public:
    virtual ~Base() { cout << "~Base" << endl; }
};

class Derived : public Base {
    int* arr;
public:
    Derived() { arr = new int[100]; }
    ~Derived() { 
        delete[] arr;
        cout << "~Derived" << endl;
    }
};

Base* ptr = new Derived();
delete ptr;  // Without virtual: only ~Base called → MEMORY LEAK!
             // With virtual: ~Derived then ~Base → Correct!
```

**Rule**: If a class has virtual functions, it should have a virtual destructor.

---

## 7.9 Pure Virtual Functions and Abstract Classes

### Pure Virtual Function

```cpp
class Shape {
public:
    virtual double area() = 0;  // Pure virtual (= 0)
};
```

**Properties**:
1. Has no implementation (or has default implementation)
2. Makes the class abstract
3. Derived classes MUST override it (or remain abstract)

### Abstract Class

```cpp
class Shape {
public:
    virtual double area() = 0;      // Pure virtual
    virtual void draw() = 0;        // Pure virtual
    void printInfo() { }            // Regular function - OK
};

// Shape s;  // ERROR! Cannot instantiate abstract class
```

### Concrete Class

A class that provides implementations for ALL pure virtual functions.

```cpp
class Circle : public Shape {
    double radius;
public:
    Circle(double r) : radius(r) {}
    
    double area() override {
        return 3.14159 * radius * radius;
    }
    
    void draw() override {
        cout << "Drawing circle" << endl;
    }
};

Circle c(5);  // OK - Circle is concrete
```

### Interface (Pure Abstract Class)

```cpp
class Drawable {
public:
    virtual void draw() = 0;
    virtual void resize(int factor) = 0;
    virtual ~Drawable() {}  // Virtual destructor
};
```

**All functions are pure virtual** → Acts like an interface.

---

## 7.10 Covariant Return Types

### Definition

Derived class override can return a more specific type.

```cpp
class Animal {
public:
    virtual Animal* clone() {
        return new Animal(*this);
    }
};

class Dog : public Animal {
public:
    Dog* clone() override {   // Returns Dog*, not Animal*
        return new Dog(*this);
    }
};
```

**Rule**: Return type must be pointer/reference to class in same hierarchy.

---

## 7.11 Object Slicing

### The Problem

When a derived class object is assigned to a base class object.

```cpp
class Base {
public:
    int x;
};

class Derived : public Base {
public:
    int y;
};

Derived d;
d.x = 1;
d.y = 2;

Base b = d;  // Object slicing! y is lost
// b.y does not exist
```

### Avoiding Object Slicing

Use pointers or references:

```cpp
Derived d;
Base* ptr = &d;  // No slicing - ptr points to full Derived object
Base& ref = d;   // No slicing - ref refers to full Derived object
```

---

## 7.12 RTTI (Run-Time Type Information)

### dynamic_cast

Safe downcasting (base to derived).

```cpp
class Base {
public:
    virtual ~Base() {}  // Must have virtual function
};

class Derived : public Base {
public:
    void derivedFunc() {}
};

Base* basePtr = new Derived();

Derived* derivedPtr = dynamic_cast<Derived*>(basePtr);
if(derivedPtr) {
    derivedPtr->derivedFunc();  // Safe to call
}
```

**Returns nullptr if cast fails** (for pointers).
**Throws std::bad_cast if cast fails** (for references).

### typeid

Get type information at runtime.

```cpp
#include <typeinfo>

Base* ptr = new Derived();
cout << typeid(*ptr).name();  // Prints derived type info
```

---

## 7.13 Common GATE Patterns

### Pattern 1: Virtual Function Output

```cpp
class A {
public:
    virtual void show() { cout << "A"; }
};

class B : public A {
public:
    void show() { cout << "B"; }
};

int main() {
    A* p = new B();
    p->show();
    return 0;
}
```

**Answer**: `B` (dynamic binding)

### Pattern 2: Constructor Order

```cpp
class A { public: A() { cout << "A"; } };
class B : public A { public: B() { cout << "B"; } };
class C : public B { public: C() { cout << "C"; } };

int main() {
    C c;
    return 0;
}
```

**Answer**: `ABC` (base constructors first)

### Pattern 3: Without Virtual

```cpp
class A {
public:
    void show() { cout << "A"; }  // NOT virtual
};

class B : public A {
public:
    void show() { cout << "B"; }
};

int main() {
    A* p = new B();
    p->show();
    return 0;
}
```

**Answer**: `A` (static binding based on pointer type)

### Pattern 4: Size with Virtual

```cpp
class A {
    int x;
public:
    virtual void func() {}
};

cout << sizeof(A);
```

**Answer**: 16 on 64-bit (8 for vptr + 4 for x + 4 padding)

### Pattern 5: Multiple Inheritance Ambiguity

```cpp
class A { public: void show() { cout << "A"; } };
class B { public: void show() { cout << "B"; } };
class C : public A, public B { };

int main() {
    C c;
    c.show();  // ERROR! Ambiguous
    c.A::show();  // OK - explicitly call A's show
    return 0;
}
```

---

## 7.14 Virtual Function Table (vtable) Deep Dive

### Memory Layout

```cpp
class Base {
public:
    int x;
    virtual void f1() { }
    virtual void f2() { }
};

class Derived : public Base {
public:
    int y;
    void f1() override { }  // Overrides
    virtual void f3() { }   // New virtual
};
```

**vtable for Base**:
```
┌───────────────────┐
│ f1() → Base::f1   │
├───────────────────┤
│ f2() → Base::f2   │
└───────────────────┘
```

**vtable for Derived**:
```
┌─────────────────────┐
│ f1() → Derived::f1  │  (overridden)
├─────────────────────┤
│ f2() → Base::f2     │  (inherited)
├─────────────────────┤
│ f3() → Derived::f3  │  (new)
└─────────────────────┘
```

### Cost of Virtual Functions

| Aspect | Cost |
|--------|------|
| Memory | Extra vptr per object (~8 bytes) |
| Time | One extra indirection per call |
| Inlining | Usually prevented |

---

## 7.15 Practice Problems

### Q1 (Output)

```cpp
class Base {
public:
    virtual void show() { cout << "Base "; }
    void print() { cout << "Print "; show(); }
};

class Derived : public Base {
public:
    void show() { cout << "Derived "; }
};

int main() {
    Base* p = new Derived();
    p->print();
    return 0;
}
```

**Answer**: `Print Derived ` 
(print() calls show(), which is virtual → calls Derived::show())

### Q2 (NAT)

How many vtables are created?

```cpp
class A { virtual void f() {} };
class B : public A { void f() {} };
class C : public A { void f() {} };
```

**Answer**: 3 (one for each class)

### Q3 (MSQ)

Which are true about pure virtual functions?

A. They make a class abstract ✅
B. They can have a body ✅ (defined outside with `= 0`)
C. They must be overridden in derived class ✅
D. They prevent object creation of that class ✅

### Q4 (Constructor/Destructor)

```cpp
class A { public: A() { cout << "A"; } ~A() { cout << "~A"; } };
class B : public A { public: B() { cout << "B"; } ~B() { cout << "~B"; } };

int main() {
    B* p = new B();
    delete p;
    return 0;
}
```

**Answer**: `AB~B~A`

---

## 7.16 Quick Reference

### Inheritance Summary

| Type | Description | Keyword |
|------|-------------|---------|
| Single | One parent | `: public Base` |
| Multiple | Many parents | `: public B1, public B2` |
| Multilevel | Chain | A → B → C |
| Hierarchical | Many children | Same base |
| Virtual | Solve diamond | `virtual public Base` |

### Virtual Functions Summary

| Concept | Description |
|---------|-------------|
| Virtual | Enables dynamic binding |
| Pure virtual | `= 0`, makes class abstract |
| Override | Derived replaces base behavior |
| vtable | Table of function pointers |
| vptr | Pointer to vtable in each object |

### Key Rules

1. **Virtual destructor** if class has any virtual functions
2. **Pure virtual** = abstract class = no instantiation
3. **Object slicing** = use pointers/references to avoid
4. **Dynamic binding** = actual type determines function
5. **Static binding** = declared type determines function

### Memory Impact

- Non-virtual class: sizeof(data members)
- Virtual class: sizeof(data members) + sizeof(vptr)
- Each derived class: own vtable

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Advanced]**

*Next: [Chapter 8: Advanced OOP and Design Patterns →](08-Advanced-OOP.md)*
