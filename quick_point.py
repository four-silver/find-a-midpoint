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

    quick_station = dozen_min(max_distance)

    print("\n#######################")
    print("가장 빨리 만나는 역:",quick_station)

    for every in quick_station:
        print("\n###",every,"###")
        each_station = 0
        for name in user_info.keys():
            print(name+" :", each_user_distance[every][each_station])
            each_station += 1

'''
다은 노원
시은 장승배기
은서 금정
가은 용산

-> 가장 빨리 만나는 역: ['역삼', '잠원', '신용산', '이촌', '반포']

### 역삼 ###
다은 : 37
시은 : 22
은서 : 37
가은 : 20

### 잠원 ###
다은 : 36
시은 : 20
은서 : 37
가은 : 16

### 신용산 ###
다은 : 36
시은 : 18
은서 : 37
가은 : 6

### 이촌 ###
다은 : 37
시은 : 16
은서 : 35
가은 : 4

### 반포 ###
다은 : 37
시은 : 20
은서 : 37
가은 : 16
'''