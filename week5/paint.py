def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def explore_patch(x, y, grid, visited, rows, cols):
    if not is_valid(x, y, rows, cols) or grid[x][y] == '.' or visited[x][y]:
        return
    
    visited[x][y] = True
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    for dx, dy in directions:
        explore_patch(x + dx, y + dy, grid, visited, rows, cols)

def count_patches(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    patch_count = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '%' and not visited[i][j]:
                explore_patch(i, j, grid, visited, rows, cols)
                patch_count += 1
                
    return patch_count

def main():
    filename = 'patches.txt'
    
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    
    grid = [list(line) for line in lines]
    patch_count = count_patches(grid)
    
    if patch_count == 1:
        print("1 patch")
    else:
        print(f"{patch_count} patches")

if __name__ == "__main__":
    main()
