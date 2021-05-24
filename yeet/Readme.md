
# 主要功能

1. 注册登录 ，snapchat，谷歌 => 中台服务。手机号之后，国外比较敏感手机号
2. 资料生成：
    - 昵称（snapchat 有则用）
    - 密码
    - 性别
    - 
    模板（服务：选了哪些模板、装饰、捏脸后的变化）模板的具体数据格式看具体是否需要存本地（描述只有 xx kb < 1000 )
3. 消息列表
    - 拉新：发送邀请（snap邀请和sharable link）和好友。分享的视频是虚拟头像的视频
    - 聊天
        - 发送文字：实时文字
        - 发送图片：拍照与上传
        - 表情： giphy gif 表情（有现成的gif图片列表）
    - 视频通话：拨打、接收、录制：发送、保存、Mute
    - 视频信息：录制、预览、播放
    - Push：消息合并等

4. 个人资料
    - 头像：可捏脸画板
    - 用户名
    - 设置：帮助、账号找回

5. 权限：通知、相机、相册
6. Buggly -> FireBase
7. jgou

# 记录项

1. 包名：`com.obias.yeet`
2. 参考项目地址：

- JEGO express SDK下载地址：https://doc-zh.zego.im/article/2969
- JEGO 外部采集文档：https://doc-zh.zego.im/article/3677

- 项目地址：https://code.inke.cn/inno/obias

- Flutter基础架构项目：https://code.inke.cn/inf/flutter/flutter_demo

- IM基础能力参考杭州项目：https://code.inke.cn/inno/obias/mido/mido_client

1v1视频通话：待定

1v1视频录制：参考映客直播，注意双音频混编，自定义视频输入源，音画同步（同步帧问题）

- 捏脸：相芯科技 https://www.faceunity.com

- iOS：https://github.com/Faceunity/FUP2AArt
- Android：https://github.com/Faceunity/FUP2AArtDroid 
- 表情：Giphy https://developers.giphy.com/docs/sdk

登陆：中台对接

- Snap Login Kit: https://kit.snapchat.com/docs/login-kit
- Google 登录
- Apple 登录
- 分享：Snap Creative Kit: https://kit.snapchat.com/docs/creative-kit

# 需求评审

1. 登录流程只要未完成，每次都重来
2. 录制短视频
3. 头像需要模型驱动（没有好友）
4. 首页权限开启通知
5. 分享 -> 打开App == 建立好友关系（口令：邀请码）
6. iMeesage -> 短信 ，允许图片

