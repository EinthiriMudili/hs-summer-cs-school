import math


class Place:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def distance(self, other_place):
        # TODO
        dLat = (other_place.latitude - self.latitude) * math.pi / 180.0
        print("distance_latitude: " + str(dLat))
        dLon = (other_place.longitude - self.longitude) * math.pi / 180.0
        print("distance_longitude: " + str(dLon))
        self.latitude = self.latitude * math.pi / 180.0
        other_place.longitude = other_place.longitude * math.pi/180.0
        a = (pow(math.sin(dLat / 2), 2) +
             pow(math.sin(dLon / 2), 2) *
             math.cos(self.latitude) * math.cos(other_place.latitude));
        rad = 3961
        c = 2 * math.asin(math.sqrt(a))
        print("distance between self and other place in miles: " + str(rad*c))

    def __str__(self):
        return f'{self.latitude}, {self.longitude}'


class City(Place):
    def __init__(self, name, zipcode, latitude, longitude):
        self.name = name
        self.zipcode = zipcode
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f'{self.name} ({self.zipcode}) {self.latitude}, {self.longitude}'


class State:
    def __init__(self, name, cities):
        self.name = name
        self.cities = cities

    def __str__(self):
        str = self.name

        for city in self.cities:
            str = f'{str} \n {city.name} ({city.zipcode}) {city.latitude}, {city.longitude}'

        return str


franklin = Place(42.902, -87.972)
shorewood = Place(43.089, -87.887)

print("Franklin: " + str(franklin))
print("Shorewood: " + str(shorewood))

print(franklin.distance(shorewood))

milwaukee = City("Milwaukee", 53201, 87.9065, 43.0389)
chicago = City("Chicago", 60007, 87.6298, 41.8781)

print(milwaukee)
print(chicago)

wisconsin = State("Wisconsin", [milwaukee, chicago])
print(wisconsin)