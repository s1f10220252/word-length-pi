## 文字列と円周率

`How I want a drink, alcoholic` の英単語の文字数を並べると 314159 になり、円周率の数字の並びと同じになります。

この問題で実装するのは、24 単語からなる下の英文:

```
How I want a drink, alcoholic of course, after the heavy chapters involving
quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
```

の文字数を並べた文字列 (str 型) を返すプログラムです。実行結果は円周率 24 桁目までの `314159265358979323846264` になるはずです。

<details><summary>ヒント</summary>

下のコードのように `list`, `map`, `len` 関数を用いると、与えられたリストの各要素の文字数を得ることができます。

```python
list(map(len, ["a", "bc", "def"]))
```

[1, 2, 3]
</details>

## 要件

- 関数名は `get_pi_digits()` とします。
- 関数は引数を取らず、文字列を返します。
- 句読点や空白は単語の一部としてカウントしません。

## 手順

1. このリポジトリをフォークします。
2. フォークしたリポジトリをローカルにクローンします。
3. `pi.py` ファイルに `get_pi_digits()` 関数を実装します。
4. 変更をコミットし、プッシュします。

## テスト結果

- 正解すると、GitHubのコミット一覧や「Actions」タブに緑のチェックマーク（✅）が表示されます。
- 誤答すると、赤いバツ印（❌）が表示されます。
