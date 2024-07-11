
"""
создать класс Airplane  для него создать перегруженные операторы как 
проверка типов самолётов ==
 увеличение кол-во пассажиров на борту + - += -=
 сравнение кол-во пассажиров:   > < >= <= 
"""
import math

class  Airplane:
  def __init__(self, type_of_plane, possajiri ):
     self.type_of_plane = type_of_plane
     self.possajiri = possajiri

  def __eq__(self, other):
      return self.type_of_plane == other.type_of_plane
  
  def __gt__(self, other):
       return self.possajiri >  other.possajiri

  def __lt__(self, other):
    return self.possajiri < other.possajiri

  def __ge__(self, other):
      return self.possajiri >= other.possajiri

  def __le__(self, other):
       return self.possajiri <= other.possajiri

  def __add__(self, other):
      return Airplane(self.possajiri + other.possajiri)

  def __sub__(self, other):
      return Airplane(self.possajiri - other.possajiri)
    
  def __iadd__(self, other):
      self.possajiri += other.possajiri
      return self
  
  def __isub__(self, other):
      self.possajiri -= other.possajiri
      return self
  
if __name__ == "__main__":
    print(" ")
    plane1 = Airplane(  str(input("vvedite type of first plane: "))   , float(input("vvedite kol-vo possajiri for first plane: ")))
    plane2 = Airplane(  str(input("vvedite type of second plane: "))  ,float(input("vvedite kol-vo possajiri for second plane: ")))
    print(" ")
    print("равны ли типы самолётов: ")
    print(plane1 == plane2) 
    print(" ")
    print("Больше ли в первом самолёте пассажиров: ")
    print(plane1 > plane2)  
    print(" ")
    print("Больше ли во втором самолёте пассажиров:  ")
    print(plane1 < plane2)  
    print(" ")

    plus1 = float(input("Увеличить количество пассажиров на первом самолёте: "))
    plane1new = plane1 + Airplane(plus1)  # по другому не смог                                                            def 11.9
    minus2 = float(input("Увеличить количество пассажиров на первом самолёте: "))
    plane2new = plane2 - Airplane(minus2) 

    print(" ")
    print(f"количество пассажиров на первом борту ={plane1new}, а втором ={plane2new}  ")
    print(" ")
    print("Больше ли людей в первом чем во втором: ")
    print(plane1new > plane2new)  
    print(" ")
    print("Больше ли людей в втором чем во первом:   ")
    print(plane1new < plane2new) 












