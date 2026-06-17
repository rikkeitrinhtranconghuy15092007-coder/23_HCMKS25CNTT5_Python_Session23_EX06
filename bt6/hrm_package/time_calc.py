from datetime import datetime

def evaluate_flex_time(attendance_book: list) -> None:
    """
    Chức năng 4: Đánh giá tình trạng vi phạm giờ giấc dựa theo luật Flex-Time.
    Luật: Đi muộn tối đa 90 phút (đến 10:00) nhưng phải bù đủ 9 tiếng làm việc.
    """
    print("\n" + "-"*15 + " KẾT QUẢ ĐÁNH GIÁ VI PHẠM FLEX-TIME " + "-"*15)
    
    # Biến mốc giới hạn 10:00 thành đối tượng datetime để so sánh toán học
    deadline_in = datetime.strptime("10:00", "%H:%M")
    has_records = False

    for emp in attendance_book:
        clock_in_str, clock_out_str = emp["times"]
        
        # Chỉ đánh giá khi nhân viên đã chấm công đầy đủ cả Vào và Ra
        if clock_in_str and clock_out_str:
            has_records = True
            
            # Ép kiểu dữ liệu chuỗi sang datetime object
            in_time = datetime.strptime(clock_in_str, "%H:%M")
            out_time = datetime.strptime(clock_out_str, "%H:%M")
            
            # Tính hiệu số thời gian di chuyển (Thời gian thực tế tại công ty)
            total_duration = out_time - in_time
            total_seconds = total_duration.total_seconds()
            hours_worked = total_seconds / 3600

            # Luồng kiểm tra 1: Kiểm tra giờ vào làm
            if in_time > deadline_in:
                print(f"❌ {emp['id']} - {emp['name']:<15} | Vi phạm: Đến muộn quá 90 phút ({clock_in_str}).")
            
            # Luồng kiểm tra 2: Giờ vào hợp lệ nhưng về sớm (chưa đủ 9 tiếng làm việc bao gồm nghỉ trưa)
            elif hours_worked < 9.0:
                print(f"⚠️ {emp['id']} - {emp['name']:<15} | Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ (Mới làm: {hours_worked:.2f}h).")
            
            # Luồng kiểm tra 3: Đáp ứng hoàn hảo luật Flex-time
            else:
                print(f"✅ {emp['id']} - {emp['name']:<15} | Hợp lệ: Hoàn thành ca làm việc ({hours_worked:.2f}h).")
                
    if not has_records:
        print("[INFO] Chưa có nhân viên nào hoàn thành đủ chu kỳ (In - Out) để đánh giá.")
        
    print("-" * 66)