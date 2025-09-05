from collections import deque
def MazeNavi():
    with open("maze-navigator.txt", "r", encoding="utf-8-sig") as filemaze: #the encoding=utf-8-sig is from chatgpt
        start = "S" #my variables
        end = "E"
        wall = "#"
        path = "."
        loop1 = 0
        loop2 = 0
        start_pos = ()
        amaze_map = []


        maze_map = [line.rstrip("\n") for line in filemaze] #converts the maze into a list of strings


        a_maze_map = [list(line) for line in maze_map]#puts into a 2d list
        #print(a_maze_map) prints the 2d list so that I can see if somehtings wrong for debugging


        for pos1 in range(len(a_maze_map)): #loop to find the start and end positions
            for pos2 in range(len(a_maze_map[pos1])):
                if a_maze_map[pos1][pos2] == start:
                    start_pos = (pos1, pos2)
                elif a_maze_map[pos1][pos2] == end:
                    end_pos = (pos1, pos2)


        # initial loop that i had
        # while loop1 < len(a_maze_map):
        #     if start == a_maze_map[loop1][loop2]:
        #         start_pos = (loop1, loop2)
        #     elif end == a_maze_map[loop1][loop2]:
        #         end_pos = (loop1, loop2)
        #     else:
        #         loop2 = loop2 + 1
        #     if loop2 == len(a_maze_map[loop1]):
        #         loop1 = loop1 + 1
        #         loop2 = 0


        #attempting to start the maze finding 
        visited = set() #set to keep track of visited positions
        notin = 0
        mazeloop = 0
        path = {start_pos: None} #keep track of the path taken
        

        queue = deque([start_pos]) 
        while queue:
            node = queue.popleft() #dequeue a node from the front of the queue (what ever that means, learning froma. webstie)
            alr_visited = False
            
            for slot in visited: # my attempt at what was show but trying in my own way of checking if the node is in the visited 
                if slot == node:
                    alr_visited = True
                    break
            if not alr_visited:
                visited.add(node)

            if node == end_pos: #if the node is the end position then it will print the path
                short_path = []
                temp_end_pos = end_pos
                while temp_end_pos is not None:
                    short_path.append(temp_end_pos)
                    temp_end_pos = path[temp_end_pos]
                print("End found", end_pos)
                print("Shortest path:", len(short_path)-1)
                print("Path:", short_path[::-1]) #the [::-1] i got from chatgpt because it was backwards and i didnt know why
                break



            row, col = node
            for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #Checks up right and down (Needed chatgpt to help with makeing this as website was doing fro somehitng slightly different)
                new_row, new_col = row + row_offset, col + col_offset #chatgpt helped with this whole part too
                if 0 <= new_row < len(a_maze_map) and 0 <= new_col < len(a_maze_map[0]): #checks if the new position is within bounds
                    if a_maze_map[new_row][new_col] != wall: #checks if the new position is not a wall
                        if (new_row, new_col) not in visited:#ensures that the position hasnt been visited
                            queue.append((new_row, new_col))
                            if (new_row, new_col) not in path:
                                path[(new_row, new_col)] = (row, col)

        print("Start:", start_pos)
        print("End:", end_pos)

MazeNavi()
