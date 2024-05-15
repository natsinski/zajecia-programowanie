vals_in_meters = [1, 2, 3 ,4 ,5]

def convert_to_centimeters(values):
    for x in values:
        print(x*100)

convert_to_centimeters(vals_in_meters)

x = map(lambda a: a*100, vals_in_meters)

print(list(x))
