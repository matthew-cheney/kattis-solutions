import re
line = input()
if len(re.findall('ss', line)) > 0:
    print("hiss")
else:
    print("no hiss")