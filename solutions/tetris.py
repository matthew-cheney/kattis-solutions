line = input().split(' ')
C = int(line[0])
P = int(line[1])
line = input().split(' ')
cols = [int(x) for x in line[:C]]

pieces = [[[0],
           [0,0,0,0],
           ],
          [[0,0],
           ],
          [[0,0,1],
           [0,-1],
           ],
          [[0,-1,-1],
           [0,1],
           ],
          [[0,0,0],
           [0,1],
           [0,-1,0],
           [0,-1]],
          [[0,0,0],
           [0,0],
           [0,1,1],
           [0,-2]],
          [[0,0,0],
           [0,2],
           [0,0,-1],
           [0,0]]
          ]

total_positions = 0

piece = pieces[P-1]
for position in piece:
    if len(cols) < len(position):
        continue
    for i in range(len(cols) + 1):
        # Not enough room on right
        if i + len(position) > len(cols):
            break
        zero = cols[i]
        trues = [cols[i+j] == zero + position[j] for j in range(len(position))]
        if trues == [True for j in range(len(trues))]:
            total_positions += 1
print(total_positions)

