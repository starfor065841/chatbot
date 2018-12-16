def min_sort(tag):
    i = 0
    m = min(tag)
    temp = []
    
    for price in tag:
        if price == m:
            temp.append(i)
        i += 1
    print('?????????' + str(temp))

    return temp
