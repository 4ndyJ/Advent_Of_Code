def D2Solution(file_input):
    total=0
    product_total=0
    
    Valid={"red":12, "green":13, "blue": 14}
    with open(file_input) as file:
        filecontents=file.readlines()
        for game in filecontents:
            product=1
            Max={"red":0, "blue":0,"green":0}
            splits=game.replace(",","").split(";")
    
            for section in splits:
                subsections=section.split()
                for colour in Max.keys():
    
                    if colour in subsections:
    
                        if Max[colour] < int(subsections[subsections.index(colour)-1]):
                            Max[colour]=int(subsections[subsections.index(colour)-1])
            
            for key in Valid.keys():
                if Valid[key] < Max[key]:
                    break
            else:
                total+=int(game.split()[1][:-1])
    
            for key in Valid.keys():
                product*=Max[key]
            product_total+=product
    return total, product_total

D2Solution("input.txt")
