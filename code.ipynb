# Rubrik 1


# Attempt 1
# Just calculates a bracelet given inputs without checking for repetition etc
'''
num1 = int(input("Number 1: "))
num1 = num1 % 10
num2 = int(input("Number 2: "))
num2 = num2 % 10

list = [num1, num2]
for i in range (50):
    newInt = (num1 + num2)
    newInt = newInt % 10
    list.append(newInt)
    num1 = num2
    num2 = newInt

print(list)   

'''



# Attempt 2
# Will try to generate all possible bracelets for up to 50 numbers
# Hopefully will then be able to see a pattern
# Bit stuck here, not sure how to use Python to see which bracelets are actually the same
'''
mega = []
for i in range (10):
    for j in range (10):
        list = [i, j]
        num1 = i
        num2 = j
        for k in range (50):
            newInt = (num1 + num2)
            newInt = newInt % 10
            list.append(newInt)
            num1 = num2
            num2 = newInt
        mega.append(list)

print(mega)
'''
# Ok, prints out all bracelets formed from 2 numbers
# I realised that when there's a 0 in a bracelet, the number before decides the rest of the bracelet
# So instead of comparing every single part against every other, I only need to look at 0s




# Attempt 3

# Will attempt a program which allows me to save all 0s and then compare
'''
nopes = 0
mega = []
for i in range (1, 10):
    for j in range (1, 10):
        list = [i, j]
        num1 = i
        num2 = j
        counter = 0
        while True:
            newInt = (num1 + num2)
            newInt = newInt % 10
            list.append(newInt)
            num1 = num2
            num2 = newInt
            counter += 1
            if newInt == 0:
                mega.append([i, j, num1, num2])
                break
            elif counter == 500:
                mega.append([list[0], list[1], "Nope"])
                nopes += 1
                break

for i in range (len(mega)):
    print(mega[i][0], mega[i][1], mega[i][2])

print("\nNopes: ")
print(nopes)
'''
# This told me that there were number bracelets with a section of the form n, 0, n
# for all numbers 0-9. There is also one bracelet which includes no zeros. Around
# here I realised that the name bracelet implies a loop, changing the question rather.
# For the next attempt I will need to heavily reformulate the code, as currently I do not
# believe that it is answering the intended question. This was frustrating to find out
# but hopefully my next attempt will solve the question.



# Attempt 4 - Playing with the problem a bit to get unstuck :)

nopes = 0
mega = []
lengths = set()
for i in range (1, 10):
    for j in range (1, 10):
        list = [i, j]
        num1 = i
        num2 = j
        counter = 0
        while True:
            newInt = (num1 + num2)
            newInt = newInt % 10
            list.append(newInt)
            num1 = num2
            num2 = newInt
            counter += 1
            if num2 == j and num1 == i:
                mega.append(list)
                lengths.add(len(list)-2)
                print(list)
                break
# Add 0, 0 bracelet
lengths.add(1)


print(lengths)
# This prints the lengths of all bracelets apart from 0, 0. I did forget this and was confused for a while
# as to why my totals did not add to 100. Incorporating an extra line into the code fixes this,
# and my answer can easily be checked as the lengths of the bracelets now add to 100. This is a neat
# conclusion to the proof, and I checked some of the number bracelets by hand to rule out logic
# errors in the code



# Side note: Upon further discussion with friends, we came up with another method of using Python
# to solve this. I have coded this beneath, but admit that I would be unlikely to write this
# solution from scratch. However I like the simplicity and elegance of the logic...
'''
pairs = []

for i in range(0,10):
    for j in range(0,10):
        pairs.append((i,j))

pairs = set(pairs)
check = set(pairs)

while len(check) != 0:
    currentLoop = check.pop()
    print(currentLoop)
    a = currentLoop[1]
    b = (currentLoop[0] + currentLoop[1]) % 10

    while ((a,b) != currentLoop):
        check.remove((a,b))
        c = (a+b) % 10
        a = b
        b = c '''
