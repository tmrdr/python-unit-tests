#Rio Grande
Rio Grande is an online retailer founded by Jerome Basile and named after his
favorite river. It started out selling books, but now they sells all sorts of
things. They need your OOP / TDD skills to help them create classes for all the
different types of items in their online store.

##Getting Started

* Fork and clone this repository
* cd into the directory

##Development Process

We are creating this using Test Driven Development. As a refresher, here is the
basic process:

* Create a test for a feature
* Run the test (it should fail)
* Write code for the feature
* Run test again (it should pass)
* Refactor if necessary

##Working in Pairs (recommended)

Due to the TDD-nature of this assignment, it's recommended that you pair up
with another person and work on this collaboratively. If you decide to take
this route:

* Have one person create the tests
* Have the other person create the code to pass the tests
* Each person should submit the same code via pull request

###Tests
Every class should have tests for all of the following:

* Initializer
* instance_of / inheritance
* getters / setters (for each attribute)
* methods
  * Check return value
  * Check that it behaves as expected
* any other expected behaviors

Navigate to the root of this repo and use this command to run the tests:

```
python3 tests.py
```

###Interactive Console
You can also test things manually in the console by starting the python
console with `python3` or `ipython` (ipython provides more features).

Load a class using an import statement, then create an instance of
the class and try interacting with it like below:

```
$ ipython3
In [1]: from items.digital_item import DigitalItem
In [2]: dd = DigitalItem("wonderwall.mp3", .97)
In [3]: dd.name
Out[3]: 'wonderwall.mp3'
In [4]: dd.price
Out[4]: 0.97
```

##Requirements

###Item

Item has already been created for you, along with the tests for Item. Take a
look at the file and inspect what the class does.

###Music, Movies, and Books

Next, let's make the following classes that inherit from Item. Each class
should have the following instance variables, as well as inherit from Item by
calling the `super` method to pass the name and price.

Here's an example of how one class inherits from another:

```py
class Animal:
  def __init__(self, name):
    self.alive = True
    self.name = name

class Reptile(Animal):
  def __init__(self, name, number_of_eggs):
    super().__init__(name)
    self.number_of_eggs = number_of_eggs
```

Create these inheritance relationships:

* Book < Item
  * Pages
  * Author
* Cd < Item
  * Tracks (number of)
  * Artist
  * Run time
* Bluray < Item
  * Run time
  * Director
  * Producer


**Usage Example**

```py
b = Book('Book Title', 12.99, 33, 'Author Name')
```

###Digital Items

Oh no the future is here!! Now we need to support digital items. Digital items are things that are downloaded and therefore they do not have a finite quantity.

* DigitalItem < Item
  * Quantity should always be 1
  * Quantity does not decrease when sold
  * Quantity should not increase on stock

---

## Licensing
1. All content is licensed under a CC-BY-NC-SA 4.0 license.
2. All software code is licensed under GNU GPLv3. For commercial use or alternative licensing, please contact legal@ga.co.
