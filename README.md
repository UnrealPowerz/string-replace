# string-replace
This is a small tool that allows you to replace strings in a binary file.  
It is mainly useful for working with 'strange' encodings like shiftjis,  
which are particularly painful to work with using a hex editor.

## Getting started

### Retrieving the strings
Find out the general range of the file which contains text and  
which encoding it uses. Then execute the following.

```
python string-finder.py FILE START END ENCODING
```

So for example:

```
python binary.bin 0x100 0x200 shiftjis
```
   
This will create a file `strings.txt` which contains all the  
valid strings it found in that file from offset 0x100 to 0x200.  
For a list of valid encodings, click [here](https://docs.python.org/3.7/library/codecs.html#standard-encodings).
 
### Editing the strings
The `strings.txt` file you created will contain stuff like

```
# "This is some text"
#@209096-23=
```

meaning that it found the string "This is some text"  
at offset 209096 and the replacement text can be up to 23 bytes long.  
Editing the text is done by removing the # in front of the @ and  
typing the replacement after the =.

So for example

```
# "This is some text"
@209096-23=This is the replacement
```

**IMPORTANT**: Do NOT change anything that does not look like  
valid text, it probably is not text at all and you might   
be changing (and possibly corrupting) unrelated things.

When you are done, run the following to do the modifications

```
python string-replace.py FILE STRINGS_FILE
```

So for example

```
python string-replace.py binary.bin strings.txt
```

This will overwrite `binary.bin`, so create a backup.
