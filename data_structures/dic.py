#do not allowed  duplicates, ordered, changeable
carDetails = {
    "brand": "Ford",
    "model" : "Mustang",
    "year" : 1964
}
# carDetails["brand"] = "tesla"
# carDetails["color"] = "Black"
# print(carDetails["brand"])
# print(carDetails.keys())
# print(carDetails.values())
# print(carDetails.get("model"))

# carDetails.pop("brand")
# carDetails.popitem()
# print(carDetails)

#printing key and value using loop
for x, y in carDetails.items():
    print(x, y)


#printing value usng loop
for x in carDetails.values():
    print(x)