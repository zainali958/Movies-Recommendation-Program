# Movies-Recommendation-Program
This is the program that to recommend movies.
Overview
This project provides a simple script to recommend movies based on a user's favorite genre. It processes data from a JSON file containing movie information and outputs a list of recommendations.

Files
1. movies.json
Description: Contains movie data in JSON format.
Structure: Each entry in the file includes:
title: The name of the movie.
genre: A list of genres associated with the movie.
rating: IMDb rating of the movie.
director: Name of the movie's director.
Example:
json
Copy code
[
    {
        "title": "Inception",
        "genre": ["Sci-fi", "Thriller"],
        "rating": 8.8,
        "director": "Christopher Nolan"
    }
]
2. Code For MR.py
Description: A Python script that recommends movies based on a user-specified genre.
Workflow:
Reads the movies.json file.
Converts the data into a pandas DataFrame for processing.
Prompts the user to input their favorite genre.
Filters and displays movies that match the selected genre.
Usage: Run the script in a Python environment:
bash
Copy code
python Code\ For\ MR.py
Example interaction:
plaintext
Copy code
Enter your favorite genre: Drama
Recommended movies based on your favorite genre:
The Shawshank Redemption
The GodFather
Schindler's List
Pulp Fiction
Requirements
Python 3.x
Dependencies:
pandas
json
Setup Instructions
Install the required dependencies:
bash
Copy code
pip install pandas
Ensure both movies.json and Code For MR.py are in the same directory.
Run the Python script as described above.
Customization
You can extend the functionality of the script to:

Recommend movies based on other criteria like rating or director.
Save the filtered recommendations to a file.
