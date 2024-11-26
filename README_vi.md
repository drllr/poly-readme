# Poly-README

Poly-README là một công cụ dòng lệnh tự động dịch các tập tin README.md của bạn sang nhiều ngôn ngữ khác nhau sử dụng mô hình GPT-4 của OpenAI.

## Tính năng

- Dịch tự động các tập tin README.md
- Hỗ trợ nhiều ngôn ngữ đích
- Giao diện dòng lệnh đơn giản
- Giữ nguyên định dạng markdown
- Sử dụng GPT-4 của OpenAI để có bản dịch chất lượng cao
- Quản lý khóa API an toàn bằng cách sử dụng hệ thống keyring
- Cấu hình cấp dự án bằng YAML
- Hiển thị tiến trình trong khi dịch
- Hỗ trợ mẫu tên tập tin đầu ra tùy chỉnh

## Cài đặt

```bash
pip install poly-readme
```

## Điều kiện tiên quyết

Trước khi sử dụng Poly-README, bạn cần:

1. Có khóa API của OpenAI
2. Hoặc là:
   - Thiết lập khóa API của OpenAI như một biến môi trường:
     ```bash
     export OPENAI_API_KEY='your-api-key-here'
     ```
   - Hoặc cài đặt nó an toàn sử dụng CLI:
     ```bash
     poly-readme install
     ```

## Cách sử dụng

### Thiết lập ban đầu

Cấu hình cài đặt dự án của bạn:

```bash
poly-readme setup
```

Điều này sẽ hướng dẫn bạn:

- Thiết lập vị trí tập tin README nguồn
- Chọn ngôn ngữ đích cho việc dịch
- Cấu hình mẫu tên tập tin đầu ra

### Dịch thuật

Dịch README của bạn theo cấu hình dự án:

```bash
poly-readme translate
```

### Mã Ngôn ngữ Có Sẵn

- `ko`: Tiếng Hàn
- `ja`: Tiếng Nhật
- `zh`: Tiếng Trung Giản Thể
- `es`: Tiếng Tây Ban Nha
- `fr`: Tiếng Pháp
- `de`: Tiếng Đức
- `it`: Tiếng Ý
- `pt`: Tiếng Bồ Đào Nha
- `ru`: Tiếng Nga
- `ar`: Tiếng Ả Rập
- `vi`: Tiếng Việt

Các tập tin đã dịch sẽ được lưu theo mẫu đã cấu hình của bạn (mặc định: `README_{lang}.md`).

## Các lệnh

- `poly-readme install` - Cấu hình khóa API OpenAI
- `poly-readme setup` - Cấu hình cài đặt dự án
- `poly-readme translate` - Dịch các tập tin README
- `poly-readme help [command]` - Hiển thị thông tin trợ giúp

## Đóng góp

Hoan nghênh các đóng góp! Vui lòng gửi một Pull Request.

## Giấy phép

Dự án này được cấp phép theo Giấy phép MIT - xem tập tin LICENSE để biết chi tiết.

## Tác giả

- Chad Lee
- Email: think.bicycle@gmail.com
- GitHub: [drllr/poly-readme](https://github.com/drllr/poly-readme)

## Lời cảm ơn

- Công cụ này sử dụng mô hình GPT-4 của OpenAI để dịch thuật