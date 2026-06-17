def check_duplicate_id(emp_id: str, attendance_book: list) -> bool:
    """
    Helper function: Kiểm tra mã nhân viên đã tồn tại chưa.
    """
    return any(emp["id"].strip().upper() == emp_id.strip().upper() for emp in attendance_book)


def clock_in(attendance_book: list) -> None:
    """
    Chức năng 2: Tiếp nhận thông tin chấm công đầu ngày (Clock-in).
    """
    print("\n--- CHẤM CÔNG VÀO (CLOCK-IN) ---")
    emp_id = input("Nhập mã nhân viên: ").strip().upper()
    
    if check_duplicate_id(emp_id, attendance_book):
        print(f"🔴 LỖI: Mã nhân viên {emp_id} đã được chấm công vào trước đó!")
        return

    name = input("Nhập tên nhân viên: ").strip()
    time_in = input("Nhập giờ vào (HH:MM): ").strip()

    # Kiểm tra định dạng giờ vào cơ bản bằng độ dài và ký tự phân tách
    if len(time_in) != 5 or ":" not in time_in:
        print("🔴 LỖI: Định dạng giờ vào không hợp lệ. Vui lòng nhập đúng chuẩn HH:MM.")
        return

    # Khởi tạo bản ghi mới với tuple chứa giờ Out là None
    new_record = {
        "id": emp_id,
        "name": name,
        "times": (time_in, None)
    }
    attendance_book.append(new_record)
    print(f"🟢 THÀNH CÔNG: Đã ghi nhận {emp_id} chấm công vào lúc {time_in}!")


def clock_out(attendance_book: list) -> None:
    """
    Chức năng 3: Chấm công kết thúc ca làm việc (Clock-out).
    Kỹ thuật: Tạo tuple mới để ghi đè thuộc tính 'times'.
    """
    print("\n--- CHẤM CÔNG RA (CLOCK-OUT) ---")
    emp_id = input("Nhập mã nhân viên cần chấm công ra: ").strip().upper()

    target_emp = None
    for emp in attendance_book:
        if emp["id"] == emp_id:
            target_emp = emp
            break

    if target_emp is None:
        print(f"🔴 LỖI: Không tìm thấy hồ sơ của nhân viên {emp_id} trong ngày hôm nay.")
        return

    time_out = input("Nhập giờ ra (HH:MM): ").strip()
    if len(time_out) != 5 or ":" not in time_out:
        print("🔴 LỖI: Định dạng giờ ra không hợp lệ. Vui lòng nhập đúng chuẩn HH:MM.")
        return

    # Xử lý Tuple cốt lõi: Lấy lại giờ vào cũ, tạo một tuple hoàn toàn mới và ghi đè
    time_in_old = target_emp["times"][0]
    target_emp["times"] = (time_in_old, time_out)
    
    print(f"🟢 THÀNH CÔNG: Đã ghi nhận nhân viên {emp_id} ra lúc {time_out}!")