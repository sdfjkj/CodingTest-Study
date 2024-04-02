/*
작성자: 이주원
작성일자: 2024-03-04
문제: 미로 탐색 (https://www.acmicpc.net/problem/2178)

거리는 BFS!!
개수는 DFS!!
붙어서 오는 입력을 따로 받아 오는 게 생각할 점
*/

#include <iostream>
#include <queue>
#include <string>

using namespace std;

int n, m, nx, ny;
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { 1, -1, 0, 0 };
int map[104][104];
int visited[104][104];

void BFS(int x, int y)
{
	queue<pair<int, int>> q;
	q.push({ x, y });
	visited[x][y] = 1;

	while (!q.empty())
	{
		x = q.front().first;
		y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			nx = x + dx[i];
			ny = y + dy[i];

			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;
			if (map[nx][ny] == 0 || visited[nx][ny])
				continue;
			visited[nx][ny] = visited[x][y] + 1;
			q.push({ nx, ny });
		}
	}
}

int main()
{
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		string s;
		cin >> s;
		for (int j = 0; j < m; j++)
		{
			map[i][j] = s[j] - '0';
		}
	}

	BFS(0, 0);
	cout << visited[n - 1][m - 1] << "\n";
}