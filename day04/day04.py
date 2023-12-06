import os
import re


def split_cards(input: list[str]):
  cards = []
  for card in input:
    prefix = re.search(r"Card\s*\d+:", card).group()
    left, right = card.replace(prefix, "").split("|")
    left_numbers = {int(num) for num in left.strip().split()}
    right_numbers = {int(num) for num in right.strip().split()}
    cards.append((left_numbers, right_numbers))
  return cards

def solve_part_1(input: list[str]) -> int:
  points = 0
  for card in split_cards(input):
    if (matches := card[0] & card[1]):
      points += 2 ** (len(matches) - 1)
  return points
  
def solve_part_2(input: list[str]) -> int:
  cards: dict[int, int] = { }
  for index, card in enumerate(split_cards(input)):
    copies = cards.get(index, 0) + 1
    cards[index] = copies
    if (matches := card[0] & card[1]):
      for i in range(len(matches)):
        cards[index + i + 1] = cards.get(index + i + 1, 0) + copies
  return sum(cards.values())

if __name__ == "__main__":
  scriptDir = os.path.dirname(os.path.abspath(__file__))
  def load_input(fileName) -> list[str]:
    with open(os.path.join(scriptDir, fileName), "r") as file:
      return [line.strip() for line in file]

  example = load_input("example.txt")
  real = load_input("input.txt")

  assert(solve_part_1(example) == 13)
  assert(solve_part_2(example) == 30)

  print("Day 4")
  print(f"- Part 1: {solve_part_1(real)}")
  print(f"- Part 2: {solve_part_2(real)}")