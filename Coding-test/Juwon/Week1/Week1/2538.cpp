/*
작성자: 이주원
작성일자: 2024-01-17
문제: 2538번 영역 구하기 (https://www.acmicpc.net/problem/2583)

DFS 사용
받아오는 좌표에 map, visited 처리 -> 못 지나가게 함
DFS 이용해서 지나간 거리만큼 +

탐색 종료 시 return 값 벡터에 추가

sort로 오름차순 정렬 후 출력
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m, k;
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { 1, -1, 0, 0 };
int nx, ny;

int map[101][101] = { 0 };
int visited[101][101] = { 0 };
vector<int> ret;

int DFS(int x, int y)
{
	visited[x][y] = 1;
	int ret = 1;

	for (int i = 0; i < 4; i++)
	{
		nx = x + dx[i];
		ny = y + dy[i];

		if (nx < 0 || ny < 0 || nx >= n || ny >= m || map[nx][ny] == 1)
			continue;
		if (visited[nx][ny] == 1)
			continue;

		if (map[nx][ny] == 0 && !visited[nx][ny])
		{
			ret += DFS(nx, ny);
		}
	}

	return ret;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> m >> k;

	// k개만큼 받아오기
	for (int i = 0; i < k; i++)
	{
		int a, b, c, d;
		cin >> a >> b >> c >> d;

		for (int j = b; j < d; j++)
		{
			for (int k = a; k < c; k++)
			{
				map[j][k] = 1;
			}
		}
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (map[i][j] == 0 && visited[i][j] == 0)
			{
				ret.push_back(DFS(i, j));
			}
		}
	}

	cout << ret.size() << "\n";
	sort(ret.begin(), ret.end());

	for (int i : ret)
	{
		cout << i << " ";
	}

	return 0;
}