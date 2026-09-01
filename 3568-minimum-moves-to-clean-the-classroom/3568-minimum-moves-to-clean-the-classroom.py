class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        L_idx = {}
        L_count = 0

        # Iterate every grid in classroom to find row and column
        for row in range(m):
            for col in range(n):
                if classroom[row][col] == "S":
                    sx, sy = (row, col)
                elif classroom[row][col] == "L":
                    L_idx[(row, col)] = L_count

                    L_count += 1

        best_e = [[[-1] * (1 << L_count) for _ in range(n)] for _ in range(m)]
        best_e[sx][sy][0] = energy
        q = deque([(sx, sy, 0, energy, 0)])
        full_mask = (1 << L_count) - 1
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
                    new_mask |= (1 << L_idx[(new_r, new_c)])

                if classroom[new_r][new_c] == "R":
                    new_e = full_energy

                if best_e[new_r][new_c][new_mask] >= new_e:
                    continue

                best_e[new_r][new_c][new_mask] = new_e

                q.append((new_r, new_c, new_mask, new_e, steps + 1))
        return -1
