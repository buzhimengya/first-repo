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
        {"role":"user","content":"输出1-100的数字，用python代码"}
    ],
    stream= True #开启了流式输出的模式
)
# 处理结果
# print(response.choices[0].message.content)

for chunk in response:
    print(chunk.choices[0].delta.content,
          end=" ", #每段之间以空格分隔
          flush= True, #立刻刷新缓冲区
          )