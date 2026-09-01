class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        L = []

        # Iterate every grid in classroom to find row and column
        for row in range(m):
            for col in range(n):
                if classroom[row][col] == "S":
                    S = (row, col)
                if classroom[row][col] == "L":
                    L.append((row, col))

        q = deque([(S[0], S[1], 0, energy, 0)])
        
        best_e = {(S[0], S[1], 0):energy}
        full_mask = (1 << len(L)) - 1
        full_energy = energy

        while q:
            R, C, mask, e, steps = q.popleft()

            if mask == full_mask:
                return steps

            if e == 0:
                continue

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for r, c in directions:
                new_r = R + r
                new_c = C + c

                if new_r < 0 or new_c < 0 or new_r >= m or new_c >= n:
                    continue

                if classroom[new_r][new_c] == "X":
                    continue

                new_e = e - 1
                new_mask = mask

                if classroom[new_r][new_c] == "L":
                    idx = L.index((new_r, new_c))
                    new_mask = mask | (1 << idx)

                if classroom[new_r][new_c] == "R":
                    new_e = full_energy

                state = (new_r, new_c, new_mask)

                if best_e.get(state, -1) >= new_e:
                    continue

                best_e[state] = new_e
                
                q.append((new_r, new_c, new_mask, new_e, steps + 1))
        return -1
