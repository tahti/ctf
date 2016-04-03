#!/usr/bin/python
import ssl, socket
import numpy

def pow(M, p, modulus):
    if p == 1:
        return M
    if p % 2 != 0:
        return (M * pow(M, p - 1, modulus)) % modulus
    X = pow(M, p/2, modulus)
    return (X * X) % modulus 

def solve(n):
    if n < 5:
        return "1 " + str(n)
    k = n - 4
    v = numpy.matrix ([[1], [1], [1], [1], [4]])
    A = numpy.matrix ([[0,1,0,0, 0], [ 0,0,1,0,0], [ 0,0,0,1,0], [1,2,3,4,0], [1,2,3,4,1]])
    mod = 10**9
    T = pow(A, k, mod)
    r = T * v
    killed = str(r.item(3))[-9:]
    sumKilled = str(r.item(4))[-9:]
    return killed + " " + sumKilled


class Connect(object):
    def __init__(self, host, port):
        self.context = ssl.create_default_context()
        self.conn = self.context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=host)
        self.conn.connect((host, port))
        self.f = self.conn.makefile('r+b', 0)
    def __enter__(self):
        return self.f
    def __exit__(self, type, value, traceback):
        self.f.close()

with Connect('programming.pwn2win.party', 9001) as f:
    for line in f:
        line = line.strip()
        print('received: %s' % line)

        if line.startswith('CTF-BR{') or \
           line == 'WRONG ANSWER': break

        number = int(line)
        s = solve(number)
        print "send "+s
        f.write('%s\n' % s)
