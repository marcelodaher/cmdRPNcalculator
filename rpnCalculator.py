#!/usr/bin/python

import calculatorQueue
import numpy

q = calculatorQueue.calculatorQueue()
exitCmd = ['quit', 'exit']
operations = {'+': 'add',
              '-': 'subtract',
              '*': 'multiply',
              '/': 'divide',
              '^': 'power',
              '**':'power'}
while (1): #routine
    #get input
    cmd = raw_input('>>')
    #check for exit
    if cmd in exitCmd: break
    #check for number
    try:
        q.push(numpy.array(cmd,dtype=float))
    #check for command
    except:
        try:
            #checks for key symbol
            if cmd in operations: cmd = operations[cmd]
            #try to find command in numpy operations
            m = getattr(numpy, cmd)
            argList = [q.get() for i in range(m.nin)]
            argList.reverse()
            q.push(m(*argList))
        #command not recognized-> repeat loop
        except: print "could not process CMD"
    print q
