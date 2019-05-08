#change lat,lon to radians
from math import radians, sin, cos, sqrt, asin

#INPUT two tuples that have lat, lon values
#RETURN distance in miles
def hd(loc1,loc2):
    latD = radians((loc2[0]-loc1[0])/2)
    lonD = radians((loc2[1]-loc1[1])/2)
    d0 = sin(latD)**2 + cos(radians(loc1[0]))*cos(radians(loc2[0]))*(sin(lonD)**2)
    d1 = 2 * r * asin(d0**(1/2))
    return d1


def dd(loc1,loc2):
    lat1,lon1 = loc1
    lat2,lon2 = loc2
    x = lat1 - lat2
    y = (lon1 - lon2)*cos(radians(lat2))
    return 69.385*sqrt(x**2 + y**2)

def eu_distance(loc1,loc2):
    return sqrt(sum([(i-j)**2 for i,j in zip(loc1,loc2)]))

#Lindley Hall where we have C200
l1 = (39.165341,-86.523588)

#Luddy Hall the new SICE building
l2 = (39.172725,-86.523295)

#Distance between Lindley and Luddy
print(hd(l1,l2))
print(eu_distance(l1,l2))
print(dd(l1,l2))