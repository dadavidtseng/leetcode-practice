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
        full_e = energy

        while q:
            r, c, mask, e, moves = q.popleft()

            if mask == full_mask:
                return moves

            if e == 0:
                continue

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                if new_r < 0 or new_c < 0 or new_r >= m or new_c >= n:
                    continue

                grid = classroom[new_r][new_c]

                if grid == "X":
                    continue

                new_e = e - 1
                new_mask = mask

                if grid == "L":
                    new_mask |= 1 << L_idx[(new_r, new_c)]

                if grid == "R":
                    new_e = energy

                if best_e[new_r][new_c][new_mask] >= new_e:
                    continue

                best_e[new_r][new_c][new_mask] = new_e
                q.append((new_r, new_c, new_mask, new_e, moves + 1))
        return -1
