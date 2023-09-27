def adjacent(skaiciai):
    if len(skaiciai) < 2:
        raise ValueError("turi buti du")

    max_product = skaiciai[0] * skaiciai[1]

    for i in range(1, len(skaiciai) - 1):
        print(i)
        product =skaiciai[i]*skaiciai[i+1]
        max_product = max(max_product,product)
    return max_product
