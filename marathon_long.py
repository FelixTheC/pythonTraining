# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 18:55:18 2017

@author: felix
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    new_list_increas = []
    new_list_decreas = []
    summe = 0
    count = 0
    if len(L) >= 2:
        while count != len(L)-1:
            if L[count] >= (L[count+1]):
                new_list_increas.append(L[count])
            elif L[count] <= (L[count+1]):
                new_list_decreas.append(L[count])
            count +=1
        if L[len(L)-1] <= L[len(L)-2]:
            new_list_increas.append(L[count])
        elif L[len(L)-1] >= L[len(L)-2]:
            new_list_decreas.append(L[count])
        if len(new_list_increas) >= len(new_list_decreas): 
            for i in new_list_increas:
                summe += i
        else:
            for i in new_list_decreas:
                summe += i
        print(new_list_increas)
        print(new_list_decreas)
        return summe
    else:
        raise ValueError