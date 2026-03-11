import random
import math 
from graphics import * 

# a graph with N nodes, with edges between nodes a distance D apart
# 0 ≤ x ≤ A and 0 ≤ y ≤ B
def randGeoGraph(A, B, N, D): 

    coords = [] # list of tuples (x,y)
    adj = {} # adjacency list 
    
    for p in range(N): 
        adj.update({p:[]}) # node index : [(neighbor index, weight)]
    j = 1

    # creating coordinates 
    for _ in range(N): 
        x = random.randint(0, A - 1)
        y = random.randint(0, B - 1)
        coords.append((x, y))
    
    # calculating distances 
    for k in range(N): 
        for j in range(k+1, N): 
            distance = round(math.sqrt((coords[k][0] - coords[j][0])**2 + (coords[k][1] - coords[j][1])**2), 3)
            if distance <= D: 
                adj[k].append((j, distance)) # (neighbor index, edge weight)
                adj[j].append((k, distance))
    
    # printing results 
    print(f"List of Coordinates: {coords}")
    print(f"Adjacency List: {adj}")

    # return results
    return coords, adj

def drawGraph(V, E): 
    # graphics 
    win = GraphWin("Window", 500, 500)
    window_size = 500
    scaled_coords = _scale_coordinates(V, window_size) # calculate scale factor

    # drawing edges 
    for node in E:
        for neighbor, weight in E[node]:
            # Draw each edge only once (node < neighbor)
            if node < neighbor:
                x1, y1 = scaled_coords[node]
                x2, y2 = scaled_coords[neighbor]
                
                line = Line(Point(x1, y1), Point(x2, y2))
                line.setOutline("gray")
                line.setWidth(1)
                line.draw(win)

    # drawing points
    for point in scaled_coords: # point is a tuple in V

        # draw the point 
        dot = Circle(Point(point[0], point[1]), 5)
        dot.setFill("light green")
        dot.draw(win)

        # label the point with its coordinates 
        str = f"({point[0]},{point[1]})"
        label = Text(Point(point[0], point[1] - 15), str)
        label.draw(win)
        
    win.getMouse()
    win.close() 

def _scale_coordinates(coords, window_size): 
    # global variables 
    margin = 5

    # finding maximum/minimum x and y coordinate 
    all_x = [x for x, y in coords]
    all_y = [y for x, y in coords]
    
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)

    range_x = max_x - min_x if max_x > min_x else 1
    range_y = max_y - min_y if max_y > min_y else 1
    
    # Available drawing area inside margins
    draw_area = window_size - 2 * margin
    
    scaled_coords = []
    for x, y in coords:
        # Scale coordinates to fit in draw_area, then add margin
        scaled_x = margin + ((x - min_x) / range_x) * draw_area
        scaled_y = margin + ((y - min_y) / range_y) * draw_area
        
        # Invert y-axis 
        scaled_y = window_size - scaled_y
        
        scaled_coords.append((round(scaled_x, 0), round(scaled_y, 0)))
    
    return scaled_coords

# Driver code 
if __name__ == "__main__":
    # Generate graph with 0≤x≤50 and 0≤y≤50, N = 50 nodes and D = 13 max edge distance
    A = B = 50
    N = 50
    D = 13
    
    print(f"Generating very cool and awesome geometric graph!")
    print(f"  A = {A}, B = {B}, N = {N}, D = {D}")
    print("-" * 50)
    
    coords, adj = randGeoGraph(A, B, N, D)
    drawGraph(coords, adj)

    
