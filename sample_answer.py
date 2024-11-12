text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# テキストからカンマとピリオドを取り除く
cleaned_text = ''.join(c for c in text if c not in ',.')

# テキストをスペースで分割し、各単語の長さを取得
word_lengths = list(map(len, cleaned_text.split()))

# 各単語の長さを文字列に変換して結合
result = ''.join(map(str, word_lengths))

print(result)
