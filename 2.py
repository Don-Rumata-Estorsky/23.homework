import math
class Complex:
  def __init__(self, real, imag):
    self.real = real
    self.imag = imag

  def __add__(self, other):
      return Complex(self.real + other.real, self.imag + other.imag)

  def __sub__(self, other):
      return Complex(self.real - other.real, self.imag - other.imag)

  def __mul__(self, other):
      real = self.real * other.real - self.imag * other.imag
      imag = self.real * other.imag + self.imag * other.real
      return Complex(real, imag)

  def __truediv__(self, other):
      denominator = other.real ** 2 + other.imag ** 2
      real = (self.real * other.real + self.imag * other.imag) / denominator
      imag = (self.imag * other.real - self.real * other.imag) / denominator
      return Complex(real, imag)

  def __neg__(self):
    return Complex(-self.real, -self.imag)

  def __abs__(self):
    return math.sqrt(self.real ** 2 + self.imag ** 2)

  def __str__(self):
    if self.imag == 0:
      return f"{self.real}"
    elif self.imag > 0:
      return f"{self.real}+{self.imag}j"
    else:
      return f"{self.real}{self.imag}j"

if __name__ == "__main__":
  real_part1 = float(input("Введите вещественную часть первого числа: "))
  imag_part1 = float(input("Введите мнимую часть первого числа: "))
  num1 = Complex(real_part1, imag_part1)    
  print("")
  real_part2 = float(input("Введите вещественную часть второго числа: "))
  imag_part2 = float(input("Введите мнимую часть второго числа: "))
  num2 = Complex(real_part2, imag_part2)  
  print("")
  print(f"Первое число = {num1}")
  print(f"Второе число = {num2}")
  print("")
  print("Сумма:")
  print(num1 + num2)
  print("")
  print("Разность:")
  print(num1 - num2)
  print("")
  print("Произведение:")
  print(num1 * num2)
  print("")
  print("Деление:")
  print(num1 / num2)
  print("")
















