# Chapter 8: Object-Oriented Programming
## The Design Paradigm | GATE, ESE, PSU, BANK

---

## The Atomic Truth
> **"OOP models the real world: Objects have state (data) and behavior (methods)."**

---

## 8.1 OOP Fundamentals

### Four Pillars of OOP

| Pillar | Definition | Real-World Analogy |
|--------|------------|-------------------|
| **Encapsulation** | Bundle data + methods, hide internals | Medicine capsule |
| **Abstraction** | Show only essential features | Car dashboard |
| **Inheritance** | Acquire properties from parent | Child inheriting traits |
| **Polymorphism** | Same interface, different behavior | "Draw" for different shapes |

### Class and Object

```cpp
// Class: Blueprint
class Car {
private:
    string brand;
    int speed;
    
public:
    void accelerate() { speed += 10; }
    void brake() { speed -= 10; }
    int getSpeed() { return speed; }
};

// Object: Instance of class
Car myCar;
myCar.accelerate();
```

### Memory Layout

```
Stack:                     Heap:
┌─────────────────┐       ┌─────────────────┐
│ Object reference│──────→│ Object data     │
│ (pointer)       │       │ - brand         │
└─────────────────┘       │ - speed         │
                          │ - vtable ptr    │
                          └─────────────────┘
```

---

## 8.2 Encapsulation

### Access Specifiers

| Specifier | Within Class | Derived Class | Outside |
|-----------|-------------|---------------|---------|
| `private` | ✓ | ✗ | ✗ |
| `protected` | ✓ | ✓ | ✗ |
| `public` | ✓ | ✓ | ✓ |

### Getter and Setter

```cpp
class BankAccount {
private:
    double balance;  // Hidden from outside
    
public:
    double getBalance() { return balance; }
    
    void deposit(double amount) {
        if (amount > 0) balance += amount;  // Validation
    }
    
    bool withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }
};
```

**Benefits:**
1. Data hiding
2. Validation control
3. Flexibility to change internal implementation

---

## 8.3 Abstraction

### Abstract Class

```cpp
class Shape {
public:
    virtual double area() = 0;    // Pure virtual function
    virtual double perimeter() = 0;
    
    void display() { cout << "I am a shape"; }  // Concrete method
};

class Circle : public Shape {
    double radius;
public:
    double area() override { return 3.14159 * radius * radius; }
    double perimeter() override { return 2 * 3.14159 * radius; }
};
```

### Interface (C++ using pure abstract class)

```cpp
class Drawable {
public:
    virtual void draw() = 0;
    virtual ~Drawable() = default;
};

class Printable {
public:
    virtual void print() = 0;
};

// Multiple interface implementation
class Document : public Drawable, public Printable {
    void draw() override { /* ... */ }
    void print() override { /* ... */ }
};
```

### 🎯 Abstract Class vs Interface

| Aspect | Abstract Class | Interface |
|--------|---------------|-----------|
| Methods | Can have concrete + abstract | Only abstract (pure virtual) |
| Variables | Can have data members | Usually no data (constants only) |
| Inheritance | Single | Multiple |
| Purpose | IS-A relationship | CAN-DO capability |

---

## 8.4 Inheritance

### Types of Inheritance

```
1. Single:          A → B
2. Multiple:        A, B → C
3. Multilevel:      A → B → C
4. Hierarchical:    A → B, A → C
5. Hybrid:          Combination of above
```

### Syntax

```cpp
class Animal {
protected:
    string name;
public:
    void eat() { cout << "Eating"; }
};

class Dog : public Animal {  // Inherits from Animal
public:
    void bark() { cout << "Barking"; }
};
```

### Access Control in Inheritance

| Base Member | public inheritance | protected inheritance | private inheritance |
|------------|-------------------|----------------------|---------------------|
| public | public | protected | private |
| protected | protected | protected | private |
| private | inaccessible | inaccessible | inaccessible |

### Constructor/Destructor Order

```cpp
class Base {
public:
    Base() { cout << "Base ctor\n"; }
    ~Base() { cout << "Base dtor\n"; }
};

class Derived : public Base {
public:
    Derived() { cout << "Derived ctor\n"; }
    ~Derived() { cout << "Derived dtor\n"; }
};

// Creating Derived object:
// Output:
// Base ctor
// Derived ctor
// Derived dtor
// Base dtor
```

**Rule:** Constructors: Base → Derived, Destructors: Derived → Base

### Diamond Problem (Multiple Inheritance)

```cpp
class A { public: int data; };
class B : public A { };
class C : public A { };
class D : public B, public C { };  // Two copies of A!

// Solution: Virtual Inheritance
class B : virtual public A { };
class C : virtual public A { };
class D : public B, public C { };  // One copy of A
```

---

## 8.5 Polymorphism

### Compile-Time (Static) Polymorphism

**1. Function Overloading:**
```cpp
class Calculator {
public:
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
    int add(int a, int b, int c) { return a + b + c; }
};
```

**2. Operator Overloading:**
```cpp
class Complex {
    double real, imag;
public:
    Complex operator+(const Complex& other) {
        return Complex(real + other.real, imag + other.imag);
    }
};
```

### Run-Time (Dynamic) Polymorphism

**Virtual Functions:**
```cpp
class Animal {
public:
    virtual void sound() { cout << "Some sound"; }
};

class Dog : public Animal {
public:
    void sound() override { cout << "Bark"; }
};

class Cat : public Animal {
public:
    void sound() override { cout << "Meow"; }
};

// Polymorphic behavior
Animal* animals[2] = {new Dog(), new Cat()};
animals[0]->sound();  // "Bark"
animals[1]->sound();  // "Meow"
```

### Virtual Table (vtable)

```
Dog object in memory:
┌─────────────────┐
│ vptr            │───→ Dog's vtable
├─────────────────┤     ┌─────────────────┐
│ Animal data     │     │ &Dog::sound     │
├─────────────────┤     │ &Animal::eat    │
│ Dog data        │     └─────────────────┘
└─────────────────┘
```

### 🚨 GATE Trap: Without `virtual`

```cpp
class Base {
public:
    void show() { cout << "Base"; }
};

class Derived : public Base {
public:
    void show() { cout << "Derived"; }
};

Base* ptr = new Derived();
ptr->show();  // Output: "Base" (static binding!)
```

**With `virtual`:** Output would be "Derived" (dynamic binding)

---

## 8.6 Constructors and Destructors

### Types of Constructors

```cpp
class MyClass {
    int x, y;
    
public:
    // Default constructor
    MyClass() : x(0), y(0) { }
    
    // Parameterized constructor
    MyClass(int a, int b) : x(a), y(b) { }
    
    // Copy constructor
    MyClass(const MyClass& other) : x(other.x), y(other.y) { }
    
    // Move constructor (C++11)
    MyClass(MyClass&& other) noexcept : x(other.x), y(other.y) { }
    
    // Destructor
    ~MyClass() { }
};
```

### Copy Constructor vs Assignment Operator

```cpp
MyClass a(10, 20);
MyClass b = a;      // Copy constructor (initialization)
MyClass c;
c = a;              // Assignment operator (already exists)
```

### Deep Copy vs Shallow Copy

```cpp
class Shallow {
    int* data;
public:
    Shallow(int val) { data = new int(val); }
    // Default copy: copies pointer (both point to same memory!)
};

class Deep {
    int* data;
public:
    Deep(int val) { data = new int(val); }
    
    // Deep copy constructor
    Deep(const Deep& other) {
        data = new int(*other.data);  // Allocate new memory
    }
};
```

### Virtual Destructor

```cpp
class Base {
public:
    virtual ~Base() { cout << "Base destructor\n"; }
};

class Derived : public Base {
    int* arr;
public:
    Derived() { arr = new int[100]; }
    ~Derived() { delete[] arr; cout << "Derived destructor\n"; }
};

Base* ptr = new Derived();
delete ptr;  // With virtual: Both destructors called
             // Without virtual: Only Base destructor (memory leak!)
```

**Rule:** If class has virtual functions, make destructor virtual.

---

## 8.7 Static Members

### Static Variables

```cpp
class Counter {
    static int count;  // Shared by all objects
public:
    Counter() { count++; }
    ~Counter() { count--; }
    static int getCount() { return count; }
};

int Counter::count = 0;  // Definition outside class

Counter c1, c2, c3;
cout << Counter::getCount();  // 3
```

### Static Methods

- Can only access static members
- Cannot use `this` pointer
- Called using class name: `ClassName::method()`

---

## 8.8 Friend Functions and Classes

### Friend Function

```cpp
class Box {
    int width;
public:
    Box(int w) : width(w) { }
    friend int getWidth(Box& b);  // Not a member!
};

int getWidth(Box& b) {
    return b.width;  // Can access private members
}
```

### Friend Class

```cpp
class Engine {
    friend class Car;  // Car can access Engine's private members
private:
    int horsepower;
};

class Car {
    Engine engine;
public:
    void boostEngine() { engine.horsepower += 50; }  // Allowed!
};
```

**Note:** Friendship is not transitive or inherited.

---

## 8.9 Templates (Generic Programming)

### Function Templates

```cpp
template <typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

// Usage
maximum(10, 20);      // T = int
maximum(3.14, 2.71);  // T = double
maximum('a', 'z');    // T = char
```

### Class Templates

```cpp
template <typename T>
class Stack {
    T arr[100];
    int top;
public:
    void push(T val) { arr[++top] = val; }
    T pop() { return arr[top--]; }
};

Stack<int> intStack;
Stack<string> strStack;
```

---

## 8.10 Exception Handling

### Try-Catch-Throw

```cpp
double divide(int a, int b) {
    if (b == 0)
        throw runtime_error("Division by zero!");
    return (double)a / b;
}

int main() {
    try {
        double result = divide(10, 0);
    } catch (const runtime_error& e) {
        cout << "Error: " << e.what();
    } catch (...) {
        cout << "Unknown error";
    }
}
```

### Exception Hierarchy

```
exception
├── logic_error
│   ├── invalid_argument
│   ├── domain_error
│   ├── length_error
│   └── out_of_range
└── runtime_error
    ├── range_error
    ├── overflow_error
    └── underflow_error
```

---

## 8.11 SOLID Principles

| Principle | Full Name | Description |
|-----------|-----------|-------------|
| **S** | Single Responsibility | Class has one reason to change |
| **O** | Open/Closed | Open for extension, closed for modification |
| **L** | Liskov Substitution | Derived can replace base without issues |
| **I** | Interface Segregation | Many specific interfaces > one general |
| **D** | Dependency Inversion | Depend on abstractions, not concretions |

---

## 8.12 Design Patterns (Overview)

### Creational Patterns
- **Singleton:** Only one instance exists
- **Factory:** Create objects without specifying class
- **Builder:** Construct complex objects step by step

### Structural Patterns
- **Adapter:** Convert interface to another
- **Decorator:** Add behavior dynamically
- **Facade:** Simplified interface to complex subsystem

### Behavioral Patterns
- **Observer:** Notify dependents of state change
- **Strategy:** Family of interchangeable algorithms
- **Iterator:** Sequential access without exposing structure

---

## 🎯 Practice Problems

### Problem 1: Virtual Functions
```cpp
class A { public: virtual void f() { cout << "A"; } };
class B : public A { public: void f() { cout << "B"; } };
A* p = new B(); p->f();
```
**Answer:** B (dynamic binding due to virtual)

### Problem 2: Constructor Order
**Q:** Order of constructor calls for `class D : public B, public C`?
**Answer:** B(), C(), D() (left to right in inheritance list)

### Problem 3: Static Member
```cpp
class X { static int count; public: X() { count++; } };
int X::count = 0;
X a, b, c;
```
**Q:** What is X::count?
**Answer:** 3

### Problem 4: Copy Constructor
**Q:** When is copy constructor called?
**Answer:** 
1. Object initialization with another object
2. Pass by value to function
3. Return object from function

### Problem 5: Pure Virtual
**Q:** Can you instantiate a class with pure virtual function?
**Answer:** No, it becomes an abstract class

---

## 🧠 The Memory Anchors

### The Bizarre Mnemonic
**"CAPE protects the superhero: C-Capsulation (hide secrets), A-Abstraction (show powers only), P-Polymorphism (shape-shift), E-nclosed Inheritance (family powers)."**

### The Mental Slider
- **Encapsulation:** A safe with a combination lock
- **Inheritance:** Family tree with inherited traits
- **Polymorphism:** Universal remote for different devices
- **Abstraction:** ATM machine (hide complexity)

### The 5-Second Snap-Check
1. **Virtual?** Check if dynamic binding needed
2. **Pure virtual?** Class becomes abstract
3. **Virtual destructor?** Required for polymorphic deletion
4. **Friend?** Breaks encapsulation, use sparingly
5. **Static?** Shared across all instances

---

## 📈 Complexity Summary

| Concept | Compile-Time | Run-Time Overhead |
|---------|--------------|-------------------|
| Function Overloading | Resolved | None |
| Virtual Functions | - | vtable lookup O(1) |
| Templates | Instantiated | None (compile-time) |
| RTTI (dynamic_cast) | - | Type check O(1) |
| Exception Handling | Setup | Throw O(n) unwinding |

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].*

[← Previous: Algorithms](07-Algorithms.md) | [Next: Complexity Analysis →](09-Complexity-Analysis.md)
