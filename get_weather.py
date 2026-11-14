import json
from openai import OpenAI

client = OpenAI(api_key="yours_api", base_url="https://api.deepseek.com")

# 1. 本地天气函数
def get_weather(city):
    return f"{city}：晴，25°C，空气质量优"

# 2. 工具说明书
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "查询指定城市的实时天气情况",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "城市名称，例如：北京、上海"}
            },
            "required": ["city"]
        }
    }
}]

# 3. 发起对话
messages = [{"role": "user", "content": "北京今天热不热？需要穿外套吗？"}]

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    tools=tools
)

msg = response.choices[0].message

# 4. 判断并执行工具
if msg.tool_calls:
    tool_call = msg.tool_calls[0]
    args = json.loads(tool_call.function.arguments)  # 拿到 {"city": "北京"}
    
    # 调用本地天气函数
    result = get_weather(args["city"])
    print(f"✅ 本地工具查到：{result}")
    
    # 5. 把天气结果还给大模型，让它结合结果回答“要不要穿外套”
    messages.append(msg)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": str(result)
    })
    
    final_response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )
    print(f"🤖 DeepSeek 最终回答：{final_response.choices[0].message.content}")