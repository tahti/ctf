import ssl, socket

def encode(flow, encr):
    upper = []
    plain = list(encr)
    for i in range(len(plain)):
        upper.append(plain[i].isupper())
        if upper[i]:
           plain[i] = ord(plain[i]) - ord('A')
        else:
           plain[i] = ord(plain[i]) - ord('a')
    for i in range(len(plain)):
        j = 0
        while flow[j] != i:
            j = j + 1
        if i % 2 == 0:
            plain[i] = (plain[i] + flow[(j + 1)%len(plain)])%26
        else:
            plain[i] = (plain[i] + flow[(j + len(plain) - 1)%len(plain)])%26
    for i in range(len(plain)):
        if upper[i]:
           plain[i] = chr(plain[i] + ord('A'))
        else:
           plain[i] = chr(plain[i] + ord('a'))
    return "".join(plain)

def decode(flow, encr):
    upper = []
    plain = list(encr)
    for i in range(len(plain)):
        upper.append(plain[i].isupper())
        if upper[i]:
           plain[i] = ord(plain[i]) - ord('A')
        else:
           plain[i] = ord(plain[i]) - ord('a')
    for i in range(len(plain)):
        j = 0
        while flow[j] != i:
            j = j + 1
        if i % 2 == 0:
            plain[i] = (26 + plain[i] - flow[(j + 1)%len(plain)])%26
        else:
            plain[i] = (26 + plain[i] - flow[(j + len(plain) - 1)%len(plain)])%26
    for i in range(len(plain)):
        if upper[i]:
           plain[i] = chr(plain[i] + ord('A'))
        else:
           plain[i] = chr(plain[i] + ord('a'))
    return "".join(plain)

def communicate():
    tgt = ('pool.pwn2win.party', 4040)
    print "Connecting ..."
    con = socket.create_connection(tgt)
    f = con.makefile()
    answer = []
    for i in range(10):
        line = f.readline()
        line = line.strip()
        print('received: %s' % line)
        l = line.split(" -> ")
        flow = l[0].replace("[","").replace("]", "").split(", ")
        flow = map(int, flow)
        enc = l[1]
        s = decode(flow, enc)
        s = s + ","
        answer.append(s)
    s =f.read(len("Decoded strings?"))
    print "received "+s
    ss = ""
    for s in answer:
      ss = ss + s
    print ss
    f.write('%s' % ss)
    f.flush()

    for line in f:
        print('received: %s' % line)

def testCase(s):
    l = s.split(" -> ")
    flow = l[0].replace("[","").replace("]", "").split(", ")
    flow = map(int, flow)
    plain= l[1].strip()
    enc = l[2].strip()
    s = decode(flow, enc)
    if  s == plain:
        print "OK dec"
    else:
        print "Wrong:"+ s + " vs:"+ plain
    s = encode(flow, plain)
    if  s == enc:
        print "OK enc"
    else:
        print "Wrong:"+ s + " vs:"+ enc
    
def test():
    testCase("[5, 0, 8, 3, 4, 9, 6, 2, 7, 1] -> aDuLteRInE -> iKbTcfTKqI")
    testCase("[1, 3, 6, 4, 9, 2, 7, 0, 8, 5] -> aboMINAblE -> igvNRVEdqI")
    testCase("[0, 9, 2, 8, 4, 7, 5, 1, 6, 3] -> ACIdophiLS -> JHQjvwkmPS")
    testCase("[5, 6, 9, 1, 3, 8, 2, 4, 7, 0] -> hypOCOtYLs -> mhtPJOcCNy")
    testCase("[9, 7, 6, 3, 4, 0, 5, 8, 1, 2] -> fuRcATIOns -> kcAiATLXou")
    testCase("[6, 0, 1, 2, 8, 7, 9, 4, 5, 3] -> ACeTaNiLid -> BCmYfRiTpk")
    testCase("[8, 0, 4, 5, 2, 7, 3, 6, 1, 9] -> FURriErIes -> JAYynIsKet")
    testCase("[9, 1, 8, 3, 6, 7, 0, 2, 5, 4] -> KidnAPPeRs -> MrivJRWkUw")
    testCase("[0, 5, 2, 9, 1, 6, 8, 4, 7, 3] -> GarmeNTiNG -> LjatlNBmRI")

communicate()
# test()
# [1, 3, 6, 4, 9, 2, 7, 0, 8, 5] -> 
# s1 = "aboMINAblE"
# s2 = "igvNRVEdqI"
#  >  <  >  <  >  <  >  <  >  <
#  0  1  2  3  4  5  6  7  8  9
# -8 -5 -7 -1 -9 -8 -4 -2 -5 -4


# [0, 9, 2, 8, 4, 7, 5, 1, 6, 3] -> 
# s1 = "ACIdophiLS" 
# s2 = "JHQjvwkmPS"
#  >  <  >  <  >  <  >  <  >  <
#  0  1  2  3  4  5  6  7  8  9
# -9 -5 -8 -6 -7 -7 -3 -4 -4  0


