text = "X-DSPAM-Confidence:    0.8475"

# Find the location of colon and get the substring having the nubmer
pos_dot = text.find(":")
num = text[pos_dot + 1 :]

#strip white space form both ends of the string
num = num.strip()
val = float(num)
print(val)