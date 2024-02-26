/*
작성자: 이주원
작성일자: 2024-02-26
문제: 1269번 대칭 차집합 (https://www.acmicpc.net/problem/1269)

map 자료구조 좋은 거구나...
*/

#include <iostream>
#include <map>
using namespace std;

int a, b;
int cnt = 0;
map<int, int> m;

int main()
{
	cin >> a >> b;

	for (int i = 0; i < a; i++)
	{
		int t;
		cin >> t;
		m[t]++;
	}

	for (int i = 0; i < b; i++)
	{
		int t;
		cin >> t;
		m[t]++;
	}

	for (auto i : m)
	{
		if (i.second == 1)
		{
			cnt++;
		}
	}

	cout << cnt << "\n";

	return 0;
}