#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def init():
    P = [9, 9, 9, 9, 9, 9, 9, 9]
    L = [7, 6, 5, 4, 3, 2, 1, 0]
    V = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    S = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    return P, V, S, L
    
def klav():
    try:
        raw_input("> ")
    except:
        print "\n\n"
        sys.exit(0)

def main(Array):
    pole, vos, spu, lef = Array
    for i in range(8):
        for j in range(8):
            if vos[i + j] and spu[i - j]:
                pole[i] = j
                vos[i + j] = 0
                spu[i - j] = 0
                print pole
                klav()
                break
        j = pole[i]
        pole[i] = 9
        vos[i + j] = 1
        spu[i - j] = 1

if __name__== "__main__":
    print "\n\n"
    sys.exit(main(init()))