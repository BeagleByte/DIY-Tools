# Name of the Project: foobar

## Scope: The project is meant to be run on ....
### Workflow:
<Support the agent with diagram if possible, Mermaid is a goog choice>

## Rules: 
       - Use for every method not more than three parameters.
       - Methods must be atomic with a single purpose
       - Use object oriented programming
       - create meaningful classes
       - document steps, method and classes
       - create the code, that someone else can read and understand what are those line of code doing
       - single responsibilty
       - interchangeable databases, LLM's, agent or other third party tools and programs
       - don't repeat yourself
       - don't overcomplicated it
       - follow KISS principles
       - check for third party dependencies, and if they REALLY necessary
       - avoid deprecated dependencies
       - IF the program needs high CPU usage, use concurrency, multithreading
       - Handle errors explicitly
       - logging errors and infos

## Desing Patterns: 
Make usage of design pattern IF necessary! Combine it with Rules of OOP and creation of classes

### Creational Design Patterns

Abstract Factory: Creates families of related or dependent objects without specifying their concrete classes.
Builder: Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
Prototype: Specifies the kinds of objects to create using a prototypical instance, and creates new objects by copying this prototype.
Singleton: Ensures a class has only one instance and provides a global point of access to it. 

### Structural Design Patterns

Adapter: Allows incompatible interfaces to work together by converting one interface into another expected by the client.
Bridge: Decouples an abstraction from its implementation so both can vary independently.
Composite: Composes objects into tree structures to represent part-whole hierarchies, allowing clients to treat individual objects and compositions uniformly.
Decorator: Adds new functionality to an object dynamically without altering its structure.
Facade: Provides a simplified interface to a complex subsystem.
Flyweight: Uses sharing to support large numbers of similar objects efficiently.
Proxy: Provides a surrogate or placeholder for another object to control access to it. 

### Behavioral Design Patterns

Chain of Responsibility: Passes a request along a chain of handlers, with each handler deciding either to process the request or pass it to the next handler.
Command: Encapsulates a request as an object, enabling parameterization of clients with different requests, queuing of requests, and support for undoable operations.
Interpreter: Defines a representation for a grammar and an interpreter to interpret sentences in the language.
Iterator: Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
Mediator: Defines an object that encapsulates how a set of objects interact, promoting loose coupling.
Memento: Captures and externalizes an object's internal state without violating encapsulation, allowing the object to be restored to this state later.
Observer (Publish/Subscribe): Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified automatically.
State: Allows an object to alter its behavior when its internal state changes, making it appear to change its class.
Strategy: Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
Template Method: Defines the skeleton of an algorithm in a method, deferring some steps to subclasses.
Visitor: Represents an operation to be performed on the elements of an object structure, allowing new operations to be defined without changing the classes of the elements. 

### Concurrency Patterns

Active Object: Decouples method execution from invocation by using asynchronous method invocation and a scheduler.
Balking: Only performs an action if the object is in a specific state.
Double-Checked Locking: Reduces lock overhead by checking the locking condition before acquiring the lock.
Guarded Suspension: Manages operations that require both a lock and a precondition to be satisfied before execution.
Reactor: Provides an asynchronous interface to resources that must be handled synchronously.
Thread Pool: Reuses a fixed number of threads to execute tasks from a queue. 

### Architectural Patterns

MVC (Model-View-Controller): Separates an application into three interconnected components to manage complexity.
MVP (Model-View-Presenter): A variation of MVC where the presenter handles all the logic and updates the view.
MVVM (Model-View-ViewModel): Used primarily in UI frameworks like WPF and modern web apps, it separates UI logic from business logic using data binding.
Front Controller: Centralizes request handling in web applications.
n-Tier Architecture: Splits an application into multiple layers (e.g., presentation, business logic, data access).
Microservices: Architectural style where an application is composed of small, independent services communicating over defined APIs.


## Stakeholder: Private usage for to explore and learn about using LLM coding agents.

## Tasks:
1. Task
2. Task

## Libraries and Tool usage
Describe if necessary which libraries or tool suposed to be used, in the project

## Tests:
Project specific tests. Integration test. Comparison of different approaches etc.

