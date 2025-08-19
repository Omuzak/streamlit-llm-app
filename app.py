# APIkeyの読み込み
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# LangChainのインポート
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

def get_response(system_message, user_message):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY)
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_message),
    ]
    result = llm(messages)
    return result.content

# アプリ本体
import streamlit as st

st.title("健康か料理についてAIに聞いてみよう！")

st.write("##### 動作モード1: 健康に関する質問")
st.write("入力フォームに健康の悩みや疑問を入力し、「実行」ボタンを押すことでAIに質問できます。")
st.write("##### 動作モード2: 料理に関する質問")
st.write("料理に関する質問を入力し、「実行」ボタンを押すことでAIに質問できます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["健康に関する質問", "料理に関する質問"]
)

st.divider()

if selected_item == "健康に関する質問":
    selected_system_message = "あなたは健康に関する質問に答えるAIです。"
    input_message = st.text_input(label="健康に関する質問を入力してください。")

else:
    selected_system_message = "あなたは料理に関する質問に答えるAIです。"
    input_message = st.text_input(label="料理に関する質問を入力してください。")

if st.button("実行"):
    st.write("実行ボタンが押されました。回答を生成中...")
    st.divider()

    if input_message:
        response = get_response(selected_system_message, input_message)
        st.write(f"AIの回答: {response}")

    else:
        st.error("質問を入力してから「実行」ボタンを押してください。")
