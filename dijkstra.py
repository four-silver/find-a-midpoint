import heapq
import sys
def dijkstra(start, station_info, line_info, user_info):
    distance = {}
    distance[start] = 0
    queue = []
    path = {}
    heapq.heappush(queue, (distance[start], start))

    for user in user_info:
        print(user_info[user])
    search_station = []
    user_station_distance = []
    max_user_station_distance = sys.float_info.max

    while queue:
        current_dist, current_name = heapq.heappop(queue)

        print(current_name)
        # 다른 user 까지의 거리를 모두 구했다면, 그 중 가장 긴 값 구하기
        if len(user_station_distance) == len(user_info):
            max_user_station_distance = max(user_station_distance)
            print("####################")
        # 현재 station이 user의 station과 같다면, distance추가
        for user in user_info:
            if user_info[user] == current_name:
                user_station_distance.append(current_dist)
                print("!!!!!!!!!!!!!!!!!!")
        if distance[current_name] < max_user_station_distance or current_dist < max_user_station_distance:
            print("++")
        if distance[current_name] < current_dist:
            continue
        for next_station in station_info[current_name]['time'].keys():
            if not (next_station in distance):
                distance[next_station] = 1000000
            if distance[next_station] > current_dist + station_info[current_name]['time'][next_station]:
                distance[next_station] = current_dist + station_info[current_name]['time'][next_station]
                heapq.heappush(queue, (distance[next_station], next_station))

                if not (current_name in path):
                    path[current_name]=[current_name]
                    
                path[next_station]=[next_station]
                for x in path[current_name]: path[next_station].append(x)

    print(user_station_distance)
    print(path['충무로'])
    return distance