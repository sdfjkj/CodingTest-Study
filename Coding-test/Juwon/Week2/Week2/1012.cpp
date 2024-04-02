/*
작성자: 이주원
작성일자: 2024-02-04
문제: 1012번 유기농 배추 (https://www.acmicpc.net/problem/1012)

탐색(DFS)을 활용해 배추가 모여있는 곳마다 배추흰지렁이 수 count++
주의할 점: 테스트 케이스를 돌릴 때마다 map, visited 배열 초기화 필요 => fill 함수 사용. count도 매번 초기화함
*/

#include <iostream>

using namespace std;

int test_case, n, m, nx, ny, cabbage_points, cabbages;
// 땅 배열
int map[51][51];
// 탐색 여부 판단용 배열
bool visited[51][51];

// 상하좌우 탐색용 x, y 배열
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { 1, -1, 0, 0 };

void DFS(int x, int y)
{
	visited[x][y] = 1;
	for (int i = 0; i < 4; i++)
	{
		// 상하좌우 돌아가기
		nx = x + dx[i];
		ny = y + dy[i];

		if (nx < 0 || nx >= n || ny < 0 || ny >= m)
			continue;

		if (map[nx][ny] == 1 && !visited[nx][ny])
		{
			// 배추가 심어져있는데 아직 방문하지 않은 곳일 경우 다시 DFS 실행 -> 모든 곳에 방문할 때까지 반복
			DFS(nx, ny);
		}
	}
}

int main()
{
	cin >> test_case;

	// 테스트 케이스만큼 for문 돌리기
	for (int c = 0; c < test_case; c++)
	{
		// 매번 초기화
		fill(&map[0][0], &map[0][0] + 51 * 51, 0);
		fill(&visited[0][0], &visited[0][0] + 51 * 51, 0);

		cabbages = 0;
		cin >> n >> m >> cabbage_points;

		for (int i = 0; i < cabbage_points; i++)
		{
			int a, b;
			cin >> a >> b;
			map[a][b] = 1;
		}

		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				// 배추가 심어져있는데 아직 방문하지 않은 곳일 경우 그 구역에서 맨 처음으로 DFS 실행
				if (map[i][j] == 1 && !visited[i][j])
				{
					DFS(i, j);
					// DFS 다 끝나면 count++
					cabbages++;
				}
			}
		}

		cout << cabbages << "\n";
	}
}