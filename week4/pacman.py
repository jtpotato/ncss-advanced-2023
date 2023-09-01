# read maze file
with open("maze.txt") as f:
    maze = f.readlines()
    # hashtags are walls.
    # get coordinates of each `G`
    ghosts = []
    for i, line in enumerate(maze):
        for j, char in enumerate(line):
            if char == "G":
                ghosts.append((i, j))

    # get coordinates of `P`
    pacman = None
    for i, line in enumerate(maze):
        for j, char in enumerate(line):
            if char == "P":
                pacman = (i, j)

    new_ghost_positions = []

    # perform BFS from each ghost to pacman, printing the shortest path.
    # avoid walls as denoted by hashtags.
    for ghost in ghosts:
        # BFS
        # queue of paths
        queue = [[ghost]]
        # set of visited nodes
        visited = set()

        path_found = False

        while queue and not path_found:
            # get the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            if node not in visited:
                # enumerate all adjacent nodes, construct a new path and push it into the queue
                for adjacent in [
                    (node[0] - 1, node[1]),
                    (node[0] + 1, node[1]),
                    (node[0], node[1] - 1),
                    (node[0], node[1] + 1),
                ]:
                    # avoid walls
                    if maze[adjacent[0]][adjacent[1]] != "#":
                        new_path = list(path)
                        new_path.append(adjacent)
                        queue.append(new_path)
                        # return path if pacman is found
                        if adjacent == pacman:
                            new_ghost_positions.append(new_path[1])
                            path_found = True
                            break
                # mark node as visited
                visited.add(node)

    # reconstruct maze with new ghost positions
    new_maze = []
    for i, line in enumerate(maze):
        new_line = ""
        for j, char in enumerate(line):
            if (i, j) in new_ghost_positions:
                new_line += "G"
            else:
                if char == "G":
                    new_line += " "
                elif char == "\n":
                    continue
                else:
                    new_line += char
        new_maze.append(new_line)

    # print new maze
    for line in new_maze:
        print(line)
