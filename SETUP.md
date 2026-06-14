# 📖 零基础搭建指南 — 让 AI 帮你学公基

> 从安装软件到 AI 开始辅导你学习，全程约 30 分钟。不需要编程基础，跟着做就行。

---

## 第一步：安装 Obsidian（你的知识管理软件）

### 什么是 Obsidian？
Obsidian 是一个免费的笔记软件。笔记存为普通的 Markdown 文本文件，数据完全在你自己电脑上，可以永久保存、自由迁移。

### 下载与安装

#### macOS
1. 打开 https://obsidian.md/download
2. 点击 "Download for macOS"，下载 .dmg 文件
3. 双击 .dmg，把 Obsidian 图标拖到 Applications 文件夹
4. 启动台找到 Obsidian 双击打开
5. 如提示"无法验证开发者"：系统设置 → 隐私与安全性 → 仍要打开

#### Windows
1. 打开 https://obsidian.md/download
2. 点击 "Download for Windows"，下载 .exe
3. 双击运行安装程序，一路「下一步」
4. 桌面双击 Obsidian 图标启动

#### Linux
1. 打开 https://obsidian.md/download
2. 下载 AppImage，右键 → 属性 → 权限 → 允许执行，双击运行

#### iPhone / iPad
1. App Store 搜索 "Obsidian" → 安装（免费）

#### Android
1. Google Play 搜索 "Obsidian" → 安装；或从 obsidian.md/download 下载 APK

### 首次启动
⚠️ 先**不要**创建 Vault。关闭 Obsidian，等下载好知识库再重新打开。

---

## 第二步：下载本知识库

### 安装 Git

#### macOS
打开「终端」（启动台搜索 Terminal），粘贴并回车：
```
xcode-select --install
```
弹出窗口点「安装」，等 2-5 分钟。

#### Windows
打开 https://git-scm.com/download/win，下载安装（一路默认）。

### 下载
打开终端（macOS）或 Git Bash（Windows）：
```bash
cd ~/Documents
git clone https://github.com/kangers/-obsidian-claude-.git
cd -obsidian-claude-
```

💡 不想装 Git？打开仓库页面 → 绿色 "Code" → Download ZIP → 解压到「文档」文件夹。

---

## 第三步：在 Obsidian 中打开知识库

1. 打开 Obsidian → 点击 "Open folder as vault"
2. 选中 `-obsidian-claude-` 文件夹 → Open
3. 弹出「信任作者？」→ 点 "Trust author and enable plugins"

✅ 现在你能浏览所有知识库内容了！试试按 `Cmd/Ctrl + O` 搜索并打开笔记。

---

## 第四步：安装 Claudian 插件（让 Claude AI 接入 Obsidian）

> Claudian 把 Claude AI 直接嵌入 Obsidian。你可以在 Obsidian 里和 Claude 对话。

### 4.1 开启社区插件
Obsidian 左下角齿轮 ⚙️ → Settings → Community plugins → "Turn on community plugins"。

### 4.2 安装 Claudian
1. Community plugins → "Browse"
2. 搜索 **Claudian** → Install → Enable

### 4.3 打开对话面板
- 左侧图标栏找聊天图标，点击 → 右侧出现 Claudian 面板
- 或按 `Cmd/Ctrl + Shift + L`

---

## 第五步：获取 Claude API Key

> Claude 是 Anthropic 公司的 AI。需要 API Key（通行证）来使用，按用量付费，很便宜。

### 5.1 注册
访问 **https://console.anthropic.com** → Sign Up（Google 或邮箱）。

### 5.2 费用
- 首次注册通常赠送 $5 免费额度
- 用完充值最低 $5（约 35 元人民币）
- **一个月学习公基约花 $2-5**

### 5.3 创建 API Key
1. Console 左侧 → API Keys → Create Key
2. 命名（如"公基学习"）→ Create
3. 🔴 **立刻复制** Key（以 `sk-ant-api03-` 开头）！只显示一次！

---

## 第六步：把 API Key 配置到 Claudian

1. Obsidian → Settings → Claudian
2. 在 "API Key" 输入框粘贴 Key
3. 推荐设置：

| 设置项 | 推荐值 | 说明 |
|--------|--------|------|
| Model | Sonnet | 性价比最高 |
| Permission Mode | Accept Edits | 允许 AI 修改笔记 |
| Locale | zh-CN | 中文回复 |

4. 测试：在 Claudian 对话框输入"你好，介绍一下公基考试"，回复了就是成功！
   - 报错 "401" → 检查 Key 是否完整
   - 报错 "429" → 检查账户余额

---

## 第七步：安装 Andrej Karpathy 的 LLM Wiki 技能

> Karpathy（前特斯拉 AI 总监、OpenAI 创始成员）提出了 LLM Wiki 方法论，让 Claude 更懂知识库维护。

打开终端粘贴：
```bash
cd ~/Documents/-obsidian-claude-
mkdir -p .claude/skills/karpathy-guidelines
curl -L -o .claude/skills/karpathy-guidelines/SKILL.md \
  "https://raw.githubusercontent.com/karpathy/llm-wiki/main/.claude/SKILL.md"
```

在 Claudian 输入 `/skills`，看到 `karpathy-guidelines` 就成功了！

---

## 第八步：第一次和 Claude 一起学习 🎉

### 了解知识库
```
请读取 wiki/总览.md，介绍这个知识库的结构和内容。
```

### 查询知识
```
请用 [[wiki/概念/宪法.md]] 中的内容，解释"宪法是国家的根本法"。
```

### 生成模拟卷
```
请参考辅导班题目/模拟1.md 的格式，生成一套包含 50 道选择题的模拟卷。
```

### 分析错题
```
我在做辅导班题目/模拟1.md，第 3、7、15 题做错了。请逐题分析错因，并关联对应的知识点。
```

---

## 第九步：进阶技巧

### 图谱视图 — 看知识网络
左侧边栏点「图谱」图标（星空 📊）→ 每个点是一个笔记，每条线是连接关系。中心大点是核心概念。

### 导入自己的资料
把新资料保存为 Markdown 放到 `raw/` 目录，在 Claudian 说：
```
摄入 raw/我找到的资料.md
```
Claude 会自动提取关键信息、更新 wiki。

### 手机同步
| 方案 | 费用 | 适用 |
|------|------|------|
| iCloud | 免费 | iPhone + Mac 最简单 |
| Obsidian Sync | $5/月 | 全平台 |
| Git + Working Copy | 免费 | 需 Git 基础 |

### 快捷键速查

| Mac | Windows | 功能 |
|-----|---------|------|
| Cmd+O | Ctrl+O | 搜索打开笔记 |
| Cmd+E | Ctrl+E | 编辑/预览切换 |
| Cmd+Shift+F | Ctrl+Shift+F | 全文搜索 |
| Cmd+P | Ctrl+P | 命令面板 |
| Cmd+Shift+L | Ctrl+Shift+L | 打开/关闭 Claudian |

---

## 常见问题

### Q: 要钱吗？
A: 知识库免费（CC BY-SA 4.0）。Obsidian 免费。Claude API 按量付费，首次赠 $5，一个月约 $2-5。

### Q: 需要编程基础吗？
A: 不需要。跟着这篇指南做就行。有 Git 基础会更方便（可一键更新）。

### Q: 准确吗？
A: 内容经过人工整理和考试验证。AI 仍可能犯错，重要知识点以教材为准。

### Q: 数据会泄露吗？
A: 不会。Key 只在你电脑上。提问时只发送当前涉及的文件内容。

### Q: 手机能用吗？
A: 可以！Obsidian 有 iOS/Android 版，Claudian 也支持移动端。建议先电脑配置。

### Q: 怎么更新？
A: 用 git clone 的：`cd ~/Documents/-obsidian-claude- && git pull`。下载 ZIP 的：重新下载覆盖。

---

## 📞 遇到问题？

1. 搜索错误信息 — 大概率有人遇到过
2. GitHub Issues：https://github.com/kangers/-obsidian-claude-/issues
3. Obsidian 官方论坛：https://forum.obsidian.md
4. Anthropic 文档：https://docs.anthropic.com

---

**🚀 祝你备考顺利，一次上岸！**
