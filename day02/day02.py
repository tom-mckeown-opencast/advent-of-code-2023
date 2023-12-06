import os
import re


def get_rgb(line) -> dict[str, int]:
  matches = re.findall(r'(\d+) (\w+)', line)
  result = { "red": 0, "green": 0, "blue": 0}
  for quantity, colour in matches:
    result[colour] = max(result[colour], int(quantity))
  return result

def is_valid(rgb) -> bool:
  return rgb["red"] <= 12 and rgb["green"] <= 13 and rgb["blue"] <= 14

def solve_part_1(input: list[str]) -> int:
  game_rgbs = [get_rgb(line) for line in input]
  possible_games = [i + 1 for i, game in enumerate(game_rgbs) if is_valid(game)]
  return sum(possible_games)
  
def solve_part_2(input: list[str]) -> int:
  game_rgbs = [get_rgb(line) for line in input]
  powers = [rgb["red"] * rgb["green"] * rgb["blue"] for rgb in game_rgbs]
  return sum(powers)

if __name__ == "__main__":
  scriptDir = os.path.dirname(os.path.abspath(__file__))
  def load_input(fileName) -> list[str]:
    with open(os.path.join(scriptDir, fileName), "r") as file:
      return [line.strip() for line in file]

  example = load_input("example.txt")
  real = load_input("input.txt")

  assert(solve_part_1(example) == 8)
  assert(solve_part_2(example) == 2286)

  print("Day 2")
  print(f"- Part 1: {solve_part_1(real)}")
  print(f"- Part 2: {solve_part_2(real)}")