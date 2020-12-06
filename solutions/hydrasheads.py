while True:
    H, T = [int(x) for x in input().split(' ')]
    if H == 0 and T == 0:
        break

    """
    Moves:
    H - 1
    T - 1
    H - 2
    T - 2
    
    Trades:
    1H -> 1H (useless)
    1T -> 2T
    2T -> 1H
    2H -> -
    """

    if T == 0:
        if H % 2 == 0:
            print(H // 2)
        else:
            print(-1)
        continue

    moves = 0

    # cut off tails first
    if T % 2 == 0:
        moves += (T // 2) - 1
        H += (T // 2) - 1
        T -= ((T // 2) - 1) * 2
    else:
        moves += T // 2
        H += T // 2
        T -= (T // 2) * 2

    # we either have 1 or 2 tails now
    # H is either odd or even

    # T is 2, H is odd
    if T == 2 and H % 2 == 1:
        # cut two tails
        moves += 1
        H += 1
    # T is 2, H is even
    elif T == 2 and H % 2 == 0:
        # cut one tail, then one tail, then two, then two
        moves += 4
        H += 2
    # T is 1, H is odd
    elif T == 1 and H % 2 == 1:
        # cut one tail, then two
        moves += 2
        H += 1
    # T is 1, H is even
    else:
        # cut one tail, then one, then one, then two, then two
        moves += 5
        H += 2

    # T = 0, H is even
    moves += H // 2
    print(moves)
