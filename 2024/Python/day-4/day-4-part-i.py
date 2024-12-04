import sys
import re
from collections import defaultdict, Counter

sys.setrecursionlimit(10**6)

# Input file handling
infile = sys.argv[1] if len(sys.argv) >= 2 else 'day-4-input.in'
p1 = 0
p2 = 0
D = open(infile).read().strip()
G = D.split('\n')  # Splitting the input into lines for the grid

def count_xmas(grid):
    # Define the word we're searching for
    word = "XMAS"
    word_length = len(word)
    
    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # Directions: (row_change, col_change) for 8 directions
    directions = [
        (-1, 0), (1, 0),  # vertical up, vertical down
        (0, -1), (0, 1),  # horizontal left, horizontal right
        (-1, -1), (1, 1),  # diagonal up-left, diagonal down-right
        (-1, 1), (1, -1)   # diagonal up-right, diagonal down-left
    ]
    
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    def find_word(r, c, dr, dc):
        # Check if word can be formed starting from (r, c) in direction (dr, dc)
        for i in range(word_length):
            nr, nc = r + dr * i, c + dc * i
            if not is_valid(nr, nc) or grid[nr][nc] != word[i]:
                return False
        return True
    
    count = 0
    for r in range(rows):
        for c in range(cols):
            # Check if the current cell can be the start of the word "XMAS"
            if grid[r][c] == word[0]:  # If the first character matches
                for dr, dc in directions:
                    if find_word(r, c, dr, dc):
                        count += 1
                        
    return count

# Using the grid G from the input
answer = count_xmas(G)
print(answer)
