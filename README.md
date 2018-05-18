Optimal Triangulation using Dynamic Programming [works only for convex polygons]
================================================================================
The problem statement is to compute an optimal triangulation for a simple polygon using dynamic programming. There are various optimization techniques. The techniques were implemented based on the Bellman equation. The software includes:

    *  Minimum weight triangulation
    *  Minimised largest of internal angles
    *  Minimised longest edge

Requirements
============
This project requires the following python modules:
1. matplotlib==2.2.2
2. shapely==1.6.4.post1
3. Tkinter
4. PIL
6. numpy==1.14.3

The installation of these modules is platform dependent.

How to run the software?
========================
1. Input the x and y coordinates of a vertex of a polygon separated by a comma. Each vertex is separated from the other by a space. The ordering of the vertices is clockwise.
2. Open terminal. Navigate to the folder containing the file "app.py".
3. Run the command "python app.py" on the terminal.
4. Choose the button "open file" and select the file containing vertices, followed by selecting an optimization technique from the drop down menu.
5. The output can be saved by clicking on the floppy disk button placed on the plot.
