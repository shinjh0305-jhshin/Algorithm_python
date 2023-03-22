slots, target = map(int, input().split())
capa = list(map(int, input().split()))
robot = {}  # 로봇의 위치
occupied = [False] * (slots * 2)  # 슬롯의 점유
robots = 1  # 몇 번째 로봇이 올라갈 차례인지


def rotate_slots():
    # 내구도 회전
    tmp = capa[slots * 2 - 1]
    for i in range(slots * 2 - 2, -1, -1):
        capa[i + 1] = capa[i]
    capa[0] = tmp

    # 로봇 회전
    to_delete = 0
    for idx, slot in robot.items():
        robot[idx] = (slot + 1) % (slots * 2)  # 회전
        if robot[idx] == slots - 1:  # 내리는 위치
            to_delete = idx
    if to_delete:
        del robot[to_delete]
    tmp = occupied[slots * 2 - 1]  # 점유 여부 회전
    for i in range(slots * 2 - 2, -1, -1):
        occupied[i + 1] = occupied[i]
    occupied[0] = tmp
    occupied[slots - 1] = False  # 내리는 위치


def rotate_robots():
    to_delete = 0
    for idx, slot in robot.items():
        next_slot = (slot + 1) % (slots * 2)
        if not occupied[next_slot] and capa[next_slot]:
            occupied[slot] = False
            capa[next_slot] -= 1
            if next_slot == slots - 1:  # 내리는 위치
                to_delete = idx
            else:
                occupied[next_slot] = True
                robot[idx] = next_slot
    if to_delete:
        del robot[to_delete]


def load_robot():
    global robots
    if capa[0]:
        robot[robots] = 0
        robots += 1
        capa[0] -= 1
        occupied[0] = True


def count_capa():
    if capa.count(0) >= target:
        return True
    return False


def operate():
    ans = 1
    while True:
        rotate_slots()
        rotate_robots()
        load_robot()
        if count_capa():
            print(ans)
            return
        ans += 1


operate()
