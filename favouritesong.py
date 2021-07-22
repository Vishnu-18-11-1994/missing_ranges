# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 17:29:33 2021

@author: user
"""

#name of the song
favourite_song="Despacito"

#artist of the song

artist="Luis Fonsi"

#year in which the song got released
year=2019

#duration of the song in second
duration_sec=281.0

#language of the song
language="spanish"

#genre of the song
genre="pop"

#producers and song writers for the song
producer,songwriter="Andres torres", "luis rodrigue"

''' despacito song become very famous and it got some
billion views in youtube'''

print(favourite_song)
print(artist)
print(year)
print(duration_sec)
print(language)
print(genre)
print(producer)
print(songwriter)

#functions
def favourite_song(name):
    name=name
    return name
song=favourite_song('despacito')
print(song)

def artist(name):
    artist_name=name
    return artist_name
singer=artist('Luis Fonsi')
print(singer)

def released_year(number):
    year=number
    return year
Year=released_year(2019)
print(Year)

def language_genre(language,genre):
    language1=language
    genre1=genre
    return language1, genre1 
    
Language_Genre2=language_genre("spanish","pop")
print(Language_Genre2)

def duration(seconds):
    if seconds==281:
        return True
    else:
        return False
song_duration=duration(281)
print(song_duration)