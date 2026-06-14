# 🤝 贡献指南

感谢你愿意为公基知识库贡献内容！

## 贡献方式

### 方式一：报告内容错误（Issue）
如果发现知识点错误、题目答案有误、或链接失效：
1. 进入 [Issues 页面](https://github.com/kangers/-obsidian-claude-/issues)
2. 点击 "New Issue" → 选择「内容贡献」模板
3. 描述问题：涉及哪个文件、哪里错了、正确的版本是什么、参考来源

### 方式二：建议新增内容（Issue）
如果建议新增考点或补充题目：
1. 提 Issue，使用「内容贡献」模板
2. 说明属于哪个科目、具体内容、参考来源

### 方式三：直接修改内容（Pull Request）
1. **Fork 本仓库** → 点击 GitHub 右上角 Fork
2. **Clone 到本地** `git clone https://github.com/<你的用户名>/-obsidian-claude-.git`
3. **创建新分支** `git checkout -b fix/内容描述`
4. **修改内容** → 请在 Obsidian 中编辑以确保 wiki-link 正确
5. **提交并推送** `git add . && git commit -m "fix: 描述" && git push origin fix/内容描述`
6. **创建 PR** → GitHub 点击 "Compare & pull request"

---

## 内容规范

### 文件格式
- 所有 `.md` 文件使用 YAML frontmatter
- 链接使用 Obsidian wiki-link 格式：`[显示名](目录/文件名)`
- 不要使用绝对路径

### Frontmatter 规范
```yaml
---
创建时间: YYYY-MM-DD
更新时间: YYYY-MM-DD
分类: 概念/实体/策略/来源/试卷/题库
标签: ["标签1", "标签2"]
状态: 待完善/活跃
---
```

### 题目格式
参考 `辅导班题目/模拟1.md`：
- 单选题 4 个选项，标明正确答案和解析
- 关联知识点（用 wiki-link 指向概念页）

### 内容原则
- **准确性第一**：不确定的内容标注 `[待核实]`
- **注明来源**：重要结论标注出处
- **原创内容**：不直接复制第三方教材原文
- **禁止提交 PDF**：PDF 文件有版权风险

---

## 社区公约
- 友善交流，尊重每个人的时间和劳动
- 对事不对人
- 维护者有权拒绝不符合规范的 PR
- 重大改动请先提 Issue 讨论

## 审核流程
1. 提交 Issue 或 PR
2. 维护者在 1-7 天内审核
3. 审核通过后合并
