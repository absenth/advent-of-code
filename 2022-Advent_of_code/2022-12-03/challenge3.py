from string import ascii_lowercase, ascii_uppercase

def main():
  priority_sum = 0
  match_output = ""

  with open('input3.txt') as elf_manifests:
    for manifest in elf_manifests:
      compartment1 = manifest[0:len(manifest)//2]
      compartment2 = manifest[len(manifest)//2:]
      matches = compare(compartment1, compartment2)
      match_output += f'{matches}'
  priority_sum = calculate_priority(match_output)
  print(priority_sum)

def compare(compartment1, compartment2):
  matches = ''
  for i in range(len(compartment1)):
    if compartment1[i] in compartment2:
      return f'{compartment1[i]}'

def calculate_priority(match_output):
  print(match_output)
  return sum(priorities[letter] for letter in match_output)


priorities = { letter: value for value, letter in enumerate((ascii_lowercase + ascii_uppercase), 1) }


if __name__ == '__main__':
  main()