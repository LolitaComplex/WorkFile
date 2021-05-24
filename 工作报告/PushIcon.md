# 一加手机

- 透传Push：✅
- OPPO厂商通知：❌
- 极光通知：❌

# 华为荣耀 6.0 (不支持)

- 透传Push：❌
- 华为厂商通知：❌
- 极光通知：❌

# 华为P9 7.0

- 透传Push：✅
- 华为厂商通知：❌
- 极光通知：✅

# 华为P40 10.0
- 透传Push：✅
- 华为厂商通知：❌
- 极光通知：❌

-----------------


1. Push对表情的支持（全部支持，包含全部Push类型）
2. Push对图标的支持情况
    - 通过长链接、极光、小米来的透传通知支持
    - 通过华为、OPPO、极光来的厂商通知支持
    - 小米厂商通知只支持 MIUI 13及以上
    - vivo厂商通道不支持

> 以上只是官网给的结论，目前没有进行过功能适配测试

3. 本地通知：定时任务官方文档支持，无论应用是否被杀都可做定时任务。国内Room支持进行了修改，测试小米手机不能在被杀的情况唤醒定时任务

4. 厂商通知的Push无法完全自定义通知栏


-----------------

- 1. 极光崩溃排查
- 2. 极光错误咨询
3. 弹框到达问题排查
- 4. Review合并代码
- 5. 权限列表提测后跟进

------------------

1. 统计的数据是根据发送，还是长链收到为准（去查询Push连接埋点）
2. 长链接是在登录后建立的，可能没建立 link_ua_connect link_ua_login
3. 


11211

"https://service.inke.cn/api/url/get_raw?meid=313636373439313330313933373638&vv=202007221221&smid=DuF9cbkLrodojIEEymW%2FEIBQgOJZN%2BvvdFKqZjisGctlaOAbYbMjbu4gi1nV5%2Fkp%2BrJ0A4VNQvv8fIGNulG%2Bsimw&conn=wifi&ast=1&icc=898600A6083805553390&ua=XiaomiMI6&sid=20sTTBgm7zqNgbi2C0Eei2ZQi1HN8PhBBAv3FOJG3SkbG8pkjO8lhuXIi3&uid=747483637&xid=354&oaid=74c144dc4aeb49b6&ram=6002479104&cc=TG36008&dev_name=Xiaomi&ndid=20200428205749f22a343a5458b3b3129caadede768488014db35ea4600a11&evid=3335333039336539356330346434386261323264636530613034373861633363&cpu=%5BAdreno_%28TM%29_540%5D%5BARMv8_638_Qualcomm_Technologies%2C_Inc_MSM8998%5D&mtid=d9c471b76710fca876003681b785db87&msid=303933333335353536373730303634&cv=IK8.0.70_Android&lc=3eaabb350e8520e8&proto=8&sign_from=android&code870125345=1596545866694&mtxid=020000000000&logid=267%2C293%2C197%2C198%2C3005%2C3006%2C207%2C232%2C236%2C100005%2C10002%2C100103%2C100201%2C100301%2C10203%2C1023601%2C1027001%2C200202%2C200401%2C200902%2C206506%2C30202%2C40201%2C50208%2C50305%2C50408%2C60201%2C70005%2C80004%2C80106%2C80202%2C80306%2C90006&osversion=android_28&aid=2ce552e1028f4879&source_info=eyJhcHBpZCI6IjEwMDAwIiwidWlkIjoiNzQ3NDgzNjM3IiwicGFnZSI6ImNvbS5tZWVsaXZlLmluZ2tlZS5idXNpbmVzcy5tYWluLmVudHJ5LmxlZ2FjeS5NYWluQWN0aXZpdHkiLCJ0aW1lIjoiMTU5NjU0NTg2NTYxOCJ9
