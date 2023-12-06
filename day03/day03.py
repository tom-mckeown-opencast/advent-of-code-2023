import os
import re


class Number:
  def __init__(self, row: int, left: int, right: int, value: str) -> None:
    self.value = int(value)
    self.adj = {(row, left - 1), (row, right)}
    for col in range(left - 1, right + 1):
      self.adj.add((row + 1, col))
      self.adj.add((row - 1, col))

def create_grid(input):
  numbers: list[Number] = []
  symbols = {}
  pattern = re.compile(r"(?P<number>\d+)|(?P<symbol>[^\d.])")
  for row, line in enumerate(input):
    for m in pattern.finditer(line):
      number, symbol = m.groups()
      col = m.start()
      if number:
        numbers.append(Number(row, col, m.end(), number))
      elif symbol:
        symbols[row, col] = symbol
  return numbers, symbols
  
def solve_part_1(input: list[str]) -> int:
  numbers, symbols = create_grid(input)
  return sum(num.value for num in numbers if num.adj & symbols.keys())
  
def solve_part_2(input: list[str]) -> int:
  numbers, symbols = create_grid(input)
  gears = { coord: [] for coord, symbol in symbols.items() if symbol == "*" }
  for num in numbers:
    for coords in num.adj:
      if (gear := gears.get(coords)) is not None:
        gear.append(num.value)
  valueList = [values for coord, values in gears.items() if len(values) == 2]
  return sum([value[0] * value[1] for value in valueList])

if __name__ == "__main__":
  scriptDir = os.path.dirname(os.path.abspath(__file__))
  def load_input(fileName) -> list[str]:
    with open(os.path.join(scriptDir, fileName), "r") as file:
      return [line.strip() for line in file]

  example = load_input("example.txt")
  real = load_input("input.txt")

  assert(solve_part_1(example) == 4361)
  assert(solve_part_2(example) == 467835)

  print("Day 3")
  print(f"- Part 1: {solve_part_1(real)}")
  print(f"- Part 2: {solve_part_2(real)}")