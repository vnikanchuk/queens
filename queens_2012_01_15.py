#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def init(N):
    P = []; V = []; S = []
    return P, V, S, N
    
def klav():
    try:
        raw_input("> ")
    except:
        print "\n\n"
        sys.exit(0)

def main(Array):
    global X
    pole, vos, spu, N = Array
    H = len(pole)
    if H == N:
        print X,"---->",pole
        X += 1
    else:
        L = range(N)
        for i in pole:
            L.remove(i)
        for V in vos:
            try: 
                L.remove(V - H)
            except: pass
        for V in spu:
            try: 
                L.remove(H + V)
            except: pass
        if len(L):
            for V in L:
                pole.append(V)
                vos.append(H + V)
                spu.append(V - H)
                
                main((pole,vos, spu, N))
        else:
            pass
    if pole: pole.pop()
    if vos: vos.pop()
    if spu: spu.pop()
    return
        
X = 1
if __name__== "__main__":
    args = sys.argv
    if len(args) == 1:
        N = 7
    else:
        N = int(args[1])
    print "\n\n"
    main(init(N))
    print X - 1
    sys.exit(0)
