
# todo: check length to end continue
def formator(origin: list[tuple[int,str]],keys: list):
    # for key in keys:
    # [(11,"kimhab")]  tuple list , ["id","name"] keys
    newDic = []
    for i in range(len(origin)):
        pair = {}
        for j in range(len(origin[i])):
            pair[keys[j]] = origin[i][j]
        newDic.append(pair)
    # print("dic: ",newDic)
    return newDic
        # pair
        # print("id: ",id," name: ",name)

        
# formator([(1,"kimhab"),(2,"sothea")],["id","name"])