
# Creating patterns
sequenceIter = 1

for i in range(5):
    pattern = ''
    for j in range(sequenceIter):
        pattern += ' * '
    print(pattern)
    sequenceIter = sequenceIter + 1

# Iteration on list

grades = [100, 100, 100, 90, 94, 98]

for index in range(0, len(grades)):
    print(grades[index])
