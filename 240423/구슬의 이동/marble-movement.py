n, m, t, k = tuple(map(int, input().split()))
mapper = {
    'U' : 0,
    'R' : 1,
    'L' : 2,
    'D' : 3
}

beads = []
new_beads= []
for i in range(1, m+1):
    (r, c, d, v) = tuple(input().split())
    dic = mapper[d]
    r, c, v = int(r)-1, int(c)-1, int(v)
    beads.append((i, r, c, dic, v))

count = [[0]*n for _ in range(n)]

def In_Range(x,y) :
    return x >= 0 and x < n and y >= 0 and y < n

# 이동 하는건 문제 없음.
def Move(bead) :
    (orr, r,c,d,v) = bead
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    dx, dy = dxs[d], dys[d]

    nx, ny = r + dx*v, c + dy*v
    if not In_Range(nx,ny) :
        if d == 0 :
            nx = abs(nx)
        elif d == 3:
            nx = 2*n - nx - 2
        elif d == 2 :
            ny = abs(ny)
        else :
            ny = 2*n - ny - 2
        
        d = 3 - d
    #print(f"({r},{c}) => ({nx},{ny})")
    return (orr, nx, ny, d, v)


def Move_all():
    global beads
    new_beads = []
    for bead in beads :
        bead = Move(bead)
        new_beads.append(bead)
        (_ , x, y, _, _) = bead
        count[x][y] += 1

    beads = new_beads[:]


def Check_Conflict():
    global beads
    new_beads = []

    for bead in beads :
        (orr, x, y, d, v) = bead 
        if count[x][y] <= k :
            new_beads.append(bead)
            continue

        count[x][y] -= 1
        new_beads.append((orr, x, y, d, -1))
            
    beads = [
        (orr, x, y, d, v) for (orr, x, y, d, v) in new_beads if v != -1
    ]


def simulation():
    for _ in range(t):
        Move_all()
        Check_Conflict()


simulation()
print(len(beads))