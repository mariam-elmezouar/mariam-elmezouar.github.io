def get_next_position(position):
    # Your code here
    # Input to this function is a tuple representing position (x,y)
    # Output/returned value is a tuple representing the next position
    pass






def treasure(treasure_map):

    # variable path where we will append the path to the treasure
    path = []
    # start position
    current_position = (1, 1)

    # A nested loop that goes over all element of the n by n matrix
    for i in range(len(treasure_map)):
        for j in range(len(treasure_map[0])):
            # Your code here
            pass


    return path

# Example usage
treasure_map = [[55, 55, 15, 53, 41],
                [51, 35, 23, 45, 41],
                [55, 44, 42, 41, 41],
                [23, 21, 15, 42, 51],
                [32, 44, 13, 34, 15]]

path = treasure(treasure_map)
print(path)  # Output: [55, 15, 41, 23]