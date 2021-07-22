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

if __name__ == '__main__':
    # station.json 파일 입력
    with open('station.json', encoding='utf-8') as station_json:
        station_info = json.load(station_json)

        print(station_info['가능'])

    # vertices.json 파일 입력 및 딕셔너리 line 생성
    line_info = {}  # 딕셔너리 생성 : 호선 정보
    make_node()

    print(line_info)