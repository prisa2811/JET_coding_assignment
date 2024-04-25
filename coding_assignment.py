import requests
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

def get_restaurant_data(postcode, no_of_restaurants):

    """
    Fetches restaurant data from the API based on the given postcode.

    Args:
    - postcode (str): The UK postcode to fetch restaurant data for.
    - no_of_restaurants (int): The number of restaurants to retrieve.

    Returns:
    - DataFrame: A DataFrame containing restaurant data.
    """

    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        data = response.json()
        df_restaurants = pd.DataFrame(data['restaurants'])
        df_restaurants = df_restaurants.head(no_of_restaurants)
        
        return df_restaurants
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None 


def processing_restaurant_data(df_restaurants):

    """
    Processes and filter the fetched restaurant data to remove unwanted data and format it accordingly.

    Args:
    - df_restaurants (DataFrame): DataFrame containing restaurant data.

    Returns:
    - DataFrame: Processed DataFrame with selected columns and modified data.
    """
    
    # Select specific columns from the DataFrame
    df_restaurants = df_restaurants[['name', 'cuisines', 'rating', 'address']]
    # Split the name to remove additional information
    df_restaurants['name'] = df_restaurants['name'].apply(lambda x: x.split('-')[0])
    # Extract the star rating from the 'rating' column
    df_restaurants['rating'] = df_restaurants['rating'].apply(lambda x: x['starRating'])
    # Remove non-cuisine words from the 'cuisines' column
    non_cuisine_words = ['Freebies', 'Deals', 'Cheeky Tuesday', 'Low Delivery Fee', 'Collect stamps', 'Local Legends']
    df_restaurants['cuisines'] = [[item['name'] for item in x if item['name'] not in non_cuisine_words] for x in df_restaurants['cuisines']]
    # Convert the list of cuisines to a comma-separated string
    df_restaurants['cuisines'] = df_restaurants['cuisines'].apply(lambda x: ', '.join(x))
    # Extract latitude and longitude coordinates from the 'address' column
    df_restaurants['lat_long'] = df_restaurants['address'].apply(lambda x: x['location']['coordinates'])
    # Format the 'address' column for display
    df_restaurants['address'] = [', '.join([item['firstLine'], item['city'], ' - '.join(['Postal code', item['postalCode']])]) for item in df_restaurants['address']]
    
    
    return df_restaurants



def display_restaurant_data(df_restaurants):
    
    """
    Displays the restaurant data in a formatted manner.

    Args:
    - df_restaurants (DataFrame): DataFrame containing restaurant data.
    """

    for index, restaurant in df_restaurants.iterrows():
        print(f"Restaurant {(index+1)}:")
        #print(restaurant.to_string())
        print(f"Name: {restaurant['name']}")
        print(f"Cuisines: {restaurant['cuisines']}")
        print(f"Rating: {restaurant['rating']}")
        print(f"Address: {restaurant['address']}")
        print(f"coordinates - {restaurant['lat_long']}")
        print()





def main():
    """
    Main function to execute the program.
    """
    postcode = input("Enter a UK postcode to fetch restaurant data: \n")
    no_of_restaurants = int(input('Number of restaurants data to be displayed ?\n'))

    restaurants = get_restaurant_data(postcode, no_of_restaurants)

    if restaurants is not None:
        restaurants = processing_restaurant_data(restaurants)
        display_restaurant_data(restaurants)
    else:
        print("An error occurred while fetching data. Please try again later.")

    

if __name__ == "__main__":
    main()


