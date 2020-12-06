class Node:
    def __init__(self, val, parent):
        self.val = val
        self.leaf = False
        self.children = dict()
        self.parent = parent

def main():
    W = int(input())

    trie = Node(None, None)
    for w in range(W):
        word = input()
        cur = trie
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node(c, cur)
            cur = cur.children[c]
        cur.leaf = True

    input()  # blank line

    B = int(input())

    adj_list = {(i, j): None for i in range(4) for j in range(4)}

    for i, j in adj_list.keys():
        cands = {(i-1, j),
                 (i+1, j),
                 (i, j-1),
                 (i, j+1),
                 (i-1, j-1),
                 (i-1, j+1),
                 (i+1, j-1),
                 (i+1, j+1)}
        adj_list[(i, j)] = [ea for ea in cands if ea[0] >= 0 and ea[0] < 4 and ea[1] >= 0 and ea[1] < 4]

    first = True

    for b in range(B):
        if first:
            first = False
        else:
            input()  # blank line
        # read in the board
        board = []
        for i in range(4):
            line = input()
            while line.strip() == '':
                line = input()
            board.append(list(line))

        words = set()

        def getWord(cur_node):
            word_so_far = ''
            while cur_node.parent is not None:
                word_so_far = cur_node.val + word_so_far
                cur_node = cur_node.parent
            return word_so_far

        visited = [[False for i in range(4)] for j in range(4)]

        # traverse board, looking for words
        def dfs(dfs_cur, parent_trie, depth):
            if depth > 8:
                return
            visited[dfs_cur[0]][dfs_cur[1]] = True
            if board[dfs_cur[0]][dfs_cur[1]] not in parent_trie.children:
                visited[dfs_cur[0]][dfs_cur[1]] = False
                return
            cur_trie = parent_trie.children[board[dfs_cur[0]][dfs_cur[1]]]
            if cur_trie.leaf:
                words.add(getWord(cur_trie))
            for child in adj_list[dfs_cur]:
                if not visited[child[0]][child[1]]:
                    dfs(child, cur_trie, depth + 1)
            visited[dfs_cur[0]][dfs_cur[1]] = False

        for start_node in adj_list.keys():
            dfs(start_node, trie, 1)

        # Calculate score
        scores = {1: 0,
                  2: 0,
                  3: 1,
                  4: 1,
                  5: 2,
                  6: 3,
                  7: 5,
                  8: 11}
        score = 0
        longest_word = ''
        for word in words:
            score += scores[len(word)]
            if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                longest_word = word

        print(score, longest_word, len(words))

main()