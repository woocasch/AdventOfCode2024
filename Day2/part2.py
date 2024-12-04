def verify_levels(levels):
    is_increasing = False
    is_safe = True
    for index, level in enumerate(levels):
        if (index == 0):
            is_increasing = levels[0] < levels[1]
            continue

        # check if increasing
        currentIncreasing = levels[index] > levels[index - 1]
        if (currentIncreasing != is_increasing):
            return { "is_safe": False, "blocking_level_index": index, "reason": "direction change" }

        # check if distance correct
        distance = abs(levels[index] - levels[index - 1])
        if (distance == 0 or distance > 3):
            return { "is_safe": False, "blocking_level_index": index, "reason": "distance to large" }
    
    return { "is_safe": True, "blocking_level_index": -1, "reason": "" }
      
with open("input.txt", "r") as file:
    reports = file.readlines()

saveReportsCount = 0
for report in reports:
    levels = [int(level) for level in report.split(' ') if level]
    result = verify_levels(levels)
    if (not result["is_safe"]):
        for index, level in enumerate(levels):
            reduced_levels = [item for i, item in enumerate(levels) if i != index]
            reduced_result = verify_levels(reduced_levels)
            if (reduced_result["is_safe"]):
                result = reduced_result
                break
        
    saveReportsCount += 1 if result["is_safe"] else 0

print(saveReportsCount)

