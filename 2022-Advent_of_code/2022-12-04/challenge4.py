def main():
  range_overlaps = 0
  with open('input4.txt') as assignment_ranges:
    for assignment_range in assignment_ranges:
      ar1, ar2 = assignment_range.split(',')
      ar1s, ar1e, ar2s, ar2e = range_builder(ar1, ar2)
      overlaps = overlap_checking(range(ar1s, ar1e), range(ar2s, ar2e))
      print(overlaps)


def range_builder(ar1, ar2):
  ar1_1, ar1_2 = ar1.split('-')
  ar2_1, ar2_2 = ar2.split('-')
  ar1_start = int(ar1_1)
  ar1_end = int(ar1_2)
  ar2_start = int(ar2_1)
  ar2_end = int(ar2_2)
  return ar1_start, ar1_end, ar2_start, ar2_end


def overlap_checking(assignment_range1, assignment_range2):
  if not assignment_range1:
    return True
  if not assignment_range2:
    return False
  if len(assignment_range1) > 1 and assignment_range1.step % assignment_range2.step:
    return False
  return assignment_range1.start in assignment_range2 and assignment_range1[-1] in assignment_range2


if __name__ == '__main__':
  main()