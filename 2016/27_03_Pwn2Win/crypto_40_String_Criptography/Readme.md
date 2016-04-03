# String Criptography (CRYPTO, 40p)

## Description:
Analyze the samples below, obtained by intercepting some Club communications,
in order to understand the logic behind the codification/generation of
the strings. Then, access the address below and decode the 10 words
which will be provided. Learning how to decode this will be useful
again later!


Samples we obtained:
> "Flow" -> Original string (plaintext) -> Codified string  
> [5, 0, 8, 3, 4, 9, 6, 2, 7, 1] -> aDuLteRInE -> iKbTcfTKqI  
> [1, 3, 6, 4, 9, 2, 7, 0, 8, 5] -> aboMINAblE -> igvNRVEdqI  
> [0, 9, 2, 8, 4, 7, 5, 1, 6, 3] -> ACIdophiLS -> JHQjvwkmPS  
> [5, 6, 9, 1, 3, 8, 2, 4, 7, 0] -> hypOCOtYLs -> mhtPJOcCNy  
> [9, 7, 6, 3, 4, 0, 5, 8, 1, 2] -> fuRcATIOns -> kcAiATLXou  
> [6, 0, 1, 2, 8, 7, 9, 4, 5, 3] -> ACeTaNiLid -> BCmYfRiTpk  
> [8, 0, 4, 5, 2, 7, 3, 6, 1, 9] -> FURriErIes -> JAYynIsKet  
> [9, 1, 8, 3, 6, 7, 0, 2, 5, 4] -> KidnAPPeRs -> MrivJRWkUw  
> [0, 5, 2, 9, 1, 6, 8, 4, 7, 3] -> GarmeNTiNG -> LjatlNBmRI


We already discovered some properties of the codification by carrying a fast
cryptanalysis which might be helpful:


>   "0" is the string's initial position  
>   Periodic boundary condition  
>   Case sensitive codification


Format of the result expected by the server: word1,word2,word3,...


>nc pool.pwn2win.party 4040


## Solution

We are given sequence of digits from 0 to 9 and string of length 10. We should
encode it according to the secret algorithm. 

Looking at the samples we can see immediately that the case of letters before
and after encryption is the same. Another observation is that array numbers from
0 to 9 can represent a permutation.

Let us write a difference between corresponding letters (modulo numbers of
letters in alphabet) in encrypted and plain strings together with key array:

> plain = "aboMINAblE"  
> encrypted = "igvNRVEdqI"  
> just sequence [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
> difference    [8, 5, 7, 1, 9, 8, 4, 2, 5, 4]  
> key           [1, 3, 6, 4, 9, 2, 7, 0, 8, 5]  
> direction     [>, <, >, <, >, <, >, <, >, <]  

Lets look at position 0. The 8 is right of 0 in the key and difference is 8 at position 0.  
Lets look at position 1. The 5 is left of 1 in the key and difference is 5 at position 1.  
Lets look at position 2. The 7 is right of 2 in the key and difference is 7 at position 2.  

Noticing the above pattern it is easy to find the encryption and decryption method. The solution
written in Python is [here](solve.py).   
The flag: `CTF-BR{This_encryption_is_crazy_bro!_Thinking_different...}`


