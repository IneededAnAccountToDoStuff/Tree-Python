# Tree-Python
The Windows tree command re-implemented in Python. Allows for custom views that "ignore" certain folders/files.

## Why?
It can show hidden files.

I was trying to go through all the files in a directory, to pick out the ones I wanted to copy. I used the tree command to generate a text list of all the files and locations to sort through. I realised that I had no way of recreating the formatting, so if I took a directory out from the list, the formatting would be wrong. I chose to understand the way tree formatted the directory(+file) view. The best way to check my understanding was to re-implement it. I used Python for quick development. It bit me.

## What can you do with this?
You can generate new views similar to tree, but remove certain aspects of the output, and keep the proper formatting.

## Hasn't someone done this before? Aren't you reinventing the wheel?
1) Yeah, probably
2) Yes. I do that a lot.
