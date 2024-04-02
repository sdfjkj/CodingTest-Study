/*
작성자: 이주원
작성일자: 2024-02-04
문제: 1980번 햄버거 사랑 (https://www.acmicpc.net/problem/1980)

[잘못 해석했던 부분]
처음에 tcoke % maxt < coke 조건 대신
tcoke % maxt == 0 이라는 조건을 세워서 바로 빠져나가도록 함
더 많은 햄버거 수를 찾을 수 있었음에도 해당 조건 때문에 빠져나갈 수 없었다
또한, m으로 나뉘고 남은 t가 생기는 경우에도 적용되지 않았다.

등호보단 부등호를 자주 쓰는 사람이 되자!

[추신]
난 햄버거 싫어!
*/

#include <iostream>
#include <algorithm>
#include <utility>
using namespace std;

int n, m, t, mint, maxt;

int main()
{
	// 버거1, 버거2, 총 시간
	cin >> n >> m >> t;

	// 우선 버거1, 버거2 중 더 시간 적은 애 찾기
	mint = min(n, m);
	maxt = max(n, m);

	int cnt = t / mint;
	int coke = t % mint;

	// while에서 사용할 temp 변수 생성
	int tcnt = cnt;
	int tcoke = coke;

	// 현재 카운트에서 n의 개수를 하나씩 줄이면서 콜라를 최대한 덜 마시도록 함
	// 남은 시간을 maxt로 나눈 나머지가 현재 coke에 소요한 시간보다 적다면 coke에 대입 후 cnt 몫만큼 추가
	while (tcnt > 0)
	{
		if (tcoke == 0)
		{
			break;
		}
		tcnt--;
		tcoke += mint;

		if (tcoke % maxt < coke)
		{
			cnt = tcnt + tcoke / maxt;
			coke = tcoke % maxt;
		}
	}

	cout << cnt << " " << coke << "\n";

	return 0;
}