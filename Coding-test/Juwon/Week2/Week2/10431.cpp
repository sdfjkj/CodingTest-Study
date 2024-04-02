/*
작성자: 이주원
작성일자: 2024-02-04
문제: 10431번 줄세우기 (https://www.acmicpc.net/problem/10431)

새로운 값이 현재 있는 배열 중 하나보다 더 작은 값일 때 맨 앞으로 가고 이미 있는 배열의 모든 인덱스를 하나씩 뒤로 보낸다
-> '새로운 값이 하나씩 앞으로 간다'와 같은 의미
-> 선택 정렬 (다만 뒤에서부터 시작하며 앞의 값과 비교)
*/

#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int p;
// 테스트 케이스와 양의 정수 벡터 쌍을 동시에 담는 벡터 선언
vector<pair<int, vector<int>>> lines;
vector<int> nums_count;

int counts(vector<int> v_origin)
{
	int ret = 0;
	vector<int> v;

	for (int i = 0; i < v_origin.size(); i++)
	{
		// 새 벡터 v와 비교할 값 temp에 대입 (orgin 벡터 순서대로)
		int temp = v_origin[i];
		v.push_back(temp);
		// 맨 뒤에서부터 시작
		for (int j = v.size() - 2; j >= 0; j--)
		{
			// 앞의 값과 비교해서 앞의 값이 더 크면 앞의 값과 교체
			// 앞의 값과 계속 비교하면서 맨 앞으로 나아간다. (v의 크기만큼)
			// 비교할 때마다 ret++ 하면서 v 크기만큼 ret에 추가 (삽입 정렬의 원리)
			if (v[j] > v[j + 1])
			{
				// 앞과 자리 교체하며 앞으로 나감
				swap(v[j], v[j + 1]);
				// 그에 따른 count++
				ret++;
			}
			else
			{
				break;
			}
		}
	}

	return ret;
}

int main()
{
	cin >> p;
	for (int i = 0; i < p; i++)
	{
		int num;
		vector<int> v;

		cin >> num;
		for (int j = 0; j < 20; j++)
		{
			int a;
			cin >> a;
			v.push_back(a);
		}
		// 벡터 다 받아온 뒤 테스트 케이스와 함께 저장
		lines.push_back({ num, v });
	}

	for (int i = 0; i < p; i++)
	{
		// 테스트 케이스별 걸음 수 벡터에 추가
		nums_count.push_back(counts(lines[i].second));
	}

	// 출력
	for (int i = 0; i < p; i++)
	{
		// 텍스트 케이스 number, 걸음 수 순
		cout << lines[i].first << " " << nums_count[i] << "\n";
	}

}