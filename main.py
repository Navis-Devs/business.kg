import sys


def printn(*args, sep=' ', end='\n', file=sys.stdout):
    output = sep.join(map(str, args))
    file.write(output + end)


def inputn(variable=''):
    sys.stdout.write(variable)
    sys.stdout.flush()
    return sys.stdin.readline().rstrip('\n')


printn(inputn())