distances = [327, 132, 22.3, 169,61.8, 216, 42.2, 155, 129, 382, 390, 275, 508, 390, 242, 314, 498, 728, 576, 327, 427, 57.6, 28.2, 323]
maxdist = 2280
line = ''
for x in range(len(distances)):
    line += "{:.1f}".format(round((10 - ((distances[x] / maxdist) * 10)), 1))
    line += ","

print(line[:-1])
