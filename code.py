# Rubric 1
# Prints set of lengths of bracelets, and total number of bracelets

lengths = set()
for i in range (1, 10):
    for j in range (1, 10):
        list = [i, j]
        num1 = i
        num2 = j
        while True:
            newInt = (num1 + num2)
            newInt = newInt % 10
            list.append(newInt)
            num1 = num2
            num2 = newInt
            if num2 == j and num1 == i:
                lengths.add(len(list)-2)
                break
            
# Add 0, 0 bracelet
lengths.add(1)


print("\nThe set of bracelets have lengths: ")
print(lengths)
print("\nTherefore there are " + str(len(lengths)) + " bracelets")

