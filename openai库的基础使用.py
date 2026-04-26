from openai import OpenAI
# 获取client对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# 调用模型
response = client.chat.completions.create(
    model = "qwen3-max",
    messages = [
        {"role":"system","content": "你是一个python 专家，并且不说废话简单回答"},
        {"role":"assistant","content":"好的，我是编程专家，并且话不多，你要问什么？"},
        {"role":"user","content":"你喜欢吃什么？"}
    ]
)
# 处理结果
print(response.choices[0].message.content)