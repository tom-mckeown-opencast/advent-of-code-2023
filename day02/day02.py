import os
import re

scriptDir = os.path.dirname(os.path.abspath(__file__))
fileDir = os.path.join(scriptDir, "input.txt")

class Day02:
  def load_input(self) -> None:
    with open(fileDir, "r") as file:
      self.input = [line.strip() for line in file]

  def load_p1_example(self) -> None:
    self.input = [
      "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
      "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
      "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
      "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
      "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ]

  def solve_part_1(self) -> int:
    def is_valid(rgb) -> bool:
      return rgb["red"] <= 12 and rgb["green"] <= 13 and rgb["blue"] <= 14
    
    game_rgbs = [self.get_rgb(line) for line in self.input]
    possible_games = [i + 1 for i, game in enumerate(game_rgbs) if is_valid(game)]
    return sum(possible_games)

  def load_p2_example(self) -> None:
    self.load_p1_example()
  
  def solve_part_2(self) -> int:
    game_rgbs = [self.get_rgb(line) for line in self.input]
    powers = [rgb["red"] * rgb["green"] * rgb["blue"] for rgb in game_rgbs]
    return sum(powers)

  def get_rgb(self, line) -> None:
    matches = re.findall(r'(\d+) (\w+)', line)
    result = { "red": 0, "green": 0, "blue": 0}
    for quantity, colour in matches:
      result[colour] = max(result[colour], int(quantity))
    return result

if __name__ == "__main__":
  day = Day02()
  # Check part 1 example
  day.load_p1_example()
  assert(day.solve_part_1() == 8)

  # Check part 2 example
  day.load_p2_example()
  assert(day.solve_part_2() == 2286)

  # Solve
  day.load_input()
  print("Day 2")
  print(f"- Part 1: {day.solve_part_1()}")
  print(f"- Part 2: {day.solve_part_2()}")