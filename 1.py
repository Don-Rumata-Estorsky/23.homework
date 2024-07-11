"""
создать класс Circle (окружность) для него создать перегруженные операторы как 
проверка равенства ==
 сравнение:   > < >= <= 
 пропорциональное увеличение окружности + - += -=

"""
import math

class  Circle:
  def __init__(self, radius ):
     self.radius = radius

  def __eq__(self, other):
      return self.radius == other.radius
  
  def __gt__(self, other):
       return self.radius >  other.radius

  def __lt__(self, other):
    return self.radius < other.radius

  def __ge__(self, other):
      return self.radius >= other.radius

  def __le__(self, other):
       return self.radius <= other.radius

  def __add__(self, other):
      return Circle(self.radius + other.radius)

  def __sub__(self, other):
      return Circle(self.radius - other.radius)
    
  def __iadd__(self, other):
      self.radius += other.radius
      return self
  
  def __isub__(self, other):
      self.radius -= other.radius
      return self
  
  def __str__(self):
    return f" имеет радиус {self.radius}"

if __name__ == "__main__":
    print(" ")
    circle1 = Circle(float(input("vvedite radius for krug number№1 : ")))
    circle2 = Circle(float(input("vvedite radius for krug number№2 : ")))
    print(" ")
    print("Равны ли две окружности: ")
    print(circle1 == circle2) 
    print(" ")
    print("Больше ли первая окружность чем вторая: ")
    print(circle1 > circle2)  
    print(" ")
    print("Больше ли вторая окружность чем первая:  ")
    print(circle1 < circle2)  
    print(" ")

    plus1 = float(input("Увеличить первую окружность: "))
    circle1new = circle1 + Circle(plus1)  # по другому не смог 
    minus2 = float(input("Уменьшить вторую окружность: "))
    circle2new = circle2 - Circle(minus2) 

    print(" ")
    print(f"теперь первый круг ={circle1new}, а второй ={circle2new}  ")
    print(" ")
    print("Равны ли две окружности: ")
    print(circle1new == circle2new) 
    print(" ")
    print("Больше ли первая окружность чем вторая: ")
    print(circle1new > circle2new)  
    print(" ")
    print("Больше ли вторая окружность чем первая:  ")
    print(circle1new < circle2new) 