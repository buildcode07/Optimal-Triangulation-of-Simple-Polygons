'''
    CG project on optimal triangluation by dyanamic programming

'''

import triangulate as optimization_triangulation
import open_file
import os,sys

file_name_old = ""

# the location of the vertices file is captured
def file_name_open(new_file_name):
    global file_name_old
    file_name_old = str(new_file_name)

# this resets all the older matplot data, and also re-runs the file 'app.py'
def reset(file_name, option):
    global file_name_old
    if len(file_name) > 2:
        file_name_old = file_name
    os.execv(sys.executable, ['python'] + [sys.argv[0]] + [file_name_old,str(option)])

# the vertices are read from the given file and are sent to the optimzation method to compute the triangluation
def main(file_name, option):
    global file_name_old
    file_name_old = file_name

    # if there is an error, try to catch it in the exception block
    try:
        vertices = open_file.get_vertices(file_name_old)
        enumerated_vertices = []
        for cordinates in vertices:
            new_cordinate = cordinates.split(",")
            for i in range(0, len(new_cordinate)):
                new_cordinate[i] = float(new_cordinate[i])
            enumerated_vertices.append(new_cordinate)

    except Exception as error:
        print error
        print "Please try a different input"

    optimization_triangulation.triangulate(enumerated_vertices, option)

if __name__ == "__main__":
    print "Select Optimization Technique" + "\n" + "============================="
    print "1. Minimum Weight Triangluation"
    print "2. Minimizing The Maximum of the Internal Angles"
    print "3. Minimizing the Longest Edge"

    option = int(raw_input())
    if option < 4:
        main(option, "vertices.txt")
    else:
        print "Invalid Input"
