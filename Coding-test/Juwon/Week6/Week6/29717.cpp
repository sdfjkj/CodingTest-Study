/*
작성자: 이주원
작성일자: 2024-03-19
문제: 슬라임 잡고 레벨 업!(https://www.acmicpc.net/problem/29717)

아아아아아아아
자료형 때문에 틀렸던 거였음
아아아아아아악....
*/

#include <iostream>

using namespace std;

int t;

void BSilLevel(long long n)
{
	long long sum = n * (n + 1) / 2;

	long long left = 1;
	long long right = n;
	long long mid;

	while (left <= right)
	{
		mid = (left + right) / 2;
		if (mid * (mid + 1) <= sum)
		{
			left = mid + 1;
		}
		else
		{
			right = mid - 1;
		}
	}
	cout << left << "\n";
}

int main()
{
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		long long n;
		cin >> n;
		BSilLevel(n);
	}

	return 0;
}