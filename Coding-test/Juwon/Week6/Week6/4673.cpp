/*
작성자: 이주원
작성일자: 2024-03-17
문제: 셀프 넘버(https://www.acmicpc.net/problem/4673)
*/

#include <iostream>
using namespace std;

int main() {
	int dN; // d(n)
	bool checkdN[10001] = { false };

	for (int n = 1; n < 10001; n++) // n: 생성자
	{ 
		if (n < 10) 
		{
			dN = n + n % 10;
		}
		else if (n < 100) 
		{
			dN = n + n / 10 + n % 10;
		}
		else if (n < 1000) 
		{
			dN = n + n / 100 + (n % 100) / 10 + n % 10;
		}
		else if (n < 10001)
		{
			dN = n + n / 1000 + (n % 1000) / 100 + (n % 100) / 10 + n % 10;
		}
		if (dN < 10001)
		{
			checkdN[dN] = true;
		}
	}

	for (int i = 1; i < 10001; i++)
	{
		if (checkdN[i] == false)
			cout << i << "\n";
	}

	return 0;
}