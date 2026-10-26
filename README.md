# TVS — TVBox 类空壳聚合播放器（Android TV / iOS / macOS）

[![Release](https://img.shields.io/github/v/release/yuluoos/TVBox-tvs?label=release&color=blue)](https://github.com/yuluoos/TVBox-tvs/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/yuluoos/TVBox-tvs/total?label=downloads&color=success)](https://github.com/yuluoos/TVBox-tvs/releases)
[![Platform](https://img.shields.io/badge/platform-Android%20TV%20%7C%20Android%20%7C%20iOS%20%7C%20macOS-lightgrey)](https://github.com/yuluoos/TVBox-tvs/releases/latest)
[![Stars](https://img.shields.io/github/stars/yuluoos/TVBox-tvs?style=flat&color=yellow)](https://github.com/yuluoos/TVBox-tvs/stargazers)
[![License](https://img.shields.io/github/license/yuluoos/TVBox-tvs?color=informational)](LICENSE)

> TVBox 类空壳聚合播放器 · Flutter 跨平台 · Android TV / 电视盒子 / iOS / iPadOS / macOS · 提供 APK / IPA / DMG 直接下载
>
> A TVBox-style shell media player built with Flutter for Android TV, iOS and macOS — no built-in content, bring your own subscription and live sources.

## 下载（最新版 1.2.5）

| 平台 | 下载 | 说明 |
| --- | --- | --- |
| Android / TV（arm64-v8a） | [GitHub 原链](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5-arm64-v8a.apk) · [GHFast（第三方加速）](https://ghfast.top/https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5-arm64-v8a.apk) · [GH-Proxy（第三方加速）](https://gh-proxy.org/https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5-arm64-v8a.apk) | 绝大多数手机与电视盒子 |
| Android / TV（armeabi-v7a） | [GitHub 原链](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5-armeabi-v7a.apk) · [GHFast（第三方加速）](https://ghfast.top/https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5-armeabi-v7a.apk) · [GH-Proxy（第三方加速）](https://gh-proxy.org/https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5-armeabi-v7a.apk) | 按设备架构选择 |
| Android / TV（x86_64） | [GitHub 原链](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5-x86_64.apk) · [GHFast（第三方加速）](https://ghfast.top/https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5-x86_64.apk) · [GH-Proxy（第三方加速）](https://gh-proxy.org/https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5-x86_64.apk) | 按设备架构选择 |
| iOS / iPadOS | [自签名 IPA（GitHub）](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-selfsign-1.2.5.ipa) · [GHFast（第三方加速）](https://ghfast.top/https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-selfsign-1.2.5.ipa) · [GH-Proxy（第三方加速）](https://gh-proxy.org/https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-selfsign-1.2.5.ipa) | 需自行签名侧载（如爱思、巨魔、AltStore、自签 API） |
| macOS（Apple Silicon） | [DMG（GitHub）](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5.dmg) · [GHFast（第三方加速）](https://ghfast.top/https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5.dmg) · [GH-Proxy（第三方加速）](https://gh-proxy.org/https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5.dmg) | 首次打开需在「隐私与安全性」中放行 |

GitHub 下载慢时可尝试表中的第三方加速；速度因地区和运营商而异，失败可切换线路。下载后请核对文末 SHA-256。

### 加入 TG 群

扫码加入 TG 群，获取使用交流、问题反馈与更新通知。

<img src="docs/assets/tg-group-qr.jpeg" alt="TVS TG 群二维码" width="280">

全部版本见 [Releases 页面](https://github.com/yuluoos/TVBox-tvs/releases)；最新版 SHA-256 校验值见文末[最新版本](#最新版本)。
也可以访问下载页：**<https://yuluoos.github.io/TVBox-tvs/>**

安装与配置指南（下载页子页面）：
[iOS / iPadOS 侧载 IPA](https://yuluoos.github.io/TVBox-tvs/ios-ipa.html) ·
[电视盒子 / Android TV 装 APK](https://yuluoos.github.io/TVBox-tvs/android-tv.html) ·
[macOS 安装 DMG](https://yuluoos.github.io/TVBox-tvs/macos.html) ·
[羊壳（PeekPro）订阅导入](https://yuluoos.github.io/TVBox-tvs/peekpili.html) ·
[直播源导入（M3U / TXT / JSON）](https://yuluoos.github.io/TVBox-tvs/live.html)

---

TVS 是一款跨平台空壳聚合播放器，支持 Android 手机、Android TV / 电视盒子、iPhone、iPad 和 macOS（Apple Silicon）。在同一个应用中浏览站点、聚合搜索、观看点播与直播，也可以后台听剧、听音乐，或浏览源提供的云盘目录和文件。

**应用本体不内置任何内容、频道或数据源**。使用前需自行导入羊壳（PeekPro）订阅或直播源；支持通过链接或本地文件导入订阅配置。内容、可用线路及云盘功能取决于导入的源。

本仓库用于管理 TVS 的打包产物（IPA / APK / DMG），最新版本信息见文末。

有功能建议或使用中遇到问题，欢迎通过 [Issues](https://github.com/yuluoos/TVBox-tvs/issues) 反馈问题，或到 [Discussions](https://github.com/yuluoos/TVBox-tvs/discussions) 提想法与交流使用经验。

---

## 空壳设计说明

- 首次启动无任何内容，需在"订阅"页导入订阅配置；**仅支持羊壳（PeekPro）订阅**，其他格式的订阅不保证可用。
- 站点、分类、搜索结果、直播频道等全部来自用户导入的源，卸载配置即恢复空壳状态。
- 应用不提供、不推荐、不分发任何内容源，仅作为个人学习与技术研究用途。

## 功能介绍

### 订阅与源管理

- 支持通过链接或本地文件导入羊壳（PeekPro）订阅，多订阅管理与切换。
- 内嵌本地服务运行 Node.js 类型 spider 站点，支持独立悦听音频源。
- 应用前后台切换时检测并恢复本地服务。

### 点播（VOD）
- **首页**：按当前配置的站点展示分类与推荐列表。
- **聚合搜索**：跨站点并发搜索，统一展示结果。
- **详情页**：剧集解析与展示，支持多线路 / 多集数结构。
- **解析播放**：支持播放地址解析（parse 接口），自动处理嗅探与防盗链请求头。

### 播放器

- 视频播放采用 **yl_player 原生播放组件**，支持点播与直播；具体媒体格式兼容性取决于设备、平台与源。
- **片头片尾跳过**：按剧集记忆片头 / 片尾跳过秒数，本地持久化。
- **m3u8 广告过滤**：对适用的点播播放列表过滤疑似广告分片，不保证所有源均可过滤。
- **播放历史与断点续播**：自动记录观看进度，随时接续播放。
- 支持倍速、画面比例切换、亮度 / 音量手势调节和播放时屏幕常亮。
- 加载与缓冲时显示播放状态和下载速度，全屏轻点空白区域可收起控制层。

### 直播（Live）

- 支持导入直播源，自动识别 **M3U / TXT（#genre# 分组）/ JSON** 三种格式。
- 频道分组浏览、台标显示、独立直播播放器，支持多线路切换与播放模式选择。
- 支持脚本与 RTMP 直播来源；刷新失败时保留已有频道，并提供错误提示。

### 听剧模式（音频播放）

- 独立音频播放页与全局迷你播放条，可后台播放（audio_service），息屏听剧。
- 支持音频选集、播放模式切换与小说定时停止；音乐可展示匹配到的封面与歌词。

### 云盘与文件预览

- 支持浏览源提供的云盘目录、打开媒体文件。
- 支持图片、PDF 与文本文件预览，具体内容由导入的源提供。

### 本地代理服务
- 内置本地 HTTP 代理：图片防盗链代理、请求头转发、m3u8 过滤。

### TV / 遥控器适配
- 支持 D-pad 遥控器按键导航、焦点选择和播放菜单操作，适配 Android TV 与电视盒子。

### 其他
- 播放历史管理页、设置中心（含各功能项细分设置）。
- 订阅配置与播放记录使用本地存储；播放、内容查询和使用统计等功能会发起网络请求。

## 技术栈

基于 Flutter（Dart）开发；视频播放使用 yl_player，音频播放使用 just_audio 与 audio_service，源运行依托本地 Node.js 服务，配置与记录使用 Isar 数据库和安全存储。

## 关键词 / Keywords

TVBox、tvbox 类客户端、空壳播放器、聚合播放器、电视盒子应用、Android TV 播放器、ATV apk、TV 版播放器、遥控器 D-pad 适配、羊壳、PeekPro 订阅、直播源播放器、M3U / IPTV 播放器、Flutter 播放器、yl_player、后台听剧、云盘浏览、nodejs spider 爬虫源、自签名 IPA、iOS 侧载、macOS DMG。

`tvbox` `android-tv` `iptv-player` `m3u` `flutter` `yl-player` `ipa` `apk` `dmg` `self-signed-ipa` `shell-player`

## 反馈与建议

- 报告 Bug / 提交问题：[GitHub Issues](https://github.com/yuluoos/TVBox-tvs/issues)（请附上系统版本、应用版本与复现步骤）
- 功能建议 / 使用交流：[GitHub Discussions](https://github.com/yuluoos/TVBox-tvs/discussions)

## 免责声明

本应用为空壳聚合播放器，不含任何内容与数据源。仅供个人学习、技术研究使用，请在遵守当地法律法规的前提下使用。

---

## 最新版本

### iOS（IPA）

| 版本 | 文件 | 大小 | SHA-256 | 打包日期 |
| --- | --- | --- | --- | --- |
| 1.2.5 (build 10) | [tvs-selfsign-1.2.5.ipa](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-selfsign-1.2.5.ipa) | 32 MB | `e6029ce62265e7579a34e27a2cbbe37e3d1eaf2e09ba2ca029c97145d2072ff7` | 2026-10-26 |

- IPA 为自签名（selfsign）Release 构建
- 每个发布版本均对应一个 git tag
- 所有产物统一发布在 [GitHub Releases](https://github.com/yuluoos/TVBox-tvs/releases)，仓库内不再存放二进制文件

### Android（APK）

按 ABI 分包，请按设备架构选择；绝大多数手机与电视盒子用 **arm64-v8a**。

| 版本 | ABI | 文件 | 大小 | SHA-256 | 打包日期 |
| --- | --- | --- | --- | --- | --- |
| 1.2.5 (build 10) | arm64-v8a | [tvs-1.2.5-arm64-v8a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5-arm64-v8a.apk) | 31 MB | `e7774c909b880d8a6e8cd57ebf3bd8a61d6554f42a762e2e88dcab560a597bab` | 2026-10-26 |
| 1.2.5 (build 10) | armeabi-v7a | [tvs-1.2.5-armeabi-v7a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5-armeabi-v7a.apk) | 30 MB | `ca3ef77d714287753dd0fdd9cfa5c3160878d8628ac6327c4f95f97535633bde` | 2026-10-26 |
| 1.2.5 (build 10) | x86_64 | [tvs-1.2.5-x86_64.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5-x86_64.apk) | 33 MB | `f2b46fd7477e289f8e4b22031ba2e68431d9f1a8c5582a58caa62cfec6060cef` | 2026-10-26 |

- 最低支持 Android 7.0（API 24），targetSdk 36
- APK 为 Release 构建，使用调试密钥签名，仅供侧载安装
- nodejs-mobile 上游无 32 位 x86 产物，故不提供 x86 包
- native 库采用压缩打包（`useLegacyPackaging`），安装时由系统解压，设备上会额外占用约 80 MB

### macOS（DMG）

| 版本 | 文件 | 大小 | SHA-256 | 打包日期 |
| --- | --- | --- | --- | --- |
| 1.2.5 (build 10) | [tvs-1.2.5.dmg](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.2.5/tvs-1.2.5.dmg) | 36 MB | `945e2fd4ee75c09769941df301b7e5a5af8ce2d8ba60781361c7ee3e4e637466` | 2026-10-26 |

- 仅提供 Apple Silicon（arm64）版本：内置的 Node 运行时上游只有 darwin-arm64 产物，Intel Mac 无法运行爬虫源
- DMG 使用 LZMA（ULMO）压缩，需 macOS 10.15+ 挂载
- 应用为 ad-hoc 自签名，首次打开会被 Gatekeeper 拦截；请在「访达」中右键点击 → 打开，或到「系统设置 → 隐私与安全性」中允许

### 1.2.5 更新内容

- 优化音频媒体类型探测，复用首次两字节与后续 Range 请求的探测结果，减少重复请求与 M4A 加载超时。
- 减少原生音频加载的重复重试，完善播放失败原因展示。
- 音频加载界面新增加载阶段和已等待时间，便于了解当前进度。
- 修复平板播放器加载期间侧栏内容消失的问题，保留线路与剧集等内容。
- 继续提供 Android App 内更新加速，以及下载页和 README 的两条第三方加速备用入口；保留 GitHub 原链与 SHA-256 校验。
