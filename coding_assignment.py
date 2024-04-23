import requests
import json
import pandas as pd

def get_restaurant_data(postcode):

    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data['restaurants'])
    df_restaurants = df[['name', 'cuisines', 'rating', 'address']]
    df_restaurants['rating'] = df_filtered['rating'].apply(lambda x: x['starRating'])
    df_restaurants['cuisines'] = df_filtered['cuisines'].apply(lambda x: ', '.join(x))

    cuisines_list = [[item['name'] for item in x] for x in df_restaurants['cuisines']]

    # Flatten the list of lists
    flat_cuisines = [item for sublist in cuisines_list for item in sublist]

    # Remove duplicates
    unique_cuisines = list(set(flat_cuisines))

    non_cuisine_words = ['Freebies', 'Deals', 'Low Delivery Fee', 'Collect stamps', 'Local Legends']

    filtered_cusines = [word for word in unique_cuisines if word not in non_cuisine_words]

    df_restaurants['cuisines'] = df_filtered['cuisines'].apply(lambda x: ', '.join(x))


    return df_restaurants



