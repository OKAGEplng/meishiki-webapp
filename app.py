from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    birth_date = request.form['birthdate']
    birth_time = request.form['birthtime']

    # 仮の命式データ（ここに計算ロジックを後で入れる）
    meishiki = {
        '年柱': '己亥',
        '月柱': '庚戌',
        '日柱': '壬寅',
        '時柱': '甲子',
        '通変星': ['偏官', '正財', '印綬', '食神'],
        '十二運': ['墓', '冠帯', '建禄', '胎'],
        '空亡': ['寅', '卯'],
        '大運': [
            {'年齢': '10〜19歳', '干支': '癸丑', '空亡': False},
            {'年齢': '20〜29歳', '干支': '甲寅', '空亡': True},
        ],
        '流年': [
            {'年': 2025, '干支': '乙巳', '空亡': False},
            {'年': 2026, '干支': '丙午', '空亡': False},
        ]
    }

    return render_template('result.html', name=name, birth_date=birth_date, birth_time=birth_time, meishiki=meishiki)

if __name__ == '__main__':
    app.run(debug=True)
