import sys
import os

def createAnotherFile():
    args = sys.argv
    if len(args) == 1:
        mess = '\nexample invocation:\n\n\t'
        mess += 'py engine.py examples/demo.kn'
        mess += '\n\n'
        mess += 'the file `examples/demo_simplified.kn` will be OVERWRITTEN/created\n'
        print(mess)
        input('(key `Enter` to quit)')
    else:
        pathSource = sys.argv[1]
        pathBase = os.path.splitext(pathSource)[0]
        pathSimplified = pathBase + '_simplified.kn'
        with open(pathSource, 'r') as sourceFile:
            st = sourceFile.read()
        with open(pathSimplified, 'w') as simplifiedFile:
            simplifiedFile.write(st)
        print('\nOVERWROTE/created ' + pathSimplified)

if __name__ == '__main__':
    createAnotherFile()
