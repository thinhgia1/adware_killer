from jnius import autoclass
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

# Import các lớp Java của Android
PythonActivity = autoclass("org.kivy.android.PythonActivity")
Intent = autoclass("android.content.Intent")
Settings = autoclass("android.provider.Settings")
Uri = autoclass("android.net.Uri")
Context = autoclass("android.content.Context")
UsageStatsManager = autoclass("android.app.usage.UsageStatsManager")
PackageManager = autoclass("android.content.pm.PackageManager")


class AdwareKillerApp(App):

  def build(self):
    self.title = "Tool Xóa Quảng Cáo Android"

    # Giao diện chính
    layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

    self.status_label = Label(
        text="Trạng thái: Đang kiểm tra quyền...",
        size_hint_y=None,
        height=50,
        color=(1, 1, 0, 1),
    )
    layout.add_widget(self.status_label)

    # Nút cấp quyền truy cập thống kê
    btn_permission = Button(
        text="1. Cấp Quyền Truy Cập Thông Tin",
        size_hint_y=None,
        height=50,
        background_color=(0, 0.5, 1, 1),
    )
    btn_permission.bind(on_press=self.open_usage_settings)
    layout.add_widget(btn_permission)

    # Khu vực hiển thị app đang chạy
    self.info_label = Label(
        text="Ứng dụng nghi vấn đang mở:\n(Chưa phát hiện)",
        size_hint_y=None,
        height=120,
        color=(0, 1, 0, 1),
    )
    layout.add_widget(self.info_label)

    # Nút quét và gỡ app
    btn_scan = Button(
        text="2. Liệt Kê & Gỡ App Cài Thêm",
        size_hint_y=None,
        height=50,
        background_color=(1, 0.3, 0.3, 1),
    )
    btn_scan.bind(on_press=self.list_installed_apps)
    layout.add_widget(btn_scan)

    # Danh sách app hiển thị cuộn
    self.scroll = ScrollView()
    self.app_list_layout = BoxLayout(
        orientation="vertical", size_hint_y=None, spacing=5
    )
    self.app_list_layout.bind(
        minimum_height=self.app_list_layout.setter("height")
    )
    self.scroll.add_widget(self.app_list_layout)
    layout.add_widget(self.scroll)

    # Kiểm tra quyền khi khởi động
    Clock.schedule_once(self.check_permissions, 1)
    return layout

  def open_usage_settings(self, instance):
    """Mở màn hình cài đặt hệ thống để bật quyền Usage Access"""
    activity = PythonActivity.mActivity
    intent = Intent(Settings.ACTION_USAGE_ACCESS_SETTINGS)
    activity.startActivity(intent)

  def check_permissions(self, dt):
    self.status_label.text = (
        "Trạng thái: Sẵn sàng. Nhớ cấp quyền dòng 1 nếu chưa bật!"
    )

  def list_installed_apps(self, instance):
    """Lấy danh sách các app người dùng cài thêm để gỡ"""
    self.app_list_layout.clear_widgets()
    activity = PythonActivity.mActivity
    pm = activity.getPackageManager()
    packages = pm.getInstalledPackages(PackageManager.GET_META_DATA)

    count = 0
    for i in range(packages.size()):
      p = packages.get(i)
      pkg_name = p.packageName
      # Lọc các app không phải hệ thống (app cài thêm)
      if (p.applicationInfo.flags & p.applicationInfo.FLAG_SYSTEM) == 0:
        count += 1
        btn = Button(
            text=f"Gỡ: {pkg_name}",
            size_hint_y=None,
            height=45,
            background_color=(0.2, 0.2, 0.2, 1),
        )
        # Gắn sự kiện gỡ app
        btn.bind(
            on_press=lambda x, p=pkg_name: self.uninstall_package_intent(p)
        )
        self.app_list_layout.add_widget(btn)

    self.status_label.text = (
        f"Tìm thấy {count} ứng dụng cài thêm có thể là rác."
    )

  def uninstall_package_intent(self, pkg_name):
    """Gọi lệnh hệ thống Android để hiện bảng xác nhận gỡ bỏ app"""
    activity = PythonActivity.mActivity
    uri = Uri.parse(f"package:{pkg_name}")
    intent = Intent(Intent.ACTION_UNINSTALL_PACKAGE, uri)
    intent.putExtra(Intent.EXTRA_RETURN_RESULT, True)
    activity.startActivity(intent)


if __name__ == "__main__":
  AdwareKillerApp().run()

