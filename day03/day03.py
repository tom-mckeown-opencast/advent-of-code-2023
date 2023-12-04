import os
import re

scriptDir = os.path.dirname(os.path.abspath(__file__))
fileDir = os.path.join(scriptDir, "input.txt")

class Number:
  def __init__(self, row: int, left: int, right: int, value: str) -> None:
    self.value = int(value)
    self.adj = {(row, left - 1), (row, right)}
    for col in range(left - 1, right + 1):
      self.adj.add((row + 1, col))
      self.adj.add((row - 1, col))

class Day03:
  def load_input(self) -> None:
    with open(fileDir, "r") as file:
      self.input = [line.strip() for line in file]

  def load_p1_example(self) -> None:
    self.input = [
      "467..114..",
      "...*......",
      "..35..633.",
      "......#...",
      "617*......",
      ".....+.58.",
      "..592.....",
      "......755.",
      "...$.*....",
      ".664.598.."
    ]
  
  def solve_part_1(self) -> int:
    self.create_grid()
    return sum(num.value for num in self.numbers if num.adj & self.symbols.keys())

  def load_p2_example(self) -> None:
    self.load_p1_example()
  
  def solve_part_2(self) -> int:
    self.create_grid()
    gears = { coord: [] for coord, symbol in self.symbols.items() if symbol == "*" }
    for num in self.numbers:
      for coords in num.adj:
        if (gear := gears.get(coords)) is not None:
          gear.append(num.value)
    valueList = [values for coord, values in gears.items() if len(values) == 2]
    return sum([value[0] * value[1] for value in valueList])
  
  def create_grid(self) -> None:
    self.numbers: list[Number] = []
    self.symbols = {}
    pattern = re.compile(r"(?P<number>\d+)|(?P<symbol>[^\d.])")
    for row, line in enumerate(self.input):
      for m in pattern.finditer(line):
        number, symbol = m.groups()
        col = m.start()
        if number:
          self.numbers.append(Number(row, col, m.end(), number))
        elif symbol:
          self.symbols[row, col] = symbol

if __name__ == "__main__":
  day = Day03()
  # Check part 1 example
  day.load_p1_example()
  assert(day.solve_part_1() == 4361)

  # Check part 2 example
  day.load_p2_example()
  assert(day.solve_part_2() == 467835)

  # Solve
  day.load_input()
  print("Day 3")
  print(f"- Part 1: {day.solve_part_1()}")
  print(f"- Part 2: {day.solve_part_2()}")