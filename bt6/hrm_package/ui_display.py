from tabulate import tabulate

def display_records(attendance_book: list) -> None:
    """
    Chức năng 1: Định dạng dữ liệu thô và in bảng chấm công ngày.
    """
    print("\n" + "="*23 + " BẢNG CHẤM CÔNG CÔNG TY " + "="*23)
    if not attendance_book:
        print("[INFO] Bảng chấm công hiện tại trống.")
        return

    # Chuẩn bị dữ liệu hiển thị (Bọc cấu trúc Tuple/None thành chuỗi giao diện)
    table_data = []
    for emp in attendance_book:
        clock_in, clock_out = emp["times"]
        display_out = clock_out if clock_out is not None else "[Đang làm việc]"
        
        table_data.append([emp["id"], emp["name"], clock_in, display_out])

    # Thiết lập tiêu đề cột cho bảng
    headers = ["Mã NV", "Tên Nhân Viên", "Giờ Vào", "Giờ Ra"]
    
    # In bảng bằng tabulate theo style đơn giản (simple)
    print(tabulate(table_data, headers=headers, tablefmt="simple", stralign="left"))
    print("=" * 70)