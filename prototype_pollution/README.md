# blogs

https://portswigger.net/daily-swig/prototype-pollution-the-dangerous-and-underrated-vulnerability-impacting-javascript-applications
https://knqyf263.hatenablog.com/entry/2020/08/11/050342
https://knqyf263.hatenablog.com/entry/2020/08/09/234544
https://qiita.com/howdy39/items/35729490b024ca295d6c
https://developer.mozilla.org/ja/docs/Web/JavaScript/Inheritance_and_the_prototype_chain
https://slides.com/securitymb/prototype-pollution-in-kibana/#/47/0/0
https://book.hacktricks.xyz/pentesting-web/deserialization/nodejs-proto-prototype-pollution

# examples

https://github.com/mpgn/CVE-2019-7609
https://snyk.io/blog/after-three-years-of-silence-a-new-jquery-prototype-pollution-vulnerability-emerges-once-again/
https://thehackernews.com/2019/07/lodash-prototype-pollution.html
https://github.com/advisories/GHSA-9qmh-276g-x5pj

# https://www.elastic.co/guide/jp/kibana/current/tutorial-load-dataset.html
こちらの

```
curl -H 'Content-Type: application/json' -XPUT http://localhost:9200/shakespeare -d '
{
 "mappings" : {
  "_default_" : {
   "properties" : {
    "speaker" : {"type": "string", "index" : "not_analyzed" },
    "play_name" : {"type": "string", "index" : "not_analyzed" },
    "line_id" : { "type" : "integer" },
    "speech_number" : { "type" : "integer" }
   }
  }
 }
}
';
```

は

```
curl -H 'Content-Type: application/json' -XPUT http://localhost:9200/shakespeare -d '
{
 "mappings" : {
  "_default_" : {
   "properties" : {
    "speaker" : {"type": "text", "index" : false},
    "play_name" : {"type": "text", "index" : false},
    "line_id" : { "type" : "integer" },
    "speech_number" : { "type" : "integer" }
   }
  }
 }
}
';
```
でうまく行く

データを流し込んだら動いた

バージョンは6.5.4を使う

サーバーサイドでいい感じだし紹介するのはkibanaにしよう
