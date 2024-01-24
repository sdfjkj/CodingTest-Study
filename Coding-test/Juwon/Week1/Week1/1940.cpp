/*
작성자: 이주원
작성일자: 2024-01-17
문제: 1940번 주몽 (https://www.acmicpc.net/problem/1940)

투 포인터 사용 구현
벡터 v 오름차순으로 정렬 후
벡터 첫 번째 값 start, 마지막 값 end로 index 설정

start + end와 원하는 수인 M과 비교하며 start, end의 인덱스를 조절
둘이 같을 경우 ret++
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;
vector<int> v;

int start_num = 0;
int end_num = 0;
int ret = 0;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> m;

	for (int i = 0; i < n; i++)
	{
		int a;
		cin >> a;
		v.push_back(a);
	}

	sort(v.begin(), v.end());

	end_num = v.size() - 1;

	while (start_num < end_num)
	{
		int sum = 0;
		sum = v[start_num] + v[end_num];

		if (sum < m) // 합이 m 보다 작으면 start 쪽을 한 칸 증가
		{
			start_num++;
		}
		else if (sum > m)
		{
			end_num--;
		}
		else
		{
			ret++;
			start_num++;
			end_num--;
		}
	}

	cout << ret << "\n";
}