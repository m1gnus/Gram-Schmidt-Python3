#!/bin/env python3

##
# gram schmidt algorithm: https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process
# Vittorio Mignini aka M1gnus
##

""" from "An Introduction to Mathematical Cryptography", Jeffrey Hoffstein, Jill Pipher, Joseph H. Silverman
u1 = v1
Loop i = 2,3...,n
   Compute μij = vi ∙ uj / ||uj||2, 1 ≤ j < i.
   Set ui = vi - μij * uj (Sum over j for 1 ≤ j < i)
End Loop 
"""

import sys, math

def usage():
    print("./gram_schmidt.py [int|float] v1 v2 v3...\nExample: ./gram_schmidt.py float 4,1,3,-1 2,1,-3,4 1,0,-2,7 6,2,9,-5")
    sys.exit(0)

def acquire_vectors(args):

    v = []
    for vect in args:
        v.append([int(x) for x in vect.split(",")])
    
    len_ = len(v[0])
    for vect in v:
        if len(vect) != len_:
            print("[-] all the vectors must have the same length")
            sys.exit(1)

    return v

def calc_size_square(v):

    res = 0
    for i in range(len(v)):
        res += pow(v[i],2)
    return res

def gram_schmidt(v, mode):

    if mode != "int" and mode != "float":
        usage()

    u = [v[0]]
    mu = [[]]

    for i in range(1, len(v)):
        mu.append([])

        for j in range(i):

            tmp = []
            for k in range(len(u[j])):
                tmp.append( v[i][k] * u[j][k] )
            tmp = sum(tmp)
            square_size = calc_size_square(u[j])

            if mode == "float":
                tmp /= square_size
            else:
                tmp //= square_size

            mu[i].append(tmp)

        u.append(v[i])
        tmpsum = [0] * len(u[0])

        for j in range(i):
            tmp = [] + u[j]
            for k in range(len(u[j])):
                tmp[k] *= mu[i][j]
            for k in range(len(tmp)):
                tmpsum[k] += tmp[k]

        for j in range(len(u[i])):
            u[i][j] -= tmpsum[j]
    
    return u

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        usage()

    v = acquire_vectors(sys.argv[2:])
    new_base = gram_schmidt(v, sys.argv[1])

    for i in range(len(new_base)):
        print("u" + str(i + 1) + ":", new_base[i])
