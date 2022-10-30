# Classes

```python
class Person:
    species = "Homo Extra Sapiens"

    def __init__(self, name, age):
        self.name= name
				self.age = age

    # Instance method
    def birthday(self):
       self.age += 1

		# Another one with argument
		def talk(self, phrase):
				print(f"{self.name}: {phrase}"
```

```python
tom = Person("Tom Hawks", 66)
print(tom.name)
print(tom.age)
tom.birthday()
print(tom.age)
tom.talk("Hi, I'm Tom!")
print(tom)
```

```python
Tom Hawks
66
67
Tom Hawks: Hi, I'm Tom!
<__main__.Person object at 0x000002CD02963FD0>
```

Dunder Methods

```python
class Person:
    species = "Homo Extra Sapiens"

    def __init__(self, name, age):
        self.name= name
				self.age = age

    # Instance method
    def birthday(self):
       self.age += 1

		# Another one with argument
		def talk(self, phrase):
				print(f"{self.name}: {phrase}"

		def __str__(self):
        return self.name

print(Person("Tom Hawks", 66))
```

```python
Tom Hawks
```

Methods like `.__init__()` and `.__str__()` are called **dunder methods**
 because they begin and end with double underscores. There are many dunder methods that you can use to customize classes in Python.

Child and Parent Classes

```python
class Doctor(Person):
		pass

class PoliceMan(Person):
		pass
```

```python
meredith = Doctor("Meredith Grey", 52)
horatio = PoliceMan("Horatio Caine", 66)

type(meredith)
isinstance(meredith, PoliceMan)
isinstance(horatio, Person)
```

- Result
    
    ```bash
    <class '__main__.Doctor'>
    False
    True
    ```
    

```python
class Influencer(Person):
		def __init__(self):
				self.brands = set()
				super().__init__()
	
		def post_insta_story():
				raise NotImplementedError()
```