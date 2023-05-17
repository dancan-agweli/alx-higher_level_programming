#!/usr/bin/python3
def weight_average(my_list=[]):
    med = 0
    ttw = 0
    tts = 0
    if (len(my_list) <= 0):
        return (0)
    for pro in my_list:
        score, weight = pro
        ttw += weight
        tts += score * weight
    return tts / ttw
