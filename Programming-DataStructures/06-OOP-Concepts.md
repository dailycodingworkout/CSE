# Chapter 6: Object-Oriented Programming (OOP) Concepts

## The Singularity | First Principles

> **The Atomic Truth:** "OOP = Data + Behavior bundled as Objects."

---

## 6.1 Introduction to OOP

### What is Object-Oriented Programming?

OOP is a programming paradigm that organizes software design around **data (objects)** rather than functions and logic.

### The Four Pillars of OOP

```
                    OOP
                     │
    ┌────────────────┼────────────────┐
    │                │                │
┌───┴───┐     ┌──────┴──────┐   ┌─────┴─────┐
│Encap- │     │Inheritance  │   │Polymor-   │
│sulation│     │             │   │phism      │
└───────┘     └─────────────┘   └───────────┘
    │
┌───┴───┐
│Abstrac│
│tion   │
└───────┘
```

### Why OOP?

| Aspect | Procedural | OOP |
|--------|------------|-----|
| Focus | Functions | Objects |
| Data | Global/passed around | Encapsulated in objects |
| Reuse | Function libraries | Class inheritance |
| Maintenance | Harder as size grows | Modular, easier |
| Real-world modeling | Difficult | Natural |

---

## 6.2 Classes and Objects

### Class: The Blueprint

A **class** is a blueprint or template that defines:
- **Attributes** (data members / fields)
- **Behaviors** (methods / member functions)

```cpp
class Car {
    // Attributes (data)
    string brand;
    string model;
    int year;
    
    // Behaviors (methods)
    void start();
    void accelerate();
    void brake();
};
```

### Object: The Instance

An **object** is a specific instance of a class with actual values.

```cpp
Car myCar;           // Object creation
myCar.brand = "Toyota";
myCar.model = "Camry";
myCar.year = 2023;
myCar.start();       // Method call
```

### Analogy

- **Class** = Cookie cutter (defines shape)
- **Object** = Actual cookie (has specific dough, decorations)

---

## 6.3 C++ Syntax for Classes

### Basic Class Structure

```cpp
class ClassName {
private:        // Access specifier
    // Private members (hidden)
    int privateData;
    
protected:      // Accessible by derived classes
    int protectedData;
    
public:         // Accessible from anywhere
    // Constructor
    ClassName();
    
    // Destructor
    ~ClassName();
    
    // Member functions
    void publicMethod();
    
    // Getter and Setter
    int getData();
    void setData(int value);
};
```

### Defining Member Functions

```cpp
// Inside class (inline)
class Rectangle {
    int width, height;
public:
    int area() { return width * height; }
};

// Outside class (using scope resolution ::)
class Rectangle {
    int width, height;
public:
    int area();
};

int Rectangle::area() {
    return width * height;
}
```

---

## 6.4 Constructors | Object Initialization

### What is a Constructor?

A **constructor** is a special member function that:
- Has the same name as the class
- Is called automatically when an object is created
- Initializes the object's data members
- Has no return type (not even void)

### Types of Constructors

#### 1. Default Constructor

```cpp
class Point {
    int x, y;
public:
    Point() {        // Default constructor
        x = 0;
        y = 0;
    }
};

Point p;  // Calls default constructor
```

#### 2. Parameterized Constructor

```cpp
class Point {
    int x, y;
public:
    Point(int a, int b) {
        x = a;
        y = b;
    }
};

Point p(10, 20);  // Calls parameterized constructor
```

#### 3. Copy Constructor

```cpp
class Point {
    int x, y;
public:
    Point(const Point &p) {   // Copy constructor
        x = p.x;
        y = p.y;
    }
};

Point p1(10, 20);
Point p2 = p1;    // Calls copy constructor
Point p3(p1);     // Also calls copy constructor
```

### Constructor Overloading

```cpp
class Rectangle {
    int width, height;
public:
    Rectangle() : width(0), height(0) {}
    Rectangle(int s) : width(s), height(s) {}  // Square
    Rectangle(int w, int h) : width(w), height(h) {}
};

Rectangle r1;        // 0x0
Rectangle r2(5);     // 5x5
Rectangle r3(4, 6);  // 4x6
```

### Initializer List

```cpp
class Point {
    const int x;  // Must be initialized in list
    int y;
public:
    Point(int a, int b) : x(a), y(b) {}  // Initializer list
};
```

**When to use initializer list:**
1. Const members
2. Reference members
3. Members without default constructor
4. Base class initialization (inheritance)

---

## 6.5 Destructors | Cleanup

### What is a Destructor?

A **destructor** is called when an object is destroyed:
- Has the same name as class, prefixed with `~`
- No parameters, no return type
- Only one destructor per class
- Used for cleanup (freeing memory, closing files)

```cpp
class Array {
    int *arr;
    int size;
public:
    Array(int n) {
        size = n;
        arr = new int[n];  // Allocate
    }
    
    ~Array() {
        delete[] arr;      // Free memory
    }
};

void foo() {
    Array a(100);
}  // Destructor called when a goes out of scope
```

### Order of Destruction

For multiple objects: **LIFO** (Last In, First Out)

```cpp
void func() {
    Object a;  // Constructed first
    Object b;  // Constructed second
}  // b destroyed first, then a
```

---

## 6.6 Encapsulation | Data Hiding

### The Concept

Encapsulation means:
1. **Bundling** data and methods that operate on that data
2. **Hiding** internal details from outside access

### Access Specifiers

| Specifier | Same Class | Derived Class | Outside |
|-----------|------------|---------------|---------|
| `private` | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ❌ |
| `public` | ✅ | ✅ | ✅ |

**Default access**: `private` for class, `public` for struct

### Getter and Setter Pattern

```cpp
class BankAccount {
private:
    double balance;   // Hidden data
    
public:
    // Getter
    double getBalance() {
        return balance;
    }
    
    // Setter with validation
    void setBalance(double amount) {
        if(amount >= 0) {
            balance = amount;
        }
    }
    
    // Controlled modification
    bool withdraw(double amount) {
        if(amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }
};
```

### Why Encapsulation?

1. **Data Protection**: Prevent invalid states
2. **Flexibility**: Change implementation without affecting users
3. **Modularity**: Self-contained units

**Analogy**: ATM machine - you can withdraw money (public interface) without knowing how it works inside (private implementation).

---

## 6.7 Abstraction | Hiding Complexity

### The Concept

Abstraction means showing **only essential features** while hiding implementation details.

### Difference from Encapsulation

| Encapsulation | Abstraction |
|---------------|-------------|
| How it's packaged | What it does |
| Implementation | Interface |
| Data hiding | Behavior hiding |

### Abstract Classes and Pure Virtual Functions

```cpp
class Shape {
public:
    // Pure virtual function (no implementation)
    virtual double area() = 0;
    
    // Regular virtual function
    virtual void draw() {
        cout << "Drawing shape" << endl;
    }
};
```

- **Pure virtual function**: Declared with `= 0`, no body
- **Abstract class**: Has at least one pure virtual function
- **Cannot instantiate** abstract classes

```cpp
Shape s;  // ERROR! Cannot create object of abstract class
```

### Concrete Implementation

```cpp
class Circle : public Shape {
    double radius;
public:
    Circle(double r) : radius(r) {}
    
    double area() override {   // Must implement
        return 3.14159 * radius * radius;
    }
};

class Rectangle : public Shape {
    double width, height;
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    
    double area() override {
        return width * height;
    }
};
```

---

## 6.8 The `this` Pointer

### What is `this`?

`this` is an implicit pointer available in all non-static member functions, pointing to the object invoking the function.

```cpp
class Point {
    int x, y;
public:
    Point(int x, int y) {
        this->x = x;  // Distinguish member from parameter
        this->y = y;
    }
    
    Point& setX(int x) {
        this->x = x;
        return *this;  // Return current object for chaining
    }
    
    Point& setY(int y) {
        this->y = y;
        return *this;
    }
};

Point p(0, 0);
p.setX(10).setY(20);  // Method chaining
```

### Use Cases for `this`

1. **Parameter shadowing**: `this->x = x`
2. **Return current object**: `return *this`
3. **Pass object to another function**: `someFunction(this)`
4. **Self-reference check**: `if(this == &other)`

---

## 6.9 Static Members

### Static Data Members

Shared by all objects of the class.

```cpp
class Counter {
    static int count;  // Declaration
    int id;
    
public:
    Counter() {
        count++;
        id = count;
    }
    
    static int getCount() {  // Static member function
        return count;
    }
};

// Definition (required, outside class)
int Counter::count = 0;

int main() {
    Counter c1, c2, c3;
    cout << Counter::getCount();  // 3
    return 0;
}
```

### Properties of Static Members

| Property | Static | Non-static |
|----------|--------|------------|
| Shared | Yes | No (per object) |
| Access without object | Yes | No |
| `this` pointer | No | Yes |
| Can access | Only static members | All members |

### Static Member Functions

```cpp
class Math {
public:
    static int add(int a, int b) {
        return a + b;
    }
};

int sum = Math::add(5, 3);  // Call without object
```

---

## 6.10 Friend Functions and Classes

### Friend Function

A non-member function with access to private/protected members.

```cpp
class Box {
    double width;
    
public:
    Box(double w) : width(w) {}
    
    friend void printWidth(Box b);  // Friend declaration
};

void printWidth(Box b) {
    cout << b.width;  // Can access private member!
}
```

### Friend Class

All member functions of one class can access private members of another.

```cpp
class Engine {
    int horsepower;
    friend class Mechanic;  // Mechanic can access Engine's private members
};

class Mechanic {
public:
    void tune(Engine& e) {
        e.horsepower += 10;  // Can access private!
    }
};
```

### Properties of Friends

1. **Not symmetric**: A is friend of B doesn't mean B is friend of A
2. **Not transitive**: Friend of friend is not automatically friend
3. **Not inherited**: Derived class doesn't inherit friendships
4. **Breaks encapsulation**: Use sparingly

---

## 6.11 Operator Overloading

### Concept

Redefine operators for user-defined types.

### Syntax

```cpp
class Complex {
    double real, imag;
    
public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}
    
    // Overload + operator
    Complex operator+(const Complex& c) {
        return Complex(real + c.real, imag + c.imag);
    }
    
    // Overload == operator
    bool operator==(const Complex& c) {
        return (real == c.real && imag == c.imag);
    }
};

Complex c1(3, 4), c2(1, 2);
Complex c3 = c1 + c2;  // Uses overloaded +
```

### Operators That CAN Be Overloaded

```
+  -  *  /  %  ^  &  |  ~  !
=  <  >  +=  -=  *=  /=  %=
^=  &=  |=  <<  >>  >>=  <<=
==  !=  <=  >=  &&  ||  ++  --
,  ->*  ->  ()  []  new  delete
```

### Operators That CANNOT Be Overloaded

```
.     (member access)
.*    (pointer-to-member)
::    (scope resolution)
?:    (ternary)
sizeof
typeid
```

### Friend vs Member Overloading

```cpp
// Member function: left operand must be object
Complex operator+(const Complex& c) { ... }
// Usage: c1 + c2  (c1.operator+(c2))

// Friend function: either operand can be different type
friend Complex operator+(double d, const Complex& c) {
    return Complex(d + c.real, c.imag);
}
// Usage: 5.0 + c1  (not possible with member function)
```

---

## 6.12 GATE-Focused OOP Concepts

### Important Points for Exam

1. **Constructor never returns anything** (not even void)
2. **Destructor is called in reverse order** of construction
3. **Static members are shared** across all objects
4. **Abstract class cannot be instantiated**
5. **Virtual keyword enables dynamic binding**

### Common Exam Patterns

#### Pattern 1: Constructor Call Counting

```cpp
class A {
    static int count;
public:
    A() { count++; }
    static int getCount() { return count; }
};
int A::count = 0;

int main() {
    A a1, a2, a3;
    A arr[5];
    cout << A::getCount();  // Output: 8
    return 0;
}
```

#### Pattern 2: Constructor/Destructor Order

```cpp
class A {
public:
    A() { cout << "A "; }
    ~A() { cout << "~A "; }
};

class B {
public:
    B() { cout << "B "; }
    ~B() { cout << "~B "; }
};

int main() {
    A a;
    B b;
    return 0;
}
// Output: A B ~B ~A
```

#### Pattern 3: Copy Constructor vs Assignment

```cpp
A a1;        // Default constructor
A a2 = a1;   // Copy constructor (initialization)
A a3;
a3 = a1;     // Assignment operator (not copy constructor)
```

---

## 6.13 Memory Layout of Objects

### Object Memory

```cpp
class Point {
    int x;    // 4 bytes
    int y;    // 4 bytes
    
    void show() { }  // Methods don't take object memory
};

sizeof(Point)  // = 8 bytes (just data members)
```

### With Virtual Functions

```cpp
class Base {
    int x;
    virtual void func() {}
};

sizeof(Base)  // = 16 bytes (8 for vptr + 4 for x + 4 padding on 64-bit)
```

**vptr**: Virtual pointer to virtual table (vtable)

---

## 6.14 Practice Problems

### Q1 (Output Prediction)

```cpp
class Test {
    int x;
public:
    Test(int a = 0) : x(a) { cout << x << " "; }
};

int main() {
    Test t1;
    Test t2(5);
    Test t3 = 10;  // Implicit conversion
    return 0;
}
```

**Answer**: `0 5 10 `

### Q2 (Static Member)

```cpp
class A {
    static int x;
public:
    A() { x++; }
    static int getX() { return x; }
};
int A::x = 0;

int main() {
    A a[4];
    cout << A::getX();
    return 0;
}
```

**Answer**: `4`

### Q3 (Destructor Order)

```cpp
class A { public: A() { cout << "A"; } ~A() { cout << "~A"; } };
class B { public: B() { cout << "B"; } ~B() { cout << "~B"; } };
class C { public: C() { cout << "C"; } ~C() { cout << "~C"; } };

int main() {
    A a;
    { B b; }
    C c;
    return 0;
}
```

**Answer**: `AB~BC~C~A`

### Q4 (NAT Type)

How many times is the destructor called?

```cpp
class A {
public:
    ~A() { cout << "D"; }
};

int main() {
    A *arr = new A[5];
    delete[] arr;
    return 0;
}
```

**Answer**: `5`

---

## 6.15 Quick Reference

### Class vs Struct in C++

| Feature | class | struct |
|---------|-------|--------|
| Default access | private | public |
| Default inheritance | private | public |
| Usage convention | Complex types | Simple data |

### Constructor Types

| Type | Purpose | Signature |
|------|---------|-----------|
| Default | No-arg initialization | `Class()` |
| Parameterized | Initialize with values | `Class(params)` |
| Copy | Initialize from another object | `Class(const Class&)` |
| Move (C++11) | Transfer resources | `Class(Class&&)` |

### Key Rules

1. **Default constructor** added only if no constructor defined
2. **Copy constructor** called for initialization, not assignment
3. **Destructor** called in reverse order of construction
4. **Static members** exist before any object
5. **Friend** bypasses access control but doesn't create membership

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Intermediate]**

*Next: [Chapter 7: Inheritance and Polymorphism →](07-Inheritance-Polymorphism.md)*
