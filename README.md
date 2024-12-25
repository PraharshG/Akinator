# Akinator: Guess Your Movie!

## Overview
**Makinator** is a Python-based interactive program that guesses a movie from the top 1000 IMDb movies based on user responses to a series of questions. It narrows down the possibilities using probabilities calculated from features such as actors, directors, genres, and certificates.

## Features
- Processes the IMDb Top 1000 movies dataset (`imdb_top_1000.csv`).
- Encodes genres into binary columns for efficient filtering.
- Asks intelligent questions to minimize the search space.
- Predicts the movie name based on user inputs.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/PraharshG/Akinator.git
   cd Akinator
   ```
2. Install the required Python packages:
   ```bash
   pip install pandas numpy
   ```
3. Ensure the dataset `imdb_top_1000.csv` is placed in the same directory as `akinator.py`.

> **Note**: The `.DS_Store` file is ignored and irrelevant to the program's functionality.

## Dataset
The program uses the IMDb Top 1000 movies dataset (`imdb_top_1000.csv`). Each movie entry contains:
- Title
- Certificate
- Genre(s)
- Star actors (up to 4)
- Director

The dataset must have these columns for the program to work correctly.

## How It Works

1. **Data Preprocessing**:
   - Removes spaces from genre names and encodes genres as binary columns.
   - Cleans the dataset by dropping irrelevant columns after filtering.

2. **Questioning Logic**:
   - Computes probabilities for each actor, certificate, director, and genre in the dataset.
   - Selects the feature closest to a 50% probability (midpoint) to ask the next question.

3. **Interactive Questions**:
   - Questions are dynamically generated to narrow down possibilities.
   - User answers "yes" or "no," and the dataset is filtered accordingly.

4. **Movie Guessing**:
   - Once the dataset is narrowed to a single movie, it guesses the movie title.

## Running the Program

1. Execute the script:
   ```bash
   python makinator.py
   ```
2. Follow the on-screen prompts:
   - Answer the questions with `yes` or `no`.
   - The program will indicate the remaining possibilities after each question.

## Example Interaction
```text
Is Robert De Niro in the movie?
yes
Possibilities left: 50

Is the movie rated PG-13?
no
Possibilities left: 25

Is Martin Scorsese the director of the movie?
yes
Possibilities left: 5

Does Drama describe your movie?
yes
Possibilities left: 1

Is your movie called 'Goodfellas'?

Took 4 tries.
```

## Customization
You can customize the following:
- Modify the dataset to include additional features.
- Adjust the questioning logic for more personalized recommendations.

## Dependencies
- Python 3.7+
- Pandas
- NumPy

## Contributions
Contributions are welcome! Please open an issue or submit a pull request for any feature requests or bug fixes.



