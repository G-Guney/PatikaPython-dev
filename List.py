# Verilen bir listeyi düzleştiren fonksiyon yazacağız
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# örnekleri çalıştıralım
exmp1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
exmp2 = ["gökhan",55,[[["merhaba","dünya",123]],6,"pyhton"],99]

print(flatten(exmp1))
print(flatten(exmp2))