# 問題

difficulty: basic

0~255のうちのどれかの値を署名したものがいくつか与えられます。
署名検証のアルゴリズムを使って鍵を特定してください。

鍵を復元したらoutput.txtのciphertextを以下のコードで復元できます。

この問題はまだ正解が確認されていません。
もし解けた方がいれば連絡いただければ嬉しいです。

```
key = long_to_bytes(key)
cipher = AES.new(key, AES.MODE_ECB)
flag = cipher.decrypt(pad(ciphertext, 16))
print(flag)
```