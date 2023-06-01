# -*- coding: utf-8 -*-
"""

Spyder Editor


This is a temporary script file.
"""
# -*- coding: utf-8 -*-

import csv

#This function reads the input file and returns a nested dictionary having all the relevant music features associated with each music
def build_music_features():
    file=open("data1.csv","r",encoding = 'ISO-8859-1')
    file_read = csv.DictReader(file)
    Music_features = {}
    for line in file_read:

        (Music_name, Accousticeness, Danceability, Energy, Liveness, Loudness, Popularity, Speechiness, Tempo, Valence) = line["name"],line["acousticness"], line["danceability"], line["energy"],line["liveness"],line["loudness"], line["popularity"], line["speechiness"],line["tempo"], line["valence"]

        Music_features.setdefault(str(Music_name), {})
 #       print(line["artists"])
        if len(str(Accousticeness)) != 0:
            Music_features[Music_name]['Accousticeness'] = float(str(Accousticeness))
        else:
            Music_features[Music_name]['Accousticeness'] = 0
        if len(str(Danceability)) !=0:
            Music_features[Music_name]['Danceability'] = float(str(Danceability))
        else:
            Music_features[Music_name]['Danceability'] = 0
        if len(str(Energy)) != 0:
            Music_features[Music_name]['Energy'] = float(str(Energy))
        else:
            Music_features[Music_name]['Energy'] = 0
        if len(str(Liveness)) != 0:
            Music_features[Music_name]['Liveness'] = float(str(Liveness))
        else:
            Music_features[Music_name]['Liveness'] = 0
        if len(str(Loudness)) != 0:
            Music_features[Music_name]['Loudness'] = float(str(Loudness))
        else:
            Music_features[Music_name]['Loudness'] = 0
        if len(str(Popularity)) != 0:
            Music_features[Music_name]['Popularity'] = float(str(Popularity))
        else:
            Music_features[Music_name]['Popularity'] = 0
        if len(str(Speechiness)) !=0:
            Music_features[Music_name]['Speechiness'] = float(str(Speechiness))
        else:
            Music_features[Music_name]['Speechiness'] = 0
        if len(str(Tempo)) !=0:
            Music_features[Music_name]['Tempo'] = float(str(Tempo))
        else:
            Music_features[Music_name]['Tempo'] = 0
        if len(str(Valence)) != 0:
            Music_features[Music_name]['Valence'] = float(str(Valence))
        else:
            Music_features[Music_name]['Valence'] = 0
    
    file.close()
    return(Music_features)


#this function reads the data file and generates artist music dictionary. 
#The dictionary has artist name as key and all the music composed by the artist in a list as the element
def build_artist_music():
    file=open("data1.csv","r",encoding = 'ISO-8859-1')
    file_read = csv.DictReader(file)
    Artist_music = {}
    bad_Chars = ['[', ']', ',', "'"]

    for line in file_read:
   #     print(line["artists"])
    #    print(line["name"])
        #Code to extract each artist from the "artist" field in the input file (There are multiple artists in some of the rows) and write to a dictionary
        for x in line["artists"].split(','):
            for i in bad_Chars:
                x=x.replace(i,'')
   #     print(x)
            y=x.strip()
   #     print (y)
 #       Artist_music[y] = str(line["name"])
        
        
            if y not in Artist_music.keys():
                Artist_music[y] = list()
                Artist_music[y].append(str(line["name"]))
            else:
                Artist_music[y].append(str(line["name"]))
 
    file.close()    
    return(Artist_music)
 

#This function has 2 artists, artist music dictionary and music features dictionary as input.
#returns the dictionary having each of the 2 artists as keys and for each artist, the average of each music feature of all the musics composed by each of the artist

def build_artist_music_features (artist1, artist2,Artist_music, Music_features):
    artist_music_features = {}
    artist_music_features.setdefault(str(artist1), {})
    count = 0
    for music in Artist_music[artist1]:
      #  print (music)
        count = count + 1
        if count ==1:
            artist_music_features[artist1]['Accousticeness'] = Music_features[music]['Accousticeness']
        else:
            artist_music_features[artist1]['Accousticeness'] = artist_music_features[artist1]['Accousticeness'] + Music_features[music]['Accousticeness']
        if count ==1:
            artist_music_features[artist1]['Danceability'] = Music_features[music]['Danceability']
        else:
            artist_music_features[artist1]['Danceability'] = artist_music_features[artist1]['Danceability'] + Music_features[music]['Danceability']
        
        if count ==1:
            artist_music_features[artist1]['Energy'] = Music_features[music]['Energy']
        else:
            artist_music_features[artist1]['Energy'] = artist_music_features[artist1]['Energy'] + Music_features[music]['Energy']
        if count ==1:
            artist_music_features[artist1]['Liveness'] = Music_features[music]['Liveness']
        else:
            artist_music_features[artist1]['Liveness'] = artist_music_features[artist1]['Liveness'] + Music_features[music]['Liveness']
        if count ==1:
            artist_music_features[artist1]['Loudness'] = Music_features[music]['Loudness']
        else:
            artist_music_features[artist1]['Loudness'] = artist_music_features[artist1]['Loudness'] + Music_features[music]['Loudness']
        if count ==1:
            artist_music_features[artist1]['Popularity'] = Music_features[music]['Popularity']
        else:
            artist_music_features[artist1]['Popularity'] = artist_music_features[artist1]['Popularity'] + Music_features[music]['Popularity']
        if count ==1:
            artist_music_features[artist1]['Speechiness'] = Music_features[music]['Speechiness']
        else:
            artist_music_features[artist1]['Speechiness'] = artist_music_features[artist1]['Speechiness'] + Music_features[music]['Speechiness']
        if count ==1:
            artist_music_features[artist1]['Tempo'] = Music_features[music]['Tempo']
        else:
            artist_music_features[artist1]['Tempo'] = artist_music_features[artist1]['Tempo'] + Music_features[music]['Tempo']
        if count ==1:
            artist_music_features[artist1]['Valence'] = Music_features[music]['Valence']
        else:
            artist_music_features[artist1]['Valence'] = artist_music_features[artist1]['Valence'] + Music_features[music]['Valence']
        #print (artist_music_features[artist1]['Accousticeness'])

    artist_music_features[artist1]['Accousticeness'] = artist_music_features[artist1]['Accousticeness']/count
    artist_music_features[artist1]['Danceability'] = artist_music_features[artist1]['Danceability']/count
    artist_music_features[artist1]['Energy'] = artist_music_features[artist1]['Energy']/count
    artist_music_features[artist1]['Liveness'] = artist_music_features[artist1]['Liveness']/count
    artist_music_features[artist1]['Loudness'] = artist_music_features[artist1]['Loudness']/count
    artist_music_features[artist1]['Popularity'] = artist_music_features[artist1]['Popularity']/count
    artist_music_features[artist1]['Speechiness'] = artist_music_features[artist1]['Speechiness']/count
    artist_music_features[artist1]['Tempo'] = artist_music_features[artist1]['Tempo']/count
    artist_music_features[artist1]['Valence'] = artist_music_features[artist1]['Valence']/count

    artist_music_features.setdefault(str(artist2), {})
    count = 0
    for music in Artist_music[artist2]:
  #      print (music)
        count = count + 1
        if count ==1:
            artist_music_features[artist2]['Accousticeness'] = Music_features[music]['Accousticeness']
        else:
            artist_music_features[artist2]['Accousticeness'] = artist_music_features[artist2]['Accousticeness'] + Music_features[music]['Accousticeness']
        if count ==1:
            artist_music_features[artist2]['Danceability'] = Music_features[music]['Danceability']
        else:
            artist_music_features[artist2]['Danceability'] = artist_music_features[artist2]['Danceability'] + Music_features[music]['Danceability']
        
        if count ==1:
            artist_music_features[artist2]['Energy'] = Music_features[music]['Energy']
        else:
            artist_music_features[artist2]['Energy'] = artist_music_features[artist2]['Energy'] + Music_features[music]['Energy']
        if count ==1:
            artist_music_features[artist2]['Liveness'] = Music_features[music]['Liveness']
        else:
            artist_music_features[artist2]['Liveness'] = artist_music_features[artist2]['Liveness'] + Music_features[music]['Liveness']
        if count ==1:
            artist_music_features[artist2]['Loudness'] = Music_features[music]['Loudness']
        else:
            artist_music_features[artist2]['Loudness'] = artist_music_features[artist2]['Loudness'] + Music_features[music]['Loudness']
        if count ==1:
            artist_music_features[artist2]['Popularity'] = Music_features[music]['Popularity']
        else:
            artist_music_features[artist2]['Popularity'] = artist_music_features[artist2]['Popularity'] + Music_features[music]['Popularity']
        if count ==1:
            artist_music_features[artist2]['Speechiness'] = Music_features[music]['Speechiness']
        else:
            artist_music_features[artist2]['Speechiness'] = artist_music_features[artist2]['Speechiness'] + Music_features[music]['Speechiness']
        if count ==1:
            artist_music_features[artist2]['Tempo'] = Music_features[music]['Tempo']
        else:
            artist_music_features[artist2]['Tempo'] = artist_music_features[artist2]['Tempo'] + Music_features[music]['Tempo']
        if count ==1:
            artist_music_features[artist2]['Valence'] = Music_features[music]['Valence']
        else:
            artist_music_features[artist2]['Valence'] = artist_music_features[artist2]['Valence'] + Music_features[music]['Valence']
    #    print (artist_music_features[artist1]['Accousticeness'])

    artist_music_features[artist2]['Accousticeness'] = artist_music_features[artist2]['Accousticeness']/count
    artist_music_features[artist2]['Danceability'] = artist_music_features[artist2]['Danceability']/count
    artist_music_features[artist2]['Energy'] = artist_music_features[artist2]['Energy']/count
    artist_music_features[artist2]['Liveness'] = artist_music_features[artist2]['Liveness']/count
    artist_music_features[artist2]['Loudness'] = artist_music_features[artist2]['Loudness']/count
    artist_music_features[artist2]['Popularity'] = artist_music_features[artist2]['Popularity']/count
    artist_music_features[artist2]['Speechiness'] = artist_music_features[artist2]['Speechiness']/count
    artist_music_features[artist2]['Tempo'] = artist_music_features[artist2]['Tempo']/count
    artist_music_features[artist2]['Valence'] = artist_music_features[artist2]['Valence']/count
    
    return(artist_music_features)
