def same_order_lifts(towers,x,y,z):
    oldTower = towers[y]
    newTower = towers[z]
    emptyBox = ''
    a = len(oldTower)
    if a -x == -1:
        emptyBox = oldTower[::-1]
    else:
        emptyBox = oldTower[len(oldTower)-x:len(oldTower)]
    oldTower = oldTower[::-1]
    oldTower = oldTower.replace(emptyBox[::-1],'',1)
    oldTower = oldTower[::-1]
    newTower = newTower + emptyBox
    towers[y] = oldTower
    towers[z] = newTower
    return towers
            
def boxes():
    with open('day5.csv') as boxes:
        towers=['','','','','','','','','']
        lines = boxes.readlines()
        x = 0
        answer1=[]
        answer2=[]
        for line in lines[7::-1]:
            for character in line[1::4]:
                towers[x] = towers[x] + character
                towers[x] = towers[x].strip()
                x+=1
            x = 0
        for line in lines[10::]:
            numbers = line.split(' ')
            numbers.remove('move')
            numbers.remove('from')
            numbers.remove('to')
            x = int(numbers[0])
            y = int(numbers[1]) - 1
            z = int(numbers[2]) - 1
            same_order_lifts(towers,x,y,z)
        for tower in towers:
            answer1.append(tower[::-1][0])
        return answer1
