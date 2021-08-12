import dijkstra

# 동시에 출발했을 때 모든 구성원의 도착 지점이 가장 빠른 지점
def quick_point(station_info, line_info, user_info):
    dijkstra_result = []
    each_user_distance = {}
    for i in user_info:
        dijkstra_result.append(dijkstra.dijkstra(user_info[i], station_info, line_info, user_info))
    for station in station_info:
        user_distance = []
        if station == '석촌고분' or station == '송파나루' or station == '한성백제' or station == '둔촌오륜' or station == '중앙보훈병원':
            continue
        for j in range(len(user_info)):
            user_distance.append(dijkstra_result[j][station])
        each_user_distance[station] = user_distance
    # print(each_user_distance)

    max_distance = {}   # 네 명이 소요되는 시간 중 가장 큰 시간 집어넣음
    for fastest in each_user_distance:
        max_distance[fastest] = max(each_user_distance[fastest])

    min_distance = 10000

    for i in max_distance.values():
        if min_distance > i:
            min_distance = i    # max_distancs 중에서 가장 작은 값이 모두 가장 빨리 만나는 지점
    quick_station = min(max_distance, key=max_distance.get)

    print("\n#######################")
    print("가장 빨리 만나는 역:",quick_station)
    each_station = 0
    for name in user_info.keys():
        print(name+" :", each_user_distance[quick_station][each_station])
        each_station += 1