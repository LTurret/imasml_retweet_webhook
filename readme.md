# imasml_retweet_webhook

透過 Twitter OAuth2.0 App-only API 和 Discord webhook自動轉推 `@imasml` 的最新推文

## Notice

[其實 OAuth 1.0a 也可以用](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent)
> OAuth 1.0a is also available for this endpoint.

## Requirement

### Tokens

> **Twitter API**

去 [Developer portal](https://developer.twitter.com/) 註冊一組token，然後在目錄下新增以下列格式的 `json` 檔案

```json
{
    "CONSUMER_KEY": "",
    "CONSUMER_KEY_SECRET": "",
    "ACCESS_TOKEN": "",
    "ACCESS_TOKEN_SECRET": "",
    "WEBHOOK_URL": ""
}
```

---

> **Discord**

在頻道裡面新增webhook，把那條url塞到 `secret.json` 裡面

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
