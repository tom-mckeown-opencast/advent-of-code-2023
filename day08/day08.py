import collections
import math
import os
import re

Node = collections.namedtuple("Node", ["left", "right"])

class Network:
  def __init__(self, input: list[str]) -> None:
    self.traversal = [c for c in input[0]]
    self.nodes: dict[str, Node] = {
      line[:3]: Node(line[7:10], line[12:15]) for line in input[2:]
    }

  def traverse(self, startNode: str = "AAA", endPattern: str = "ZZZ") -> int:
    end_regex = re.compile(endPattern)
    steps: int = 0
    currentNode: str = startNode
    while not end_regex.match(currentNode):
      nextInstruction = self.traversal[steps % len(self.traversal)]
      currentNode = self.nodes[currentNode].left if nextInstruction == "L" else self.nodes[currentNode].right
      steps += 1
    return steps
  
  def traverse_lcm(self) -> int:
    start_regex = re.compile(r"\w\wA")
    node_steps: list[int] = [ self.traverse(node, r"\w\wZ") for node in self.nodes if start_regex.match(node) ]
    return math.lcm(*node_steps)

def solve_part_1(input: list[str]) -> int:
  network = Network(input)
  return network.traverse()
  
def solve_part_2(input: list[str]) -> int:
  network = Network(input)
  return network.traverse_lcm()

if __name__ == "__main__":
  scriptDir = os.path.dirname(os.path.abspath(__file__))
  def load_input(fileName) -> list[str]:
    with open(os.path.join(scriptDir, fileName), "r") as file:
      return [line.strip() for line in file]

  example1 = load_input("example1.txt")
  example2 = load_input("example2.txt")
  example3 = load_input("example3.txt")
  real = load_input("input.txt")

  assert(solve_part_1(example1) == 2)
  assert(solve_part_1(example2) == 6)
  assert(solve_part_2(example3) == 6)

  print("Day 8")
  print(f"- Part 1: {solve_part_1(real)}")
  print(f"- Part 2: {solve_part_2(real)}")