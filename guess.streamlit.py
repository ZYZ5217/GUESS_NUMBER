import streamlit as st
import random

# 设置页面标题和图标
st.set_page_config(page_title="猜猜看", page_icon="🎮")

# 随机回复池（可根据需要自由扩展）
success_responses = {
    1: [  # 第一次猜中的回复
        "哇塞！第一次就成功了，我们心有灵犀耶！( •̀ ω •́ )✧",
        "天呐！第一次就猜对了，你是我的灵魂伴侣吗？✨",
        "Σ(っ °Д °;)っ 第一次就中？你开挂了吧！"
    ],
    2: [  # 第二次猜中的回复
        "好棒，成功了耶！ψ(｀∇´)ψ",
        "第二次就猜对啦，看来我们越来越默契了~ (^_−)☆",
        "这么快就猜中了？你是不是偷看了答案？(¬‿¬)"
    ],
    3: [  # 第三次猜中的回复
        "hhh 终于猜对啦！╰(*°▽°*)╯",
        "压线成功！差一点就要暴露我的数字啦~ (＞ω＜)",
        "呼~ 第三次才猜中，你的运气刚刚好呢 (´▽`ʃ♡ƪ)"
    ],
    "fail": [  # 失败时的回复
        "u_u 我想的是 %s，下次一定能猜中！( •̯́ _ •̯̀)",
        "答案是 %s 啦，别灰心，再试一次吧~ (ง •̀_•́)ง",
        "悄悄告诉你：其实是 %s，下次要更细心哦 (๑•́ ∀ •̀๑)"
    ]
}

# 初始化游戏状态
if 'num' not in st.session_state:
    st.session_state.num = random.randint(1, 8)  # 随机生成目标数字
if 'guess_count' not in st.session_state:
    st.session_state.guess_count = 0  # 初始化猜测次数

# 页面布局
st.title("猜数字游戏 (2-8) 🎲")
st.write("hi姐姐(●'◡'●),这是一个简单的小游戏")
st.write("我会在2-8之间随机想一个数字,看我们是否心有灵犀！")

# 用户输入
guess = st.number_input("你想的是多少呀：", min_value=2, max_value=8, step=1)

# 提交按钮
if st.button("提交猜测"):
    st.session_state.guess_count += 1
    if guess == st.session_state.num:
        # 根据尝试次数随机选择回复
        response = random.choice(success_responses[st.session_state.guess_count])
        st.success(response)
        # 重置游戏
        st.session_state.num = random.randint(2, 8)
        st.session_state.guess_count = 0
    else:
        # 提示用户猜测结果
        hint = "大" if guess > st.session_state.num else "小"
        st.error(f"第{st.session_state.guess_count}次猜测：比我想得要{hint}（＞人＜；），加油加油(●'◡'●)")
        if st.session_state.guess_count >= 3:
            # 三次都失败时随机选择回复
            response = random.choice(success_responses["fail"]) % st.session_state.num
            st.warning(response)
            # 重置游戏
            st.session_state.num = random.randint(2, 8)
            st.session_state.guess_count = 0

# 添加重新开始按钮
if st.button("重新开始"):
    st.session_state.num = random.randint(2, 8)
    st.session_state.guess_count = 0
    st.experimental_rerun()