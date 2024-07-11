"""
создать класс Circle (окружность) для него создать перегруженные операторы как 
проверка равенства ==
 сравнение:   > < >= <= 
 пропорциональное увеличение окружности + - += -=
"""
import math

class  flat:
  def __init__(self, ploshad, cost ):
     self.ploshad = ploshad
     self.cost = cost
  def __eq__(self, other):
      return self.ploshad == other.ploshad
  
  def __eq__(self, other):
      return self.ploshad != other.ploshad

  def __gt__(self, other):
       return self.cost >  other.cost

  def __lt__(self, other):
    return self.cost < other.cost

  def __ge__(self, other):
      return self.cost >= other.cost

  def __le__(self, other):
       return self.cost <= other.cost


if __name__ == "__main__":
    print(" ")
    flat1 = flat(float(input("vvedite poloshad for flat number№1 : ")), float(input("vvedite cost  for first flat: ")))
    flat2 = flat(float(input("vvedite poloshad for flat number№2 : ")), float(input("vvedite cost  for second flat: ")))
    print(" ")
    print("Равны ли две окружности: ")
    print(flat1 == flat2) 
    print(" ")
    print("НеРавны ли две окружности: ")
    print(flat1 != flat2) 
    print(" ")
    print("Больше ли первая квартира стоит: ")
    print(flat1 > flat2)  
    print(" ")
    print("Больше ли вторая квартира стоит:  ")
    print(flat1 < flat2)  
    print(" ")
















