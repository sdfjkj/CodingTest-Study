/*
작성자: 이주원
작성일자: 2024-03-13
문제: 참외밭(https://www.acmicpc.net/problem/2477)

변의 형태는 육각형으로 정해져 있기 때문에 전체 사각형에서 width의 쪼개진 값 중 하나와 height의 쪼개진 값이 연속되는 부분이 빠짐
전체 width, 전체 height가 연속해서 나온(maxIdx) 이후 다다음 인덱스와 다다다음 인덱스가 그 역할을 함
단, maxIdx를 구할 때 인덱스가 0, 5이면 5을 대입하는 것이 아닌 0을 대입해야 함 (연속된 값 이후 인덱스를 반환해야 해서) - 이게 반례

인덱스 0, 5일 때 예시
7
2 160
4 30
1 60
4 20
1 100
3 50
43400 (정답 47600)
*/

#include <iostream>
#include <vector>
using namespace std;

int n;
vector<int> melons;

// 전체 너비 인덱스, 전체 높이 인덱스
int hIdx = 0;
int wIdx = 0;

// 전체 사각형의 너비, 높이
int hMax = 0;
int wMax = 0;

// 전체 사각형에서 뺄 작은 사각형의 너비, 높이가 들어가 있는 인덱스
int idx1, idx2;

// 전체 너비, 전체 높이가 모두 나왔을 때 인덱스
int maxIdx = 0;

int MinusN(int n)
{
	// 인덱스 0 ~ 5로 맞추기
	if (n > 5)
	{
		n -= 6;
	}
	return n;
}

void GetMaxIdx()
{
	// 반례: 인덱스가 0, 5로 나온 경우
	if ((wIdx == 0 && hIdx == 5) || (wIdx == 5 && hIdx == 0))
	{
		maxIdx = 0;
	}
	else
	{
		maxIdx = max(wIdx, hIdx);
	}
}

int main()
{
	cin >> n;

	for (int i = 0; i < 6; i++)
	{
		int a, b;
		cin >> a >> b;

		// 동서일 때와 남북일 때 나눠서 계산
		if (a == 1 || a == 2)
		{
			if (wMax < b)
			{
				wMax = b;
				wIdx = i;
			}
		}

		if (a == 3 || a == 4)
		{
			if (hMax < b)
			{
				hMax = b;
				hIdx = i;
			}
		}

		melons.push_back(b);
	}

	GetMaxIdx();

	idx1 = maxIdx + 2;
	idx2 = maxIdx + 3;
	
	idx1 = MinusN(idx1);
	idx2 = MinusN(idx2);

	int ret = (wMax * hMax - melons[idx1] * melons[idx2]) * n;

	cout << ret << "\n";
}