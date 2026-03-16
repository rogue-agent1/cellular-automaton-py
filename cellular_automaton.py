#!/usr/bin/env python3
"""Cellular automata — Rule 110 and Conway's Game of Life."""
def rule110(width=50,steps=20):
    state=[0]*width;state[width-1]=1;results=[list(state)]
    for _ in range(steps):
        new=[0]*width
        for i in range(width):
            l=state[i-1] if i>0 else 0;c=state[i];r=state[i+1] if i<width-1 else 0
            pattern=(l<<2)|(c<<1)|r
            new[i]=(110>>pattern)&1
        state=new;results.append(list(state))
    return results
def game_of_life(grid,steps=1):
    rows,cols=len(grid),len(grid[0])
    for _ in range(steps):
        new=[[0]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                n=sum(grid[(r+dr)%rows][(c+dc)%cols] for dr in[-1,0,1] for dc in[-1,0,1] if(dr,dc)!=(0,0))
                if grid[r][c]:new[r][c]=1 if n in(2,3) else 0
                else:new[r][c]=1 if n==3 else 0
        grid=new
    return grid
def main():
    r=rule110(20,5)
    for row in r:print("".join("█" if c else " " for c in row))
if __name__=="__main__":main()
