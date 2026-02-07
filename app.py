import streamlit as st
import os
from src.gemini_client import get_stair_data_from_image
from src.logic import check_stair_compliance
from PIL import Image

st.set_page_config(page_title="AI階段判定ツール", layout="centered")

st.title("🏗️ 階段図面 AI判定アプリ")
st.write("図面画像をアップロードすると、AIが数値を抽出し、建築基準法に適合しているか判定します。")

# サイドバーで建物の種類を選択
building_type = st.sidebar.selectbox(
    "建物の種類を選択してください",
    options=["dwelling", "primary_school", "public_use", "other"],
    format_func=lambda x: {
        "dwelling": "住宅",
        "primary_school": "小学校",
        "public_use": "駅",
        "other": "その他"
    }[x]
)

# ファイルアップローダー
uploaded_file = st.file_uploader("図面画像を選択してください...", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # 画面に画像を表示
    image = Image.open(uploaded_file)
    st.image(image, caption='アップロードされた図面', use_container_width=True)
    
    if st.button('AI判定を実行する'):
        with st.spinner('AI解析中...'):
            # 画像を解析関数に渡す
            data = get_stair_data_from_image(uploaded_file)
            
            if data:
                st.subheader("📊 解析結果")
                
                # 判定ロジック実行
                result = check_stair_compliance(
                    width=data.get('width'),
                    tread=data.get('tread'),
                    riser=data.get('riser'),
                    building_type=building_type
                )
                
                # 結果表示のデコレーション
                if result['is_all_ok']:
                    st.success("✅ 適合：全ての基準を満たしています。")
                else:
                    st.error("⚠️ 不適合：基準を満たさない箇所があります。")
                
                # 詳細を表示
                for detail in result['details']:
                    st.write(detail)
                
                with st.expander("AIが読み取った生データ"):
                    st.json(data)
            else:
                st.error("解析に失敗しました。画像が鮮明か、APIキーが正しいか確認してください。")