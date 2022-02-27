# Deploy article storage and feed provider on fly.io

Clone or download this repo and setup environment:

```
# Clone (or download)
git clone https://github.com/stefanw/articles-to-feed.git
cd articles-to-feed

# Setup Python virtualenv
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install datasette datasette-publish-fly
```

[`flyctl`](https://fly.io/docs/getting-started/installing-flyctl/) must be installed.

```
datasette publish fly \
    --app <your-app-name> \
    --create-volume 1 \
    --create-db articles \
    --install datasette-init \
    --install datasette-atom \
    --install datasette-auth-tokens \
    --install datasette-auth-passwords \
    --metadata metadata.yml \
    --plugins-dir ./plugins/ \
    --region fra

```

Generate password hash for user with username `user`:

```
datasette hash-password
```

Generate a secret bot token:

```
python -c 'import secrets; print(secrets.token_hex(32))'
```

Set secret on fly app:

```
flyctl --app <your-app-name> secrets set BOT_TOKEN=<bot token here> PASSWORD_HASH=<password_hash>
```

Go to `/-/login` on your instance to login.

Use the following URL to accept content via POST requests:

```
https://example.fly.dev/articles/add_article?_auth_token=<bot token here>
```

Use the following URL for your feed reader:

```
https://example.fly.dev/articles/feed.atom?_auth_token=<bot token here>
```