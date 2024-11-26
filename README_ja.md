# Poly-README

Poly-READMEは、OpenAIのGPT-4モデルを使用してREADME.mdファイルを自動的に多言語に翻訳するコマンドラインツールです。

## 機能

- README.mdファイルの自動翻訳
- 複数のターゲット言語をサポート
- シンプルなコマンドラインインターフェース
- Markdownフォーマットを保持
- 高品質な翻訳のためのOpenAI GPT-4を使用
- システムキーリングを使用した安全なAPIキー管理
- YAMLによるプロジェクトレベルの設定
- 翻訳中の進行状況インジケータ
- カスタム出力ファイル名パターンのサポート

## インストール

```bash
pip install poly-readme
```

## 前提条件

Poly-READMEを使用する前に、以下の手順を行ってください:

1. OpenAI APIキーを取得する
2. 以下のいずれかの方法でAPIキーを設定する：
   - 環境変数として設定:
     ```bash
     export OPENAI_API_KEY='あなたのAPIキー'
     ```
   - CLIを使用して安全にインストール:
     ```bash
     poly-readme install
     ```

## 使用法

### 初期設定

プロジェクト設定を行います:

```bash
poly-readme setup
```

これにより以下の設定が行えます：

- 元のREADMEファイルの場所を設定
- 翻訳ターゲット言語の選択
- 出力ファイル名パターンの設定

### 翻訳

プロジェクト設定に基づきREADMEを翻訳します:

```bash
poly-readme translate
```

### 利用可能な言語コード

- `ko`: 韓国語
- `ja`: 日本語
- `zh`: 中国語（簡体字）
- `es`: スペイン語
- `fr`: フランス語
- `de`: ドイツ語
- `it`: イタリア語
- `pt`: ポルトガル語
- `ru`: ロシア語
- `ar`: アラビア語
- `vi`: ベトナム語

翻訳されたファイルは、設定されたパターン（デフォルトは`README_{lang}.md`）に従い保存されます。

## コマンド

- `poly-readme install` - OpenAI APIキーの設定
- `poly-readme setup` - プロジェクト設定の構成
- `poly-readme translate` - READMEファイルの翻訳
- `poly-readme help [command]` - ヘルプ情報の表示

## 貢献

貢献は歓迎されます! プルリクエストの提出をお待ちしております。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています - 詳細についてはLICENSEファイルをご覧ください。

## 作者

- Chad Lee
- Email: think.bicycle@gmail.com
- GitHub: [drllr/poly-readme](https://github.com/drllr/poly-readme)

## 謝辞

- このツールは、OpenAIのGPT-4モデルを使用して翻訳を行っています。