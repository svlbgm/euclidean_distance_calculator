# Function to calculate Euclidean Distance#

import math

# Pick the number of points to be added (1-5)
while True:
    try:
        n = int(input("Number of points you would like to add? Between(1-5)\n: "))
        if 1 <= n <= 5:
            break
    except ValueError:
        print("Invalid input please enter a valid integer between 1 and 5.")

# Creating a list that includes the points
points = []

# Enter the coordinates of the points, raise an error if input is wrong
for i in range(n):
    while True:
        try:
            x, y = map(float, input(f"Enter {i + 1}. (x,y) coordinates with a blank in between: ").split())
            if len([x, y]) != 2:
              raise ValueError("Please enter exactly two values separated by a space.")
            points.append((x, y))
            break
        except ValueError as e:
            print(f"Invalid Input : {e}. Please enter coordinates as two numbers separated by a space.")


# Empty list to store distances after
distances = []

# Euclidean Distance Formula
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

# Calculate the Distances
for i in range(len(points)):
    for j in range(i + 1 , len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Find the minimum distance
min_distance = min(distances)
print(f"Minimum Öklid mesafesi: {min_distance}")







