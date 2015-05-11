import sys

# our original alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
a_position = ord('a')
z_position = ord('z')
# all the rotations!
rotalphas = []
# try all offsets
for i in range(26):
    rotalpha = []
    for a in alphabet:
        # if the rotation is "less than or equal to z", we don't have to wrap around
        if ord(a) + i <= z_position:
            rotalpha.append(chr(ord(a) + i))
        # this does the mod function to "wrap around" back to a, b, c, ...
        else:
            rotalpha.append(chr(((ord(a) + i) % (z_position + 1)) + a_position))
    # add each new alphabet to the master list
    rotalphas.append(rotalpha)
        
# these are all the possible mappings
ciphers = []
for bet in rotalphas:
    cipher = {}
    string = "".join(bet)
    # mapping the letter to its rotated form
    for a in xrange(len(alphabet)):
        cipher[alphabet[a]] = string[a]
    ciphers.append(cipher)

# get input from the usser
input_string = sys.argv[1].lower()

# holds the possible solutions
deciphered_text = []
# test each of our ciphers to see which works
for test in ciphers:
    for c in input_string:
        # we only translate letters
        if c in alphabet:
            deciphered_text.append(test[c])
        else:
            deciphered_text.append(c)
    # separate each "attempt"
    deciphered_text.append("\n")
          
deciphered_text = "".join(deciphered_text)
attempts = deciphered_text.split("\n")

# now weed out the ones that are bad using a wordlist
good_attempts = []
with open('wordlist.txt', 'rb') as words:
    lines = words.read().splitlines()
    for a in attempts:
        tokens = a.split(" ")
        for t in tokens:
            # we check to see if each word is a real dictionary word
            # if it is, then we add it to our "good" pile
            if t in lines:
                if a not in good_attempts:
                    good_attempts.append(a)

print "\nperhaps one of these?"
print "---------------------\n"
for g in good_attempts:
    print g
print "\n"
