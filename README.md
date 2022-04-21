## Find the Midpoint of Multiple Vertices using Dijkstra Algorithm
🔍 2022 ICNCT 국제학술대회 게재

### 요약
 타당한 중간 지점을 선택하는 것은 이동 및 송수신의 효율성 측면에서 중요하다.
따라서 본 논문에서는 그래프에서 입력된 여러 노드의 중간 지점을 구하는 알고리즘을 제안한다.
중간지점은 ‘입력 노드에서 동시에 출발하였을 때 가장 빨리 만나는 점’으로 정의한다.
효율적인 탐색을 위해 탐색 범위를 제한하고 해당 범위 안에서 중간 지점을 선택한다.
해당 알고리즘을 모의 실험을 통해 중간 지점의 타당성을 증명하였다.

### 1. 탐색범위 제한<br>
 입력 노드마다 가장 먼 다른 입력 노드까지의 최단 거리 안에 있는 노드들을 해당 입력 노드의 탐색범위로 설정한다. 모든 입력 노드의 탐색 범위를 구했다면, 탐색 범위들의 교집합을 최종 탐색 범위로 설정한다.<br>
 
![image](https://user-images.githubusercontent.com/80963996/164452920-05f9b448-b44a-4338-ab52-d5ae33f5b6f8.png) <br>


### 2. 중간 지점 찾기 알고리즘<br>
 중간 지점은 ‘입력노드에서 동시에 출발하였을 때 가장 빨리 만나는 점’으로 정의한다. 한 정점에서 모든 입력 노드까지의 최단 거리 중 최댓값을 소요시간이라고 정의하고, 소요시간이 최소인 정점이 중간지점이다.
* durations=max⁡( distance(i)), i=inputnode, exploration_range:all node
* candidate_midpoints=vertex(min⁡( durations))
* midpoint = vertex(min(sum(distance(i))), i = inputnode, exploration_range:candidate_midpoints

### 3. 시뮬레이션<br>
 역 간의 연결성 및 역 간 이동 시 소요시간 데이터를 활용해 여러 실험을 진행하여 타당성을 증명하였다. 또한 SPFA와 DFS와의 비교를 통해 효율성을 증명하였다.
