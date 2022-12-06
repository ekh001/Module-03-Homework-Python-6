# places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

# print("Original list is: " + str(places))

# places = list(filter(None, places))
# print(places)
# strip method - strip the list!

# new_places_lambda = list(filter(lambda place: place.strip(' '), places))



# print(new_places_lambda)

def liz_range(stop, start, step = 1):
    while start < stop:
        yield start
        start += step

for i in liz_range(0, start = 10):
    liz_generator_value = i
    print(liz_generator_value)