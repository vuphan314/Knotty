'''
print test string
'''

# tst: object -> print
def tst(o = 'DEFAULT TEST STRING'):
    st = str(o)
    st = markerComment + '\nTEST\n' + st + '\n' + markerComment + '\n'
    print(st)

###########################################################
'''
raise error
'''

# raiseError: raise
def raiseError(o = 'DEFAULT ERROR MESSAGE'):
    st = '\n\n' + str(o)
    raise NameError(st)
err = raiseError

###########################################################
'''
mark start and end of wanted string
'''

# markStartEnd: str -> str
def markStartEnd(st):
    st = startComment + st + endComment
    return st

# blockComment: str -> str
def blockComment(st):
    return '/* ' + st + ' */'

markerComment = blockComment(
'********** ********** ********** ********** ********** **********')

startComment = markerComment + '\n' + blockComment('SECTION START')
endComment = blockComment('SECTION END') + '\n' + markerComment
