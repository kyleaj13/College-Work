distance = input("What distance are you travelling in miles? ")
distance = int(distance)
if distance < 3:
    transportation = "Walking"
elif distance < 300:
    transportation = "Driving"
else:
    transportation = "Flying"
print("I suggest {} to your destination.".format(transportation))
