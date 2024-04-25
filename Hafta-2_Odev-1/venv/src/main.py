import random
import math
def euclideanDistance(point:tuple, point2:tuple):
    x1,y1 = point[0],point[1]
    x2,y2 = point2[0],point2[1]
    distance = math.sqrt(math.abs(x1-x2)**2 + math.abs(y1-y2)**2)
    return distance

if __name__=="main":
    points=[]
    distances=[]
    for i in range(10):
        x=random.randint(0,100)
        y=random.randint(0,100)
        points.append((x,y))

    for i in range(10):
        temp = points[i]
        for j in range(10):
            if i==j:
                continue
            else:
                distance=euclideanDistance(temp,points[j])
                distances.append(distance)
    print(distances)

    