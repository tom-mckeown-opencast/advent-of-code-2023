import os
import re


def get_digit(text: str, step: int = 1) -> str:
  written_digits = {
    "one": "1", "two": "2", "three": "3",
    "four": "4", "five": "5", "six": "6",
    "seven": "7", "eight": "8", "nine": "9"
  }

  match = re.search(r"\d|" + "|".join([key[::step] for key in written_digits.keys()]), text[::step], re.IGNORECASE)
  if match:
    result = match.group().lower()[::step]
    return written_digits.get(result, result)
  else:
    None

def solve_part_1(input: list[str]) -> int:
  numerics = [re.sub("[^0-9]", "", line) for line in input]
  calibration = [line[0] + line[-1] for line in numerics]
  return sum(int(number) for number in calibration)

def solve_part_2(input: list[str]) -> int:  
  calibration = [get_digit(line) + get_digit(line, -1) for line in input]
  return sum(int(number) for number in calibration)

if __name__ == "__main__":
  scriptDir = os.path.dirname(os.path.abspath(__file__))
  def load_input(fileName) -> list[str]:
    with open(os.path.join(scriptDir, fileName), "r") as file:
      return [line.strip() for line in file]

  example1 = load_input("example1.txt")
  example2 = load_input("example2.txt")
  real = load_input("input.txt")

  assert(solve_part_1(example1) == 142)
  assert(solve_part_2(example2) == 281)

  print("Day 1")
  print(f"- Part 1: {solve_part_1(real)}")
  print(f"- Part 2: {solve_part_2(real)}")
  