/*
작성자: 이주원
작성일자: 2024-03-18
문제: 평범한 배낭(https://www.acmicpc.net/problem/12865)

배낭 문제
최대 가치합 dp[] 선언후 i번째 무게를 추가할 경우와 추가하지 않을 경우 비교
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dp[101][100001];
int n, k;
pair<int, int> backpack[101];

int main()
{
	cin >> n >> k;

	for (int i = 1; i <= n; i++) {
		// 물건의 무게, 가치 입력받기
		cin >> backpack[i].first >> backpack[i].second;
	}
	sort(backpack + 1, backpack + n + 1);

	// 한 줄씩 돌리기
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= k; j++) {
			// 무게가 아직 초과 안됐으면
			if (j >= backpack[i].first)
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - backpack[i].first] + backpack[i].second);
			else
				dp[i][j] = dp[i - 1][j];
		}
	}

	cout << dp[n][k];

	return 0;
}