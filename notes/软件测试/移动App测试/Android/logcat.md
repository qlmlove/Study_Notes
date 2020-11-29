# Logcat 命令行工具

Logcat 是一个命令行工具，用于转储系统消息日志，包括设备抛出错误时的堆栈轨迹，以及从您的应用使用 Log 类写入的消息。

本页介绍了命令行 Logcat 工具，但在 Android Studio 中，您也可以从 Logcat 窗口查看日志消息。如需了解如何在 Android Studio 中查看和过滤日志。

> 具体参考官方文档 [Logcat 命令行工具](https://developer.android.google.cn/studio/command-line/logcat)

[toc]

## 命令行语法
如需通过 adb shell 运行 Logcat，一般用法如下：

```sh
[adb] logcat [<option>] ... [<filter-spec>] ...
```

### 选项参考官方文档或者 `adb logcat --help`
例如 `-v color` 彩色输出
## 过滤日志输出

- 日志消息的标记是一个简短的字符串，指示消息所源自的系统组件（例如，“View”表示视图系统）。
- 优先级是以下字符值之一（按照从最低到最高优先级的顺序排列）：
    - V：详细（最低优先级）
    - D：调试
    - I：信息
    - W：警告
    - E：错误
    - F：严重错误
    - S：静默（最高优先级，绝不会输出任何内容）
通过运行 Logcat 并观察每条消息的前两列，您可以获取系统中使用的带有优先级的标记列表，格式为 <priority>/<tag>。

以下是使用 logcat -v brief output 命令获取的简短 Logcat 输出的示例。它表明消息与优先级“I”和标记“ActivityManager”相关：

```
I/ActivityManager(  585): Starting activity: Intent { action=android.intent.action...}
```
如要将日志输出降低到可管理的水平，您可以使用过滤器表达式限制日志输出。通过过滤器表达式，您可以向系统指明您感兴趣的标记/优先级组合，系统会针对指定的标记抑制其他消息。

过滤器表达式采用 `tag:priority ...` 格式，其中 tag 指示您感兴趣的标记，priority 指示可针对该标记报告的最低优先级。不低于指定优先级的标记的消息会写入日志。您可以在一个过滤器表达式中提供任意数量的 tag:priority 规范。一系列规范使用空格分隔。

以下是一个过滤器表达式的示例，该表达式会抑制除标记为“ActivityManager”、优先级不低于“信息”的日志消息，以及标记为“MyApp”、优先级不低于“调试”的日志消息以外的所有其他日志消息：

```
adb logcat ActivityManager:I MyApp:D *:S
```
上述表达式中最后一个元素 *:S 将所有标记的优先级设为“静默”，从而确保系统仅显示标记为“ActivityManager”和“MyApp”的日志消息。使用 *:S 是确保日志输出受限于您已明确指定的过滤器的绝佳方式，它可以让过滤器充当日志输出的“许可名单”。

以下过滤器表达式显示了优先级不低于“警告”的所有标记的所有日志消息：

```
adb logcat *:W
```
如果您从开发计算机运行 Logcat（相对于在远程 adb shell 上运行），则也可以通过导出环境变量 ANDROID_LOG_TAGS 的值设置默认过滤器表达式：

```
export ANDROID_LOG_TAGS="ActivityManager:I MyApp:D *:S"
```
请注意，如果您从远程 shell 或使用 adb shell logcat 运行 Logcat，系统不会将 ANDROID_LOG_TAGS 过滤器导出到模拟器/设备实例。

## 控制日志输出格式

除标记和优先级外，日志消息还包含许多元数据字段。您可以修改消息的输出格式，以便它们显示特定的元数据字段。为此，您可以使用 -v 选项，并指定下列某一受支持的输出格式。

- brief：显示优先级、标记以及发出消息的进程的 PID。
- long：显示所有元数据字段，并使用空白行分隔消息。
- process：仅显示 PID。
- raw：显示不包含其他元数据字段的原始日志消息。
- tag：仅显示优先级和标记。
- thread:：旧版格式，显示优先级、PID 以及发出消息的线程的 TID。
- threadtime（默认值）：显示日期、调用时间、优先级、标记、PID 以及发出消息的线程的 TID。
- time：显示日期、调用时间、优先级、标记以及发出消息的进程的 PID。

启动 Logcat 时，您可以使用 -v 选项指定所需的输出格式：

```
[adb] logcat [-v <format>]
```
以下示例显示了如何生成输出格式为 thread 的消息：

```
adb logcat -v thread
```
请注意，您只能使用 -v 选项指定一种输出格式，但可以指定任意数量的有意义的修饰符。Logcat 会忽略没有意义的修饰符。

## 格式修饰符
格式修饰符依据以下一个或多个修饰符的任意组合更改 Logcat 输出。如要指定格式修饰符，请使用 -v 选项，如下所示：

```
adb logcat -b all -v color -d
```
每个 Android 日志消息都有一个与之相关联的标记和优先级。您可以将任何格式修饰符与以下任一格式选项进行组合：brief、long、process、raw、tag、thread、threadtime 和 time。

您可以通过在命令行中输入 logcat -v --help 获取格式修饰符详细信息。

- color：使用不同的颜色来显示每个优先级。
- descriptive：显示日志缓冲区事件说明。此修饰符仅影响事件日志缓冲区消息，不会对其他非二进制文件缓冲区产生任何影响。事件说明取自 event-log-tags 数据库。
- epoch：显示自 1970 年 1 月 1 日以来的时间（以秒为单位）。
- monotonic：显示自上次启动以来的时间（以 CPU 秒为单位）。
- printable：确保所有二进制日志记录内容都进行了转义。
- uid：如果访问控制允许，则显示 UID 或记录的进程的 Android ID。
- usec：显示精确到微秒的时间。
- UTC：显示 UTC 时间。
- year：将年份添加到显示的时间。
- zone：将本地时区添加到显示的时间。

## 查看备用日志缓冲区
Android 日志记录系统为日志消息保留了多个环形缓冲区，而且并非所有的日志消息都会发送到默认的环形缓冲区。如要查看其他日志消息，您可以使用 -b 选项运行 logcat 命令，以请求查看备用的环形缓冲区。您可以查看下列任意备用缓冲区：

- radio：查看包含无线装置/电话相关消息的缓冲区。
- events：查看已经过解译的二进制系统事件缓冲区消息。
- main：查看主日志缓冲区（默认），不包含系统和崩溃日志消息。
- system：查看系统日志缓冲区（默认）。
- crash：查看崩溃日志缓冲区（默认）。
- all：查看所有缓冲区。
- default：报告 main、system 和 crash 缓冲区。

以下是 -b 选项的用法：

```
[adb] logcat [-b <buffer>]
```
以下示例显示了如何查看包含无线装置和电话相关消息的日志缓冲区。

```
adb logcat -b radio
```
此外，您也可以为要输出的所有缓冲区指定多个 -b 标记，如下所示：

```
logcat -b main -b radio -b events
```
您可以指定一个 -b 标记，后跟缓冲区逗号分隔列表，例如：

```
logcat -b main,radio,events
```

## 通过代码记录日志

通过 Log 类，您可以在代码中创建日志条目，而这些条目会显示在 Logcat 工具中。常用的日志记录方法包括：

- Log.v(String, String)（详细）
- Log.d(String, String)（调试）
- Log.i(String, String)（信息）
- Log.w(String, String)（警告）
- Log.e(String, String)（错误）

例如，使用以下调用：

```KOTLIN
Log.i("MyActivity", "MyClass.getView() — get item number $position")
```
Logcat 输出类似如下：

```
I/MyActivity( 1557): MyClass.getView() — get item number 1
```