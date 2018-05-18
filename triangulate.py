import math, sys, string
from shapely.geometry.polygon import LinearRing, Polygon
from matplotlib import pyplot as plot

lines_list = []

# the function where diagonals are connected
def connectpoints(x,y):
    x1, x2 = x[0], y[0]
    y1, y2 = x[1], y[1]
    plot.plot([x1,x2],[y1,y2],color="grey")

class Point:
    def __init__(self,x,y):
        self.x, self.y = x,y

# finds the euclidean distance between two given points
def dist(p1,p2):
    return math.sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))

def lengthSquare(p1,p2):
    xDiff = p1[0]- p2[0]
    yDiff = p1[1]- p2[1]
    return xDiff*xDiff + yDiff*yDiff

def cost(points,i,k,j, option):
    result = 0

    # Minimum Weight Triangulation
    if option == 1:
        p1 = points[i]
        p2 = points[j]
        p3 = points[k]
        result = dist(p1, p2) + dist(p2, p3) + dist(p3, p1)

    # Minimised largest of Internal Angles
    elif option == 2:
        p1 = points[i]
        p2 = points[j]
        p3 = points[k]

        a2 = float(lengthSquare(p1,p2))
        b2 = float(lengthSquare(p1,p3))
        c2 = float(lengthSquare(p2,p3))

        # lenght of sides be a, b, c
        a = float(math.sqrt(a2))
        b = float(math.sqrt(b2))
        c = float(math.sqrt(c2))

        # From Cosine law
        try:
            alpha = float(math.acos((b2 + c2 - a2)/(2*b*c)))
            betta = float(math.acos((a2 + c2 - b2)/(2*a*c)))
            gamma = float(math.acos((a2 + b2 - c2)/(2*a*b)))

        # Converting to degree
            alpha = (float(alpha * 180 / math.pi))
            betta = (float(betta * 180 / math.pi))
            gamma = (float(gamma * 180 / math.pi))

        except:
            traceback.print_exc()
        result = max(alpha,betta,gamma)

    # Minimised Longest Edge
    elif option == 3:
        p1, p2, p3 = points[i], points[j], points[k]
        result = max(dist(p2, p3), dist(p3, p1))

    return result

# computes the diagonals that need to be connected between vertices of the polygon
def print_solution(points,s,i,j):
    if(j-i < 2):
    	return

    print_solution(points,s,i,s[i][j])
    lines_list.append([i,s[i][j]])
    lines_list.append([s[i][j],j])
    print_solution(points,s,s[i][j],j)

# the main function where the optimization is done
def triangulate(vertices, option):
    option = int(option)
    number_of_vertices = len(vertices)
    if number_of_vertices < 3:
        return False
    else:
        Matrix = [[0 for x in range(number_of_vertices)] for y in range(number_of_vertices)]
        s = [[0 for x in range(number_of_vertices)] for y in range(number_of_vertices)]
        for L in range(0, number_of_vertices):
            for a in range(0,number_of_vertices - L ):
                b = a + L
                if (b-a < 2):
                    Matrix[a][b] = 0
                else:
                    Matrix[a][b] = sys.maxint
                    for k in range(a+1,b):
                        if option == 1:
                            value = Matrix[a][k] + Matrix[k][b] + round(cost(vertices, a, k, b, option),3)
                        elif option == 2:
                            value = max(Matrix[a][k], Matrix[k][b], cost(vertices, a, k, b, option))
                        else:
                            value = max(Matrix[a][k], Matrix[k][b], round(cost(vertices, a, k, b, option),3))
                        if value < Matrix[a][b]:
                            Matrix[a][b] = round(value,3)
                            s[a][b] = k

        print_solution(vertices,s,0,number_of_vertices-1)

        # to plot the figure using matplotlib
        poly = Polygon(vertices)
        x,y = poly.exterior.xy
        plot.figure(num = 'Optimal Polygon Triangluation')
        fig = plot.figure(1, figsize=(5,5), dpi=90)
        ax = fig.add_subplot(111)
        ax.plot(x, y)

        if option == 1:
            ax.set_title('Minimum Weight Triangulation - ' + str(round(Matrix[0][number_of_vertices-1], 3)) + ' Units' + '\n')
        elif option ==2:
            ax.set_title('Minimised largest of Internal Angles - ' + str(round(Matrix[0][number_of_vertices-1], 3)) + ' Degrees' + '\n')
        else:
            ax.set_title('Minimised Longest Edge - ' + str(round(Matrix[0][number_of_vertices-1], 3)) + ' Units' +'\n')

        plot.plot(x,y, 'ro')

        x_list = []
        y_list = []

        for i in range(0, len(lines_list)):
            connectpoints(vertices[int(lines_list[i][0])],vertices[int(lines_list[i][1])])
        connectpoints(vertices[0],vertices[number_of_vertices-1])

        plot.axis('equal')

        # seperating the x and y cordinates into individual lists but the ordering remians the same.
        for i in range(0,len(vertices)):
            x_list.append(vertices[i][0])
            y_list.append(vertices[i][1])

        # give label to the vertices
        n = list(string.ascii_uppercase)
        plot.scatter(x_list, y_list)

        # the position of label of all vertices can be changed
        for i in range(0, len(vertices)):
            plot.annotate(n[i], (x_list[i],y_list[i]), xytext=(x_list[i] + 0.15, y_list[i] + 0.15))

        # displays the plot
        plot.show()

# if this file is run directly, there is no enough input so the file is forced to terminate
if __name__ == "__main__":
    print "No input is accepted => No output. EOP"
