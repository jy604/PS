def solution(wallpaper):
    dx, dy = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                dx.append(i)
                dy.append(j)
    return [min(dx),min(dy), max(dx) + 1, max(dy) + 1]