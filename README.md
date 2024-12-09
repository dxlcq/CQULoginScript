# **重庆大学校园网登录脚本**


**为什么？**

* 重庆大学的校园网只允许一个账号在一台桌面设备与一台移动设备上同时登录

**是什么？**

* 一个账号在两台桌面设备上同时登录
* 可以通过系统的计划任务实现自动登录

**不是什么？**

* 突破校园网的资费/带宽限制

**如何使用？**

```shell
python cqu.py 账号 密码 客户端
```

* 账号：学号

* 密码：校园网密码

* 客户端：

    * `0`：桌面端

    * `1`：移动端

> 此脚本原理非常简单，如果有相关疑问，建议寻求周围 cs 专业的同学帮助