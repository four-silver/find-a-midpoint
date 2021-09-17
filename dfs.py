import preprocessing

dfs= []
dist={}
path=" "
n=" "

def DFS(current_station, sum, s,cost):
    print ('@')
    if not current_station in dist:
        dist[current_station]=9999

    if (dist[current_station]<sum):
        return
    else:
        dist[current_station]=sum

    if (sum>cost):
            return

    if (current_station==n):
        if(sum<cost):
            cost=sum
            path=s
        return

    for next_station in station_info[current_station]['time'].keys():
      if not next_station in dfs:
        dfs.append(next_station)
        print (next_station)
        DFS(next_station,sum+station_info[current_station]['time'][next_station],next_station,cost)
        dfs.remove(next_station)




def start(start, end):
    cost=9999
    n=end
    dist[start] = cost
    dfs.append(start)
    DFS(start,0," ",cost)

start("충무로","서울역")
print (path)
