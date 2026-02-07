import os
from google import genai
from dotenv import load_dotenv
import json
from PIL import Image # 画像読み込み用

load_dotenv()

def get_stair_data_from_image(image_path):
    # クライアントの初期化（新しい書き方）
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    # モデル名は現在安定している "gemini-2.0-flash" を指定します
    # ※サンプルにある "2.5" はまだ存在しないか、将来のプレビュー版の可能性があります
    model_id = "gemini-2.5-flash"

    prompt = """
    添付された階段図面から、以下の3つの数値を抽出し、必ずJSON形式のみで出力してください。
    - width: 階段の有効幅(mm)
    - tread: 踏面(mm)
    - riser: 蹴上げ(mm)
    出力例: {"width": 1400, "tread": 300, "riser": 150}
    """

    print("--- Gemini API (New SDK) 解析開始 ---")

    try:
        # 画像を開く
        img = Image.open(image_path)
        
        # 解析実行
        response = client.models.generate_content(
            model=model_id,
            contents=[prompt, img]
        )

        # JSON抽出
        result_text = response.text
        clean_json = result_text.replace('```json', '').replace('```', '').strip()
        return json.loads(clean_json)

    except Exception as e:
        print(f"解析失敗: {e}")
        return None