# JET_coding_assignment

# Restaurant Data Display

## Instructions:
1. Install Python if not already installed.
2. Clone this repository.
3. Navigate to the cloned directory.
4. Ensure the libraries required (pandas, warnings, requests) are already installed.
5. Run the script using the following command: python coding_assignment.py
6. Enter a UK postcode and number of restaurants data to be displayed when prompted to fetch restaurant data.
7. View the displayed restaurant information.

## Assumptions:
- Some names of the restaurants contains the location(for instance "subway - wales - UK"), these location details are removed from the names assuming they are reflected in the        address.
- Non cuisine words like 'Freebies', 'Deals', 'Cheeky Tuesday', 'Low Delivery Fee', 'Collect stamps', 'Local Legends' etc are removed from cuisines object as they are not suitable to be displayed under cuisines.
- Only data from name object are considered and not the uniquename. 
- Assumes the user is familiar with running Python scripts from the command line.

## Potential Improvements:
- Error handling for invalid postcodes, number of restaurants or failed API requests.
- Implement a graphical user interface (GUI) for a more user-friendly experience.
- Understanding the requirements and use case of displaying the data and modifying the displayed data if something is missing.
