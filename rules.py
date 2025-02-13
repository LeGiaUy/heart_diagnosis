def infer_heart_disease(symptoms):
    rules = [
        # 🟥 Nhóm 1: Bệnh mạch vành
        ({"đau ngực", "khó thở", "tê tay"}, "Bệnh mạch vành"),
        ({"đau ngực", "mệt mỏi", "đánh trống ngực"}, "Bệnh mạch vành"),
        ({"đau thắt ngực", "khó thở", "chóng mặt"}, "Bệnh mạch vành"),
        ({"đau ngực", "tiền sử gia đình bệnh tim", "huyết áp cao"}, "Bệnh mạch vành"),
        ({"chế độ ăn uống không lành mạnh", "huyết áp cao", "đau ngực"}, "Bệnh mạch vành"),
        ({"tuổi trên 50", "khó thở", "mệt mỏi"}, "Thiếu máu cơ tim"),
        ({"tim đập nhanh", "đau ngực", "mệt mỏi"}, "Nhồi máu cơ tim"),
        
        # 🟩 Nhóm 2: Suy tim
        ({"mệt mỏi", "khó thở", "phù chân"}, "Suy tim"),
        ({"khó thở", "tức ngực", "môi tím tái"}, "Suy tim giai đoạn nặng"),
        ({"mệt mỏi", "khó thở", "ho kéo dài"}, "Suy tim mãn tính"),
        ({"khó thở về đêm", "phù chân", "mệt mỏi"}, "Suy tim giai đoạn nặng"),
        ({"tăng huyết áp", "khó thở", "mệt mỏi"}, "Suy tim do tăng huyết áp"),
        ({"tuổi trên 50", "khó thở", "mệt mỏi"}, "Suy tim do tuổi già"),
        
        # 🟦 Nhóm 3: Rối loạn nhịp tim
        ({"đánh trống ngực", "hoa mắt", "chóng mặt"}, "Rối loạn nhịp tim"),
        ({"mệt mỏi", "huyết áp thấp", "đánh trống ngực"}, "Rối loạn nhịp tim"),
        ({"tức ngực", "tim đập nhanh", "chóng mặt"}, "Ngoại tâm thu"),
        ({"tim đập nhanh", "khó thở", "hồi hộp"}, "Nhịp tim nhanh"),
        ({"tim đập chậm", "mệt mỏi", "chóng mặt"}, "Nhịp tim chậm"),
        ({"giới tính nam", "tim đập nhanh", "chóng mặt"}, "Nhịp tim nhanh nguy hiểm"),
        ({"giới tính nữ", "mệt mỏi", "huyết áp thấp"}, "Rối loạn nhịp tim do huyết áp thấp"),
        
        # 🟧 Nhóm 4: Huyết áp bất thường
        ({"huyết áp cao", "đau đầu", "mệt mỏi"}, "Tăng huyết áp"),
        ({"huyết áp thấp", "chóng mặt", "mất ý thức"}, "Huyết áp thấp"),
        ({"huyết áp thấp", "tê bì chân tay", "hoa mắt"}, "Huyết áp thấp kéo dài"),
        ({"đau đầu buổi sáng", "mờ mắt", "huyết áp cao"}, "Tăng huyết áp nguy hiểm"),
        ({"tiền sử gia đình bệnh tim", "huyết áp cao", "chóng mặt"}, "Nguy cơ tăng huyết áp di truyền"),
        
        # 🟨 Nhóm 5: Rối loạn tuần hoàn não
        ({"tê tay", "hoa mắt", "chóng mặt"}, "Rối loạn tuần hoàn não"),
        ({"đau đầu", "khó thở", "buồn nôn"}, "Rối loạn tuần hoàn não"),
        ({"mờ mắt", "mất thăng bằng", "chóng mặt"}, "Rối loạn tuần hoàn não"),
        ({"mệt mỏi", "chóng mặt", "mất ý thức"}, "Nguy cơ đột quỵ"),
        ({"giới tính nam", "huyết áp cao", "chóng mặt"}, "Rối loạn tuần hoàn não nguy hiểm"),
        
        # 🟠 Nhóm 6: Viêm màng ngoài tim
        ({"đau ngực", "sốt", "khó thở"}, "Viêm màng ngoài tim"),
        ({"đau nhói ngực", "mệt mỏi", "sốt"}, "Viêm màng ngoài tim cấp tính"),
        ({"khó thở", "đau ngực khi nằm", "mệt mỏi"}, "Viêm màng ngoài tim mãn tính"),
        
        # ⚫ Nhóm 7: Nguy cơ đột quỵ
        ({"nói lắp", "yếu liệt tay chân", "chóng mặt"}, "Dấu hiệu đột quỵ sớm"),
        ({"huyết áp cao", "đau đầu", "chóng mặt"}, "Nguy cơ đột quỵ do tăng huyết áp"),
        ({"tuổi trên 50", "mất ý thức", "huyết áp cao"}, "Đột quỵ nguy hiểm"),
    ]

    diagnoses = set()
    for rule_symptoms, result in rules:
        if rule_symptoms.issubset(symptoms):
            diagnoses.add(result)  # Nhóm bệnh không trùng lặp

    return list(diagnoses) if diagnoses else ["Không có dấu hiệu bệnh tim"]
