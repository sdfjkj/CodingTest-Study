/*
작성자: 이주원
작성일자: 2024-02-26
문제: 4375번 1 (https://www.acmicpc.net/problem/4375)

시간초과 해결 => 모듈러 연산
(a + b) % n = ((a % n) + (b % n)) % n
*/

#include <iostream>
#include <string>
using namespace std;

typedef long long ll;

int n;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	while (cin >> n) // or !cin.eof()
	{
		ll ret = 1;
		ll ones = 1;

		while (true) // 1, 11, 111이 n으로 나누어 떨어질 때까지
		{
			if (ones % n == 0)
			{
				break;
			}
			// 111 = 11 * 10 + 1
			ones = (ones % n * 10 % n) + 1;
			ones %= n;
			ret++;
		}

		cout << ret << "\n";
	}

	return 0;
}