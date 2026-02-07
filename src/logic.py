def check_stair_compliance(building_type, width, tread, riser):
    """
    建築基準法施行令23条に基づく階段の判定ロジック
    """
    # 判定基準のマスターデータ
    # 用途に応じて: (最小幅, 最小踏面, 最大蹴上げ)
    RULES = {
        "primary_school": {"min_w": 1400, "min_t": 260, "max_r": 160}, # 小学校
        "public_use":     {"min_w": 1500, "min_t": 300, "max_r": 160}, # 集会場・店舗等
        "dwelling":       {"min_w": 750,  "min_t": 150, "max_r": 230}, # 直通階段以外の住宅
        "other":          {"min_w": 1400,  "min_t": 210, "max_r": 200}, # その他
    }

    # 用途が見つからない場合は「その他」を適用
    rule = RULES.get(building_type, RULES["other"])

    results = []
    is_ok = True

    # 幅のチェック
    if width < rule["min_w"]:
        results.append(f"× 幅不足: {width}mm (基準: {rule['min_w']}mm以上)")
        is_ok = False
    else:
        results.append(f"○ 幅適合: {width}mm")

    # 踏面のチェック
    if tread < rule["min_t"]:
        results.append(f"× 踏面不足: {tread}mm (基準: {rule['min_t']}mm以上)")
        is_ok = False
    else:
        results.append(f"○ 踏面適合: {tread}mm")

    # 蹴上げのチェック
    if riser > rule["max_r"]:
        results.append(f"× 蹴上げ過大: {riser}mm (基準: {rule['max_r']}mm以下)")
        is_ok = False
    else:
        results.append(f"○ 蹴上げ適合: {riser}mm")

    return {
        "is_all_ok": is_ok,
        "details": results
    }