/*
작성자: 이주원
작성일자: 2024-03-18
문제: 용돈 관리(https://www.acmicpc.net/problem/6236)

답 봄..ㅠ
*/

#include <iostream>
#include <vector>

using namespace std;

int n, m, k, sum;
vector<int> money;

int main()
{
	cin >> n >> m;

	sum = 0;
	for (int i = 0; i < n; i++)
	{
		int a;
		cin >> a;
		money.push_back(a);
		sum += a;
	}

	k = sum / m; // k 초기값 설정




	return 0;
}