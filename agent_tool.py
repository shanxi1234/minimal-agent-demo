import sys
import io
import os
import json
from openai import OpenAI

# 1. 解决中文乱码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 2. 设置 API Key（换成你自己的）
os.environ["DEEPSEEK_API_KEY"] = "yours_API"

# 3. 初始化客户端
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# 4. 定义你的真实工具（给模型用的“手”）
def add(a: int, b: int):
    print(f"👉 [系统提示] 模型决定调用工具：正在计算 {a} + {b}")
    return a + b

# 5. 把工具描述给模型（也就是“说明书”）
tools = [{
    "type": "function",
    "function": {
        "name": "add",
        "description": "计算两个数字的加法",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "integer", "description": "第一个数字"},
                "b": {"type": "integer", "description": "第二个数字"}
            },
            "required": ["a", "b"]
        }
    }
}]

# 6. 发起对话
print("正在呼叫 DeepSeek 进行计算...")
messages = [{"role": "user", "content": "请帮我算一下 123 加上 456 等于多少？"}]

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    tools=tools
)

# 7. 处理模型的回复
msg = response.choices[0].message

# 如果模型决定调用工具
if msg.tool_calls:
    print("\n🔥 成功！模型决定调用工具了！")
    tool_call = msg.tool_calls[0]
    
    # 解析模型要传的参数
    args = json.loads(tool_call.function.arguments)
    
    # 你的代码去执行真正的函数
    result = add(args["a"], args["b"])
    
    print(f"✅ 代码执行完毕，结果是：{result}")
    
    # （可选进阶）你可以把结果再发回给模型，让它总结：
    # messages.append(msg)
    # messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": str(result)})
    # final_response = client.chat.completions.create(model="deepseek-chat", messages=messages)
    # print(f"🤖 模型最终回答：{final_response.choices[0].message.content}")
else:
    print("模型没有调用工具，直接回答了。")