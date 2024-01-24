/*
작성자: 이주원
작성일자: 2024-01-17
문제: 2606번 바이러스 (https://www.acmicpc.net/problem/2606)

DFS 사용
1번 컴퓨터에서 탐색이 끝날 때까지 DFS() 함수 실행시키면서 cnt 값 1씩 증가시킴
*/

#include <iostream>
#include <queue>
#include <tuple>

using namespace std;

int cnt = -1;
vector<int> adj[101];
bool visited[101];
int n, m;

void DFS(int a)
{
	cnt++;
	visited[a] = 1;
	for (int i : adj[a])
	{
		if (!visited[i])
		{
			DFS(i);
		}
	}
	return;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		int a, b;
		cin >> a >> b;
		adj[a].push_back(b);
		adj[b].push_back(a);
	}

	DFS(1);

	cout << cnt << "\n";
}