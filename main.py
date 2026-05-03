# 파일이름 :파이썬 실행결과
# 작 성 자 :송치
win_compensation=10000000000
lose_compensation=win_compensation/5


team=['토트넘','맨유','첼시','아스날','맨시티','리버풀','파리생제르망','유벤투스','AC밀란','인테르','바르셀로나','레알마드리드']
team_prestige=[50,80,65,65,70,75,65,65,70,65,80,85]
importance=["final","semi-finals","quarter-finals","round-of-16","qualifiers"]

Ateam=team[int(input('Ateam 인덱스 번호:'))]
Bteam=team[int(input('Bteam 인덱스 번호:'))]
Ateam_prestige=team_prestige[int(input('Ateam 명성 인덱스 번호:'))]
Bteam_prestige=team_prestige[int(input('Bteam 명성 인덱스 번호:'))]
print(f'Ateam:{Ateam}, Bteam:{Bteam}')
print(f'Ateam의 명성:{Ateam_prestige}, Bteam의 명성:{Bteam_prestige}')


A_tac_poi=input('Ateam의 전술과 포지션:')
B_tac_poi=input('Bteam의 전술과 포지션:')
Acaptain=input('Ateam의 주장선수:')
Bcaptain=input('Bteam의 주장선수:')


game_importance=importance[int(input('게임 중요도의 인덱스 번호:'))]
audience_num=int(input('관중의 숫자:'))
print(f'게임의 중요도:{game_importance}, 관중의 숫자:{audience_num} ')


Ateam_goal=int(input('Ateam의 골 숫자:'))
Bteam_goal=int(input('Bteam의 골 숫자:'))


Ateambestplayer=input('A team bestplayer:')
Bteambestplayer=input('B team bestplayer:')


Abestplayer_point=int(input('Ateam 베스트 플레이어의 활약포인트:'))
Bbestplayer_point=int(input('Bteam 베스트 플레이어의 활약포인트:'))


if Abestplayer_point > Bbestplayer_point :
    print(f"mvp선수:{Ateambestplayer}")
else :
    print(f"mvp선수:{Bteambestplayer}")


if Ateam_goal > Bteam_goal :
    Ateam_compensation=win_compensation
    Bteam_compensation=lose_compensation
    print('경기결과:Ateam 승/Bteam 패')
else :
    Bteam_compensation=win_compensation
    Ateam_compensation=lose_compensation
    print('경기결과:Bteam 승/Ateam 패')


if Ateam_prestige+Bteam_prestige >= 160 :
    win_compensation*=3
    lose_compensation*=3
elif Ateam_prestige+Bteam_prestige >= 145 :
    win_compensation*=2
    lose_compensation*=2
else :
    win_compensation*=1
    lose_compensation*=1


if audience_num >= 40000 :
    win_compensation*=2
    lose_compensation*=2
elif audience_num >= 20000:
    win_compensation*=1
    lose_compensation*=1
else :
    win_compensation*=0.5
    lose_compensation*=0.5


if game_importance=="final" :
    win_compensation*=6
    lose_compensation*=6
elif game_importance=="semi-finals" :
    win_compensation*=4
    lose_compensation*=4
elif game_importance=="quarter-finals" :
    win_compensation*=3
    lose_compensation*=3
elif game_importance=="round-of-16" :
    win_compensation*=2
    lose_compensation*=2
elif game_importance=="qualifiers" :
    win_compensation*=1
    lose_compensation*=1


print(f'Ateam의 보상은 {Ateam_compensation}원 입니다!!')
print(f'Bteam의 보상은 {Bteam_compensation}원 입니다!!')
