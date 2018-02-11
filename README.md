# LINE_BOT_MITUBA

## Usage
Please write your token to ./env_var.txt and put firebase key in project root directory.

And run the following command.

```
sh setup.sh
```

Please open other window, and ngrok command.

```
ngrok http 8000
```

## deploy

I use docker deploys of heroku

[Docker Deploys](https://devcenter.heroku.com/articles/container-registry-and-runtime)

Please use following commands

```
heroku container:login
heroku create
heroku container:push web
```

## dependencies

- [line/line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)
- docker
- python3.6.4
