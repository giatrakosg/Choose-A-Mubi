# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 08:44:48 2020

@author: jacka
"""

import random
import requests
import csv

from bs4 import BeautifulSoup

url = 'https://mubi.com/showing'
currentFilms = []

def getCurrentFilms():
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    headers = soup.find_all('h2')
    
    for header in headers:
        titles = header.contents[0]
        currentFilms.append(titles)
        
        
    del currentFilms[-1] #Delete the film from the previous day    
    return currentFilms


def chooseAFilm(currentFilms):
    randomMovie = random.choice(currentFilms)
    chosenFilm = str(randomMovie)
    return chosenFilm


def getWatchedFilms():
    with open('FilmList.csv', newline='') as f:
        reader = csv.reader(f)
        filmTracking = list(reader)
        flatList = []
        # Quick fix here to convert list of lists into flat list
        for sublist in filmTracking:
            for item in sublist:
                flatList.append(item)
        return flatList           


if __name__ == '__main__':
    # Get the current list of films
    getCurrentFilms()
    while True:
        chosenFilm = chooseAFilm(currentFilms)
        # Get the list of previously watched films as a flat list
        filmList = getWatchedFilms()
        if chosenFilm not in filmList:
                filmList.append(chosenFilm)
                with open('FilmList.csv', 'a', newline='') as fp:
                    a = csv.writer(fp)
                    a.writerow([chosenFilm])
                    print("Your mubi choice: ", chosenFilm)
                    break
