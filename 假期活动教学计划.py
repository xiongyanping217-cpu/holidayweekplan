import streamlit as st
import base64
import os

# 1. 页面基本配置（宽屏模式、标题）
st.set_page_config(
    page_title="Teaching and Learning Portal - Sparkletots",
    page_icon="🌟",
    layout="wide",
)

# 2. 自定义 CSS 样式：优化全局字体与 Streamlit 输入界面
st.markdown(
    """
    <style>
    /* 全局背景色微调 */
    .stApp {
        background-color: #f7f9fc;
    }
    
    input, textarea, button, select, label, p, div, span {
        font-family: "KaiTi", "楷体", "STKaiti", serif !important;
    }
    textarea, input {
        font-size: 16px !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. 顶部状态栏：左侧标题，右侧输入框
col_top_left, col_top_right = st.columns([3, 1])

with col_top_left:
    st.markdown(
        """
        <div style="padding-top: 8px;">
            <span style="font-size: 18px; font-weight: lighter; color: #1e293b;">PCF Sparkletots Preschool @ Punggol Shore (EY)</span>          
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_top_right:
    col_label, col_box = st.columns([1, 2])

    with col_label:
        st.markdown(
            "<p style='text-align: right; margin-top: 8px; font-weight: lighter; color: #334155;'>教师姓名：</p>",
            unsafe_allow_html=True,
        )

    with col_box:
        selected_teacher = st.text_input(
            "选择教师",
            label_visibility="collapsed",  # 隐藏 Streamlit 自带的标签名，保持简洁
        )

col_info1, col_info2, col_info3, col_info4 = st.columns(4)
with col_info1:
    centre_level = st.selectbox("年级", ["豆豆班", "幼小班", "幼儿班"])
with col_info2:
    centre_class = st.selectbox("班级", ["PN-2(2026)", "PN-3(2026)", "PN-4(2026)","PN-8(2026)","PN-9(2026)","PN-12(2026)"])
with col_info3:
    centre_term = st.selectbox("学段", ["第一学段", "第二学段", "第三学段","第四学段"])
with col_info4:
    centre_week = st.selectbox("周数", ["1", "2", "3","4","5","6","7","8","9","10","复习周"])

st.divider()

# 4. 中部周计划（星期与活动编号）
col_day1, col_day2, col_day3, col_day4, col_day5 = st.columns(5)
options1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12" ,"13", "14", "15", "16","17", "18", "19", "20"]

with col_day1:
    day1 = st.date_input("星期一")
    day_no1 = st.selectbox("活动编号", options1, key="day_1") 
    
with col_day2:
    day2 = st.date_input("星期二" )
    day_no2 = st.selectbox("活动编号", options1, key="day_2")
    
with col_day3:
    day3 = st.date_input("星期三")
    day_no3 = st.selectbox("活动编号", options1, key="day_3")
    
with col_day4:
    day4 = st.date_input("星期四")
    day_no4 = st.selectbox("活动编号", options1, key="day_4")
    
with col_day5:
    day5 = st.date_input("星期五")
    day_no5 = st.selectbox("活动编号", options1, key="day_5")

# 5. 学习品质
col_praise1, col_praise2, col_praise3, col_praise4, col_praise5 = st.columns(5)
options2 = ["坚毅", "专注", "好奇心", "创造", "赏识", "反思"]

with col_praise1:
    praise1 = st.selectbox("学习品质", options2, key="praise_1") 
with col_praise2:
    praise2 = st.selectbox("学习品质", options2, key="praise_2") 
with col_praise3:
    praise3 = st.selectbox("学习品质", options2, key="praise_3") 
with col_praise4:
    praise4 = st.selectbox("学习品质", options2, key="praise_4")  
with col_praise5:
    praise5 = st.selectbox("学习品质", options2, key="praise_5")  

# 6. 必要生活技能
col_skill1, col_skill2, col_skill3, col_skill4, col_skill5 = st.columns(5)
options3 = ["专注力与自控能力", "换位思考", "沟通能力", "建立联系", "思辨能力", "接受挑战", "自主学习、参与式学习"]

with col_skill1:
    skill1 = st.selectbox("必要生活技能", options3, key="skill1")
with col_skill2:
    skill2 = st.selectbox("必要生活技能", options3, key="skill2")
with col_skill3:
    skill3 = st.selectbox("必要生活技能", options3, key="skill3")
with col_skill4:
    skill4 = st.selectbox("必要生活技能", options3, key="skill4")
with col_skill5:
    skill5 = st.selectbox("必要生活技能", options3, key="skill5")

# 7. 活动目标
col_object1, col_object2, col_object3, col_object4, col_object5 = st.columns(5)

with col_object1:
    object1 = st.text_area("活动目标", key="object1", height=250)
with col_object2:
    object2 = st.text_area("活动目标", key="object2", height=250) 
with col_object3:
    object3 = st.text_area("活动目标", key="object3", height=250)
with col_object4:
    object4 = st.text_area("活动目标", key="object4", height=250)
with col_object5:
    object5 = st.text_area("活动目标", key="object5", height=250)

# 8. 底部其他课程与活动（学习站）
st.markdown(
    """
    <div style="
        border: 1px solid #cbd5e1; 
        border-radius: 8px; 
        padding: 12px 15px; 
        background-color: #ffffff; 
        margin-top: 15px;
        margin-bottom: 10px;
    ">
        <div style="font-weight: bold; font-size: 15px; color: #1e293b; font-family: 'KaiTi', '楷体', serif;">
            🎯 其他课程与活动 / 学习站
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

col_station1, col_sep1, col_station2, col_sep2, col_station3, col_sep3, col_station4, col_sep4, col_station5 = st.columns([
    1, 0.05, 1, 0.05, 1, 0.05, 1, 0.05, 1
])

with col_station1:
    station1 = st.text_area("学习站 1", key="station1", height=200)
with col_sep1:
    st.markdown("<div style='border-left: 1px solid #cbd5e1; height: 220px; margin: auto;'></div>", unsafe_allow_html=True)

with col_station2:
    station2 = st.text_area("学习站 2", key="station2", height=200)
with col_sep2:
    st.markdown("<div style='border-left: 1px solid #cbd5e1; height: 220px; margin: auto;'></div>", unsafe_allow_html=True)

with col_station3:
    station3 = st.text_area("学习站 3", key="station3", height=200)
with col_sep3:
    st.markdown("<div style='border-left: 1px solid #cbd5e1; height: 220px; margin: auto;'></div>", unsafe_allow_html=True)

with col_station4:
    station4 = st.text_area("学习站 4", key="station4", height=200)
with col_sep4:
    st.markdown("<div style='border-left: 1px solid #cbd5e1; height: 220px; margin: auto;'></div>", unsafe_allow_html=True)

with col_station5:
    station5 = st.text_area("学习站 5", key="station5", height=200)

st.info("字体提示：楷体。若电脑未安装楷体，浏览器可能改用后备字体。")

st.divider()

# 9. 高颜值排版 HTML 生成函数
def generate_html_report():
    days = [day1 if day1 else '星期一', day2 if day2 else '星期二', day3 if day3 else '星期三', day4 if day4 else '星期四', day5 if day5 else '星期五']
    day_nos = [day_no1, day_no2, day_no3, day_no4, day_no5]
    praises = [praise1, praise2, praise3, praise4, praise5]
    skills = [skill1, skill2, skill3, skill4, skill5]
    objects = [object1, object2, object3, object4, object5]
    stations = [station1, station2, station3, station4, station5]

    # 动态构建 5 天每一行的数据单元格
    header_cells = "".join([f"<th>📅 {d}</th>" for d in days])
    no_cells = "".join([f"<td class='highlight-text'>{n}</td>" for n in day_nos])
    praise_cells = "".join([f"<td>{p}</td>" for p in praises])
    skill_cells = "".join([f"<td>{s}</td>" for s in skills])
    object_cells = "".join([f"<td class='content-cell'>{o if o else '-'}</td>" for o in objects])
    station_cells = "".join([f"<td class='content-cell'>{s if s else '-'}</td>" for s in stations])

    # 自动读取同目录下的 pcf1.png 并转换为 Base64
    img_base64 = ""
    if os.path.exists("pcf1.png"):
        with open("pcf1.png", "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            img_base64 = f"data:image/png;base64,{encoded}"


    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>每周教学计划 - {centre_class}</title>
    <style>
        /* 页面基础全局设置 */
        @page {{
            size: A4 landscape; /* 设置横向打印 A4 */
            margin: 12mm;
        }}
        body {{
            background-color: #f1f5f9;
            font-family: "KaiTi", "楷体", "STKaiti", serif;
            margin: 0;
            padding: 30px 20px 20px 20px;
            color: #0f172a;
            -webkit-print-color-adjust: exact;
            position: relative; /* 作为绝对定位的参考系 */
        }}
        .page-container {{
            max-width: 1280px;
            margin: 0 auto;
            background: #ffffff;
            padding: -25px -30px ;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border: 1px solid #e2e8f0;
        }}     
        /* 右上角图标样式 */
        .top-right-icon {{
            position: absolute;
            top: -5px;
            right: 0px;
            width: 65px;
            height: auto;
            z-index: 9999;
        }}
        
        .header-bar {{
            /* ... 原有属性 ... */
            padding-right: 80px; /* 留出空间避免与右上角图标重叠 */
        }}
        /* 顶部 Logo 与表头 */
        .header-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #2563eb;
            padding-top: 12px;    /* 【新增】增加顶部内边距，给 Logo 顶部留出安全距离 */
            padding-bottom: 12px;
            margin-top: 15px;     /* 【新增】增加顶部外边距，防止紧贴打印页边缘被裁切 */
            margin-bottom: 18px;
            overflow: visible;    /* 【新增】确保溢出内容可见 */
            box-sizing: border-box;
        }}
        .brand-title {{
            font-size: 30px;
            font-weight: bold;
            color: #1e293b;
            letter-spacing: 0.5px;
        }}
        .brand-sub {{
            font-size: 20px;
            color: #2563eb;
            font-weight: normal;
        }}
        .teacher-badge {{
            font-size: 15px;
            color: #334155;
            background: #f8fafc;
            padding: 6px 14px;
            border-radius: 6px;
            border: 1px solid #cbd5e1;
        }}

        /* 档案卡信息栏 */
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin-bottom: 20px;
            background: #f8fafc;
            padding: 12px 18px;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            font-size: 15px;
        }}
        .info-item span {{
            color: #64748b;
        }}
        .info-item strong {{
            color: #0f172a;
        }}

        /* 表格样式 */
        .plan-table {{
            width: 100%;
            border-collapse: collapse;
            table-layout: fixed;
            margin-bottom: 15px;
            background: #ffffff;
        }}
        .plan-table th, .plan-table td {{
            border: 1px solid #cbd5e1;
            padding: 10px 12px;
            text-align: center;
            vertical-align: middle;
            word-wrap: break-word;
        }}
        .plan-table th {{
            background-color: #eff6ff;
            color: #1e40af;
            font-size: 16px;
            font-weight: bold;
            width: 18%;
        }}
        .plan-table td.row-header {{
            background-color: #f8fafc;
            color: #475569;
            font-weight: bold;
            width: 10%;
            font-size: 14px;
        }}
        .highlight-text {{
            font-weight: bold;
            color: #2563eb;
            font-size: 15px;
        }}
        .content-cell {{
            text-align: left !important;
            vertical-align: top !important;
            font-size: 14px;
            line-height: 1.5;
            white-space: pre-wrap;
            color: #1e293b;
        }}

        /* 导出网页专属打印按钮 */
        .print-btn-wrapper {{
            text-align: center;
            margin-top: 25px;
            margin-bottom: 5px;
        }}
        .print-btn {{
            background-color: #2563eb;
            color: #ffffff;
            padding: 12px 30px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2);
            font-family: "KaiTi", "楷体", serif;
            transition: all 0.2s ease;
        }}
        .print-btn:hover {{
            background-color: #1d4ed8;
        }}

        /* 打印模式控制 */
        @media print {{
            body {{
                background-color: #ffffff;
                padding: 0;
            }}
            .page-container {{
                box-shadow: none;
                border: none;
                padding: 0;
                width: 100%;
                max-width: 100%;
            }}
            .print-btn-wrapper {{
                display: none !important;
            }}
        }}
    </style>
</head>
<body>
    <!-- 将图标放在 page-container 外面，以 body 为定位基准，彻底解决被容器裁切覆盖的问题 -->
    <img src="{img_base64}" alt="Logo" class="top-right-icon">

    <div class="page-container">      
        <!-- 页头 Logo 标识 -->
        <div class="header-bar">
            <div>
                <span class="brand-title">PCF Sparkletots Preschool</span>
                <span class="brand-sub">@ Punggol Shore (EY)</span>
            </div>
            <div class="teacher-badge">
                教师姓名：<b>{selected_teacher if selected_teacher else '未填写'}</b>
            </div>
        </div>

        <!-- 课程信息格 -->
        <div class="info-grid">
            <div class="info-item"><span>年级：</span><strong>{centre_level}</strong></div>
            <div class="info-item"><span>班级：</span><strong>{centre_class}</strong></div>
            <div class="info-item"><span>学段：</span><strong>{centre_term}</strong></div>
            <div class="info-item"><span>周数：</span><strong>第 {centre_week} 周</strong></div>
        </div>

        <!-- 主结构教案表格 -->
        <table class="plan-table">
            <thead>
                <tr>
                    <th style="width: 10%;">活动日期</th>
                    {header_cells}
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="row-header">活动编号</td>
                    {no_cells}
                </tr>
                <tr>
                    <td class="row-header">学习品质</td>
                    {praise_cells}
                </tr>
                <tr>
                    <td class="row-header">必要生活技能</td>
                    {skill_cells}
                </tr>
                <tr>
                    <td class="row-header">活动目标</td>
                    {object_cells}
                </tr>
                <tr>
                    <td class="row-header">其他课程/学习站</td>
                    {station_cells}
                </tr>
            </tbody>
        </table>

        <!-- 嵌入在 HTML 页面底部的直接打印按钮 -->
        <div class="print-btn-wrapper">
            <button class="print-btn" onclick="window.print()">🖨️ 打印网页 / 导出为 PDF</button>
        </div>
    </div>
</body>
</html>'''


# 10. Streamlit 页面使用图片按钮替换原本的文本下载按钮
html_data = generate_html_report()
b64_html_content = base64.b64encode(html_data.encode("utf-8")).decode()
filename = f"Weekly_Plan_{centre_class}_Week{centre_week}.html"

# 读取 download_icon1.png 并转换为 Base64
btn_img_base64 = ""
if os.path.exists("download_icon1.png"):
    with open("download_icon1.png", "rb") as f:
        encoded_btn = base64.b64encode(f.read()).decode()
        btn_img_base64 = f"data:image/png;base64,{encoded_btn}"

# 渲染自定义的图片下载按钮
if btn_img_base64:
    download_link_html = f"""
    <div style="text-align: center; margin: 15px 0;">
        <a href="data:text/html;charset=utf-8;base64,{b64_html_content}" download="{filename}" title="点击下载教案">
            <img src="{btn_img_base64}" alt="下载教案" style="width: 180px; height: auto; cursor: pointer; border-radius: 6px; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        </a>
    </div>
    """
    st.markdown(download_link_html, unsafe_allow_html=True)
else:
    st.warning("未找到名为 'download_icon1.png' 的下载按钮图片文件，请确保它与 Python 脚本在同一目录下。")