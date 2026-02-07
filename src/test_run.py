from logic import check_stair_compliance

# 図面の数値（1400, 300, 159）をテスト
print("--- 図面データの判定テスト ---")
data = {"type": "other", "w": 1400, "t": 300, "r": 159}
res = check_stair_compliance(data["type"], data["w"], data["t"], data["r"])

print(f"最終判定: {'適合' if res['is_all_ok'] else '不適合'}")
for d in res["details"]:
    print(d)