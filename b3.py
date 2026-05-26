# C1: Phân tích Input / Output
# - Input:
#   + order_list: danh sách mã đơn hàng kiểu list.
#   + choice: dữ liệu người dùng nhập từ bàn phím để chọn menu.
#   + order_code: mã đơn hàng nhập vào để thêm hoặc xóa.
#
# - Output:
#   + Hiển thị danh sách đơn hàng hiện tại.
#   + Hiển thị danh sách sau khi thêm đơn hàng mới.
#   + Hiển thị kết quả xóa đơn hàng.
#   + Thông báo nếu danh sách rỗng.
#   + Thông báo lỗi nếu nhập sai menu hoặc mã đơn hàng không tồn tại.


# C2: Đề xuất giải pháp
# - Dùng list để lưu danh sách đơn hàng.
# - Dùng while True để tạo menu chạy liên tục.
# - Dùng input() để nhận lựa chọn từ người dùng.
# - Dùng isdigit() và range(1,5) để kiểm tra menu hợp lệ.
# - Dùng strip() để xóa khoảng trắng thừa ở mã đơn hàng.
# - Dùng upper() để chuẩn hóa mã đơn hàng thành chữ hoa.
# - Dùng append() để thêm đơn hàng mới vào cuối danh sách.
# - Dùng remove() để xóa đơn hàng theo giá trị.
# - Dùng toán tử in để kiểm tra mã đơn hàng có tồn tại hay không.
# - Dùng len(order_list) hoặc if not order_list để kiểm tra danh sách rỗng.
# - Dùng enumerate() để hiển thị danh sách có đánh số thứ tự.


# C3: Thiết kế thuật toán / Mô tả luồng chương trình
# B1: Khởi tạo danh sách order_list.
# B2: Hiển thị menu bằng vòng lặp while True.
# B3: Người dùng nhập choice.
# B4: Nếu choice không hợp lệ:
#       - In thông báo lỗi
#       - Quay lại menu
# B5: Nếu chọn 1:
#       - Kiểm tra danh sách có rỗng không
#       - Nếu rỗng -> báo danh sách trống
#       - Nếu có dữ liệu -> duyệt và in danh sách
# B6: Nếu chọn 2:
#       - Nhập mã đơn hàng mới
#       - Chuẩn hóa bằng strip().upper()
#       - Thêm vào danh sách bằng append()
# B7: Nếu chọn 3:
#       - Nhập mã đơn hàng cần xóa
#       - Chuẩn hóa dữ liệu
#       - Kiểm tra mã có tồn tại không
#       - Nếu có -> remove()
#       - Nếu không -> báo không tìm thấy

order_list = ["GE001", "GE002", "GE003"]
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    if not choice.isdigit() or int(choice) not in range(1, 5):
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    if choice == 1:
        if not order_list:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("\nDanh sách đơn hàng hiện tại:")
            for index, order in enumerate(order_list, start=1):
                print(f"{index}. {order}")

    elif choice == 2:
        new_order = input("Nhập mã đơn hàng mới: ")

        new_order = new_order.strip().upper()

        if new_order == "":
            print("Mã đơn hàng không được để trống!")
            continue
        order_list.append(new_order)

        print("Thêm đơn hàng thành công!")
        print("Danh sách hiện tại:", order_list)

    elif choice == 3:
        delete_order = input("Nhập mã đơn hàng cần xóa: ")

        delete_order = delete_order.strip().upper()

        if delete_order in order_list:
            order_list.remove(delete_order)
            print("Xóa đơn hàng thành công!")
            print("Danh sách hiện tại:", order_list)
        else:
            print("Không tìm thấy mã đơn hàng cần xóa!")

    elif choice == 4:
        print("Thoát chương trình.")
        break