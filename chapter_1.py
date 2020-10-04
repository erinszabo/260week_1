import random

"""
   Chapter 1.10
"""
print()
print()

print("self_check_1:")

# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
wordlist = ['cat', 'dog', 'rabbit']
letterlist = []
for aword in wordlist:
    for aletter in aword:
        if aletter not in letterlist:
            letterlist.append(aletter)
print(letterlist)

print()
print("self_check_2:")

# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']
awordlist = ['cat', 'dog', 'rabbit']
aletterlist = [letter for word in awordlist for letter in word]
print(aletterlist)

print("extra challege:")
aletter_set = set(aletterlist)
new_letterlist = [letter for letter in aletter_set]
print(new_letterlist)

print()
print("self_check_3:")

quote = "methinks it is like a weasel"  # goal string
qlen = 28  # length of quote


def monkey(qlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(qlen):
        res = res + alphabet[random.randrange(27)]
    return res


print(monkey(qlen))

print("self_check_3 Challenge:")


def luck(quote, guess):
    num_same = 0
    for i in range(qlen):
        if quote == guess[i]:
            num_same += 1
    return num_same / qlen


def lucky_monkey():
    new_guess = monkey(qlen)
    best = 0
    count = 0
    mluck = luck(quote, new_guess)
    while mluck < 1 or count < 10:
        if mluck > best:
            print(mluck, new_guess)
            best = mluck
        count += 1
        new_guess = monkey(qlen)
        mluck = luck(quote, new_guess)
    print(new_guess)


# lucky_monkey()


print("not working but I realized I didn't need to do this one anyway...")