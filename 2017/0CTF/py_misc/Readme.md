# 0CTF 2017 Quals 
    py

    137

    We permutate the opcode of python2.7, and use it to encrypt the flag.. Try to recover it!

    py_d5764c66f02cccdb356c532d60d4d079.zip

**Category:** misc 

## Write-up

In the [zip file](py_d5764c66f02cccdb356c532d60d4d079.zip) we can find crypt.pyc and an encrypted flag `encrypted_flag`.
When we tried using [Python dissasembler](https://nedbatchelder.com/blog/200804/the_structure_of_pyc_files.html), we get 
errors. We modified [dis.py](dis.py) file so the dissambly passes without errors. Here is the result of 
running [demarshal.py](demarshal.py):

    magic 03f30d0a
    moddate 66346f58 (Fri Jan  6 07:08:38 2017)
    code
       argcount 0
       nlocals 0
       stacksize 2
       flags 0040
     153   0   0 153   1   0 134   0   0 145
       0   0 153   2   0 136   0   0 145   1
       0 153   3   0 136   0   0 145   2   0
     153   1   0  83
    Line:       Pos Name:                Opcode:   Arg:
      1           0 <153>                153       0
                  3 <153>                153       1
                  6 MAKE_CLOSURE         134       0
                  9 EXTENDED_ARG         145       0
    
      2          12 <153>                153      2L
                 15 LOAD_DEREF           136       0 oparg:0 - wrong freevar
    
                 18 EXTENDED_ARG         145       1
    
     10          21 <153>                153   65539L
                 24 LOAD_DEREF           136       0 oparg:0 - wrong freevar
    
                 27 EXTENDED_ARG         145       2
                 30 <153>                153   131073L
                 33 RETURN_VALUE         83   
       consts
          -1
          None
          code
             argcount 1
             nlocals 6
             stacksize 3
             flags 0043
     153   1   0 104   1   0 153   2   0 104
       2   0 153   3   0 104   3   0  97   1
       0 153   4   0  70 153   5   0  39  97
       2   0  97   1   0  39  97   3   0  39
     153   6   0  70  39 153   5   0  39  97
       2   0 153   6   0  70  39 153   7   0
      39 104   4   0 155   0   0  96   1   0
      97   4   0 131   1   0 104   5   0  97
       5   0  96   2   0  97   0   0 131   1
       0  83
    Line:       Pos Name:                Opcode:   Arg:
      3           0 <153>                153       1
                  3 BUILD_SET            104       1
    
      4           6 <153>                153       2
                  9 BUILD_SET            104       2
    
      5          12 <153>                153       3
                 15 BUILD_SET            104       3
    
      6          18 STORE_GLOBAL         97        1 (newrotor)
                 21 <153>                153       4
                 24 PRINT_EXPR           70   
                 25 <153>                153       5
                 28 <39>                 39   
                 29 STORE_GLOBAL         97        2 (encrypt)
                 32 STORE_GLOBAL         97        1 (newrotor)
                 35 <39>                 39   
                 36 STORE_GLOBAL         97        3 oparg:3 -  wrong name
    
                 39 <39>                 39   
                 40 <153>                153       6
                 43 PRINT_EXPR           70   
                 44 <39>                 39   
                 45 <153>                153       5
                 48 <39>                 39   
                 49 STORE_GLOBAL         97        2 (encrypt)
                 52 <153>                153       6
                 55 PRINT_EXPR           70   
                 56 <39>                 39   
                 57 <153>                153       7
                 60 <39>                 39   
                 61 BUILD_SET            104       4
    
      7          64 <155>                155       0
                 67 DELETE_ATTR          96        1 (newrotor)
                 70 STORE_GLOBAL         97        4 oparg:4 -  wrong name
    
                 73 CALL_FUNCTION        131       1
                 76 BUILD_SET            104       5
    
      8          79 STORE_GLOBAL         97        5 oparg:5 -  wrong name
    
                 82 DELETE_ATTR          96        2 (encrypt)
                 85 STORE_GLOBAL         97        0 (rotor)
                 88 CALL_FUNCTION        131       1
                 91 RETURN_VALUE         83   
             consts
                None
                '!@#$%^&*'
                'abcdefgh'
                '<>{}:"'
                4
                '|'
                2
                'EOF'
             names ('rotor', 'newrotor', 'encrypt')
             varnames ('data', 'key_a', 'key_b', 'key_c', 'secret', 'rot')
             freevars ()
             cellvars ()
             filename '/Users/hen/Lab/0CTF/py/crypt.py'
             name 'encrypt'
             firstlineno 2
       0   1   6   1   6   1   6   1  46   1
      15   1
          code
             argcount 1
             nlocals 6
             stacksize 3
             flags 0043
     153   1   0 104   1   0 153   2   0 104
       2   0 153   3   0 104   3   0  97   1
       0 153   4   0  70 153   5   0  39  97
       2   0  97   1   0  39  97   3   0  39
     153   6   0  70  39 153   5   0  39  97
       2   0 153   6   0  70  39 153   7   0
      39 104   4   0 155   0   0  96   1   0
      97   4   0 131   1   0 104   5   0  97
       5   0  96   2   0  97   0   0 131   1
       0  83
    Line:       Pos Name:                Opcode:   Arg:
     11           0 <153>                153       1
                  3 BUILD_SET            104       1
    
     12           6 <153>                153       2
                  9 BUILD_SET            104       2
    
     13          12 <153>                153       3
                 15 BUILD_SET            104       3
    
     14          18 STORE_GLOBAL         97        1 (newrotor)
                 21 <153>                153       4
                 24 PRINT_EXPR           70   
                 25 <153>                153       5
                 28 <39>                 39   
                 29 STORE_GLOBAL         97        2 (decrypt)
                 32 STORE_GLOBAL         97        1 (newrotor)
                 35 <39>                 39   
                 36 STORE_GLOBAL         97        3 oparg:3 -  wrong name
    
                 39 <39>                 39   
                 40 <153>                153       6
                 43 PRINT_EXPR           70   
                 44 <39>                 39   
                 45 <153>                153       5
                 48 <39>                 39   
                 49 STORE_GLOBAL         97        2 (decrypt)
                 52 <153>                153       6
                 55 PRINT_EXPR           70   
                 56 <39>                 39   
                 57 <153>                153       7
                 60 <39>                 39   
                 61 BUILD_SET            104       4
    
     15          64 <155>                155       0
                 67 DELETE_ATTR          96        1 (newrotor)
                 70 STORE_GLOBAL         97        4 oparg:4 -  wrong name
    
                 73 CALL_FUNCTION        131       1
                 76 BUILD_SET            104       5
    
     16          79 STORE_GLOBAL         97        5 oparg:5 -  wrong name
    
                 82 DELETE_ATTR          96        2 (decrypt)
                 85 STORE_GLOBAL         97        0 (rotor)
                 88 CALL_FUNCTION        131       1
                 91 RETURN_VALUE         83   
             consts
                None
                '!@#$%^&*'
                'abcdefgh'
                '<>{}:"'
                4
                '|'
                2
                'EOF'
             names ('rotor', 'newrotor', 'decrypt')
             varnames ('data', 'key_a', 'key_b', 'key_c', 'secret', 'rot')
             freevars ()
             cellvars ()
             filename '/Users/hen/Lab/0CTF/py/crypt.py'
             name 'decrypt'
             firstlineno 10
       0   1   6   1   6   1   6   1  46   1
      15   1
       names ('rotor', 'encrypt', 'decrypt')
       varnames ()
       freevars ()
       cellvars ()
       filename '/Users/hen/Lab/0CTF/py/crypt.py'
       name '<module>'
       firstlineno 1
      12   1   9   8

 * Three names are used in main function: `rotor`, `encrypt` and `decrypt`. 
    Later there are functions defined with names `encrypt` and `decrypt`, so we
    guess that `rotor` is the name of imported module. It appears to be 
    [this](https://docs.python.org/2.0/lib/module-rotor.html) module.
 * From number of variable names and argument count we can see that functions take parameter `data`
 * There are local variables in funtions `key_a`, `key_b`, `key_c`, `secret`, `rot`
 * Some opcodes appear not to be scrambled, e.g. `RETURN_VALUE` and `CALL_FUNCTION`
Let us create a file [test.py](test.py) that we can use as reference. We try to make it decompile to the similar code as crypt.pyc.
We make a wild guess that 'key_a`, 'key_b` and `key_c` are assigned constants indexed from `1` to `3` based on `6` first lines of 
dissasembled code.

Here is the result of dissasembling [test.py](test.py)

    magic 03f30d0a
    moddate dcc9d058 (Tue Mar 21 07:36:12 2017)
    code
       argcount 0
       nlocals 0
       stacksize 2
       flags 0040
     100   0   0 100   1   0 108   0   0  90
       0   0 100   2   0 132   0   0  90   1
       0 100   1   0  83
    Line:       Pos Name:                Opcode:   Arg:
      1           0 LOAD_CONST           100       0 (-1)
                  3 LOAD_CONST           100       1 (None)
                  6 IMPORT_NAME          108       0 (rotor)
                  9 STORE_NAME           90        0 (rotor)
    
      3          12 LOAD_CONST           100       2 (<code object encrypt at 0x7f0a4bbae830, file "test.py", line 3>)
                 15 MAKE_FUNCTION        132       0
                 18 STORE_NAME           90        1 (encrypt)
                 21 LOAD_CONST           100       1 (None)
                 24 RETURN_VALUE         83   
       consts
          -1
          None
          code
             argcount 1
             nlocals 4
             stacksize 1
             flags 0043
     100   1   0 125   1   0 100   2   0 125
       2   0 100   3   0 125   3   0 100   0
       0  83
    Line:       Pos Name:                Opcode:   Arg:
      4           0 LOAD_CONST           100       1 ('!@#$%^&*')
                  3 STORE_FAST           125       1 (key_a)
    
      5           6 LOAD_CONST           100       2 ('abcdefgh')
                  9 STORE_FAST           125       2 (key_b)
    
      6          12 LOAD_CONST           100       3 ('<>{}:"')
                 15 STORE_FAST           125       3 (key_c)
                 18 LOAD_CONST           100       0 (None)
                 21 RETURN_VALUE         83   
             consts
                None
                '!@#$%^&*'
                'abcdefgh'
                '<>{}:"'
             names ()
             varnames ('data', 'key_a', 'key_b', 'key_c')
             freevars ()
             cellvars ()
             filename 'test.py'
             name 'encrypt'
             firstlineno 3
       0   1   6   1   6   1
       names ('rotor', 'encrypt')
       varnames ()
       freevars ()
       cellvars ()
       filename 'test.py'
       name '<module>'
       firstlineno 1
      12   2

Comparing both outputs of dissasembly we can easily see that the following
opcodes can be deciphered:
 * `153` is `LOAD_CONST`
 * `134` is `IMPORT_NAME`
 * `145` is `STORE_NAME`
 * `136` is `MAKE_FUNCTION`
 * `104` is `STORE_FAST`
Now looking at documentation of `rotor` module and seeing that
    rot = rotor.newrotor(secret)
    return rot.decrypt(data)
decompiles to (assuming secret is local variable):

      8          24 LOAD_GLOBAL          116       0 (rotor)
                 27 LOAD_ATTR            106       1 (newrotor)
                 30 LOAD_FAST            124       4 (secret)
                 33 CALL_FUNCTION        131       1
                 36 STORE_FAST           125       5 (rot)
    
      9          39 LOAD_FAST            124       5 (rot)
                 42 LOAD_ATTR            106       2 (decrypt)
                 45 LOAD_FAST            124       0 (data)
                 48 CALL_FUNCTION        131       1
                 51 RETURN_VALUE         83   

we can deduce how some more opcodes should be deciphered:
 * `155` is `LOAD_GLOBAL`
 * `96` is `LOAD_ATTR`
 * `97` is `LOAD_FAST`

We are left with one line numbered `6` in the original file, which probably
assigns value to the `secret` based on values of `key_a`,`key_b` and `key_c`.
After patching crypt.pyc the relevant line decompiles to:

      6          18 LOAD_FAST            124       1 (key_a)
                 21 LOAD_CONST           100       4 (4)
                 24 PRINT_EXPR           70   
                 25 LOAD_CONST           100       5 ('|')
                 28 <39>                 39   
                 29 LOAD_FAST            124       2 (key_b)
                 32 LOAD_FAST            124       1 (key_a)
                 35 <39>                 39   
                 36 LOAD_FAST            124       3 (key_c)
                 39 <39>                 39   
                 40 LOAD_CONST           100       6 (2)
                 43 PRINT_EXPR           70   
                 44 <39>                 39   
                 45 LOAD_CONST           100       5 ('|')
                 48 <39>                 39   
                 49 LOAD_FAST            124       2 (key_b)
                 52 LOAD_CONST           100       6 (2)
                 55 PRINT_EXPR           70   
                 56 <39>                 39   
                 57 LOAD_CONST           100       7 ('EOF')
                 60 <39>                 39   
                 61 STORE_FAST           125       4 (secret)

Basically we are left with two opcodes (`70` and `39`) which we need to decipher.
Counting variables on the stack, we can see that those should be binary operations, 
and since we calculate the value of `secret` we can assume string operations. 
Guessing that `39` is `BINARY_ADD` was easy. Assigning `70` to `BINARY_MULTIPLY` took us 
a bit more time as we tried all possible different binary operations on string like `SLICE+1` etc.
With those two last opcodes we can construct the algorithm to encrypt/decrypt [solve.py](solve.py).
Running `python solve.py` gives us the flag:
    flag{Gue55_opcode_G@@@me 
