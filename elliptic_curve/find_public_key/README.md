
# 問題

difficulty: basic

楕円曲線暗号のd倍を実装して、公開鍵を計算してください。
公開鍵のx座標を求めたら以下のようなコードでフラグを復元可能です。

ヒント: dの値が大きいので少し工夫して計算する必要があります。参考: https://www.youtube.com/watch?v=HKDyUELFdXs

```
m = hashlib.sha256()
m.update(long_to_bytes( dGのx座標 ))
key = m.digest()[:16]
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.decrypt(pad(ciphertext, 16))
key = bytes_to_long(key)
```
