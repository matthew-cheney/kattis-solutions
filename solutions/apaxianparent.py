Y, P = input().split(' ')

vowels = 'aeiou'

if Y[-1] in vowels:
    print(Y[:-1] + 'ex' + P)
elif Y[-2:] == 'ex':
    print(Y + P)
else:
    print(Y + 'ex' + P)