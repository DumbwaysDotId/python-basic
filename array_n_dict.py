# Dict
fruits = [
    {'id': 1, 'name': "Apple",}, #0
    {'id': 2, 'name': "Grape"}, #1
]

x = []
y = []
# 1. start looping fruits
for f in fruits:
    x.append(f['id'])
    y.append(f['name'])
# eof 1

print(x)
print(y)


# Looping standard bingits

# # javascript
# for(i=0;i<10;i++){
#
# }

#python
for i in range(1, 10):
    print(i)

coffees = [
    "cappucino",
    "expresso",
    "machiato"
]
for coffee in coffees:
    print(coffee)
