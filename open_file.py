'''
    file open and reading input
    first line gives the x and y coordinates of p (separated by a space) and also gives a clockwise listing of the (x, y) coordinates (floating point) of the vertices (two floating point numbers, separated by a space)
'''

# the file is opened and read
def get_vertices(file_name):
    file         = open(file_name,'r')
    file_content = file.read()
    lines        = file_content.split("\n")
    vertices     = lines[0].split(" ")
    file.close()

    return vertices

if __name__ == "__main__":
    print_vertices.display(get_vertices())
