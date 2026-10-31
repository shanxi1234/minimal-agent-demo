import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF-8')
import os
from openai import OpenAI

# 1. 设置你的 API Key
# 把下面引号里的内容换成你刚刚在 DeepSeek 后台复制的真实 Key
# 注意：保留外面的引号，千万不要把 Key 传到 GitHub 上！
os.environ["DEEPSEEK_API_KEY"] = "yours_API"

# 2. 初始化客户端
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# 3. 发送请求并获取回答
print("正在呼叫 DeepSeek，请稍等...")
response = client.chat.completions.create(
    model="deepseek-chat", # DeepSeek 官方通用的聊天模型
    messages=[
        {"role": "user", "content": "用一句话给我解释什么是AI Agent？"}
    ],
)

# 4. 打印结果
print("\n--- DeepSeek 的回答 ---")
print(response.choices[0].message.content)