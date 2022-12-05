

txt = """1 2
2 1
3 3""" 
#a rock b paper c cissor
#x rock y paper z cissor
array = txt.split("\n")

print(array)

results = []
count = 0
for x in array:
        if x.isdigit():
            count += int(x)
        else:
            results.append(count)
            count = 0

results.sort()



print(69359 + 71144+72017)
