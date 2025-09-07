# 希沃管家 V2 密码解码工具
工具在本地运行，不获取您的隐私数据。[下载工具](https://yuyudifiesh.github.io/seewo-adminpassword-v2/SeewoPassv2_GUI_clean.exe)

>  **工具仅可用于希沃管家 `1.4.6.3588` 及以下版本，运行脚本前请您先安装并配置 Python 环境。**
>
> [点击此处下载 Python 安装包（python-3.13.5-amd64）](https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe)
>
> [点击此处下载 希沃管家 安装包（SeewoService_1.4.6）](https://soft.wsyhn.com/soft/SeewoService_1.4.6.exe)

## 文件说明
脚本会自动拉起希沃管家集控配置文件，您需要找到 `PASSWORDV2` 或者 `LockPasswardV2` 的值。

如果您是覆盖安装，那么一个标准的配置文件应该看起来像这样：

>  **注意：部分值的内容涉及集控安全，在如下示例中不会显示。**

### 管理员密码配置文件 `SeewoCore.ini`
```ini
[ADMIN]
PASSWORDV2=191292355c5e7f57  <-- 您需要记录的值
PASSWORDV3=9c31e6ddc98199a8a161292d2bb240356616f0a75081f0db0adeb10615b5628873c2c3753fd2831080d23f8b83409d23
[BIND-CACHE]
school-code=示例内容不显示
school-name=测试学校
[GUARD]
TIME_DELAY_GUARD=30
[PERMISSION]
FREEZE=yes
[device]
id=示例内容不显示
```

### 屏幕锁密码配置文件 `SeewoLockConfig.ini`
```ini
BindSchoolStatus=yes
DeviceId=示例内容不显示
EnablePowerOnLock=no
FinishClassLockStatus=no
LockPasswardV2=191292355c5e7f57 <-- 您需要记录的值
LockPasswardV3=00431c5a6b2fc52f31d59ac847ce06566ffc2155e0d97301321393e8c4ec1c6e4fe34ad125f8bfc15304230d536ee2a2
LockStatus=no
OperationLogId=示例内容不显示
SmartLockTime=0
UnlockMode=0
[Wallpaper]
PictureSizeType=0
Source=
Status=no
SwitchInterval=0
```

<div align="center">Copyright © 2025 Yuyudifiesh</div>
