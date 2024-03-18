/*
작성자: 이주원
작성일자: 2024-03-18
문제: 동전 1(https://www.acmicpc.net/problem/2293)

가치합 문제
경우를 나누자!
*/

#include <iostream>
#include <vector>

using namespace std;

int coins[101];
int dp[100001];

int main()
{
	int n;
	int k;
	cin >> n >> k;

	for (int i = 1; i <= n; i++)
	{
		// 동전 받아오기
		cin >> coins[i];
	}

	dp[0] = 1;	
	for (int i = 1; i <= n; i++)
	{
		// 동전 종류별로 넣어보기
		for (int j = coins[i]; j <= k; j++)
		{
			dp[j] += dp[j - coins[i]];
		}
	}

	cout << dp[k];

	return 0;
}