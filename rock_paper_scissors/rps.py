#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  possible_plays = [["rock"], ["paper"], ["scissors"]]
  if n == 0:
    return [[]]
  if n == 1:
    return possible_plays
  else:
    previous_plays = rock_paper_scissors(n - 1)
    new = []
    for play in previous_plays:
      for possibility in possible_plays:
        new.append(play + possibility)
    return new


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')