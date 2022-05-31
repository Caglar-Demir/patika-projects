#%% Reverse Function

def reverse(liste):
    liste = list(reversed(liste)) #Elemanları ters çevirir.
    
    #List tipi elemanlar varsa onların içeriğini de ters çevirir.
    for i in range(len(liste)):
        if type(liste[i]) == list:
            liste[i] = reverse(liste[i])
    return liste

#%% Main Function

liste = [[1, 2], [3, 4], [5, 6, 7]]
liste = reverse(liste)
print(liste)