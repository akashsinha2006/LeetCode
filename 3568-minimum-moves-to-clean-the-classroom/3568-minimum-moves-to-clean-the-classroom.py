from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        n, m = len(classroom), len(classroom[0])
        sr = sc = -1
        trash = []

        for i in range(n):
            for j in range(m):
                if classroom[i][j] == 'S': sr, sc = i, j
                elif classroom[i][j] == 'L': trash.append((i, j))

        k = len(trash)
        if k == 0: return 0

        id_ = [[-1] * m for _ in range(n)]
        for i, (r, c) in enumerate(trash): id_[r][c] = i

        full_mask = (1 << k) - 1
        dist = [[[[ -1] * (1 << k) for _ in range(energy + 1)]
                  for _ in range(m)] for _ in range(n)]

        dist[sr][sc][energy][0] = 0
        q = deque([(sr, sc, energy, 0)])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            r, c, e, mask = q.popleft()
            moves = dist[r][c][e][mask]

            if mask == full_mask: return moves

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < m): continue
                ch = classroom[nr][nc]
                if ch == 'X' or e == 0: continue

                ne, nmask = e - 1, mask
                if ch == 'L': nmask |= (1 << id_[nr][nc])
                if ch == 'R': ne = energy

                if dist[nr][nc][ne][nmask] == -1:
                    dist[nr][nc][ne][nmask] = moves + 1
                    q.append((nr, nc, ne, nmask))

        return -1