import dijkstra

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

    # 소요시간이 가장 작은 역 구하기
    quick_station = min(max_distance, key=max_distance.get)

    # 출력
    print("중간지점 역:",quick_station)

    i = 0
    for name in user_info.keys():
        print(name+" :", each_user_distance[quick_station][i])
        print("[",end='')
        for j in range(0, len(dijkstra_path[i][quick_station])-1):
            print(dijkstra_path[i][quick_station][len(dijkstra_path[i][quick_station])-j-1], end='->')
        print(dijkstra_path[i][quick_station][0] + "]")
        i += 1