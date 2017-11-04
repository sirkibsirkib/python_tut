"""
TODO
"""
lb_per_kg = 2.204
km_per_mi = 1.6
print('Input your value:')
string_value = input()
value = float(string_value)
print('Input your unit:')
unit = input()

if unit == 'kg':
    print(str(value*lb_per_kg) + ' lb')
elif unit == 'lb':
    print(str(value/lb_per_kg) + ' kg')
elif unit == 'mi':
    print(str(value*km_per_mi) + ' km')
elif unit == 'km':
    print(str(value/km_per_mi) + ' mi')
else:
    print('Unknown unit!')
