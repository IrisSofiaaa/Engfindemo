print("NOUN")
noun = d.dictionary.get(i)
try:
    trans = noun[2]
except IndexError:
    trans = noun[0]
except TypeError:
    trans = ""
if i.endswith("s"):
    trans = trans + "t"
print(trans)
mode = rest[i]
print(i, mode)

strip1 = strip[0]
strip2 = strip[1]
strip3 = strip[2]
strip4 = strip[3]
strip5 = strip[4]
strip6 = strip[5]

print(strip1, strip2, strip3, strip4, strip5, strip6)
sentence = " ".join([strip1, strip2, strip3, strip4, strip5, strip6])
for i in strip:
    t = d.dictionary.get(i)
    try:
        print(t[2])
    except IndexError:
        print(t[0])
    except TypeError:

        print("")

for i in sentence.split():

    if i == strip1:
        prev = "None"
    elif i == strip2:
        prev = strip1
    elif i == strip3:
        prev = strip2
    elif i == strip4:
        prev = strip3
    elif i == strip5:
        prev = strip4
    else:
        prev = strip5

    return prev
if i == "hers" or i == "his":
    trans = "hänen"
    print(trans)
elif i == "my" or i == "mine":
    trans = "minun"
    print(trans)
elif i == "theirs":
    trans = "heidän"
    print(trans)
elif i == "our":
    trans = "meidän"
    print(trans)
elif i == "yours":
    trans = "sinun"
    print(trans)
if prev == "to" or prev == "into":
    trans = trans + "een"
    print(trans)
elif prev == "in":
    trans = trans + "ssa"
    print(trans)
elif prev == "for":
    trans = trans + "lle"
    print(trans)
elif prev == "at":
    trans = trans + "ssa"
    print(trans)
else:
    pass
