from collections import namedtuple


City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print('>>> tokyo\n', tokyo)
print('>>> tokyo.population\n', tokyo.population)
print('>>> tokyo.coordinates\n', tokyo.coordinates)

print('Named tuple attributes and methods:')
print('>>> City._fields\n', City._fields)  # _fields is a tuple with the field names of the class

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.61389, 77.208889))

# _make() allow you to instantiate a named tuple from an iterable; City(*delhi_data) would do the same
delhi = City._make(delhi_data)

# _asdict() returns a collections.OrderedDict built from the named tuple
# instance. That can be used to produce a nice display of city data.
print('>>> delhi._asdict()\n', delhi._asdict())

print(">>> key, value in delhi._asdict().items():\n\t\t print(key + ':', value)")
for key, value in delhi._asdict().items(): 
    print(key + ':', value)
