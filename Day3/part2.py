import re

with open("input.txt", "r") as file:
    memory_entries = file.readlines()

multiplication_pattern = re.compile("^mul\((\d+)\,(\d+)\)$")

is_active = True

def calculate_entry(entry):
    global is_active
    changes = []
    current_substring = entry
    while current_substring.find('do') >= 0:
        do_index = current_substring.find('do')
        changes.append(int(do_index))
        current_substring = current_substring [ do_index + 2 : len(current_substring) ]

    for i, change in enumerate(changes):
        if i == 0:
            continue
        changes[i] = change + changes[i - 1] + 2

    current_substring = entry
    full_length = len(entry)
    total = 0
    while current_substring.find('mul') >= 0:
        mul_index = current_substring.find('mul')
        current_change = -1
        mul_index_adjusted = mul_index + (full_length - len(current_substring))
        for change in changes:
            if (change < mul_index_adjusted):
                current_change = change

        mul_subpart = current_substring[ mul_index : len(current_substring) ]
        next_closing_parantheses_index = mul_subpart.find(')')
        mul_subpart_to_closing = mul_subpart[ 0 : next_closing_parantheses_index + 1 ]
        if (mul_subpart_to_closing[ 2 : len(mul_subpart_to_closing) ].find('mul') >= 0):
            current_substring = current_substring[mul_index + 2 : len(current_substring) ]
            continue

        result = multiplication_pattern.match(mul_subpart_to_closing)
        if not bool(result):
            current_substring = current_substring[mul_index + 2 : len(current_substring) ]
            continue

        if current_change != -1 and entry[ current_change : len(entry)].startswith('don\'t'):
            is_active = False
        elif current_change != -1 and entry[ current_change : len(entry)].startswith('do'):
            is_active = True

        if is_active:
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
