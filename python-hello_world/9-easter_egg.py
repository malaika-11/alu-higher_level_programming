#!/usr/bin/python3
import this

zen = this.s.encode('utf-8')   # get the encoded string
import codecs
text = codecs.decode(zen, 'rot_13')  # decode it
print(text, end="")  # print without adding a final newline
