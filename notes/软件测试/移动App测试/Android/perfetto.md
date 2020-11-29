# perfetto

使用 perfetto 工具，您可以通过 Android 调试桥 (ADB) 在 Android 设备上收集性能信息。perfetto 从您的设备上收集性能跟踪数据时会使用多种来源，例如：

- 使用 ftrace 收集内核信息
- 使用 atrace 收集服务和应用中的用户空间注释
- 使用 heapprofd 收集服务和应用的本地内存使用情况信息

本页介绍了如何调用 perfetto 并对其进行配置，以生成所需的输出。

> 参考官方文档 [perfetto](https://developer.android.google.cn/studio/command-line/perfetto)