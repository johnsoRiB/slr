
# Created by Efrain Noa     May 31, 2017
import io
#  INTRODUCTION:
# In "Sea level rise migration project", the US terrain was represented by hexagons in order to obtain a coarse grid
# scale of the terrain and improve subsequent geoprocesses. Thus, large counties such as Yukon in Alaska were
# represented by several hexagons, while small counties barely occupied part of one hexagon. In this last case, one
#  hexagon for example covered several counties.

# Migration data between US-counties were transferred to those hexagons. This transfer resulted in 95 source-hexagons,
# 714 target-hexagons, and 46204 links between them. Favorably some links have the same sources and targets, and other
# have no flows, then links will be smaller in number.

# Identification and fusion of these hexagons involve working with database and shapefiles that developing manually
#  would result in a tedious labor. Hence, THIS CODE SOLVES THE ABOVE PROBLEM BY IDENTIFYING AND MERGING DUPLICATES
# LINKS BETWEEN HEXAGONS.

# DESCRIPTION
# Sources, Targets, and Links are considered as 3D (X, Y, Z) coordinates
# This code sorts sources, targets and links ascendingly in this order.
# Next, once X and Y are identified the, Z values (migration flows) are merged
# How to use:
# Input: 1) provide coordinates (x,y,z), which a = [x1,x2,...]
#           b = [y1, y2, ...], and c = [z1, z2, ...]

# This code calls to another sub-code named "read_csvfile_3columns_data.py" which reads csv and shapefile
# ----------------------------------------------------------------------------------------
import arcpy, sys

def setup_inputs():
    a = [1,1,1,1,4,4,6,8]#a = [3,4,5,6,12,4,6,8]
    b = [2,2,2,2,5,5,7,9]#b = [3,4,5,6,12,5,7,9]
    c = [10,20,30,120,120,100,150,200]#c = [10,20,30,120,120,100,150,200]

    xx, yy, zz = excel_process(a,b,c) # <---  call function

def sort_list (a,b,c):
    n = len (a)
    print n

    x = a[0]; #print x
    y = b[0]; #print y
    z = c[0]

    xx = []; yy=[]; zz=[]; j=2

    for i in range(1,n):
        print "i = ",i
        if (a[i] == x and b[i] == y):
            z = z + c[i]
            #print "z : ", z
        else:
            xx.append(a[i-1]); #print "else ",xx
            yy.append(b[i-1]); #print "else ",yy
            zz.append(z); #print "else ",zz

            x = (a[i]); y = (b[i]); z = (c[i])
            #print x,y,z
            j += 1 # number of final rows
            print

    xx.append(a[i])
    yy.append(b[i])
    zz.append(z);

    print "xx: ", xx
    print "yy: ", yy
    print "zz: ", zz
    return xx, yy, zz

if __name__ == "__main__":
    setup_inputs()
