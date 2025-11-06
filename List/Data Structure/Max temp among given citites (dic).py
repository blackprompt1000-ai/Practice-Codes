# program to print the city with the highest temperature taken in the dictionary
city = {"Bombay": 48, "Delhi": 45, "Chennai": 50, "Bangalore": -23}
max_city = max(city, key=city.get)
print(f"City with highest temperature is {max_city} with temperature {city[max_city]}")