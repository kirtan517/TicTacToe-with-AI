import math


box_center_cords = [(100, 100), (100, 300), (100, 500), (300, 100),
                    (300, 300), (300, 500), (500, 100), (500, 300), (500, 500)]






def checkWinner(visited):
    results = {"x": {100: 0, 300: 0, 500: 0}, "y": {100: 0, 300: 0, 500: 0}}
    for  i in visited.keys():
        if visited[i]==1:
            results["x"][i[0]] +=1
            results["y"][i[1]] +=1
        if visited[i]==-1:
            results["x"][i[0]] +=-1
            results["y"][i[1]] +=-1
    # Diagonals
    if (300, 300) in visited.keys() and (100, 100) in visited.keys() and (500, 500) in visited.keys():
        if visited[(300, 300)] == visited[(100, 100)] == visited[(500, 500)]:
            return visited[(300, 300)]
    if (300, 300) in visited.keys() and (100, 500) in visited.keys() and (500, 100) in visited.keys():
        if visited[(300, 300)] == visited[(100, 500)] == visited[(500, 100)]:
            return visited[(300, 300)]

    for i in results.keys():
        for value in results[i]:
            if(results[i][value] == 3):
                winner = 1

                return winner
            elif(results[i][value] == -3):
                winner = -1
                return winner
            else:
                winner = 0
    return winner

   



def Computer(turn, visited):
    visited_2=visited.copy()
    x=checkWinner(visited)
    
    if x==1:
        return 1
    
    if x == -1:
        return -1
    
    if len(visited_2)==9:
        return checkWinner(visited_2)

    if turn==1:
        best_score= -math.inf
        for i in box_center_cords:
            if i not in visited_2.keys():
                turn = -1
                visited_2[i]=1
                best_score  =  max(Computer(turn, visited_2),best_score)
                visited_2.pop(i)
            
    else:
        best_score = math.inf
        for i in box_center_cords:
            if i not in visited_2.keys():
                turn = 1
                visited_2[i]=-1
                best_score = min(Computer(turn, visited_2), best_score)
                visited_2.pop(i)

    return best_score

def best_move(turn,visited):
    position = (0,0)
    best_score= -1*turn*math.inf
    for i in box_center_cords:
        if i not in visited.keys():
            visited[i] = turn
            score=Computer(turn*-1,visited)
            if turn ==1:
                if score > best_score:
                    best_score=score
                    position=i
            if turn ==-1:
                if score < best_score:
                    best_score = score
                    position = i
            visited.pop(i)
    return position

if __name__ == "__main__":
    visited = {(100.0, 100.0): 1, (500.0, 100.0): -1, (100.0, 300.0): 1}
    print(best_move(-1,visited))
    # omputer()
    # 





