import dijkstra

# 최솟값이 여러개일 때 모두 저장하여 배열로 반환
def dozen_min(args):
    min_result = []     # 여러 역들을 저장할 배열
    minimum = min(args.values())    # value 최소값 저장

    for i, j in zip(args.values(), args.keys()):  # 그 가장 작은 value 값이랑 같은 역들 모두 저장
        if i == minimum:
            min_result.append(j)
    return min_result   # value가 가장 작은 역들 모두 저장한 배열 반환

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
    print(quick_station)
    all_sum = {}

    # quick_station에 저장된 값들 모두 더해서
    for i in quick_station:
        all_sum[i] = sum(each_user_distance[i])
    print(all_sum)
    meet_station = min(all_sum, key=all_sum.get)  # 합이 가장 작은 역이 만날 역
    # 출력
    print("중간지점 역:",meet_station)


    i = 0
    for name in user_info.keys():
        print(name+" :", each_user_distance[meet_station][i])
        print("[",end='')
        for j in range(0, len(dijkstra_path[i][meet_station])-1):
            print(dijkstra_path[i][meet_station][len(dijkstra_path[i][meet_station])-j-1], end='->')
        print(dijkstra_path[i][meet_station][0] + "]")
        i += 1
