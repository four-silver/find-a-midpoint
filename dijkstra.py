import heapq
import sys

def dijkstra(start, station_info, user_info, search_station):

###예외처리 해본부분
    station_info['쌍문']['time'] = {}
    station_info['수유']['time'] = {}
    station_info['창동']['time'] = {}
###여기까지
    distance = {}
    distance[start] = 0
    queue = []
    path = {}
    visited = []
    heapq.heappush(queue, (distance[start], start))

    user_distance = []
    max_user_distance = sys.maxsize
    new_search_station = []

    while queue:
        current_dist, current_name = heapq.heappop(queue)
        if current_name in visited:
            continue
        visited.append(current_name)
        ### 배제
        # user의 max distance보다 거리가 짧으면, 탐색 수행
        if current_dist < max_user_distance:
            # 이미 search_station에 있는 값들만 추가(교집합)
            if current_name in search_station:
                new_search_station.append(current_name)
        else:
            continue
        # 현재 역이 user의 역이라면, user의 distance 추가
        if current_name in user_info.values():
            user_distance.append(current_dist)
            # user의 distance를 모두 구했다면, max 값 구하기
            if len(user_distance) == len(user_info):
                max_user_distance = max(user_distance)

        ### 다익스트라
        if distance[current_name] < current_dist:
            continue
        for next_station in station_info[current_name]['time'].keys():
            if not (next_station in distance):
                distance[next_station] = sys.maxsize
            if distance[next_station] > current_dist + station_info[current_name]['time'][next_station]:
                distance[next_station] = current_dist + station_info[current_name]['time'][next_station]
                heapq.heappush(queue, (distance[next_station], next_station))

                if not (current_name in path):
                    path[current_name] = [current_name]

                path[next_station] = [next_station]
                for x in path[current_name]: path[next_station].append(x)

    if not (len(user_distance) == len(user_info)):
        print('역이 연결되어있지 않습니다!')
        exit(0)

    #print(path['충무로'])
    return distance, path, new_search_station