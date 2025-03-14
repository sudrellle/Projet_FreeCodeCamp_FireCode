import numpy as np
def calculate(liste):
    if len(liste)!=9 :
        raise ValueError('la liste doit contenir 9 chiffres')
    arr=np.array(liste)
    tableau=arr.reshape(3,3)
    return {'mean':[tableau.mean(axis=0).tolist(),tableau.mean(axis=1).tolist(),tableau.mean()],
    "variance":[tableau.var(axis=0).tolist(),tableau.var(axis=1).tolist(),tableau.var().tolist()],
    "standard-deviation":[tableau.std(axis=0).tolist(),tableau.std(axis=1).tolist(),tableau.std().tolist()],
    "max":[tableau.max(axis=0).tolist(),tableau.max(axis=1).tolist(),tableau.max().tolist()],
    "min":[tableau.min(axis=0).tolist(),tableau.min(axis=1).tolist(),tableau.min().tolist()],
    "somme":[tableau.sum(axis=0).tolist(),tableau.sum(axis=1).tolist(),tableau.sum().tolist()]
    
    }  
    
    
    

liste1=[10,2,63,4,8,0,5,9] 
print(calculate(liste1))