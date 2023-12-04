import os
import re

scriptDir = os.path.dirname(os.path.abspath(__file__))
fileDir = os.path.join(scriptDir, "input.txt")

class Day04:
  def load_input(self) -> None:
    with open(fileDir, "r") as file:
      self.input = [line.strip() for line in file]

  def load_p1_example(self) -> None:
    self.input = [
      "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
      "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
      "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
      "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
      "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
      "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
    ]

  def solve_part_1(self) -> int:
    points = 0
    for card in self.split_cards():
      if (matches := card[0] & card[1]):
        points += 2 ** (len(matches) - 1)
    return points

  def load_p2_example(self) -> None:
    self.load_p1_example()

  def solve_part_2(self) -> int:
    cards: dict[int, int] = { }
    for index, card in enumerate(self.split_cards()):
      copies = cards.get(index, 0) + 1
      cards[index] = copies
      if (matches := card[0] & card[1]):
        for i in range(len(matches)):
          cards[index + i + 1] = cards.get(index + i + 1, 0) + copies

    return sum(cards.values())
  
  def split_cards(self):
    cards = []
    for card in self.input:
      prefix = re.search(r"Card\s*\d+:", card).group()
      left, right = card.replace(prefix, "").split("|")
      left_numbers = {int(num) for num in left.strip().split()}
      right_numbers = {int(num) for num in right.strip().split()}
      cards.append((left_numbers, right_numbers))
    return cards

if __name__ == "__main__":
  day = Day04()
  # Check part 1 example
  day.load_p1_example()
  assert(day.solve_part_1() == 13)

  # Check part 2 example
  day.load_p2_example()
  assert(day.solve_part_2() == 30)

  # Solve
  day.load_input()
  print("Day 4")
  print(f"- Part 1: {day.solve_part_1()}")
  print(f"- Part 2: {day.solve_part_2()}")
  