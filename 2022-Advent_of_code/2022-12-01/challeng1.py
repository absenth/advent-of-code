from heapq import nlargest

def main():
  elf_index = 0
  elf_calorie = 0
  elf_dict = array_setup(elf_index, elf_calorie)
  three_total = find_highest(elf_dict)
  print(three_total)



def array_setup(elf_index, elf_calorie):
  elf_dict = {}
  with open('input1.txt') as elf_input:
    for line in elf_input:
      if line != '\n':
        elf_calorie += int(line)
      else:
        elf_dict[elf_index] = elf_calorie
        elf_calorie = 0
        elf_index += 1
    elf_dict[elf_index] = elf_calorie
    return elf_dict

def find_highest(elf_dict):
  max_calories = max(elf_dict.values())
  max_elf = max(elf_dict, key=elf_dict.get)
  three_highest = nlargest(3, elf_dict, key = elf_dict.get)
  three_total = 0
  for elf in three_highest:
    three_total += elf_dict.get(elf)

  return three_total






if __name__ == "__main__":
  main()