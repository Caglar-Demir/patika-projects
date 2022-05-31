#%% Flatten Function

def flatten(liste, flat):
    for ele in liste:
        if type(ele) == list:
            # N-dimensional listleri kontrol eder
            # Tuple gibi diğer non-scalar yapılar için genişletilebilir.
            flatten(ele, flat) #Her list türündeki elemanın içine girer.
            
        else:
            flat.append(ele) #ELeman list değilse çıktı list'ine eklenir.

#%% Main Function

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat = []

flatten(liste,flat)
print("Input:", liste, "\nOutput:", flat)