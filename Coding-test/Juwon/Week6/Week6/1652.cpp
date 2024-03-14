/*
작성자: 이주원
작성일자: 2024-03-14
문제: 누울 자리를 찾아라(https://www.acmicpc.net/problem/1652)

처음에 틀렸던 점: 한 줄에 누울 수 있는 공간이 있으면 cnt++하고 바로 다음 줄로 넘어가는줄
그게 아니라 두 칸 이상이기만 하면 cnt++를 하는 거였다
문제를 잘 읽자
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int n;
int w_num = 0;
int h_num = 0;
vector<string> room;

// 가로로 누울 수 있는 자리 수 더하기 - 받아오자마자 검사
void TestString(string s)
{
	int cnt = 0;
	for (int i = 0; i < n; i++)
	{
		if (s[i] == '.')
		{
			cnt++;
		}
		if (s[i] == 'X')
		{
			if (cnt >= 2)
			{
				w_num++;
			}
			cnt = 0;
		}
	}
	if (cnt >= 2)
	{
		w_num++;
	}
}

int main()
{
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		string s;
		cin >> s;
		TestString(s);
		room.push_back(s);
	}

	// 세로로 받아올 수 있는 자리 수 더하기 - 각 요소의 i번째 값끼리 비교
	for (int i = 0; i < n; i++)
	{
		int cnt = 0;
		for (int j = 0; j < n; j++)
		{
			if (room[j][i] == '.')
			{
				cnt++;
			}
			if (room[j][i] == 'X')
			{
				if (cnt >= 2)
				{
					h_num++;
				}
				cnt = 0;
			}
		}
		if (cnt >= 2)
		{
			h_num++;
		}
	}

	cout << w_num << " " << h_num << "\n";

	return 0;
}