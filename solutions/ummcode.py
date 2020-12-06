speech = list(input())

valids = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
           'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F',
           'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
           'W','X','Y','Z','1','2','3','4','5','6','7','8','9','0', ' '}

speech_filtered = [x for x in speech if x in valids]

rebuilt = ''.join(speech_filtered)

speech_filtered = [x for x in rebuilt.split(' ') if set(x).issubset({'u','m'})]

message = []
current = 0
# u = 1
# 0 = m
counter = 0
for um in speech_filtered:
    for c in um:
        if c == 'u':
            current |= 1
        if counter == 6:
            message.append(chr(current))
            current = 0
            counter = 0
        else:
            current <<= 1
            counter += 1
print(''.join(message))