from sys import stdin

n, w, l = map(int, stdin.readline().split())
trucks = list(map(int, stdin.readline().split()))

bridge = [0] * w  # 다리 길이만큼 자리 만들어주기
time, bridge_weight = 0, 0  # 시간, 다리 위 무게


while True:
    end = bridge.pop(0)  # 다리 다 건넌 트럭 제거
    bridge_weight -= end  # 다리 건넌 트럭 무게 제거

    if trucks:  # 남은 트럭이 있을 경우

        if bridge_weight + trucks[0] <= l:  # 다리 하중보다 작거나 같으면 건널 수 있음
            bridge.append(trucks[0])  # 다리 위에 트럭 올리기
            bridge_weight += trucks[0]  # 다리 하중 증가
            trucks.pop(0)
        else:  # 하중이 무거워서 다리를 건널 수 없음
            bridge.append(0)  # 트럭 대신 0 넣어주기

    time += 1  # 시간 증가

    if not trucks:  # 남은 트럭이 없을 경우
        time += w  # 마지막 트럭 건너는 시간
        break

print(time)
