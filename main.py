# Math Magician Main File
# usage: math operator operand1 operand2

def subtract(a, b):
      """Subtract b from a"""
      return a - b

def main():
      import sys

      print("Welcome to Math Magician!")


      op = sys.argv[1]
      a = float(sys.argv[2])
      b = float(sys.argv[3])

      if op == "subtract":
            result = subtract(a, b)
            print(f"{a} - {b} = {result}")


if __name__ == "__main__":
      main()