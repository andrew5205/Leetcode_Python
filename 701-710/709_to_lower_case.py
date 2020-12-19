# Implement function ToLowerCase() that has a string parameter str, 
# and returns the same string in lowercase.

# Example 1:

# Input: "Hello"
# Output: "hello"

# Example 2:
# Input: "here"
# Output: "here"

# Example 3:
# Input: "LOVELY"
# Output: "lovely"

# https://ss64.com/ascii.html



class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)
        # return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)
        # return ''.join([chr(ord(char)+32) if ord(char) in range(65,91) else char for char in str ])
        # return ''.join([ chr( ord(c)|32 ) for c in str ]) 


p = Solution()
print(p.toLowerCase("Hello"))
print(p.toLowerCase("here"))
print(p.toLowerCase("LOVELY"))



# python ord() returns an integer representing Unicode character

# python chr() method returns a character (a string) from an integer (represents unicode code point of the character







class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        for i in range(65, 91):
            if chr(i) in str:
                str = str.replace(chr(i), chr(i+32))
        return str
q = Solution()
print(q.toLowerCase("Hello"))
print(q.toLowerCase("here"))
print(q.toLowerCase("LOVELY"))







# Dec Hex     ascii   Dec Hex     ascii
# 65  0x41	A	    97  0x61	a
# 66  0x42	B	    98  0x62	b
# 67  0x43	C	    99  0x63	c
# 68  0x44	D	    100 0x64	d
# 69  0x45	E	    101 0x65	e
# 70  0x46	F	    102 0x66	f
# 71  0x47	G	    103 0x67	g
# 72  0x48	H	    104 0x68	h
# 73  0x49	I	    105 0x69	i
# 74  0x4A	J	    106 0x6A	j
# 75  0x4B	K	    107 0x6B	k
# 76  0x4C	L	    108 0x6C	l
# 77  0x4D	M	    109 0x6D	m
# 78  0x4E	N	    110 0x6E	n
# 79  0x4F	O	    111 0x6F	o
# 80  0x50	P	    112 0x70	p
# 81  0x51	Q	    113 0x71	q
# 82  0x52	R	    114 0x72	r
# 83  0x53	S	    115 0x73	s
# 84  0x54	T	    116 0x74	t
# 85  0x55	U	    117 0x75	u
# 86  0x56	V	    118 0x76	v
# 87  0x57	W	    119 0x77	w
# 88  0x58	X	    120 0x78	x
# 89  0x59	Y	    121 0x79	y
# 90  0x5A	Z	    122 0x7A	z


