/*
작성자: 이주원
작성일자: 2024-03-03
문제: 14425번 문자열 집합 (https://www.acmicpc.net/problem/14425)

N개의 문자열로 이루어진 집합 S
입력으로 주어지는 M개의 문자열 중 집합 S에 포함되어 있는 것이 총 몇 개인지 구하기

처음에 간과한 점: M개의 문자열 중 같은 문자열이 중복되어 들어올 수 있었음
map에서 비교 후 같을 때마다 cnt++ 하는 걸로 변경
*/

#include <iostream>
#include <map>
#include <string>
using namespace std;

int n, m;
map<string, int> words;
string temp;

int cnt = 0;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> m;

	for (int i = 0; i < n; i++)
	{
		cin >> temp;
		words[temp]++;
	}

	for (int j = 0; j < m; j++)
	{
		cin >> temp;
		if (words.find(temp) != words.end())
		{
			cnt++;
		}
	}

	cout << cnt << "\n";

	return 0;
}