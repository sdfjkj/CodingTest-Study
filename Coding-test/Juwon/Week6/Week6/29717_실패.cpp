/*
작성자: 이주원
작성일자: 2024-03-19
문제: 슬라임 잡고 레벨 업!(https://www.acmicpc.net/problem/29717)
*/

#include <iostream>

using namespace std;

int t;
int sum = 0;
int ret = 1;

void BSilLevel(int n)
{
	sum = n * (n + 1) / 2;

	long long left = 1;
	long long right = 1000000001;
	long long mid;

	while (left <= right)
	{
		mid = int((left + right) / 2);
		if (mid * (mid + 1) <= sum)
		{
			left = mid + 1;
		}
		else
		{
			right = mid - 1;
		}
	}
	cout << int(left) << "\n";
}

int main()
{
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int n;
		cin >> n;
		BSilLevel(n);
	}

	return 0;
}