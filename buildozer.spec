[app]

# Tên ứng dụng của bạn
title = Adware Killer

# Tên package
package.name = adwarekiller

# Tên miền package
package.domain = org.thinh

# Thư mục chứa mã nguồn
source.dir = .

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

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android build tools version to use
android.build_tools_version = 30.0.3

# Tự động đồng ý cấp phép SDK để tránh lỗi thiếu Aidl
android.accept_sdk_license = True

# Kiến trúc chip hỗ trợ
android.archs = arm64-v8a, armeabi-v7a

android.skip_target_api_compatibility_check = True
