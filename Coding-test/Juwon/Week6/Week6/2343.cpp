/*
작성자: 이주원
작성일자: 24-03-25
문제: 기타 레슨(https://www.acmicpc.net/problem/2343)

m개(10,000)의 블루레이에 n개(100,000)의 강의 담기
블루레이 크기는 최소로
*/

#include <iostream>
#include <vector>

using namespace std;

int n, m, s, e, ret, sum, mx;
vector<int> a;

bool Check(int mid)
{
    // max 값이 mid보다 큰 경우는 올 수 없으므로 바로 return false
    // start 부분을 왼쪽으로 옮겨서 mid 값이 커지도록 함
    if (mx > mid)
    {
        return false;
    }

    int temp = mid;
    int cnt = 0;

    // 강의 전체 개수 완전탐색
    for (int i = 0; i < n; i++)
    {
        // mid 값보다 현재 강의 크기가 더 크다면
        // 이제 더 못 담음! => 여기서 블루레이 개수 1개 증가
        if (mid < a[i])
        {
            mid = temp;
            cnt++;
        }
        // mid 값에서 현재 강의 크기 뺌 -> 현 블루레이에 얼만큼 담을지 알기 위해서
        mid -= a[i];
    }

    // mid 값과 temp 값이 다른 경우 블루레이 개수가 하나 더 필요함
    if (mid != temp)
    {
        cnt++;
    }

    return cnt <= m;
}

int main()
{
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        a.push_back(temp);

        sum += temp;
        mx = max(mx, temp);
    }

    // 블루레이 크기 기준 이분 탐색
    s = 0;
    e = sum;

    while (s <= e)
    {
        int mid = (s + e) / 2;

        // mid 기준 check 함수 돌림
        // 블루레이들이 돌어가는 공간이 하나 만들어질 때마다 check() 종료
        if (Check(mid))
        {
            e = mid - 1;
            // 가능한 블루레이 크기 중 최소 값
            ret = mid;
        }
        else
        {
            s = mid + 1;
        }
    }

    cout << ret << "\n";
    return 0;
}