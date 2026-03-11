# Math Magician Main File
# usage: math operator operand1 operand2

def main():
      import sys

      print("Welcome to Math Magician!")


      op = sys.argv[1]
      a = float(sys.argv[2])
      b = float(sys.argv[3])


if __name__ == "__main__":
      main()

def add(a, b):
      return a + b

def subtract(a, b):
      """Subtract b from a"""
      return a - b

def division(a,b);
    """Divide a by b"""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b