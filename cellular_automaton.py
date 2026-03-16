def game_of_life(grid,steps=1):
    rows,cols=len(grid),len(grid[0])
    for _ in range(steps):
        new=[[0]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                neighbors=sum(grid[(r+dr)%rows][(c+dc)%cols] for dr in [-1,0,1] for dc in [-1,0,1] if dr or dc)
                if grid[r][c]: new[r][c]=1 if neighbors in (2,3) else 0
                else: new[r][c]=1 if neighbors==3 else 0
        grid=new
    return grid
def rule110(state,steps=1):
    rule={(1,1,1):0,(1,1,0):1,(1,0,1):1,(1,0,0):0,(0,1,1):1,(0,1,0):1,(0,0,1):1,(0,0,0):0}
    for _ in range(steps):
        new=[0]*len(state)
        for i in range(len(state)):
            l=state[(i-1)%len(state)]; c=state[i]; r=state[(i+1)%len(state)]
            new[i]=rule[(l,c,r)]
        state=new
    return state
if __name__=="__main__":
    # Blinker oscillator
    grid=[[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
    g2=game_of_life(grid,1)
    assert g2[2][1]==1 and g2[2][3]==1  # horizontal blinker
    g3=game_of_life(g2,1)
    assert g3[1][2]==1 and g3[3][2]==1  # back to vertical
    state=[0]*20; state[10]=1
    r=rule110(state,5)
    assert sum(r)>1  # pattern grows
    print(f"GoL blinker works, Rule 110: {sum(r)} cells alive")
    print("All tests passed!")
