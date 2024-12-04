with open("input.txt", "r") as file:
    reports = file.readlines()

saveReportsCount = 0
for report in reports:
    levels = [int(level) for level in report.split(' ') if level]
    is_increasing = False
    is_safe = True
    for index, level in enumerate(levels):
        if (index == 0):
            is_increasing = levels[0] < levels[1]
            continue
        
        # check if increasing
        currentIncreasing = levels[index] > levels[index - 1]
        if (currentIncreasing != is_increasing):
            is_safe = False
            break
            
        # check if distance correct
        distance = abs(levels[index] - levels[index - 1])
        if (distance == 0 or distance > 3):
            is_safe = False
            break
    
    saveReportsCount += 1 if is_safe else 0

print(saveReportsCount)
