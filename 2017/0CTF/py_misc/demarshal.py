import dis, marshal, struct, sys, time, types
from opcode import *

def show_file(fname):
    f = open(fname, "rb")
    magic = f.read(4)
    moddate = f.read(4)
    modtime = time.asctime(time.localtime(struct.unpack('i', moddate)[0]))
    print("magic %s" % (magic.encode('hex')))
    print("moddate %s (%s)" % (moddate.encode('hex'), modtime))
    code = marshal.load(f)
    #exec code
    show_code(code)

def show_code(code, indent=''):
    print("%scode" % indent)
    indent += '   '
    print("%sargcount %d" % (indent, code.co_argcount))
    print("%snlocals %d" % (indent, code.co_nlocals))
    print("%sstacksize %d" % (indent, code.co_stacksize))
    print("%sflags %04x" % (indent, code.co_flags))
    show_hex("code", code.co_code, indent=indent)
    print("Line:       Pos Name:                Opcode:   Arg:")
    dis.disassemble(code)
    print("%sconsts" % indent)
    for const in code.co_consts:
        if type(const) == types.CodeType:
            show_code(const, indent+'   ')
        else:
            print("   %s%r" % (indent, const))
    print("%snames %r" % (indent, code.co_names))
    print("%svarnames %r" % (indent, code.co_varnames))
    print("%sfreevars %r" % (indent, code.co_freevars))
    print("%scellvars %r" % (indent, code.co_cellvars))
    print("%sfilename %r" % (indent, code.co_filename))
    print("%sname %r" % (indent, code.co_name))
    print("%sfirstlineno %d" % (indent, code.co_firstlineno))
    show_hex("lnotab", code.co_lnotab, indent=indent)

def show_hex(label, h, indent):
  for i in range(len(h)):
    sys.stdout.write("%4d"% ord(h[i]))
    if (i%10 == 9):
      print("")

  print("")

show_file(sys.argv[1])
