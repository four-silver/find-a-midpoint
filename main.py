import preprocessing
import quick_point

if __name__ == '__main__':
    # 'vertices.json & station.json' 파일 입력 및 딕셔너리 line 생성

    station_info = preprocessing.make_node()

    # user 정보 저장
    user_info = {}                    # user 정보 저장할 딕셔너리
    preprocessing.input_data(user_info)

    print("dijkstra")
    quick_point.dijkstra_quickpoint(station_info, user_info)
    print("\nSPFA")
    quick_point.SPFA_quickpoint(station_info, user_info)
    print("DFS")
    quick_point.DFS_quickpoint(station_info, user_info)
