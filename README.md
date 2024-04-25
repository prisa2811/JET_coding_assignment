# JET_coding_assignment

## Restaurant Data Display

This Python script retrieves restaurant data from the Just Eat API based on a UK postcode and displays it in a formatted manner. It limits the displayed data to the first N restaurants returned by the API.

## Instructions:

1. **Clone Repository**: Clone this repository to your local machine.
git clone https://github.com/prisa2811/JET_coding_assignment.git

2. **Navigate to Directory**: Navigate to the cloned directory.

4. **Run Script**: Run the Python script using the following command:
python coding_assignment.py

5. **Enter Postcode**: Enter a UK postcode when prompted to fetch restaurant data.

6. **Enter Number of Restaurants**: Enter the number of restaurants' data you want to be displayed.

7. **View Output**: View the displayed restaurant information in the console.

## Assumptions:
- Some names of the restaurants contains the location(for instance "subway - wales - UK"), these location details are removed from the names assuming they are already reflected in the address.
- Non cuisine words like 'Freebies', 'Deals', 'Cheeky Tuesday', 'Low Delivery Fee', 'Collect stamps', 'Local Legends' etc are removed from cuisines object as they are not suitable to be displayed under cuisines. 
- Only data from name object are considered and not the uniquename. 


## Potential Improvements:
- Error handling for invalid postcodes, number of restaurants or failed API requests.
- Implement a graphical user interface (GUI) for a more user-friendly experience.
- Understanding the requirements and use case of displaying the data and modifying the data to be displayed if something is missing.

## Dependencies:

- [requests](https://pypi.org/project/requests/): For making HTTP requests to the API.
- [pandas](https://pypi.org/project/pandas/): For data manipulation and analysis.
- [warnings](https://docs.python.org/3/library/warnings.html): For ignoring warnings.

## Addressed Improvements

- API error handling

## Author:

- [Lakshmi Narasimha Priyatham Kumanduri](https://github.com/prisa2811)

## License:
c645477