"""
AISDI - Zad 1
Jakub Robaczewski, Oskar Bartosz
"""


def bubblesort():
    pass


def selectionsort():
    pass

def show_me(table, a, b):
    print(table)
    print(a)
    print(b)


    
  

def quicksort(table,low,high): 
    if low < high:
        i = ( low-1 )
        pivot = table[high]    
        for j in range(low , high): 
            if table[j] <= pivot: 
                i = i+1 
                table[i],table[j] = table[j],table[i] 
        table[i+1],table[high] = table[high],table[i+1] 
        pi = i+1 
        quicksort(table, low, pi-1) 
        quicksort(table, pi+1, high) 

  
table = [5,2,7,1,9,2]
print(quicksort(table, 0, len(table)-1))   
print(table)


    

    

