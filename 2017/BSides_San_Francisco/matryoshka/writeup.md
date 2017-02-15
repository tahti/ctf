* Task matryoshka (666)
** Description
After a lecture on files and the structure of the file system, William James was accosted by a little old lady.

"Your theory that the file system is the primary unit of storage has a very convincing ring to it, Mr. James, but it's wrong. I've got a better theory," said the little old lady.

"And what is that, madam?" Inquired James politely.

"That every file we create is just inside of an archive,"

Not wishing to demolish this absurd little theory by bringing to bear the masses of computer scientific evidence he had at his command, James decided to gently dissuade his opponent by making her see some of the inadequacies of her position.

"If your theory is correct, madam," he asked, "what is this archive stored in?"

"You're a very clever man, Mr. James, and that's a very good question," replied the little old lady, "but I have an answer to it. And it is this: The first archive is stored in a second, far larger, archive."

"But what is this second archive stored in?" persisted James patiently.

To this the little old lady crowed triumphantly. "It's no use, Mr. James – it's archives all the way down."

Note: Flag does not follow the "Flag:" format but is recognizable

    file.bin *

** Solution
file.bin appears to be file pack multiple times. Here is the list of packers used:

Format         Notes
 - zip
 - rar
 - zip
 - compress
 - tar         - file command reports gzip for some reason
 - rar multivolume
 - WIM         - use 7z
 - DCT         - use Dynamic Adaptive Compression Tool by Roy Keen
 - cpio
 - F (frozen)  - use freeze
 - xar
 - lz4
 - cpio
 - 7z
 - BinHex
 - Windows cabinet
 - suffit
 - lzip
 - bzip2
 - HFS 
 - arj
 - tar
 - Parity Archive Volume Set
 - zoo
 - xz
 - lzop
 - arc
 - LHarc
 - ACE        - I had to DOS version.
 - squashfs
 - zpaq       - Linux version did not work for me 
 - ar
 - cpio

Finally we get flac file. Opening file in audacity we can see not that long
sound with 1Hz! frequency.
I tried saving file using different wav formats to see if I get anything
sensible. When I saved using Unsigned 8-bit PCM I got bunch of dots dashes and
commas with some 0x1F bytes in the mix. This steered me towards the Morse code.
But I could not make any way to make it sensible conversion until (inpired by
looking at the contents of flac file) I used libFLAC library. I had to convert it
using Audacity first but the result was sequence of bytes 0xae, 0xad, 0xa0.
Changing 0xae to -, 0xa0 to space and  0xad to . we get the following in morse
code:
.. - ... - .... . .. -. -.-. .-. . -.. .. -... .-.. . ... .... .-. .. -. -.- .. -. --. -- --- .-. ... . -.-. --- -.. .
itstheincredibleshrinkingmorsecode
