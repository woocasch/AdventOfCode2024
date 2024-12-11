import re

with open("input.txt", "r") as file:
    memory_entries = file.readlines()

pattern = re.compile("^mul\((\d+)\,(\d+)\)$")

def calculate_entry(entry):
    current_substring = entry
    total = 0
    while current_substring.find('mul') >= 0:
        mul_index = current_substring.find('mul')
        mul_subpart = current_substring[ mul_index : len(current_substring) ]
        next_closing_parantheses_index = mul_subpart.find(')')
        mul_subpart_to_closing = mul_subpart[ 0 : next_closing_parantheses_index + 1 ]
        if (mul_subpart_to_closing[ 2 : len(mul_subpart_to_closing) ].find('mul') >= 0):
            current_substring = current_substring[mul_index + 2 : len(current_substring) ]
            continue

        result = pattern.match(mul_subpart_to_closing)
        if not bool(result):
            current_substring = current_substring[mul_index + 2 : len(current_substring) ]
            continue

        left_hand_side = int(result.group(1))
        right_hand_side = int(result.group(2))
        multiplication_result = left_hand_side * right_hand_side
        total += multiplication_result
        current_substring = current_substring[mul_index + 2 : len(current_substring) ]

    return total

total = 0

for memory_entry in memory_entries:
    total += calculate_entry(memory_entry)

print(total)
