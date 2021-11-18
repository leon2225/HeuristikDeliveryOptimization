import matplotlib.pyplot as plt
import numpy as np
import math

points = np.array([[0.0086276, 0.2944565],[0.7387214, 0.4072671],[0.0878135, 0.2084033],[0.5727416, 0.0684485],[0.9035656, 0.9886895],
          [0.3906147, 0.4177884],[0.1604959, 0.5533878],[0.2001559, 0.8485555],[0.2769964, 0.0228912],[0.9303299, 0.1921670],
          [0.1678083, 0.8750068],[0.2404479, 0.0490358],[0.0789103, 0.5994416],[0.5337572, 0.3791154],[0.3825358, 0.1614337],
          [0.5151550, 0.5831543],[0.4225558, 0.2636385],[0.3836946, 0.5393434],[0.4930736, 0.3671721],[0.1948620, 0.0689326]])
X = [point[0] for point in points]
Y = [point[1] for point in points]
#plt.scatter(X,Y)
#plt.show()

# b) - calculate heatmap
def dist(x1, x2, y1, y2):
    return math.sqrt(((x1-x2)**2) + ((y1-y2)**2))
heatMap = []
steps = 100
for x in np.linspace(0,1,steps):  
    distanceCol = []
    for y in np.linspace(0,1,steps):
        distance = 0
        for point in points:
            distance += dist(point[0], x, point[1], y)
            #distance += np.linalg.norm(currentPoint - point)
            
        distanceCol.append(distance)
    heatMap.append(distanceCol)
    
fig = plt.figure()
ax = fig.add_subplot()
ax.pcolormesh(heatMap, cmap = 'plasma')
plt.title("Plot 2D array")
plt.show()

#d)
x,y = np.unravel_index(np.argmin(heatMap, axis=None), np.array(heatMap).shape)
print("Nile should build at x={} and y={}".format(x,y))
#x = 0.39; Y = 0.38

#e)
k_max = 100
N = len(X)

d_old = [(1 / N) * np.sum(X), (1 / N) * np.sum(Y)]
d = d_old

for k in range(k_max):
    
    for d_index in range(2):
        d[d_index] = np.sum([points[i][d_index] / dist(d_old[0], X[i], d_old[1], Y[i]) for i in range(N)]) / np.sum([ 1 / dist(d_old[0], X[i], d_old[1], Y[i]) for i in range(N)])

print(d)