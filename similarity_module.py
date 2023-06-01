# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:26:43 2020

@author: archa
"""

import math
def eucilidean_distance(music1, music2, music_features):
    music_attributes = ['Accousticeness', 'Danceability', 'Energy', 'Liveness', 'Loudness', 'Popularity', 'Speechiness', 'Tempo', 'Valence']
    #calculate Eucilidean distance for each attribute
    #Eucilidean distance sqrt((x1-y1)^2+(x2-y2)^2+....+(xi-yi)^2)
    Eucilidean_distance = 0
    for attribute in music_attributes:
        Eucilidean_distance = Eucilidean_distance + (pow((music_features[music1][attribute] - music_features[music2][attribute]), 2))
    Eucilidean_distance = math.sqrt(Eucilidean_distance)
    return (Eucilidean_distance)


def cosine_distance(music1, music2, music_features):
    music_attributes = ['Accousticeness', 'Danceability', 'Energy', 'Liveness', 'Loudness', 'Popularity', 'Speechiness', 'Tempo', 'Valence']
    #calculate cosine distance for each attribute
    #cosine distance (x1y1+x2y2+x3y3+...xnyn)/(sqrt(x1^2 +x2^2+... xn^2)*sqrt(y1^2 + y2^2+....+yn^2))
    Cosine_distance_numerator = 0
    cosine_distance_denominator1 = 0
    cosine_distance_denominator2 = 0
    for attribute in music_attributes:
        Cosine_distance_numerator = Cosine_distance_numerator + (music_features[music1][attribute] * music_features[music2][attribute])
        cosine_distance_denominator1 = cosine_distance_denominator1 + (pow(music_features[music1][attribute], 2))
        cosine_distance_denominator2 = cosine_distance_denominator2 + (pow(music_features[music2][attribute], 2))
    
    cosine_distance_denominator2 = math.sqrt(cosine_distance_denominator2)
    cosine_distance_denominator1 = math.sqrt(cosine_distance_denominator1)    
    cosine_distance = Cosine_distance_numerator/(cosine_distance_denominator1 * cosine_distance_denominator2)
    return(cosine_distance)


def jaccard_distance(music1, music2, Music_features):
    #Jaccard Distance Coefficient: 𝐽(𝑋,𝑌)=  |𝑋∩𝑌|/|𝑋∪𝑌| 
    music1_set = {Music_features[music1]['Accousticeness'], Music_features[music1]['Danceability'], Music_features[music1]['Energy'], Music_features[music1]['Liveness'], Music_features[music1]['Loudness'], Music_features[music1]['Popularity'], Music_features[music1]['Speechiness'], Music_features[music1]['Tempo'], Music_features[music1]['Valence']}
    music2_set = {Music_features[music2]['Accousticeness'], Music_features[music2]['Danceability'], Music_features[music2]['Energy'], Music_features[music2]['Liveness'], Music_features[music2]['Loudness'], Music_features[music2]['Popularity'], Music_features[music2]['Speechiness'], Music_features[music2]['Tempo'], Music_features[music2]['Valence']}
#    print (music1_set)
#    print (music2_set)
#    print (music1_set.intersection(music2_set))
#    print(music1_set.union(music2_set))

    Jaccard_Distance = len(music1_set.intersection(music2_set))/len(music1_set.union(music2_set))
    #print ('Jaccard Distance: ', Jaccard_Distance)
    return (Jaccard_Distance)

def manhattan_distance(music1, music2, Music_features):
    music_attributes = ['Accousticeness', 'Danceability', 'Energy', 'Liveness', 'Loudness', 'Popularity', 'Speechiness', 'Tempo', 'Valence']
    #calculate Manhattan distance for each attribute
    #Manhattan Distance Metric:𝑚𝑎𝑛(𝑥,𝑦)= abs(x1 - y1)+abs(x2-y2) +abs(x3-y3)+....abs(xn-yn)
    Manhattan_distance = 0
    for attribute in music_attributes:
        Manhattan_distance = Manhattan_distance + (abs(Music_features[music1][attribute] - Music_features[music2][attribute]))
    return (Manhattan_distance)


def pearson_coefficient(music1, music2, Music_features):
    #calculate pearson coefficient
    average_music1 = 0
    average_music2 = 0
    count = 0
    music_attributes = ['Accousticeness', 'Danceability', 'Energy', 'Liveness', 'Loudness', 'Popularity', 'Speechiness', 'Tempo', 'Valence']
    #calculate the average of attributes of music1
    for attribute in music_attributes:
        average_music1 = average_music1 + Music_features[music1][attribute]
        count = count + 1
    average_music1 = average_music1 /count
    count = 0
    #calculate the average of attributes of music2
    for attribute in music_attributes:
        average_music2 = average_music2 + Music_features[music2][attribute]
        count = count + 1
    average_music2 = average_music2/count

    #calculate pearson coeff numerator
    pearson_coeff_numerator = 0
    pearson_coeff_denom1 = 0
    pearson_coeff_denom2 = 0
    for attribute in music_attributes:
        pearson_coeff_numerator = pearson_coeff_numerator + ((Music_features[music1][attribute] - average_music1)*(Music_features[music2][attribute] - average_music2))
    for attribute in music_attributes:
        pearson_coeff_denom1 = pearson_coeff_denom1 + pow((Music_features[music1][attribute] - average_music1), 2)
        pearson_coeff_denom2 = pearson_coeff_denom2 + pow((Music_features[music2][attribute] - average_music2), 2)

    pearson_coeff_denom1 = math.sqrt(pearson_coeff_denom1)
    pearson_coeff_denom2 = math.sqrt(pearson_coeff_denom2)
    pearson_coefficient = pearson_coeff_numerator/(pearson_coeff_denom1 * pearson_coeff_denom2)
    return (pearson_coefficient)
