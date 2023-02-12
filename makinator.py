import numpy as np
import pandas as pd
import random

df = pd.read_csv("imdb_top_1000.csv")

df['Genre'] = df['Genre'].str.replace(' ', '')
encodedGenres = df['Genre'].str.get_dummies(sep = ',')
df.drop('Genre', inplace=True, axis=1)
genres = [f"Genre_{column}" for column in encodedGenres.columns]
df[genres] = encodedGenres

def minDistanceFromMidpoint(pairs):
  return min(pairs, key = lambda x: abs(x[1] - 0.5))

def questioning():
    actors = [(actor, len(df[(df['Star1'] == actor) | (df['Star2'] == actor) | (df['Star3'] == actor) | (df['Star4'] == actor)]) / len(df))
                for actor in pd.concat([df['Star1'], df['Star2'], df['Star3'], df['Star4']]).unique()]
    certificates = [(certificate, len(df[df['Certificate'] == certificate]) / len(df)) for certificate in df['Certificate'].unique()]
    directors = [(director, len(df[df['Director'] == director]) / len(df)) for director in df['Director'].unique()]
    genres = [(genre, df[genre].sum() / len(df)) for genre in [column for column in df if column.startswith('Genre_')]]

    featureProbabilities = []

    actor, probability = minDistanceFromMidpoint(actors)
    featureProbabilities.append(probability)

    certificate, probability = minDistanceFromMidpoint(certificates)
    featureProbabilities.append(probability)

    director, probability = minDistanceFromMidpoint(directors)
    featureProbabilities.append(probability)

    genre, probability = minDistanceFromMidpoint(genres)
    featureProbabilities.append(probability)

    questions = [f"Is {actor} in the movie?",
                 f"Is the movie rated {certificate}?",
                 f"Is {director} the director of the movie?",
                 f"Does {genre[6:]} describe your movie?"]
    
    question = questions[featureProbabilities.index(min(featureProbabilities, key = lambda x: abs(x - 0.5)))]

    index = questions.index(question)

    return index, question, actor, certificate, director, genre

actorsFound = 0
certificateFound = False
directorFound = False
genresFound = 0
questionsAsked = 0

while(df.shape[0] > 1):
    df = df.loc[:, (df != 0).any(axis=0)] # removes all columns that are entirely zeros

    index, question, actor, certificate, director, genre = questioning()

    if((actorsFound > 4 and index == 0) or (certificateFound and index == 1) or (directorFound and index == 2) or (genresFound > 3 and index == 3)):
        continue
    
    print(question)
    questionsAsked += 1
    user = input().lower()

    if(index == 0):
        if(user == "yes"):
            df = df[(df['Star1'] == actor) | (df['Star2'] == actor) | (df['Star3'] == actor) | (df['Star4'] == actor)]
            actorsFound += 1
        else:
            df = df[(df['Star1'] != actor) & (df['Star2'] != actor) & (df['Star3'] != actor) & (df['Star4'] != actor)]
    elif(index == 1):
        if(user == "yes"):
            df = df[df['Certificate'] == certificate]
            certificateFound = True
        else:
            df = df[df['Certificate'] != certificate]
    elif(index == 2):
        if(user == "yes"):
            df = df[df['Director'] == director]
            directorFound = True
        else:
            df = df[df['Director'] != director]
    elif(index == 3):
        if(user == "yes"):
            df = df[df[genre] == 1]
            genresFound += 1
        else:
            df = df[df[genre] != 1]
            df = df.drop(genre, axis=1)
    print(f"Possibilities left: {df.shape[0]}")
    print()

if df.empty:
    print("Movie does not exist.")
else:
    print (f"Is your movie called '{df['Series_Title'].iloc[0]}'?")

print(f"Took {questionsAsked} tries.")
