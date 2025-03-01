import pandas as pd

data = pd.read_csv('Top Indian Places to Visit.csv')  

def rank_places(city_name):

    city_places = data[data['City'].str.contains(city_name, case=False, na=False)]
    
    if city_places.empty:
        return f"No places found for the city: {city_name}"
    
    city_places_sorted = city_places.sort_values(by=['Google review rating', 'time needed to visit in hrs'], ascending=[False, True])
    

    top_places = city_places_sorted.head(5)
    
    ranked_places = top_places[['Name', 'City', 'Google review rating', 'time needed to visit in hrs', 'Entrance Fee in INR', 'Number of google review in lakhs']]
    
    return ranked_places


city_name = input("Enter the city name: ")
result = rank_places(city_name)
print(result)
