#!/usr/bin/env python3

import sys

def getCols(f):
    headings = f.readline().strip().split(",")
    num_col = None  
    mark_col = None 
    i = 0  #(Error1) start at 0, not 1
    for head in headings:
        if head == "Student Number": 
            num_col = i
        elif head == "Mark": 
            mark_col = i
        i += 1
    return num_col, mark_col

def findTop(f, num_col, mark_col):
    best = -1
    best_student = None  #(Error2) store student number, not index
    for line in f:
        data = line.strip().split(",")
        mark = int(data[mark_col])
        student = data[num_col]  #(Error3) get student number
        if mark > best:
            best = mark
            best_student = student  #(Change) update student number
    return best_student, best  #(Error4) return student, not index

f = open(sys.argv[1])
num_col, mark_col = getCols(f)
best_student, best = findTop(f, num_col, mark_col)  #(Changed) unpack differently
print("The top student was student %s with %d" % (best_student, best))
f.close()