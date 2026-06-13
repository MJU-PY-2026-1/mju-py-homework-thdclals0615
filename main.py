# 파일이름 :파이썬 실행결과
# 작 성 자 :송치민
win_compensation=10000000000
lose_compensation=win_compensation/5


team=['토트넘','맨유','첼시','아스날','맨시티','리버풀','파리생제르망','유벤투스','AC밀란','인테르','바르셀로나','레알마드리드']
team_prestige=[50,80,65,65,70,75,65,65,70,65,80,85]
importance=["final","semi-finals","quarter-finals","round-of-16","qualifiers"]


while True :
    print("\n=== 축구 경기 분석 및 보상 시스템 ===")
    print("1.경기데이터 입력 및 분석과 보상 분배")
    print("2.mvp선수 선정")
    print("3.시스템에 등록된 팀 목록 확인")   
    print("4.시스템 종료")
    menu = int(input("메뉴를 선택하세요.:"))
    if menu == 1 :
        print("경기데이터를 입력해주세요.")
        Ateam=team[int(input('Ateam 인덱스 번호:'))]
        Bteam=team[int(input('Bteam 인덱스 번호:'))]
        Ateam_prestige=team_prestige[int(input('Ateam 명성 인덱스 번호:'))]
        Bteam_prestige=team_prestige[int(input('Bteam 명성 인덱스 번호:'))]
        print(f'Ateam:{Ateam}, Bteam:{Bteam}')
        print(f'Ateam의 명성:{Ateam_prestige}, Bteam의 명성:{Bteam_prestige}')

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
        pass
    elif menu == 2 :
        print("mvp선수를 선정하겠습니다.")
        high_score = 0
        mvp_player = " "
        while True :
            print("선수의 각 포인트를 입력하세요.(주요선수들의 포인트만 입력하고 그만하려면 이름에 종료를 입력하세요)")
            player_name = input("선수의 이름을 입력하세요 :")
            if player_name == "종료" :
                break
            goals = int(input("선수의 골수 :"))
            assists = int(input("선수의 도움수:"))
            defence = int(input("선수의 수비 포인트:"))

            total_score = 5*goals + 3*assists + 2*defence
            print(f"{player_name} 선수의 총점: {total_score}점")

            if total_score > high_score:
                high_score = total_score
                mvp_player = player_name
                print(f"*** 현재까지 MVP 1순위: {mvp_player} ***")
        print("mvp선수 선정 완료 !!!!!!")  
        if mvp_player == " " :
            print("선수의 정보가 없습니다.")
        else :
            print(f"축하합니다! mvp선수는 {mvp_player}선수입니다!")    


    elif menu == 3 :
        print(f"등록된 팀의 목록입니다. {team=}")
        pass
    elif menu == 4 :
        print("시스템을 종료합니다.")
        break
    else :
        print("잘못된 입력입니다. 다시 입력해주세요.")

