T = int(input())

# 총 얻은 경험치
def all_exp(a : int) -> int:
    return (1+a) / 2 * a

# 경험치를 레벨로 환산
def level_up(a : int) -> int:
    level = 1
    while(True):
        if (level-1) * level < a:
            level += 1
        else:
            return level-1


for testcase in range(T):
    gain_exp = all_exp(int(input()))
    print(level_up(gain_exp))