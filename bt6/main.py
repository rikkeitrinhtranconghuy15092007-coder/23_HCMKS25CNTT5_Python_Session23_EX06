# Thực hiện Import các hàm chức năng và đặt bí danh trực quan
from hrm_package.ui_display import display_records as view_book
from hrm_package.attendance_logic import clock_in as action_in, clock_out as action_out
from hrm_package.time_calc import evaluate_flex_time as analyze_book

# Khởi tạo Mock Data ban đầu theo đặc tả yêu cầu nghiệp vụ
attendance_book = [
    {"id": "NV01", "name": "Nguyễn Văn A", "times": ("08:30", "17:30")},
    {"id": "NV02", "name": "Trần Thị B", "times": ("09:30", None)},
    {"id": "NV03", "name": "Lê Văn C", "times": ("10:15", "19:15")}
]

def main():
    while True:
        print("\n=== HỆ THỐNG CHẤM CÔNG RIKKEI (FLEX-TIME) ===")
        print("1. Xem bảng chấm công ngày")
        print("2. Chấm công Vào (Clock-in)")
        print("3. Chấm công Ra (Clock-out)")
        print("4. Đánh giá vi phạm")
        print("5. Thoát chương trình")
        print("=================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            view_book(attendance_book)
        elif choice == "2":
            action_in(attendance_book)
        elif choice == "3":
            action_out(attendance_book)
        elif choice == "4":
            analyze_book(attendance_book)
        elif choice == "5":
            print("\nCảm ơn bạn đã sử dụng hệ thống điều hành Rikkei HRM. Tạm biệt!")
            break
        else:
            print("🔴 CẢNH BÁO: Lựa chọn không hợp lệ. Vui lòng nhập lại số từ 1 đến 5.")

if __name__ == "__main__":
    main()