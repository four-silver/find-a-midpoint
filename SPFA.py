import queue
import sys

def SPFA(start, station_info, user_info, search_station, compare):
    DIST = {}       # 각 역마다의 거리
    inqueue = [start]
    q = queue.Queue()
    q.put(start)
    DIST[start] = 0
    visited = []

    user_distance = []
    max_user_distance = sys.maxsize
    new_search_station = []

    while not q.empty():
        current_name = q.get()
        inqueue.remove(current_name)

        if current_name in visited:
            continue
        visited.append(current_name)

        ## 배제
        ## max보다 거리 짧으면, 탐색 수행
        if DIST[current_name] < max_user_distance:
            # 교집합만 추가
            if current_name in search_station:
                new_search_station.append(current_name)
        else:
            continue

        # user의 distance구하기
        if current_name in user_info.values():
            user_distance.append(DIST[current_name])
            # user의 distance를 모두 구했으면, max 값 구하기
            if len(user_distance) == len(user_info):
                max_user_distance = max(user_distance)

        ## SPFA
        if max_user_distance < DIST[current_name]:
            continue
        compare += 1
        for next_station in station_info[current_name]['time'].keys():
            compare += 1
            cost = DIST[current_name] + station_info[current_name]['time'][next_station]

            if next_station not in DIST.keys():     # 초기화
                DIST[next_station] = sys.maxsize

            if DIST[next_station] > cost:
                DIST[next_station] = cost
                if next_station not in inqueue:
                    q.put(next_station)
                    inqueue.append(next_station)

    for i in user_info:
        if user_info[i] not in DIST:
            print('역이 연결되어있지 않습니다!')
            exit(0)

    return DIST, new_search_station, compare