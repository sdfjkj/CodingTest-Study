/*
작성자: 이주원
작성일자: 2024-03-12
문제: RGB거리 (https://www.acmicpc.net/problem/1149)

현재 색상이 각각 R, G, B 일 때의 경우를 dp로 구한 뒤
그 중에서도 가장 작은 값을 찾는 문제

dp는 식 자체는 단순하지만 떠올리는 게 쉽지 않았다...
케이스를 쪼개는 게 핵심인 듯
*/


#include <iostream>
using namespace std;

int n;
int dp[1001][3];
int nums[3];

int main()
{
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cin >> nums[0] >> nums[1] >> nums[2];
		dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + nums[0];
		dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + nums[1];
		dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + nums[2];
	}

	cout << min(dp[n][2], min(dp[n][0], dp[n][1]));

	return 0;
}