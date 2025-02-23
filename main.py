from fastapi import FastAPI
import requests

app = FastAPI()

# 🔹 Thay API Key của bạn vào đây (đăng ký tại https://deepseek.com)
DEEPSEEK_API_KEY = "sk-831e1740053f4cadbdc0fc2837a1f6ad"

# 🔹 URL API của DeepSeek
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

@app.get("/")
def home():
    """Kiểm tra API đang chạy."""
    return {"message": "DeepSeek AI Chatbot is running!"}

@app.post("/chat")
def chat(request: dict):
    """Nhận tin nhắn từ người dùng và gửi tới DeepSeek."""
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",  # Model AI cần sử dụng
        "messages": [{"role": "user", "content": request["message"]}],
        "temperature": 0.7  # Mức độ sáng tạo của AI
    }
    
    # Gửi request đến DeepSeek API
    response = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers)

    # Trả kết quả về client
    return response.json()
