import os
import re


def solve_part_1(input: list[str]) -> int:
  return
  
def solve_part_2(input: list[str]) -> int:
  return

if __name__ == "__main__":
  scriptDir = os.path.dirname(os.path.abspath(__file__))
  def load_input(fileName) -> list[str]:
    with open(os.path.join(scriptDir, fileName), "r") as file:
      return [line.strip() for line in file]

  example = load_input("example.txt")
  real = load_input("input.txt")

  assert(solve_part_1(example) == None)
  assert(solve_part_2(example) == None)

  print("Day Template")
  print(f"- Part 1: {solve_part_1(real)}")
  print(f"- Part 2: {solve_part_2(real)}")