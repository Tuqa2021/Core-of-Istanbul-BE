A class is like a blueprint for creating objects. Objects are instances of a class and can have their own unique data.
Constructor (Initializer):
You can define a special method called __init__ within a class to initialize its attributes. This method is called when you create a new object from the class
**Instance Variables**: Variables defined within the `__init__` method and prefaced with `self` are instance variables. They are unique to each object and can be accessed with dot notation.
**Class Variables**: Class variables are shared among all instances of a class. They are defined within the class but outside any method.
**Methods**: Methods are functions defined within a class. They can access and modify instance variables.
**Inheritance**: Python supports inheritance, allowing you to create a new class based on an existing class. The new class (subclass) can inherit attributes and methods from the base class (superclass).
Polymorphism: Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables you to write more generic and reusable code.
Method Overriding: Subclasses can override methods of their superclass to provide specialized implementations while maintaining the same method signature.
Abstraction: Abstraction involves simplifying complex reality by modeling classes based on the essential characteristics and behaviors of real-world objects.
Magic Methods: Python has special methods like __str__, __add__, and __eq__, which can be defined to customize the behavior of your class.
Class and Static Methods: Besides instance methods, you can define class methods (using @classmethod) and static methods (using @staticmethod) within a class.
Getter and Setter Methods: You can create getter and setter methods to control access to instance variables, enabling data validation and encapsulation.
Follow naming conventions for classes (CamelCase) and use meaningful class and method names. Document your classes and methods using docstrings.
Composition vs. Inheritance: Prefer composition over inheritance when designing classes. It's often more flexible and less prone to issues.
Class Modularity: Aim for classes with single responsibilities. Each class should do one thing well (the Single Responsibility Principle).
Dunder Methods for Customization: we can use dunder methods to customize how your objects behave in specific contexts. For example, __str__ for human-readable representations, __eq__ for object equality, and __lt__ for less-than comparisons.