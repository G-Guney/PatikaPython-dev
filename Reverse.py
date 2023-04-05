#verilen liste içindeki elemanları tersine döndüren fonksiyoz yazacağız
# eğer elemanlarda liste ise onlarıda tersine çevireceğiz

exmp1 = [1,2,3,4,5,6]
exmp2 = [[5,2,3],[3,5,9],[9,4,1]]

def reverse_list(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            lst[i] = reverse_list(lst[i])
        else:
            lst[i] = str(lst[i])[::-1]
    return lst[::-1]

print(reverse_list(exmp1))
print(reverse_list(exmp2))

