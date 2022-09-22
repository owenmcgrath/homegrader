import csv 
import matplotlib.pyplot as plt
import numpy as np

weights = []
places = []
categories = []
scores = []
strscores =[[]]
totalgrades = []

with open('data.csv', 'r', newline='') as csvfile:
    rdr = csv.reader(csvfile, delimiter=',')
    array = list(rdr)
    categories = array[0]
    weights = array[1]
    places = array[2]
    strscores = array[3:]

    print(' '.join(categories))
    print(' '.join(weights))
    print(' '.join(places))
    print(len(places))
    for x in strscores:
        print(len(x))
    
    # for i in range(len(places)):
    #     totalgrade = 0
    #     for j in range(len(weights)):
    #         totalgrade += float(weights[j]) * float(scores[j][i])
    #     print(places[i] + " " + str(totalgrade))
    #     totalgrades.append(totalgrade)

new = []
for j in range(len(weights)):
    for i in range(len(places)):
        new.append(float(strscores[j][i]) * float(weights[j]))
    scores.append(new)
    print(scores[j])
    new = []

fig, ax = plt.subplots()

arr0 = np.array(scores[0])
arr1 = np.array(scores[1])
arr2 = np.array(scores[2])
arr3 = np.array(scores[3])


ax.bar(places, arr0, .4, label = categories[0])
ax.bar(places, arr1, .4, label = categories[1], bottom=arr0)
ax.bar(places, arr2, .4, label = categories[2], bottom=arr0+arr1)
ax.bar(places, arr3, .4, label = categories[3], bottom=arr0+arr1+arr2)
ax.legend(categories)
ax.set_xlabel("Place")
ax.set_ylabel("Grade")
ax.set_title("Overall Score")

for bars in ax.containers:
    ax.bar_label(bars)

plt.legend(bbox_to_anchor=(1.02,.9), loc="upper left", borderaxespad=0)
plt.setp(ax.get_xticklabels(), rotation=15, horizontalalignment='right')
plt.show()