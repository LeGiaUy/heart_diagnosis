def infer_heart_disease(symptoms):
    rules = [
        # 🟥 Nhóm 1: Bệnh mạch vành
        ({"đau ngực", "khó thở", "tim đập nhanh"}, "Bệnh mạch vành"),
        ({"mệt mỏi", "huyết áp cao", "đau thắt ngực"}, "Bệnh mạch vành"),
        ({"chóng mặt", "tức ngực", "mệt mỏi"}, "Thiếu máu cơ tim"),
        ({"tiền sử gia đình bệnh tim", "huyết áp cao", "đau đầu"}, "Nguy cơ bệnh mạch vành"),
        ({"đau thắt ngực", "mệt mỏi", "đổ mồ hôi"}, "Bệnh động mạch vành"),
        ({"khó thở khi vận động", "đau ngực", "buồn nôn"}, "Bệnh mạch vành mãn tính"),
        ({"mệt mỏi", "tăng huyết áp", "tê bì chân tay"}, "Nguy cơ tắc nghẽn mạch máu"),
        ({"đau đầu", "chóng mặt", "mất ngủ"}, "Nguy cơ bệnh mạch vành nhẹ"),
        ({"đau thắt ngực", "mệt mỏi", "buồn nôn"}, "Cơn đau thắt ngực ổn định"),
        ({"đau ngực khi gắng sức", "khó thở", "tim đập nhanh"}, "Cơn đau thắt ngực không ổn định"),
        ({"đau ngực", "khó thở", "chóng mặt"}, "Bệnh mạch vành tiến triển"),
        ({"huyết áp cao", "tức ngực", "mệt mỏi"}, "Nguy cơ bệnh mạch vành cấp tính"),
        ({"khó thở", "đau thắt ngực", "tê bì chân tay"}, "Bệnh động mạch vành mãn tính"),
        ({"mất ý thức", "chóng mặt", "tức ngực"}, "Cơn đau tim nhẹ"),
        ({"khó thở về đêm", "mệt mỏi", "đau thắt ngực"}, "Bệnh động mạch vành nguy hiểm"),

        # 🟩 Nhóm 2: Suy tim
        ({"khó thở", "phù chân", "mệt mỏi vào ban đêm"}, "Suy tim giai đoạn nặng"),
        ({"ho kéo dài", "mệt mỏi", "khó thở về đêm"}, "Suy tim do ứ dịch"),
        ({"khó thở khi nằm", "tím môi", "mệt mỏi"}, "Suy tim do thiếu oxy"),
        ({"tăng huyết áp", "đau đầu", "khó thở"}, "Nguy cơ suy tim do huyết áp cao"),
        ({"khó thở khi vận động", "mệt mỏi kéo dài", "phù chân"}, "Suy tim sung huyết"),
        ({"tim đập nhanh", "mệt mỏi", "tím môi"}, "Suy tim cấp tính"),
        ({"mệt mỏi kéo dài", "chóng mặt", "tím tay chân"}, "Suy tim giai đoạn đầu"),
        ({"đau ngực", "khó thở về đêm", "mất ngủ"}, "Nguy cơ suy tim nhẹ"),
        ({"tức ngực", "phù chân", "khó thở khi nằm"}, "Suy tim sung huyết nặng"),
        ({"mệt mỏi", "khó thở khi leo cầu thang", "tăng cân đột ngột"}, "Suy tim do ứ nước"),
        ({"khó thở khi leo cầu thang", "mệt mỏi kéo dài", "tím môi"}, "Suy tim tiềm ẩn"),
        ({"mệt mỏi kéo dài", "chóng mặt", "phù chân"}, "Suy tim giai đoạn đầu"),
        ({"tím môi", "mất ngủ", "khó thở"}, "Suy tim mãn tính"),
        ({"tăng cân đột ngột", "phù chân", "khó thở"}, "Suy tim do ứ nước"),

        # 🟦 Nhóm 3: Rối loạn nhịp tim
        ({"tim đập nhanh", "mệt mỏi", "chóng mặt khi đứng dậy"}, "Nhịp tim nhanh"),
        ({"tim đập chậm", "chóng mặt", "mệt mỏi vào buổi sáng"}, "Nhịp tim chậm"),
        ({"hồi hộp", "đánh trống ngực", "huyết áp thấp"}, "Rối loạn nhịp tim nhẹ"),
        ({"huyết áp thấp", "chóng mặt", "tim đập nhanh"}, "Rối loạn nhịp tim nguy hiểm"),
        ({"tim đập chậm", "tức ngực", "mệt mỏi"}, "Rối loạn nhịp tim mãn tính"),
        ({"huyết áp không ổn định", "đánh trống ngực", "mệt mỏi"}, "Loạn nhịp tim do huyết áp thất thường"),
        ({"tim đập nhanh", "ra mồ hôi", "chóng mặt"}, "Nhịp tim nhanh cơn kịch phát"),
        ({"chóng mặt khi thay đổi tư thế", "hồi hộp", "tim đập nhanh"}, "Nhịp tim bất thường"),
        ({"ngất xỉu", "tim đập chậm", "mệt mỏi"}, "Rối loạn dẫn truyền nhịp tim"),
        ({"đánh trống ngực", "chóng mặt", "khó thở"}, "Rối loạn nhịp tim nhanh nguy hiểm"),
        ({"huyết áp thấp", "chóng mặt", "tim đập nhanh"}, "Rối loạn nhịp tim nguy hiểm"),
        ({"tim đập chậm", "tức ngực", "mệt mỏi"}, "Rối loạn nhịp tim mãn tính"),
        ({"tim đập nhanh", "ra mồ hôi", "chóng mặt"}, "Nhịp tim nhanh cơn kịch phát"),

        # 🟧 Nhóm 4: Huyết áp bất thường
        ({"huyết áp cao", "đau đầu vào buổi sáng", "mệt mỏi"}, "Tăng huyết áp mãn tính"),
        ({"huyết áp thấp", "chóng mặt khi thay đổi tư thế", "mệt mỏi"}, "Huyết áp thấp tư thế đứng"),
        ({"đau đầu", "tê bì chân tay", "huyết áp cao"}, "Nguy cơ huyết áp cao nguy hiểm"),
        ({"huyết áp cao", "tức ngực", "mệt mỏi"}, "Tăng huyết áp nguy cơ suy tim"),
        ({"huyết áp không ổn định", "chóng mặt", "buồn nôn"}, "Huyết áp dao động thất thường"),
        ({"huyết áp cao", "mất ngủ", "đau đầu"}, "Tăng huyết áp nhẹ"),
        ({"huyết áp thấp", "tim đập nhanh", "chóng mặt"}, "Huyết áp thấp nguy hiểm"),
        ({"tăng huyết áp", "mệt mỏi", "khó thở"}, "Nguy cơ tăng huyết áp cấp tính"),
        ({"huyết áp không ổn định", "chóng mặt", "mệt mỏi"}, "Rối loạn huyết áp"),
        ({"tức ngực", "huyết áp cao", "đau đầu dữ dội"}, "Cơn tăng huyết áp cấp tính"),
        

        # 🟨 Nhóm 5: Rối loạn tuần hoàn não
        ({"hoa mắt", "chóng mặt", "tê bì chân tay"}, "Rối loạn tuần hoàn não mãn tính"),
        ({"đau đầu dữ dội", "mất thăng bằng", "mờ mắt"}, "Nguy cơ đột quỵ nhẹ"),
        ({"mất ý thức", "huyết áp cao", "mệt mỏi"}, "Rối loạn tuần hoàn não nguy hiểm"),
        ({"tê tay", "mệt mỏi", "chóng mặt"}, "Thiếu máu não nhẹ"),
        ({"mất ngủ", "đau đầu", "chóng mặt"}, "Thiếu máu não mãn tính"),
        ({"mất ý thức", "chóng mặt kéo dài", "huyết áp cao"}, "Đột quỵ nhẹ"),
        ({"chóng mặt", "mờ mắt", "mệt mỏi"}, "Rối loạn tuần hoàn máu lên não"),
        ({"tức ngực", "đau đầu", "chóng mặt"}, "Thiếu oxy não"),
        ({"mất ý thức", "chóng mặt", "mệt mỏi"}, "Nguy cơ rối loạn tuần hoàn não"),
        ({"tê bì chân tay", "huyết áp thấp", "chóng mặt"}, "Thiếu máu não nặng"),
        ({"mất ý thức", "huyết áp cao", "mệt mỏi"}, "Rối loạn tuần hoàn não nguy hiểm"),
        ({"tê tay", "mệt mỏi", "chóng mặt"}, "Thiếu máu não nhẹ"),
     
        # 🟠 Nhóm 6: Viêm màng ngoài tim
        ({"đau ngực", "sốt", "khó thở"}, "Viêm màng ngoài tim"),
        ({"đau ngực", "mệt mỏi", "sốt"}, "Viêm màng ngoài tim cấp tính"),
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
