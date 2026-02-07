import sys
import os

# パスの設定（前回学んだ、上の階層を探しに行くおまじない）
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gemini_client import get_stair_data_from_image

# dataフォルダ内の画像ファイル名に合わせて書き換えてください
image_path = "data/0ea1c761-76de-4759-80d2-bef8139fff83.jpg" # 実際のファイル名に変更

print("--- Gemini API 解析開始 ---")
result = get_stair_data_from_image(image_path)

if result:
    print(f"AIが読み取った数値: {result}")
else:
    print("解析に失敗しました。APIキーや画像名を確認してください。")