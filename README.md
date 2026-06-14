# 🏛️ 公基知识库 — 公共基础知识备考 Wiki

> 基于 [LLM Wiki](https://github.com/karpathy/llm-wiki) 方法论构建的公共基础知识（公基）备考知识库。
> 覆盖政治、法律、管理、经济、公文写作等核心科目，
> 包含 4000+ 考点、14 套模拟试卷、20 个专项题库。

[![License: CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)

---

## 🚀 快速开始

### 🅰️ 只想在线浏览？
→ 直接访问文档站：**https://kangers.github.io/-obsidian-claude-**

支持全文搜索、暗色模式、手机浏览。

### 🅱️ 想用 AI 辅助学习？（⭐ 推荐）
→ 安装 Obsidian + Claude AI，让 AI 帮你：
- 查询任意知识点
- 生成模拟试卷
- 分析错题、定位薄弱环节

👉 **[📖 零基础完整搭建指南 → (SETUP.md)](SETUP.md)**

从安装软件到 AI 开始辅导，全程约 30 分钟，不需要编程基础。

### 🅲️ 只用 Obsidian（不用 AI）
```bash
git clone https://github.com/kangers/-obsidian-claude-.git
```
然后用 Obsidian 打开 `-obsidian-claude-` 文件夹即可。所有 wiki-link 直接可用。

---

## 📚 内容清单

### 核心知识库
| 目录 | 内容 | 规模 |
|------|------|------|
| `wiki/概念/` | 政治、法律、管理、经济、公文写作等科目知识体系 | 12+ 科目 |
| `wiki/实体/` | 宪法、民法典、公务员法、监察法等核心法律实体 | 8+ 实体 |
| `wiki/策略/` | 高频考点、易错点突破、备考策略建议 | 5 个文件 |

### 题库
| 目录 | 内容 | 规模 |
|------|------|------|
| `练题班题库/` | 按科目分类的专项练习题 | 20 个科目 |
| `辅导班题目/` | 全真模拟试卷（含答案和解析） | 14 套 |

### 速记与导图
| 目录 | 内容 | 规模 |
|------|------|------|
| `考前必背-SVG/` | 核心概念 SVG 记忆导图 | 5 张 |
| `Excalidraw/` | 思维导图源文件（可编辑） | 9 张 |
| `错题集/` | 考前 30 分钟速记卡片 | 4 个文件 |

### 参考资料
| 目录 | 内容 |
|------|------|
| `时政/` | 二十大、三中全会、年度时政核心考点 |
| `陕西省/` | 陕西省情省况、政府工作报告核心数据 |

---

## 🧠 LLM Wiki 方法论

这个知识库采用了 Andrej Karpathy 提出的 [LLM Wiki](https://github.com/karpathy/llm-wiki) 模式——不是传统的上传文件然后等 AI 检索（RAG），而是让 AI **主动构建和维护一个持久化的 Wiki**。

```
raw/           → 原始来源（不可变）
wiki/          → LLM 维护的结构化知识库  
LLM-WORKFLOW.md → Schema 配置（告诉 AI 怎么维护）
```

每次添加新资料，AI 不只索引它，而是：
- 提取关键信息
- 更新相关概念页面
- 更新相关实体页面
- 标注新旧知识的矛盾
- 追加操作日志

**结果是**：知识在积累，交叉引用是现成的，矛盾已被标记，综合判断已反映所有已读内容。

详见 [[LLM Wiki.md]](LLM Wiki.md) 和 [[LLM-WORKFLOW.md]](LLM-WORKFLOW.md)。

---

## 🤝 贡献

欢迎贡献！你可以：

- 🐛 报告内容错误 → [提 Issue](https://github.com/kangers/-obsidian-claude-/issues/new?template=内容贡献.md)
- 📝 新增考点或题目 → [Pull Request](CONTRIBUTING.md)
- 💡 提出改进建议 → [Discussions](https://github.com/kangers/-obsidian-claude-/discussions)

详见 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📜 许可证

本知识库内容采用 [CC BY-SA 4.0](LICENSE) 许可证。

这意味着你可以自由：
- **共享** — 复制、分发本作品
- **改编** — 修改、转换、基于本作品创作

但必须：
- **署名** — 标注原作者
- **相同方式共享** — 衍生作品须使用相同许可证

---

## ⚠️ 免责声明

本知识库的内容基于公开资料和考试经验整理，仅供参考。
考试大纲可能随时调整，请以官方发布的最新信息为准。
