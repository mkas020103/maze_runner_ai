# Define the 2D list of tuples
coordinates = [
    [(0, 1), (7, 2), (2, 30), (0, 4), (0, 5)],
    [(6, 6), (7, 7), (7, 8), (7, 9), (0, 10)],
    [(5, 11), (7, 12), (0, 13), (7, 14), (0, 0)],
    [(4, 16), (2, 17), (7, 18), (7, 19), (2, 20)],
    [(4, 0), (8, 22), (7, 23), (0, 24), (1, 25)],
    [(7, 0), (0, 27), (1, 30), (7, 29), (0, 30)],
]

# Function to find and print tuples at the edges
def find_edge_tuples(matrix):
    # Initialize variables to store edge coordinates
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')

    edge_tuples = []

    # Find the min and max x and y values
    for row in matrix:
        for x, y in row:
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

    # Collect the tuples that are at the edges
    for row in matrix:
        for tuple in row:
            if tuple[0] == min_x or tuple[0] == max_x or tuple[1] == min_y or tuple[1] == max_y:
                edge_tuples.append(tuple)
                print(f'found tuple {tuple} at the edge')

    return edge_tuples

# Call the function
edge_tuples = find_edge_tuples(coordinates)
print("Edge tuples:", edge_tuples)