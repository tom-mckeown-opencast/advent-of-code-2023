# Advent of Code

## [Day 1](./day01/day01.py) - Trebuchet
### Difficulty 1
#### Part 1 
1. Get the number values from the string
2. Concatenate the first and last to get the calibration value
3. Sum all the calibration values
#### Part 2
1. Get the first numeric or written digit using regex
2. Get the last numeric or written digit using regex and reversing
3. Concatenate the first and last to get the calibration value
4. Sum all the calibration values

## [Day 2](./day02/day02.py) - Cube Conundrum
### Difficulty 1
#### Part 1
1. Match the pattern `<quantity> <colour>` using regex
2. Loop through the game string and keep track of the largest values of each colour
3. Count the number of possible games by checking the values of each colour don't exceed the maximum
#### Part 2
1. Match the game pattern - same as part 1
2. Get the product of each game by multiplying the colour counts together
3. Sum the products

## [Day 3](./day03/day03.py) - Gear Ratios
### Difficulty 5
#### Part 1
1. Pattern match to find numbers and symbols in a grid
2. Identify the bounding box for each number
3. Sum all the numbers where a symbol overlaps its bounding box
#### Part 2
1. Pattern match to find numbers and symbols in a grid
2. Identify specifically the gear symbols
3. If the gear overlaps a number's bounding box then keep track of it
4. Filter out gears that only have 2 adjacent numbers
5. Sum the products of each gear 

## [Day 4](./day04/day04.py) - Scratchcards 
### Difficulty 2 
#### Part 1
1. Get all cards in a list of tuples
2. Can work out the matches by getting the set intersection
3. For each card add 2 ^ (number of matches - 1) to total points
4. Answer is total points after all cards are processed
#### Part 2
1. Get all cards in a list of tuples
2. Work out how many copies of each card there are
3. Sum total number of cards after processing

## [Day 5](./day05/day05.py) - If You Give A Seed A Fertilizer
### Difficulty 7
#### Part 1
1. Build up the almanac with maps from seed -> soil -> ... -> location
2. For each seed keep track of the lowest location value
3. Answer is the lowest after all seeds have been processed
#### Part 2
1. Build up the almanac with maps
2. Work out the input seed ranges using every 2 values (initial, range)
3. Starting with 0 increase the location value until we find a match
4. Reverse map from location -> seed and check if it intersects any input seed range
5. Faster than processing all input seeds (~1.3 trillion inputs) but can take a couple of mins to finish

## [Day 6](./day06/day06.py) - Wait For It
### Difficulty 3
#### Part 1
1. Read in races by removing the prefixes and zipping the values together into a tuple
2. Race wins calculated by checking all variations of time held
3. Keep track of a count of wins for each race
4. Calculate the product of the win count for each race
#### Part 2
1. Read in races by removing the prefixes and spaces (for the kerning error part) and zip the values together into a tuple
2. Race wins calculated by checking all variations of time held
3. Keep track of a count of wins
4. Calculate the product of the win count for each race
5. This takes about a minute to calculate this way

## [Day 7](./day07/day07.py) - Camel Cards
### Difficulty 4
#### Part 1
1. Use an enum for the HandType and class to store the hand data (cards + bid)
2. Set up comparator functions to allow sort to work
3. Sort in ascending order
4. Sum the bid * placement for each card
#### Part 2
1. Add an optional wildcard parameter to the hand and HandType
2. If the wildcard is set then reduce its individual value
3. Calculate the best hand type by substituting in the wildcard
4. Sort in ascending order
5. Sum the bid * placement for each card