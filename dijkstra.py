import heapq
def dijkstra(start, station_info, line_info):
    distance = {}
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (distance[start], start))

    while queue:
        current_dist, current_name = heapq.heappop(queue)
        if distance[current_name] < current_dist:
            continue
        for next_station in station_info[current_name]['time'].keys():
            if not (next_station in distance):
                distance[next_station] = 1000000
            if distance[next_station] > current_dist+station_info[current_name]['time'][next_station]:
                distance[next_station] = current_dist+station_info[current_name]['time'][next_station]
                heapq.heappush(queue, (distance[next_station], next_station))

    return distance