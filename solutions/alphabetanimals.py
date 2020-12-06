def solution():
    prev = input()
    N = int(input())
    target_letter = prev[-1]
    first_letters = {x: 0 for x in 'abcdefghijklmnopqrstuvwxyz'}
    valid_animals = list()
    choose_me = list()
    for n in range(N):
        new_animal = input()
        first_letters[new_animal[0]] += 1
        valid_animals.append(new_animal)
        if new_animal[0] == target_letter:
            choose_me.append(new_animal)

    if len(choose_me) == 0:
        print('?')
        return

    for animal in choose_me:
        if first_letters[animal[-1]] < 1 + (animal[0] == animal[-1]):
            print(f'{animal}!')
            return
    print(choose_me[0])

solution()