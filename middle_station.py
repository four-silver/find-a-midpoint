import sys
import math
import dijkstra

def middle_station(station_info, line_info, user_info):
    # 다익스트라
    dijkstra_result = []
    for i in user_info:
        dijkstra_result.append(dijkstra.dijkstra(user_info[i], station_info, line_info))

    # middle_station 탐색
    middle_station = ""
    min_sum_time = sys.float_info.max
    min_sum_deviation = sys.float_info.max
    for station in line_info:       # 탐색할 역 전체
        if station == '석촌고분' or station == '송파나루' or station == '한성백제' or station == '둔촌오륜' or station == '중앙보훈병원':
            continue

        print("현재 역 :", station)
        user_distance = []  # user에서 해당 역까지 거리의 리스트
        for i in range(len(user_info)):
            #distance = "user 탑승위치 -> 알아볼 역의 거리"
            distance = dijkstra_result[i][station]
            user_distance.append(distance)
        print("합 :", sum(user_distance))

        # 편차 구하기
        average = sum(user_distance) / len(user_info)  # 평균
        user_deviation = list(map(lambda x: (x - average) ** 2, user_distance))  # 각 user의 편차
        standard_deviation = math.sqrt(sum(user_deviation) / len(user_info))  # 표준편차
        print("표준편차 :", standard_deviation)

        # middle_station 업데이트
        if sum(user_distance) < min_sum_time and standard_deviation <= 25:
            middle_station = station
            min_sum_time = sum(user_distance)
            min_sum_deviation = standard_deviation
        elif sum(user_distance) == min_sum_time and standard_deviation < min_sum_deviation and standard_deviation <= 25:
            middle_station = station
            min_sum_time = sum(user_distance)
            min_sum_deviation = standard_deviation

        print("현재 중간지점 :", middle_station)
        print()