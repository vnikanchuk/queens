#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def init():
    L = [7, 6, 5, 4, 3, 2, 1, 0]
    V = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    S = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    return L, [], [], V, S, 0 # P=[]; R=[]
    
def klav():
    try:
        raw_input("> ")
    except:
        print "\n\n"
        sys.exit(0)

def main(Array):
    print "="*78,"\n","="*78
    lef, rig, pole, vos, spu, H = Array
    print "main(\tlef = {0}\n\trig = {1}\n\tpole = {2}\n\tvos = {3}\n\tspu = {4}\n\tH = {5})".format(lef,rig,pole,vos,spu,H)
    while len(lef):
        print "while len(lef):\t\tlef = {0}, len ={1}".format(lef,len(lef))
        V = lef.pop()
        print "\t\t\tV =",V
        print "if vos[H + V] and spu[H - V]:\t",vos[H + V] and spu[H - V]
        if vos[H + V] and spu[H - V]:
            vos[H + V] = 0
            spu[H - V] = 0
            pole.append(V)
            print "vos[H + V] = 0\nspu[H - V] = 0"
            print "pole.append(V)"
            H += 1
            print "H += 1\t\t\tH =",H
            rig.reverse()
            lef = lef + rig[:]
            rig = []
            print "rig.reverse()\t\trig =",rig
            print "lef = lef + rig[:]\tlef =",lef
            print "rig = []"
            print "="*30,"\npole =", pole,"\nvos =",vos,"\nspu =",spu
            klav()
            main((lef,rig,pole,vos,spu,H))
        else:
            print "else:"
            rig.append(V)
            print "rig.append(V)\t\trig =",rig
        klav()
        
    else:
        print "else:"
        print "Ничего не осталось"
        print "pole = ", pole
        print "H =", H, "\nV =", V
        print "rig =", rig
        
    return

if __name__== "__main__":
    print "\n\n"
    sys.exit(main(init()))