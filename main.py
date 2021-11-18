import matplotlib.pyplot as plt
import numpy as np

points = np.array([[0.0086276, 0.2944565],[0.7387214, 0.4072671],[0.0878135, 0.2084033],[0.5727416, 0.0684485],[0.9035656, 0.9886895],
          [0.3906147, 0.4177884],[0.1604959, 0.5533878],[0.2001559, 0.8485555],[0.2769964, 0.0228912],[0.9303299, 0.1921670],
          [0.1678083, 0.8750068],[0.2404479, 0.0490358],[0.0789103, 0.5994416],[0.5337572, 0.3791154],[0.3825358, 0.1614337],
          [0.5151550, 0.5831543],[0.4225558, 0.2636385],[0.3836946, 0.5393434],[0.4930736, 0.3671721],[0.1948620, 0.0689326]])
X = [point[0] for point in points]
Y = [point[1] for point in points]
#plt.scatter(X,Y)
#plt.show()

# b) - calculate heatmap
heatMap = [[],[],[]]
steps = 5
for x in np.linspace(0,1,steps):  
    for y in np.linspace(0,1,steps):
        distance = 0
        currentPoint = np.array([x,y])
        for point in points:
            distance += np.linalg.norm(currentPoint - point)
            
        heatMap[0].append(x)
        heatMap[1].append(y)
        heatMap[2].append(distance)
    
X = np.array(heatMap[0])
Y = np.array(heatMap[1])
Z = np.array(heatMap[2])
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(X,Y,Z)
plt.show()

