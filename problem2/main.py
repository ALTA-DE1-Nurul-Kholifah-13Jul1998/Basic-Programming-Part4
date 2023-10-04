def draw_xyz(N):
    pattern = ""
    pola = ["X","Y","Z"]
    
    for i in range(1, (N * N) + 1):
        if i%3==0:
            pattern+=pola[0] + " "
        elif i%2!=0:
            pattern+=pola[1] + " "
        elif i%2==0:
            pattern+=pola[2] + " "
        if i%N==0:
            pattern+="\n"   
    return pattern
    
if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """

    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """