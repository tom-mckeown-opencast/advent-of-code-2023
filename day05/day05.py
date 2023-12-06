import collections
import os
import re

SeedRange = collections.namedtuple("SeedRange", ["number", "range"])
Mapping = collections.namedtuple("Mapping", ["dest", "source", "range"])
class Map:
  def __init__(self) -> None:
    self.mappings: list[Mapping] = []

  def add_mapping(self, vals: list[int]) -> None:
    self.mappings.append(Mapping(vals[0], vals[1], vals[2]))
  
  def map(self, input: int) -> int:
    for mapping in self.mappings:
      if (mapping.source <= input and input < (mapping.source + mapping.range)):
        difference = input - mapping.source
        return mapping.dest + difference
    return input
  
  def unmap(self, input: int) -> int:
    for mapping in self.mappings:
      if (mapping.dest <= input and input < (mapping.dest + mapping.range)):
        difference = input - mapping.dest
        return mapping.source + difference
    return input

class Almanac:
  map_names = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location"
  ]

  def __init__(self, input: list[str]) -> None:
    self.seed_to_soil = Map()
    self.soil_to_fertilizer = Map()
    self.fertilizer_to_water = Map()
    self.water_to_light = Map()
    self.light_to_temperature = Map()
    self.temperature_to_humidity = Map()
    self.humidity_to_location = Map()
    self.__create_maps__(input)

  def __create_maps__(self, input: list[str]) -> None:
    map_name = ""
    for line in input:
      if line == "":
        map_name = ""
      elif re.match(r".+map:", line):
        map_name = line.replace(" map:", "").replace("-", "_")
      elif re.match(r"\d+ \d+ \d+", line):
        map = getattr(self, map_name) if hasattr(self, map_name) else Map()
        map.add_mapping([int(val) for val in line.split()])
        setattr(self, map_name, map)

  def get_location(self, seed_number: int) -> int:
    val = self.seed_to_soil.map(seed_number)
    val = self.soil_to_fertilizer.map(val)
    val = self.fertilizer_to_water.map(val)
    val = self.water_to_light.map(val)
    val = self.light_to_temperature.map(val)
    val = self.temperature_to_humidity.map(val)
    return self.humidity_to_location.map(val)
  
  def get_seed_number(self, location: int) -> int:
    val = self.humidity_to_location.unmap(location)
    val = self.temperature_to_humidity.unmap(val)
    val = self.light_to_temperature.unmap(val)
    val = self.water_to_light.unmap(val)
    val = self.fertilizer_to_water.unmap(val)
    val = self.soil_to_fertilizer.unmap(val)
    return self.seed_to_soil.unmap(val)

def seed_in_range(seed_number: int, seed_range: SeedRange) -> bool:
  return seed_range.number <= seed_number and seed_number < (seed_range.number + seed_range.range)

def solve_part_1(input: list[str]) -> int:
  almanac = Almanac(input)
  seeds_line = input[0].replace("seeds: ", "").split()
  lowest = almanac.get_location(int(seeds_line[0]))
  for seed in [SeedRange(int(val), 1) for val in seeds_line]:
    lowest = min(lowest, almanac.get_location(seed.number))
  return lowest

def solve_part_2(input: list[str]) -> int:
  almanac = Almanac(input)
  seeds_line = input[0].replace("seeds: ", "").split()
  seed_ranges = []
  for i in range(0, len(seeds_line), 2):
    seed_ranges.append(SeedRange(int(seeds_line[i]), int(seeds_line[i + 1])))
  
  location = 0
  print("Brute forcing by location... This might take a while...")
  while (True):
    seed_number = almanac.get_seed_number(location)
    if (any(seed_in_range(seed_number, range) for range in seed_ranges)):
      return location
    location += 1

if __name__ == "__main__":
  scriptDir = os.path.dirname(os.path.abspath(__file__))
  def load_input(fileName) -> list[str]:
    with open(os.path.join(scriptDir, fileName), "r") as file:
      return [line.strip() for line in file]

  example = load_input("example.txt")
  real = load_input("input.txt")

  assert(solve_part_1(example) == 35)
  assert(solve_part_2(example) == 46)

  print("Day 5")
  print(f"- Part 1: {solve_part_1(real)}")
  print(f"- Part 2: {solve_part_2(real)}")