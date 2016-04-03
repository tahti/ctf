# Death Sequence (PPC-M, 100p)

## Description:
During the Brazilian military dictatorship, many people were simply eliminated.
At a given time, the Club decided to check the number of dead people to not
arouse suspicion. When the check began, it was found that the following
sequence indicates the number of deaths per week:


> 1 1 1 1 10 46 217 1027 4861 23005 108874 515260 2438533 11540665


Anyway... Two things are clear here. The logic of sequence and that the the
amount of killing was becoming uncontrollable. At this rate, within a few
months the Brazilian population would end and within not much more than that
the world population would end too. The numbers were so big, but they did not
give up entirely on the challenge. They want to know (but they do not want to
calculate it, they need you for that) the last 9 digits of nth sequence
term and the last 9 digits of the total number of death people since the
beginning, separated by a single space in a single line, with n given
(n<10^18).


*Example*

input:

> 4


output:

> 1 4

## Solution

First we determine the formula for n'th element:

>f(x) = 1, for x in in range <1,4> (inclusive) 

>f(x) = 4*f(x-1) + 3*f(x-2) + 2*f(x-3) + f(x-4)

The problem is that we have to calculate the value of the formula for a large n
and doing it recusively is not feasible.
[Here](http://fusharblog.com/solving-linear-recurrence-for-programming-contest/)
is a nice article how to solve recurrence problems efficiently.

Following article we found the characteristic A matrix to be:

|**0**|**1**|**0**|**0**|
|:--:|:--:| :--:| :--:|
|**0**|**0**|**1**|**0**|
|**0**|**0**|**0**|**1**|
|**1**|**2**|**3**|**4**|

and initial vector v:

|**1**|
|:--:|:
|**1**|
|**1**|
|**1**|

which is more or less direct application of recursive formula. The n'th element
is the last element of vector A^n * v. Now we need also sum. Let us extend the
matrix A to calculate the sum as well. We store the sum in the last element of
vector. Matirx A is now:

|**0**|**1**|**0**|**0**|**0**|
|:--:|:--:| :--:| :--:|:--:|
|**0**|**0**|**1**|**0**|**0**|
|**0**|**0**|**0**|**1**|**0**|
|**1**|**2**|**3**|**4**|**0**|
|**1**|**2**|**3**|**4**|**1**|

and initial vector v:

|**1**|
|:--:|:
|**1**|
|**1**|
|**1**|
|**4**|

The n'th element and a sum are (A^n * v)[3] and (A^n * v)[4]. Now all we need to
do is to power matrix A efficiently modulo 10^9 which is easily implemented in
Python:

```python
def pow(M, p, modulus):
    if p == 1:
        return M
    if p % 2 != 0:
        return (M * pow(M, p - 1, modulus)) % modulus
    X = pow(M, p/2, modulus)
    return (X * X) % modulus 
```

Wrapping that all up we get [this](solve.py) scripts which allows us to get the 
flag: `CTF-BR{It-wAs-jUsT-a-ReCURsIVe-SequenCE-to-BE-coded-In-LOGN-XwmIBVyZ5QEC}`
