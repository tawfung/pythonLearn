# class Dog():
#     def __init__ (self, breed, name, age):
#         self.breed = breed
#         self.name = name
#         self.age = age

# myDog=Dog(breed='Steve', name = 'Joe', age =5)
# print('Breed is:', myDog.breed,'\nName is:',myDog.name,'\nAge is:', myDog.age)


# class Circle():
#     pi=3.14
#     def __init__(self, radius):
#         self.radius =radius

#     def area(self):
#         return self.radius*self.radius* Circle.pi

#     def set_radius(self,new_r):
#         self.radius = new_r

# value = Circle(3)
# value.set_radius(10)
# print(value.area())


# class Animal():
#     def __init__ (self):
#         print('ANIMAL IS CREATED')
#     def whoAmI(self):
#         print('ANIMAL')
#     def eat(self):
#         print("EATING")
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print('Dog is created')
#     def bark(self):
#         print('Woof')
#     def eat(self):
#         print('Dog eat')

# #mya = Animal()
# myDog=Dog()
# myDog.whoAmI()
# myDog.eat()
# myDog.bark()

# class Book():
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages =pages
#     def __str__(self):
#         return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)
#     def __len__(self):
#         return self.pages
#     def __del__(self):
#         print("A book was destroyed!")
# b= Book('Shelock Holmes','Arthur Conan Doyle', 1234)
# print(len(b))
# del b