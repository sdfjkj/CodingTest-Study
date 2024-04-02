/*
작성자: 이주원
작성일자: 2024-02-26
문제: 4375번 1 (https://www.acmicpc.net/problem/4375)

시간 초과...
*/

#include <iostream>
#include <string>
using namespace std;

int n;
long long ret = 0;

int main()
{
	while (!cin.eof())
	{
		cin >> n;

		// 각 자릿수가 모두 1로면 이루어진 n의 배수
		// 1, 11, 111, 1111, 11111
		// 이거 str으로 생각하고 받아오면 될듯?
		string ones = "1";
		while (true) // 1, 11, 111이 n으로 나누어 떨어질 때까지
		{
			long long ones_int = stoll(ones) % n;
			if (ones_int == 0)
			{
				ret = ones.length();
				break;
			}
			ones.append("1");
		}

		cout << ret << "\n";

	}

	return 0;
}