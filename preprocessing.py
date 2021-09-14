import json

def make_node():
    # station.json 파일 입력
    with open('station.json', encoding='utf-8') as station_json:
        station_info = json.load(station_json)

    return station_info

def input_data(user_info):
    # input_file 텍스트 파일 입력
    f = open("input_file.txt", encoding='utf-8')

    while True:
        line = f.readline().strip()     # 파일 내용 한 줄씩 읽어오면서 '\n' 포함되는 것 제거
        if not line: break
        user_name = line.split(' ')[0]          # 띄어쓰기로 구분하여 앞에는 유저 이름
        boarding_station = line.split(' ')[1]   # 뒤에는 탑승 역

        user_info[user_name] = boarding_station      # 딕셔너리에 집어넣음 { 이름 : 탑승역 }
    f.close()