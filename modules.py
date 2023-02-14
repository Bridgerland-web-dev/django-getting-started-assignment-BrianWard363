#!/usr/bin/env python3

def main():
    r = float(input('What is the radis of the sphere?: '))
    #valume of sphere
    pi = 22/7
    V = 4.0/3.0*pi* r**3
    #area of sphere
    a = 4 * pi * r **2
    #round to two decimal places
    va = round(V, 2)
    aa = round(a, 2)
    #print volume and area of sphere
    print('The radis of the sphere is: ', r)
    print('The volume of a phere is: ', va)
    print('The area of a sphere is: ', aa)

if __name__ == '__main__': main()