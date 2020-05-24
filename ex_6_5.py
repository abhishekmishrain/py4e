text = "X-DSPAM-Confidence:    0.8475";

dotpos = text.find('.')
num = float(text[dotpos-1:])
print(num)
