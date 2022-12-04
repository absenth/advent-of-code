from string import ascii_lowercase, ascii_uppercase

def main():
  manifest_counter = 1
  matches, match_output = "",""

  with open('input3.txt') as elf_manifests:
    for manifest in elf_manifests:
      if manifest_counter == 1:
        rucksack1 = manifest
        manifest_counter += 1
      elif manifest_counter == 2:
        rucksack2 = manifest
        manifest_counter += 1
      else:
        rucksack3 = manifest
        manifest_counter = 1
        matches = compare(rucksack1, rucksack2, rucksack3)
        match_output += f'{matches}'
  priority_sum = calculate_priority(match_output)
  print(priority_sum)


def compare(rucksack1, rucksack2, rucksack3):
  matches = ''
  for i in range(len(rucksack1)):
    if rucksack1[i] in rucksack2:
      if rucksack1[i] in rucksack3:
        return f'{rucksack1[i]}'


def calculate_priority(match_output):
  return sum(priorities[letter] for letter in match_output)

priorities = { letter: value for value, letter in enumerate((ascii_lowercase + ascii_uppercase), 1) }


if __name__ == '__main__':
  main()