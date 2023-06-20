import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random


def select_leader(members):
    leader = random.choice(members)
    return leader

def write_leader(members):
    if len(members) < 2:
        st.warning("참가자는 최소 2명 이상이어야 합니다.")
    else:
        st.write("* 등록된 참가자")
        for i in range(len(members)):
            st.write(members[i])

        if st.button("선출"):
            leader = select_leader(members)
            leader2 = select_leader(members)
            while leader == leader2:
                leader2 = select_leader(members)

            st.success(f"팀1 팀장: {leader}")
            st.success(f"팀2 팀장: {leader2}")

def write_team(team1, team2):
    position = ["탑　","정글","미드","원딜","서폿"]
    tap1, tap2, tap3 = st.columns(3)
    tap1.subheader("포지션")
    tap2.subheader("1팀")
    tap3.subheader("2팀")

    for i in range(5) :
        tap1.write(position[i])
        tap2.write(team1[i])
        tap3.write(team2[i])

def main():
    st.title("팀장(노예)을 뽑아봅시다")

    st.header("인원체크 중")

    # Google 스프레드시트 연결 설정
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("json/friendlymatch-34e818879fda.json", scope)
    client = gspread.authorize(creds)

    # 스프레드시트 선택
    spreadsheet_url = "https://docs.google.com/spreadsheets/d/1Ql3YeyosrUuoQ2XpNj6sS7kJUmGwZ1TaMVG8Rj7cgwY/edit#gid=191955157"  # Google 스프레드시트 URL 입력
    sheet_name = "진행중인내전"  # 시트 이름 입력

    sheet_leader = client.open_by_url(spreadsheet_url).worksheet(sheet_name)
    sheet_record = client.open_by_url(spreadsheet_url).worksheet(sheet_name)

    # 스프레드시트에서 참가자 목록 가져오기
    members = sheet_leader.col_values(2)[1:]  # 이름 배열
    members_team1 = sheet_record.row_values(15)[3:8]
    members_team2 = sheet_record.row_values(15)[8:13]

    write_leader(members)
    write_team(members_team1, members_team2)

if __name__ == "__main__":
    main()