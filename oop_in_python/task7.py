class Person:
    def __init__(self, name, age):
        """Initializes the person's attributes."""
        self.name = name
        self.age = age
        
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Alice", 30)
person4 = Person("Alice", 31)

print(f"Comparing '{person1.name}' and '{person2.name}':")
print(f"Are they equal? {person1 == person2}")  # Expected: False

print(f"\nComparing '{person1.name}' and '{person3.name}' (same data):")
print(f"Are they equal? {person1 == person3}")  # Expected: True

print(f"\nComparing '{person1.name}' and '{person4.name}' (same name, different age):")
print(f"Are they equal? {person1 == person4}")  # Expected: False

print(f"\nComparing a Person to a string:")
print(f"Are they equal? {person1 == 'Alice'}") # Expected: False
