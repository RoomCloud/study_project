import pandas as pd

# 엑셀 파일 불러오기
df = pd.read_excel('C:/Users/NT551/Desktop/데이터 추출(연습)/crawling_result_with_codenames.xlsx')

# 데이터 예시 구조
# df = pd.DataFrame({
#     'blueteam': ['GEN.G', 'DRX', 'T1', ...],
#     'redteam': ['T1', 'GEN.G', 'DRX', ...],
#     'winner_side': ['blue', 'red', 'red', ...]
# })

# 승자 팀을 결정하여 'winner_team' 컬럼에 추가하는 함수
def determine_winner_team(row):
    if row['winner_side'] == 'Blue':
        return row['blueteam']
    elif row['winner_side'] == 'Red':
        return row['redteam']
    else:
        return None  # 예외 처리

# 'winner_team' 컬럼 추가
#  axis=1 열 추가
df['winner_team'] = df.apply(determine_winner_team, axis=1)


# index = False 데이터 프레임파일을 저장할 때, 데이터프레임의 행번호를 포함하지않도록 설정
df.to_excel('updated_league_of_legends_matches.xlsx', index=False)

# 결과 출력
print("파일이 저장되었습니다.")
