import json
import preprocessing
import dijkstra

if __name__ == '__main__':
    # 'vertices.json & station.json' 파일 입력 및 딕셔너리 line 생성
    line_info = {}  # 딕셔너리 생성 : 호선 정보
    station_info = preprocessing.make_node(line_info)

    # user 정보 저장
    user_info = {}                    # user 정보 저장할 딕셔너리
    preprocessing.input_data(user_info)

    print(station_info)
    print(line_info)
    print(user_info)

    distance = dijkstra.dijkstra('금정', station_info, line_info)
    print(distance)