import json

def make_node():
    with open('vertices.json', encoding='utf-8') as vertices_json:
        vertices_info = json.load(vertices_json)

    for i in range(len(vertices_info['station'])):
        station_nm = vertices_info['station'][i]['station_nm']      # 역 이름
        line_num = vertices_info['station'][i]['line_num']          # 호선

        if station_nm in line_info:      # 이미 해당 역에 대한 정보가 있으면, 새로운 '호선' append
            line_info[station_nm].append(line_num)
        else:                       # 새로운 '역'이면, 리스트로 '호선' 추가
            line_info[station_nm] = [line_num]

def input_data():                                                           # ***************** 역이름에 '\n'까지 포함됨! 수정 필요!!!
                                                                            # ex. {'다은': '캠퍼스타운\n', '시은': '쌍문\n', '은서': '금정\n', '가은': '수원'}
    # input_file 텍스트 파일 입력
    f = open("input_file.txt", encoding='utf-8')

    while True:
        line = f.readline()     # 파일 내용 한 줄씩 읽어옴
        if not line: break

        user_name = line.split(' ')[0]          # 띄어쓰기로 구분하여 앞에는 유저 이름
        boarding_station = line.split(' ')[1]   # 뒤에는 탑승 역

        user_info[user_name] = boarding_station      # 딕셔너리에 집어넣음 { 이름 : 탑승역 }
        print(user_name + " : " + user_info[user_name])
    f.close()

if __name__ == '__main__':
    # station.json 파일 입력
    with open('station.json', encoding='utf-8') as station_json:
        station_info = json.load(station_json)

        print(station_info['가능'])

    # vertices.json 파일 입력 및 딕셔너리 line 생성
    line_info = {}  # 딕셔너리 생성 : 호선 정보
    make_node()

    # user 정보 저장
    user_info = {}                    # user 정보 저장할 딕셔너리
    input_data()

    print(user_info)
    #print(line_info)