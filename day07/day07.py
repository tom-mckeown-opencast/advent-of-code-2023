import os
from collections import Counter
from enum import Enum
from functools import total_ordering


@total_ordering
class HandType(Enum):
  FIVE_OF_A_KIND = 6
  FOUR_OF_A_KIND = 5
  FULL_HOUSE = 4
  THREE_OF_A_KIND = 3
  TWO_PAIR = 2
  ONE_PAIR = 1
  HIGH_CARD = 0

  def __str__(self) -> str:
    return self.name
  
  def __eq__(self, other) -> bool:
    return self.value == other.value
  def __lt__(self, other) -> bool:
    return self.value < other.value

  def from_hand(cards: list, wildcard: str = None):
    wildcard_count = cards.count(wildcard)
    if wildcard_count == 5: return HandType.FIVE_OF_A_KIND

    filtered = [card for card in cards if card != wildcard]
    counter_values = list(Counter(filtered).values())
    counter_values.sort(reverse=True)
    counter_values[0] += wildcard_count

    if (counter_values == [5]):
      return HandType.FIVE_OF_A_KIND
    elif (counter_values == [4,1]):
      return HandType.FOUR_OF_A_KIND
    elif (counter_values == [3,2]):
      return HandType.FULL_HOUSE
    elif (counter_values == [3,1,1]):
      return HandType.THREE_OF_A_KIND
    elif (counter_values == [2,2,1]):
      return HandType.TWO_PAIR
    elif (counter_values == [2,1,1,1]):
      return HandType.ONE_PAIR
    else:
      return HandType.HIGH_CARD

@total_ordering
class Hand:
  CONST_MAP = {
    "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10,
    "9":  9, "8":  8, "7":  7, "6":  6, "5":  5,
    "4":  4, "3":  3, "2":  2
  }

  def __init__(self, line: str, wildcard: str = None) -> None:
    self.map = Hand.CONST_MAP.copy()
    if (wildcard): self.map.update({ wildcard: 1 })

    hand, bid = line.split()
    self.bid = int(bid)
    self.cards: list[str] = []
    for card in hand:
      self.cards.append(card)
    self.hand_type = HandType.from_hand(self.cards, wildcard)
  
  def __repr__(self) -> str:
    return f"Hand({''.join(self.cards)}, {self.hand_type}, bid: {self.bid})"
  
  def __eq__(self, other: "Hand") -> bool:
    if self.hand_type != other.hand_type: return False
    for i in range(len(self.cards)):
      if self.cards[i] != other.cards[i]: return False
    return True

  def __lt__(self, other: "Hand") -> bool:
    if self.hand_type != other.hand_type:
      return self.hand_type < other.hand_type
    for i in range(len(self.cards)):
      if self.cards[i] != other.cards[i]:
        return self.map.get(self.cards[i]) < self.map.get(other.cards[i])

def solve_part_1(input: list[str]) -> int:
  hands = [Hand(line) for line in input]
  hands.sort()
  return sum([hand.bid * (index + 1) for index, hand in enumerate(hands)])
  
def solve_part_2(input: list[str]) -> int:
  hands = [Hand(line, wildcard="J") for line in input]
  hands.sort()
  return sum([hand.bid * (index + 1) for index, hand in enumerate(hands)])

if __name__ == "__main__":
  scriptDir = os.path.dirname(os.path.abspath(__file__))
  def load_input(fileName) -> list[str]:
    with open(os.path.join(scriptDir, fileName), "r") as file:
      return [line.strip() for line in file]

  example = load_input("example.txt")
  real = load_input("input.txt")

  assert(solve_part_1(example) == 6440)
  assert(solve_part_2(example) == 5905)

  print("Day 7")
  print(f"- Part 1: {solve_part_1(real)}")
  print(f"- Part 2: {solve_part_2(real)}")