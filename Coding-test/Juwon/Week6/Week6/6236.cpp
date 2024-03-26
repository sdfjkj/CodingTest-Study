/*
작성자: 이주원
작성일자: 2024-03-18
문제: 용돈 관리(https://www.acmicpc.net/problem/6236)

답 봄..ㅠ
*/

#include <iostream>
#include <vector>

using namespace std;

int n, m, k, sum, mx, ret;
int s, e, mid;
vector<int> money;

bool Check(int mid)
{
	int cnt = 1;
	int temp = mid;
	for (int i = 0; i < n; i++)
	{
		if (mid < money[i])
		{
			mid = temp;
			cnt++;
		}
		mid -= money[i];
	}
	return cnt <= m;
}

int main()
{
	cin >> n >> m;

	sum = 0;
	for (int i = 0; i < n; i++)
	{
		int a;
		cin >> a;
		money.push_back(a);
		mx = max(a, mx);
	}

	s = mx, e = 1000000004;

	while (s <= e)
	{
		mid = (s + e) / 2;
		if (Check(mid))
		{
			e = mid - 1;
			ret = mid;
		}
		else
		{
			s = mid + 1;
		}
	}

	cout << ret << "\n";
	return 0;
}