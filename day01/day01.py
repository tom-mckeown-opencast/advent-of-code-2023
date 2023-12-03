import os
import re

scriptDir = os.path.dirname(os.path.abspath(__file__))
fileDir = os.path.join(scriptDir, "input.txt")

class Day01:
  def load_input(self) -> None:
    with open(fileDir, "r") as file:
      self.input = [line.strip() for line in file]

  def load_p1_example(self) -> None:
    self.input = [
      "1abc2",
      "pqr3stu8vwx",
      "a1b2c3d4e5f",
      "treb7uchet"
    ]

  def solve_part_1(self) -> int:
    numerics = [re.sub("[^0-9]", "", line) for line in self.input]
    calibration = [line[0] + line[-1] for line in numerics]
    calibration_sum = sum(int(number) for number in calibration)
    return calibration_sum

  def load_p2_example(self) -> None:
    self.input = [
      "two1nine",
      "eightwothree",
      "abcone2threexyz",
      "xtwone3four",
      "4nineeightseven2",
      "zoneight234",
      "7pqrstsixteen"
    ]

  def solve_part_2(self) -> int:
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
    
    calibration = [get_digit(line) + get_digit(line, -1) for line in self.input]
    calibration_sum = sum(int(number) for number in calibration)
    return calibration_sum

if __name__ == "__main__":
  day = Day01()
  # Check part 1 example
  day.load_p1_example()
  assert(day.solve_part_1() == 142)

  # Check part 2 example
  day.load_p2_example()
  assert(day.solve_part_2() == 281)

  # Solve
  day.load_input()
  print("Day 1")
  print(f"- Part 1: {day.solve_part_1()}")
  print(f"- Part 2: {day.solve_part_2()}")
  