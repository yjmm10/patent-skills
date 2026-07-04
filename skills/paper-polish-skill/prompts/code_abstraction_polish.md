# Step 3d: Code Abstraction — 代码与实现细节抽象化

**Read** `references/code-abstraction.md`；Method/Evaluation 章可对照 `chapter-guidelines.md`、`figure-and-experiment.md`。

## 适用场景

- 正文含文件路径、函数名、类名、库版本、Python 代码块
- 用户要求：去代码化、抽象化、更像顶刊论文
- diagnose 发现 P1d 代码暴露问题
- full 润色时 Method / Evaluation 章含实现描述

## 执行步骤

1. **扫描**（Grep 或逐段）：
   - 路径：`.py`, `.yaml`, `configs/`, `./results/`, `/home/`
   - 标识符：`def `, `class `, `import `, `torch`, `numpy`, 行号 `line 42`
   - 内联代码块与反引号函数名
2. **分类**：每处标记策略 1–5
3. **改写**：保留科学语义（公式、超参数值、episode 数、seed 数）；删除工程暴露面
4. **分流**：细节 → 建议 Appendix A/B 或 `[移至附录: 超参数表]`
5. **补伪代码**：训练/推理流程若缺 Algorithm 1，按 code-abstraction 策略 3 + chapter-guidelines 生成
6. **三问验证**：贡献性 / 持久性 / 领域专家可读性

## 输出

```markdown
## 代码抽象润色结果

（润色后相关段落/章节全文）

---

## 代码抽象改进摘要
| 位置 | 原表述 | 润色后 | 策略 |

## 检查清单（code-abstraction.md）
- ✅ / ⚠️ / ❌ 各项

## 建议附录（若有）
- Appendix A: ...
```

## 禁止

- 不删除真实超参数数值、实验设置（50 seeds、2000 episodes）——只改表述方式
- 不虚构 GitHub URL；无链接时用 `[Code URL upon acceptance]`
- 不把整篇 Method 改成空泛 prose 而无公式/伪代码

## 与 full 模式关系

专项 **code_abstraction** 模式只改含代码痕迹的段落；**full** 模式在 Method/Evaluation 润色时自动应用本 reference，无需单独跑本 prompt。
