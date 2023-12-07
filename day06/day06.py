import collections
import math
import os
import re

Race = collections.namedtuple("Race", ["time", "distance"])

def read_races(timeStr: str, distanceStr: str) -> list[Race]:
  times = [int(time) for time in timeStr.removeprefix("Time:").split()]
  distances = [int(dist) for dist in distanceStr.removeprefix("Distance:").split()]
  return [Race._make(r) for r in zip(times, distances)]

def race_wins(race: Race) -> int:
  wins = 0
  for time_held in range(1, race.time):
    distance = (race.time - time_held) * time_held
    if (distance > race.distance):
      wins += 1
  return wins

def solve_part_1(input: list[str]) -> int:
  races = read_races(input[0], input[1])
  wins = [race_wins(race) for race in races]
  return math.prod(wins)
  
def solve_part_2(input: list[str]) -> int:
  races = read_races(input[0].replace(" ", ""), input[1].replace(" ", ""))
  wins = [race_wins(race) for race in races]
  return math.prod(wins)

if __name__ == "__main__":
  scriptDir = os.path.dirname(os.path.abspath(__file__))
  def load_input(fileName) -> list[str]:
    with open(os.path.join(scriptDir, fileName), "r") as file:
      return [line.strip() for line in file]

  example = load_input("example.txt")
  real = load_input("input.txt")

  assert(solve_part_1(example) == 288)
  assert(solve_part_2(example) == 71503)

  print("Day 6")
  print(f"- Part 1: {solve_part_1(real)}")
  print(f"- Part 2: {solve_part_2(real)}")

