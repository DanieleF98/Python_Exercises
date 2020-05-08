text = "X-DSPAM-Confidence:    0.8475";
ipos = text.rfind(" ")
ntext = text[ipos+1:]
fnum = float(ntext)
print(fnum)

text = "X-DSPAM-Confidence:    0.8475";
ipos = text.find(":")
ntext = text[ipos+1:]
fnum = float(ntext.lstrip())
print(fnum)
