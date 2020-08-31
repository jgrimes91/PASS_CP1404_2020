city_to_postcode = {"Cairns": 4870, "Townsville": 4810, "Mackay": 4740}
print("Brisbane" in city_to_postcode)
city_to_postcode["Brisbane"] = 4000
print(city_to_postcode["Cairns"])

for key, value in city_to_postcode.items():
    print(key + "'s postcode is {}".format(value))

nsw_city_to_postcode = {"Tamworth": 2340, "Sydney": 2000, "Dubbo": 2830}
city_to_postcode.update(nsw_city_to_postcode)
print(city_to_postcode)
print(city_to_postcode.pop("Sydney"))
print(city_to_postcode.keys())
print(city_to_postcode)
