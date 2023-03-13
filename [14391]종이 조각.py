rows, cols = map(int, input().split())
k = [list(map(int, input().rstrip())) for _ in range(rows)]
dx, dy = [1, 0], [0, 1]
dp = [-1] * (1 << 16)


def split(visited=0, cs=0):
    if dp[visited] >= cs:
        return
    dp[visited] = cs
    for i in range(rows):
        for j in range(cols):
            if visited & (1 << (i * cols + j)) == 0:
                split(visited | (1 << (i * cols + j)), cs + k[i][j])
                for l in range(2):
                    nv = visited | (1 << (i * cols + j))
                    ns = k[i][j]
                    cx, cy = i, j
                    while True:
                        cx, cy = cx + dx[l], cy + dy[l]
                        if 0 <= cx < rows and 0 <= cy < cols:
                            if visited & (1 << (cx * cols + cy)) == 0:
                                nv = nv | (1 << (cx * cols + cy))
                                ns = ns * 10 + k[cx][cy]
                                split(nv, cs + ns)
                            else:
                                break
                        else:
                            break
                return


split()
print(dp[(1 << rows * cols) - 1])
