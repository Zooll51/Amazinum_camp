ball = "B.BB..B.BB.B.BBBBBBBBBB............"

def search_iter (x):
    list_ball = list(x)

    if list_ball.count("B")-1 > list_ball.count("."):
        return -1

    count = 0
    for i in x.split("."):
        if i == "B":
            continue
        else:
            count += len(i)//2

    return count

print(search_iter(ball))
