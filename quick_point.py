import dijkstra
import SPFA
import time

# 최솟값이 여러개일 때 모두 저장하여 배열로 반환
def dozen_min(args):
    min_result = []     # 여러 역들을 저장할 배열
    minimum = min(args.values())    # value 최소값 저장

    for station in args:
        if args[station] == minimum:
            min_result.append(station)

    return min_result   # value가 가장 작은 역들 모두 저장한 배열 반환

# 동시에 출발했을 때 모든 구성원의 도착 지점이 가장 빠른 지점
def find_middle_point(search_station, user_info, distance_result):
    # 각 역별로 user까지 거리 list 생성
    # ex. '가능': [115, 19, 87, 107]
    each_user_distance = {}
    for station in search_station:
        user_distance = []
        for j in range(len(user_info)):
            user_distance.append(distance_result[j][station])
        each_user_distance[station] = user_distance

    # 각 역별로 '소요시간(user의 distance 중 가장 큰 값)' 구하기
    # ex. '가능': 115
    max_distance = {}
    for station in search_station:
        max_distance[station] = max(each_user_distance[station])  # 소요시간

    # 소요시간이 가장 작은 역들 구하기
    quick_station = dozen_min(max_distance)
    all_sum = {}
    for station in quick_station:
        print("중간지점 역 : ", station)
        i = 0
        for name in user_info.keys():
            print(name + "(" + user_info[name] + ") :", each_user_distance[station][i])
            i += 1
    # quick_station에 저장된 값들 모두 더해서
    for i in quick_station:
        all_sum[i] = sum(each_user_distance[i])
    print(all_sum)
    min_sum = min(all_sum.values())  # 합이 가장 작은 역이 만날 역

    for meet_station in all_sum:
        if min_sum != all_sum[meet_station]:
            continue
        # 출력
        print("===============================")
        print("중간지점 역:", meet_station)

        i = 0
        for name in user_info.keys():
            print(name + "(" + user_info[name] + ") :", each_user_distance[meet_station][i])
            print("[", end='')
            #for j in range(0, len(path_result[i][meet_station]) - 1):
            #    print(path_result[i][meet_station][len(path_result[i][meet_station]) - j - 1], end='->')
            #print(path_result[i][meet_station][0] + "]")
            i += 1

def dijkstra_quickpoint(station_info, user_info):
    start = time.time()
    # 탐색할 역 이름 저장
    search_station = list(station_info.keys())

    # user별 dijkstra 수행
    distance_result = []
    #path_result = []
    for i in user_info:
        distance, path, search_station = dijkstra.dijkstra(user_info[i], station_info, user_info, search_station)
        distance_result.append(distance)
        #path_result.append(path)
    print(search_station)

    find_middle_point(search_station, user_info, distance_result)
    end = time.time()
    print('dijkstra', end-start, 'sec')
def SPFA_quickpoint(station_info, user_info):
    start = time.time()
    # 탐색할 역 이름 저장
    search_station = list(station_info.keys())

    # user별 dijkstra 수행
    distance_result = []
    for i in user_info:
        distance, search_station = SPFA.SPFA(user_info[i], station_info, user_info, search_station)
        distance_result.append(distance)
    print(search_station)

    find_middle_point(search_station, user_info, distance_result)
    end = time.time()
    print('SPFA', end-start, 'sec')