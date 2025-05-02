from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# 十干・十二支・六十干支
jikkan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
junishi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
kan_shi = [j + s for i, j in enumerate(jikkan) for s in junishi[i % 6::2] * 5][:60]

def calc_nisshi(birth_date):
    base_date = datetime(1900, 1, 31)  # 干支起点日（甲子）
    target = datetime.strptime(birth_date, "%Y-%m-%d")
    delta_days = (target - base_date).days
    return kan_shi[delta_days % 60]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    birth_date = request.form['birthdate']
    birth_time = request.form['birthtime']

    # 実際に日柱を算出
    nisshi = calc_nisshi(birth_date)

    # 仮データ（次に差し替え予定）
    meishiki = {
        '年柱': '調整中',
        '月柱': '調整中',
        '日柱': nisshi,
        '時柱': '調整中',
        '通変星': ['（後ほど追加）'],
        '十二運': ['（後ほど追加）'],
        '空亡': ['（後ほど追加）'],
        '大運': [],
        '流年': []
    }

    return render_template('result.html', name=name, birth_date=birth_date, birth_time=birth_time, meishiki=meishiki)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
