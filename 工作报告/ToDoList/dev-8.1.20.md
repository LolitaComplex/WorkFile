1. 新人入职后的引导
    - 新手任务：https://wiki.inkept.cn/pages/viewpage.action?pageId=110511571
    - 社招入职指南：https://wiki.inkept.cn/pages/viewpage.action?pageId=110500904
    - 客户端入职指引：https://wiki.inkept.cn/pages/viewpage.action?pageId=110522305
    - 新人培养计划：https://wiki.inkept.cn/pages/viewpage.action?pageId=110497009


报告：

> 1. 需求评审 （上一个版本最后两天，全用例之前）
> 2. worktile排期 （上一个版本全用例之前）
> 3. 开发周期（开发、联调、提测）
> 4. 过测试用例（保证P1 case通过）
> 5. bug修复、测试通过、代码Review、合版
> 6. 全用例
> 7. 灰度发版



2. 软声的小米Push问题
3. https://bugly.qq.com/v2/crash-reporting/crashes/900012289/13333873?pid=1 待修复
4. Push文档输出
5. 分享总结
- 6. 大厅最初选中第二个Tab的逻辑
- 7. 8120惩罚恶搞消除  需求
- 8. 动态封面调整 （4g支持动态封面），上线后同步给 【动态封面调整】群里
9. 小米图标的问题
10. WebView内存泄漏的额问题
11. 切换账号页面的遗留问题 http://s3.ikstatic.cn/client-log-1/log/118320313/Ingkee/1599670195573.1。 钉钉群名：账号列表请求失败
- 12. 方形头像（搜索列表）
13. 二维码分享点击时会有问题
- 14. PK结束后QA环境流不正常
15. 未处理的工单
16. 大厅刷新埋点数据异常
- 17. 812——注销-账号金融行为判断 群里的账号提示修改
18. MVP特效重叠与连送恶搞礼物数量对不上的问题
- 19. 母包要把报的信息添加到wiki文档中


-----------


技术记录：

1. `com.meelive.ingkee.business.room.roompk.Contract`
2. `UltraViewPagerView`，阿里的开源库 https://github.com/alibaba/UltraViewPager
3. 在linux中一个文件、一个串口、一个socket、一个线程都可以是一个文件，而一个文件会占用一个句柄，linux中一个进程默认的句柄最大数值是1024，当超过这个数值，linux就会对当前的进程进行kill，而kill的对象可以是任意对象，所以会造成各种异常原因的崩溃。https://blog.csdn.net/qq_33617079/article/details/82316606

> Buggly 异常：https://bugly.qq.com/v2/crash-reporting/crashes/900012289/10655805?pid=1
```log
# main(2)

java.lang.RuntimeException

Could not read input channel file descriptors from parcel.

解析原始
1 android.view.InputChannel.nativeReadFromParcel(Native Method)
2 android.view.InputChannel.readFromParcel(InputChannel.java:148)
3 android.view.IWindowSession$Stub$Proxy.addToDisplay(IWindowSession.java:804)
4 android.view.ViewRootImpl.setView(ViewRootImpl.java:755)
5 android.view.WindowManagerGlobal.addView(WindowManagerGlobal.java:359)
6 android.view.WindowManagerImpl.addView(WindowManagerImpl.java:93)
7 android.app.ActivityThread.handleResumeActivity(ActivityThread.java:3955)
8 android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:3130)
9 android.app.ActivityThread.-wrap11(Unknown Source:0)
10 android.app.ActivityThread$H.handleMessage(ActivityThread.java:1821)
11 android.os.Handler.dispatchMessage(Handler.java:106)
12 android.os.Looper.loop(Looper.java:192)
13 android.app.ActivityThread.main(ActivityThread.java:6890)
14 java.lang.reflect.Method.invoke(Native Method)
15 com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:556)
16 com.android.internal.os.ZygoteInit.main(ZygoteInit.java:875)
```

3. http://www.martinrgb.com/Animer_Web/# 动画网址

https://wiki.inkept.cn/display/INKE/inke_live_business#inke_live_business-2.2%E5%BC%80%E6%92%AD%E6%8E%A5%E5%8F%A3 
@杜营 开播接口body中新增了几个参数，用来做脸萌机型白名单的，你看下哈

pk_mvp_resource
pkrws 王冠

--------------------

1. 约会前除了饭馆计划好之后所有行程
2. 约会前计划好推荐食品与饮品
3. 约会后记得拿好账单，记住她吃过的每一份食物，仔细观察她讨厌吃什么，喜欢吃什么
4. 聊天中注意记录她的喜好与不喜欢的
5. 聊天中注意她说过的一些特殊地方，记下来
6. 聊天中注意她说过的游戏与喜欢的，练熟练


--------------------

# 周会

1. P_Thread OOM问题
2. 本期需求合版后最好对应开发人员自测
3. 新增类必须使用Kotlin
4. 杨哥、康哥人事调整
5. 设计模式：Builder

6. 如果功能灰度的用户大概率触发不了功能，那么就要设法用一些策略才规避问题
7. 上线可能会遇到的情况：礼物资源需要运营那边配置，新的配置项可能配错
8. 灰度发布后，最早也需要6 ~ 7更新率才能上去。服务上线的风险，首先要确定那块服务要上线，重要模块上线的风险要考虑进去，不要高峰期

/storage/emulated/0/Android/data/com.meelive.ingkee/files/IngkeeQa/vr/effects/MTU1Mjk2NjkxMSM4ODY=.zip



