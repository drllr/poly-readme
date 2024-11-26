# Poly-README

Poly-README 是一个命令行工具，可利用 OpenAI 的 GPT-4 模型自动将您的 README.md 文件翻译成多种语言。

## 功能

- 自动翻译 README.md 文件
- 支持多种目标语言
- 简单的命令行界面
- 保持 Markdown 格式
- 使用 OpenAI 的 GPT-4 确保高质量翻译
- 使用系统密钥环安全管理 API 密钥
- 使用 YAML 进行项目级别配置
- 翻译过程中显示进度指示器
- 支持自定义输出文件名模式

## 安装

```bash
pip install poly-readme
```

## 先决条件

在使用 Poly-README 之前，您需要：

1. 拥有一个 OpenAI API 密钥
2. 选择以下两种方式之一：
   - 将您的 OpenAI API 密钥设置为环境变量：
     ```bash
     export OPENAI_API_KEY='your-api-key-here'
     ```
   - 或使用 CLI 安全安装：
     ```bash
     poly-readme install
     ```

## 使用方法

### 初始设置

配置项目设置：

```bash
poly-readme setup
```

这将引导您完成：

- 设置源 README 文件位置
- 选择翻译的目标语言
- 配置输出文件名模式

### 翻译

根据您的项目配置翻译 README：

```bash
poly-readme translate
```

### 可用语言代码

- `ko`: 韩语
- `ja`: 日语
- `zh`: 简体中文
- `es`: 西班牙语
- `fr`: 法语
- `de`: 德语
- `it`: 意大利语
- `pt`: 葡萄牙语
- `ru`: 俄语
- `ar`: 阿拉伯语
- `vi`: 越南语

翻译后的文件将根据您配置的模式保存（默认：`README_{lang}.md`）。

## 命令

- `poly-readme install` - 配置 OpenAI API 密钥
- `poly-readme setup` - 配置项目设置
- `poly-readme translate` - 翻译 README 文件
- `poly-readme help [command]` - 显示帮助信息

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 许可证

此项目基于 MIT 许可证 - 详细信息请参阅 LICENSE 文件。

## 作者

- Chad Lee
- 邮箱: think.bicycle@gmail.com
- GitHub: [drllr/poly-readme](https://github.com/drllr/poly-readme)

## 致谢

- 本工具使用了 OpenAI 的 GPT-4 模型进行翻译。