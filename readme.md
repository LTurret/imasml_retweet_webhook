# imasml_retweet_webhook

透過 Twitter API 和 Discord webhook 自動轉推 `@imasml` 的最新推文

## Requirement

### Tokens

此專案需要使用兩個服務的 API，其中 Discord 為選擇性使用

#### Twitter

去 [Developer portal](https://developer.twitter.com/) 註冊一組 token，然後在目錄下新增以下列格式的 `json` 檔案

```json
{
  "CONSUMER_KEY": "",
  "CONSUMER_KEY_SECRET": "",
  "ACCESS_TOKEN": "",
  "ACCESS_TOKEN_SECRET": "",
  "WEBHOOK_URL": ""
}
```

#### Discord (Optional)

在頻道裡面新增 webhook，把那條 url 塞到 `secret.json` 裡面

### Libraries / Packages

```console
requests_oauthlib
```

## Usage

```console
$ pyhton3 -B main.py
> OAuth response: ...
> Discord webhook response: ...
> ...
```

## TODO

- [ ] fix my spaghetti code
- [ ] split "retweeting" and "discord" function respectively
- [ ] easy CLI testing interface
- [ ] GUI interface
