import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials



def record():
    st.title("팀별 승패기록 페이지")

    st.header("1팀")

    # Google 스프레드시트 연결 설정
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("json/friendlymatch-34e818879fda.json", scope)
    client = gspread.authorize(creds)

    # 스프레드시트 선택
    spreadsheet_url = "https://docs.google.com/spreadsheets/d/1Ql3YeyosrUuoQ2XpNj6sS7kJUmGwZ1TaMVG8Rj7cgwY/edit#gid=191955157"  # Google 스프레드시트 URL 입력
    sheet_name = "진행중인내전"  # 시트 이름 입력
    sheet = client.open_by_url(spreadsheet_url).worksheet(sheet_name)

    # 스프레드시트에서 참가자 목록 가져오기
    members = sheet.row_values(13)[1:]  # 이름 배열

    if len(members) < 2:
        st.warning("참가자는 최소 2명 이상이어야 합니다.")
    else:
        st.write("등록된 참가자:")
        st.write(members)

        # if st.button("선출"):
        #     leader = select_leader(members)
        #     leader2 = select_leader(members)
        #     while leader == leader2:
        #         leader2 = select_leader(members)
        #
        #     st.success(f"팀1 팀장: {leader}")
        #     st.success(f"팀2 팀장: {leader2}")