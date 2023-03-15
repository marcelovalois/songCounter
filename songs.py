from collections import defaultdict
from difflib import SequenceMatcher

def sequenceMatcher(str1, str2):
    return SequenceMatcher(a=str1.lower(), b=str2.lower()).ratio()

file1 = open('song-list-2.txt', 'r')
songList = file1.readlines()

dict = defaultdict(lambda: 0)

for item in songList:
    # Retira os \n
    item = item.replace('\n', '')
    # Quebra no + entre o nome da música e o peso
    splittedItem = item.split('+')
    # Adiciona peso 0 nos que não têm peso
    if len(splittedItem) == 1:
        splittedItem.append('0')
    # Separa em nome da música e peso
    song, weight = splittedItem
    # Coloca tudo para lowercase
    lowerSong = song.lower()
    # Retira os espaços do final
    while(lowerSong[-1] == ' '):
        lowerSong = lowerSong[:-1]
    
    # Colocar todas as primeiras letras em Caps
    titleSong = lowerSong.title()

    curSong = titleSong

    if curSong not in dict.keys():
        for song in dict.keys():
            if abs(len(song) - len(titleSong)) <= 2:
                if sequenceMatcher(song, titleSong) > 0.8:
                    curSong = song
                    break

    if dict[curSong] != 0:
        quant, oldWeight = dict[curSong]
        if int(oldWeight) < int(weight):
            dict[curSong] = (quant + 1, weight)
        else:
            dict[curSong] = (quant + 1, oldWeight)
    else:
        dict[curSong] = (1, weight)


sortedDict = sorted(dict.items(), key=lambda x:(x[1][0], x[1][1]), reverse=True)

index = 1

for song, quant in sortedDict:
    if int(quant[1]) != 0:
        print(index, '-', song+':', quant[0], ' ( Peso:', quant[1], ')')
    else:    
        print(index, '-', song+':', quant[0])
    
    index += 1

file1.close()