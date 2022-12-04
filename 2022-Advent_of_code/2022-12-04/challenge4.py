def main():
  pairs_overlaps, range_overlaps = 0, 0
  with open('input4.txt') as assignment_ranges:
    for assignment_range in assignment_ranges:
      ar1, ar2 = assignment_range.split(',')
      ar1s, ar1e, ar2s, ar2e = range_builder(ar1, ar2)
      overlaps = overlap_checking(ar1s, ar1e, ar2s, ar2e)
      if overlaps:
        range_overlaps += 1
      pairs = pairs_checking(ar1s, ar1e, ar2s, ar2e)
      if pairs:
          pairs_overlaps += 1
    print(f' Part1: {range_overlaps},  Part2: {pairs_overlaps}')


def range_builder(ar1, ar2):
  ar1_1, ar1_2 = ar1.split('-')
  ar2_1, ar2_2 = ar2.split('-')
  ar1_start = int(ar1_1)
  ar1_end = (int(ar1_2) + 1)
  ar2_start = int(ar2_1)
  ar2_end = (int(ar2_2) + 1)
  return ar1_start, ar1_end, ar2_start, ar2_end


def overlap_checking(ar1s, ar1e, ar2s, ar2e):
    if set((range(ar1s, ar1e))).issubset(range(ar2s, ar2e)):
        return True
    if set((range(ar2s, ar2e))).issubset(range(ar1s, ar1e)):
        return True


def pairs_checking(ar1s, ar1e, ar2s, ar2e):
    for i in range(ar1s, ar1e):
        if i in range(ar2s, ar2e):
            return True

if __name__ == '__main__':
  main()
