
#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.

#first method:
text = "X-DSPAM-Confidence:    0.8475";

#with the .rfind() method we search from the right to the left, with this instruction we search for the last whitespace in the line
ipos = text.rfind(" ")

#now we get and print the number, we need to do ipos+1 to slice the string skipping the first blankspace  
ntext = text[ipos+1:]
fnum = float(ntext)
print(fnum)

#second method:
text = "X-DSPAM-Confidence:    0.8475";

#here we search from the left for the first occurrence of :
ipos = text.find(":")
ntext = text[ipos+1:]

#by doing ntext.lstrip() we cancel all the blankspaces that are present on the left side of the number 
fnum = float(ntext.lstrip())
print(fnum)
