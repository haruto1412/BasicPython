text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

text = text.replace(',', '')  # カンマを削除
text = text.replace('.', '')  # ピリオドを削除
words = text.split()  # テキストを空白で分割するやつ
word_lengths = list(map(len, words))  # 各単語の文字数を取得してリストに格納
result_string = ''.join(map(str, word_lengths))
print(result_string)
