#!/usr/bin/python3
import time
import curses
import math
from kanren import run, isvar, membero
from kanren.core import success,fail,condeseq,eq,var
from sympy.ntheory.generate import prime,isprime
import itertools as it

def main( stdscr ):
    curses.curs_set( False )
    FPS = 60 
    
    minFrameTime = 1/FPS
    frameDelta = 0
    
    height,width = stdscr.getmaxyx()
    height -= 1
    
    g1Yrange = range( 0, int((width/2)-1) )
    g2Yrange = range( int((width/2)+1), width-1 )
    midLoc = int( width/2 - 1 )
    midWidth = 2
    graphWidth = int( width/2 - 1 )
    g1Title = 'y=sin(x), where x is prime and 0 < x < 100,000'
    g2Title = 'y=sin(sqrt(x)), where x is prime and 0 < x < 100,000'
    g1TitleLoc = midLoc - int( graphWidth/2 ) - int( len(g1Title)/2 )
    g2TitleLoc = midLoc + int( graphWidth/2 ) - int( len(g2Title)/2 )
    leftBuffer = []
    midBuffer = []
    rightBuffer = []

    loadingMsg1 = 'Calculating prime numbers between 0 and 100,000'
    loadingMsg2 = 'Please wait...'
    stdscr.addstr( int( height/2 ), int( midLoc - len(loadingMsg1)/2 ), loadingMsg1 )
    stdscr.addstr( int( height/2)+1, int( midLoc - len(loadingMsg2)/2 ), loadingMsg2 )
    stdscr.refresh()

    for i in range( 0, graphWidth ):
        leftBuffer.append( [] )
        for j in range( 0, height ):
            leftBuffer[i].append( '1' )
    
    for i in range( 0, midWidth ):
        midBuffer.append( [] )
        for j in range( 0, height ):
            midBuffer[i].append( ' ' )
   
    for i in range( 0, graphWidth ):
        rightBuffer.append( [] )
        for j in range( 0, height ):
            rightBuffer[i].append( '1' )

    n = var()
    primeSet = sorted( set( run( 0, n, (membero, n, range(1, 100000)), (prime_test, n) ) ) )

    for entry in primeSet:
        frameStart = time.time()

        g1Col = []
        g2Col = []
        for i in range( 0, height ):
            g1Col.append( '1' )
            g2Col.append( '1' )

        g1Index = int( (math.sin( entry ) + 1) / 2 * (height-1) )
        g2Index = int( (math.sin( math.sqrt( entry ) ) + 1) / 2 * (height-1) )
        
        g1Col[g1Index] = ' '
        g2Col[g2Index] = ' '

        del leftBuffer[0]
        del rightBuffer[0]
        leftBuffer.append( g1Col )
        rightBuffer.append( g2Col )

        stdscr.addstr( 0, g1TitleLoc, g1Title, curses.A_UNDERLINE )
        stdscr.addstr( 0, g2TitleLoc, g2Title, curses.A_UNDERLINE )

        for i in g1Yrange:
            for j in range( 0, height-1 ):
                if leftBuffer[i][j] == ' ':
                    stdscr.addch( j+1, i, leftBuffer[i][j], curses.A_STANDOUT )
                else:
                    stdscr.addch( j+1, i, leftBuffer[i][j] )
        
        for i in range( 0, midWidth ):
            for j in range( 0, height-1 ):
                stdscr.addch( j+1, midLoc+i, midBuffer[i][j], curses.A_STANDOUT )

        for i,k in zip(g2Yrange, range( 0, graphWidth )): 
            for j in range( 0, height-1 ):
                if rightBuffer[k][j] == ' ':
                    stdscr.addch( j+1, i, rightBuffer[k][j], curses.A_STANDOUT )
                else:
                    stdscr.addch( j+1, i, rightBuffer[k][j] )

        if frameDelta > 0:
            fpsDisplay = 'FPS: '+'{0:.2f}'.format( 1/frameDelta )
            stdscr.addstr( height, 0, fpsDisplay )
            stdscr.addstr( height, len( fpsDisplay ), '\t\tCTRL+C to exit', curses.A_BLINK )

        frameDelta = time.time() - frameStart
        while frameDelta < minFrameTime:
            frameDelta = time.time() - frameStart 

        stdscr.refresh()

    input()

def prime_test( n ):
    if isvar( n ):
        return condeseq( [(eq, n, p)] for p in map( prime, it.count(1) ) )
    else:
        return success if isprime( n ) else fail

curses.wrapper( main )