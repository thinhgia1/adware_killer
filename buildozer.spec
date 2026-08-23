[app]

# Tên ứng dụng của bạn
title = Adware Killer

# Tên package
package.name = adwarekiller

# Tên miền package
package.domain = org.thinh

# Các định dạng file nguồn đi kèm
source.include_exts = py,png,jpg,kv,atlas

# Các thư viện Python cần thiết
requirements = python3,kivy,pyjnius

# Phiên bản ứng dụng
version = 0.1

# Hướng màn hình chính
orientation = portrait

# Quyền truy cập Android
android.permissions = INTERNET

# Cấu hình API và Build Tools chuẩn ổn định (tránh lỗi bản quyền bản 37)
android.api = 33
android.min_api = 21
android.build_tools_version = 33.0.2

# Kiến trúc chip hỗ trợ (giúp file chạy mượt trên hầu hết các dòng máy Android)
android.archs = arm64-v8a, armeabi-v7a

android.skip_target_api_compatibility_check = True
