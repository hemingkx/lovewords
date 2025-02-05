# 文件位置
origin_data_path = './love_word/data.csv'  # 情话的文本文件存放路径
data_path = './love_word/data.json'  # 诗歌的json文件存放路径
pickle_path = './love_word/love_word.npz'  # 预处理好的二进制文件

# 学习率设置
lr = 1e-3
# 训练轮次
epoch = 50
# batch size
batch_size = 128

# 模型参数
embedding_dim = 256
hidden_dim = 512

# 情话生成设置
vocab_size = 6497
maxlen = 60  # 超过这个长度的之后字被丢弃，小于这个长度的在前面补空格
max_gen_len = 80  # 生成情话最长长度
prefix_words = '我的胸口有点疼，因为你堵在我的心口了。'  # 生成情话的语境，如'我爱你'
start_words = '我爱你'  # 情话的开头部分
model_prefix = 'checkpoints/love_word'  # 模型保存路径
