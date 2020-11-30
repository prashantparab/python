text = "X-DSPAM-Confidence:    0.8475";
netext  = text[text.find(':')+1:]
ntext = netext.strip()
val = float(ntext)
print(ntext)