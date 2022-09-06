import csv 
import matplotlib.pyplot as plt

weights = []
places = []
categories = []
scores = [[]]
totalgrades = []

with open('data.csv', 'r', newline='') as csvfile:
    rdr = csv.reader(csvfile, delimiter=',')
    array = list(rdr)
    categories = array[0]
    weights = array[1]
    places = array[2]
    scores = array[3:]

    print(' '.join(categories))
    print(' '.join(weights))
    print(' '.join(places))
    for x in scores:
        print(x)
    
    for i in range(len(places)):
        totalgrade = 0
        for j in range(len(weights)):
            totalgrade += float(weights[j]) * float(scores[i][j])
        print(places[i] + " " + str(totalgrade))
        totalgrades.append(totalgrade)

fig = plt.figure(figsize=(10,5))
plt.bar(places, totalgrades, color = 'blue', width = .4)

plt.xlabel("Place")
plt.ylabel("Grade")
plt.title("Overall Score")
plt.show()