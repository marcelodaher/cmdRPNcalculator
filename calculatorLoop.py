import cmd
import calculatorQueue
import numpy

class CalculatorLoop(cmd.Cmd):
    
    q = calculatorQueue.CalculatorQueue()
    
    operations = {'+': 'add',
                  '-': 'subtract',
                  '*': 'multiply',
                  '/': 'divide',
                  '^': 'power',
                  '**':'power'}

    prompt = '>>'
    
    def default(self,cmd):
        #check for number
        try:
            self.q.push(numpy.array(cmd,dtype=float))
        #check for command
        except:
            try:
                #checks for key symbol
                if cmd in self.operations: cmd = self.operations[cmd]
                #try to find command in numpy operations
                m = getattr(numpy, cmd)
                argList = [self.q.get() for i in range(m.nin)]
                argList.reverse()
                self.q.push(m(*argList))
            #command not recognized-> repeat loop
            except:
                print "could not process CMD"
    
    def postcmd(self, stop, line):
        print self.q
        return cmd.Cmd.postcmd(self, stop, line)
    
    def emptyline(self):
        return
    
    """
    do commands
    """
    
    def do_exit(self, line):
        """Exit calculator"""
        stop = True
        return cmd.Cmd.postcmd(self, stop, line)
    
    def do_clear(self, line):
        """Empty the queue"""
        self.q.clear()
    
    def do_drop(self, line):
        """Drop the last value on the queue"""
        if not self.q.empty():
            self.q.get()
        else: print "Queue is already empty"
    
    do_EOF = do_exit