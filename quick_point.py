import dijkstra
import sys

# 동시에 출발했을 때 모든 구성원의 도착 지점이 가장 빠른 지점
def quick_point(station_info, line_info, user_info):
    # 탐색할 역 이름 저장
    search_station = list(station_info.keys())

    # user별 dijkstra 수행
    dijkstra_result = []
    for i in user_info:
        dijkstra_result.append(dijkstra.dijkstra(user_info[i], station_info, user_info, search_station))

    # 각 역별로 user까지 거리 list 생성
    # ex. '가능': [115, 19, 87, 107]
    each_user_distance = {}
    for station in search_station:
        user_distance = []
        for j in range(len(user_info)):
            user_distance.append(dijkstra_result[j][station])
        each_user_distance[station] = user_distance

    # 각 역별로 '소요시간(user의 distance 중 가장 큰 값)' 구하기
    # ex. '가능': 115
    max_distance = {}
    for station in search_station:
        max_distance[station] = max(each_user_distance[station])        # 소요시간

    # 소요시간이 가장 작은 역 구하기
    quick_station = min(max_distance, key=max_distance.get)

    # 출력
    print("\n#######################")
    print("가장 빨리 만나는 역:",quick_station)

    each_station = 0
    for name in user_info.keys():
        print(name+" :", each_user_distance[quick_station][each_station])
        each_station += 1