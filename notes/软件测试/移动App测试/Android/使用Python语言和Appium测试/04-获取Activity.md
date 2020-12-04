# 获取Android App 的 Activity

## 已安装在设备上的App

```sh
# < Android 8.0
adb dumpsys activity activities | grep mFocusedActivity

# >= Android 8.0
adb shell dumpsys activity activities| grep mResumeActivity

# activities 好像可以省略，反正我没加activities也能行
adb shell dumpsys activity | grep mResumeActivity

#  mResumedActivity 可以只写开头的mResume，反正这个字段打头的只有一行
adb shell dumpsys activity | grep mResume

```
> Windows上可以将grep换成findstr

## apk文件

```sh
adb dump badging *.apk
```