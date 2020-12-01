# Desired Capabilities详解

Desired Capabilities是启动时候的必须参数。

> 参考官方文档 [Appium 服务器初始化参数（Capability）](http://appium.io/docs/cn/writing-running-appium/caps/)

## 必填参数
示例一
```json
{
  "platformName": "Android",
  "deviceName": "V1824A",
  "platformVersion": "10",
  "appPackage": "com.android.bbkcalculator",
  "appActivity": ".Calculator"
}
```

- platformName：平台名字，安卓默认填【Android】，iOS默认填【iOS】

- deviceName：设备名称，`adb devices -l`命令中的model字段，示例如下：
    ```powershell
    PS C:\Users\pinesnow> adb devices -l
    List of devices attached
    94dda289               device product:lineage_oneplus3 model:ONEPLUS_A3010 device:OnePlus3T transport_id:1
    ```
- platformVersion：平台版本，查看方式`adb shell getprop ro.build.version.release` 示例如下：
    ```powershell
    PS C:\Users\pinesnow> adb shell getprop ro.build.version.release
    10
    ```

- appPackage：包名
  - 已安装在手机上的包，手动打开APP后运行 `adb shell dumpsys activity | findstr mResume` 示例如下：
    ```powershell
    PS C:\Users\pinesnow> adb shell dumpsys activity | findstr mResume
    mResumedActivity: ActivityRecord{d749e77 u0 com.android.calculator2/.Calculator t71}
    # 其中 "com.android.calculator2" 就是 appPackage ，".Calculator" 就是 appActivity
    ```
  - apk文件，`aapt dump badging *.apk`，示例如下：（其中第一行就可以看到包名）
    ```powershell
    PS E:\code\python\appium\abc> aapt dump badging .\abc.apk
    package: name='com.xunyi.ptt.activity' versionCode='99' versionName='1.0' platformBuildVersionName='8.0.0'
    sdkVersion:'19'
    targetSdkVersion:'19'
    uses-permission: name='android.permission.INTERNET'
    uses-permission: name='android.permission.VIBRATE'
    uses-permission: name='android.permission.SYSTEM_ALERT_WINDOW'
    uses-permission: name='android.permission.MODIFY_AUDIO_SETTINGS'
    uses-permission: name='android.permission.RECORD_AUDIO'
    uses-permission: name='android.permission.RECEIVE_BOOT_COMPLETED'
    uses-permission: name='android.permission.WAKE_LOCK'
    uses-permission: name='android.permission.DISABLE_KEYGUARD'
    uses-permission: name='android.permission.GET_TASKS'
    uses-permission: name='android.permission.READ_LOGS'
    uses-permission: name='android.permission.ACCESS_NETWORK_STATE'
    ...
    ```