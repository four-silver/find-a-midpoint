import dijkstra

# 최솟값이 여러개일 때 모두 저장하여 배열로 반환
def dozen_min(args):
    min_result = []     # 여러 역들을 저장할 배열
    minimum = 100000
    print_station = []  # 역 이름을 반환하기 위해 저장할 임시 배열
    for i in args:
        print_station.append(i) # 역 이름들 저장
    for i in args.values(): # 가장 작은 value값 찾기
        if i < minimum:
            minimum = i
    for i, j in zip(args.values(), print_station):  # 그 가장 작은 value값이랑 같은 역들 모두 저장
        if i == minimum:
            min_result.append(j)
    return min_result   # value가 가장 작은 역들 모두 저장한 배열 반환

def min_sum(args):
    sum = 0
    for i in args:
        sum += i
    return sum

# 동시에 출발했을 때 모든 구성원의 도착 지점이 가장 빠른 지점
def quick_point(station_info, line_info, user_info):
    # 탐색할 역 이름 저장
    search_station = list(station_info.keys())

    # user별 dijkstra 수행
    dijkstra_distance = []
    dijkstra_path = []
    for i in user_info:
        distance, path, search_station = dijkstra.dijkstra(user_info[i], station_info, user_info, search_station)
        dijkstra_distance.append(distance)
        dijkstra_path.append(path)

    # 각 역별로 user까지 거리 list 생성
    # ex. '가능': [115, 19, 87, 107]
    each_user_distance = {}
    for station in search_station:
        user_distance = []
        for j in range(len(user_info)):
            user_distance.append(dijkstra_distance[j][station])
        each_user_distance[station] = user_distance

    # 각 역별로 '소요시간(user의 distance 중 가장 큰 값)' 구하기
    # ex. '가능': 115
    max_distance = {}
    for station in search_station:
        max_distance[station] = max(each_user_distance[station])        # 소요시간

    # 소요시간이 가장 작은 역들 구하기
    quick_station = dozen_min(max_distance)
    sum = {}
    # quick_station에 저장된 값들 모두 더해서
    for i in quick_station:
        sum[i] = min_sum(each_user_distance[i])

    meet_station = min(sum, key=sum.get)  # 합이 가장 작은 역이 만날 역
    # 출력
    print("\n#######################")
    print("가장 빨리 만나는 역:",meet_station)

    each_station = 0
    for name in user_info.keys():
        print(name+" :", each_user_distance[meet_station][each_station])
        each_station += 1