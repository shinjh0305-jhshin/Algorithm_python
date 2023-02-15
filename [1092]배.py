cranes = int(input())
crane = list(map(int, input().split()))
boxes = int(input())
box = list(map(int, input().split()))
moved = [False] * boxes
next_target_box = [0] * cranes


def operate():
    crane.sort(reverse=True)
    box.sort(reverse=True)

    if box[0] > crane[0]:
        print(-1)
        return

    ans = 0
    to_move = boxes
    while to_move:
        for cur_crane in range(cranes):
            for cur_box in range(next_target_box[cur_crane], boxes):
                if not moved[cur_box] and crane[cur_crane] >= box[cur_box]:
                    moved[cur_box] = True
                    to_move -= 1
                    next_target_box[cur_crane] += 1
                    break
                next_target_box[cur_crane] += 1
        ans += 1

    print(ans)


operate()
