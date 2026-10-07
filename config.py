HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

FIRMAS_ERROR_GLOBAL = [
    "page not found", "página no encontrada", "user not found",
    "usuario no encontrado", "account not found", "cuenta no encontrada",
    "this profile doesn't exist", "does not exist", "no existe", "404 not found",
    "login", "sign in", "iniciar sesión"
]

PLATAFORMAS = {
    # 💬 Mensajería y Chat
    "WhatsApp": {
        "url": "https://api.whatsapp.com/send?phone={}",
        "firmas_error": ["phone number shared via url is invalid", "el número de teléfono es inválido"]
    },
    "Telegram": {
        "url": "https://t.me/{}",
        "firmas_error": ["if you have telegram, you can contact", "telegram: contact"]
    },
    "Messenger": {
        "url": "https://m.me/{}",
        "firmas_error": ["this page isn't available", "esta página no está disponible"]
    },
    "Signal": {
        "url": "https://signal.me/#p/{}",
        "firmas_error": ["invalid link", "enlace no válido"]
    },
    "Discord": {
        "url": "https://discord.com/users/{}",
        "firmas_error": ["unknown user", "usuario desconocido"]
    },
    "Viber": {
        "url": "https://viber.click/{}",
        "firmas_error": ["number not found", "número no encontrado"]
    },
    "Line": {
        "url": "https://line.me/R/ti/p/@{}",
        "firmas_error": ["user not found", "account not found"]
    },
    "KakaoTalk": {
        "url": "https://open.kakao.com/o/{}",
        "firmas_error": ["page not found", "not found"]
    },
    "Threema": {
        "url": "https://threema.id/{}",
        "firmas_error": ["id not found", "id no encontrada"]
    },
    "Session": {
        "url": "https://session.me/{}",
        "firmas_error": ["invalid id", "user not found"]
    },
    "Slack": {
        "url": "https://{}.slack.com",
        "firmas_error": ["there’s been a glitch", "workspace not found"]
    },
    "Snapchat": {
        "url": "https://www.snapchat.com/add/{}",
        "firmas_error": ["couldn't find", "sorry, couldn't find"]
    },
    "GroupMe": {
        "url": "https://groupme.com/contact/{}",
        "firmas_error": ["contact not found", "404"]
    },
    "Kik": {
        "url": "https://kik.me/{}",
        "firmas_error": ["user not found", "404"]
    },

    # 📸 Fotos, Videos y Streaming
    "Instagram": {
        "url": "https://www.instagram.com/{}/",
        "firmas_error": ["sorry, this page isn't available", "esta página no está disponible"]
    },
    "TikTok": {
        "url": "https://www.tiktok.com/@{}",
        "firmas_error": ["couldn't find this account", "no se pudo encontrar esta cuenta"]
    },
    "YouTube": {
        "url": "https://www.youtube.com/@{}",
        "firmas_error": ["404 not found", "this page isn't available", "esta página no está disponible"]
    },
    "Facebook": {
        "url": "https://www.facebook.com/{}",
        "firmas_error": ["this content isn't available right now", "este contenido no está disponible"]
    },
    "Pinterest": {
        "url": "https://www.pinterest.com/{}/",
        "firmas_error": ["user not found", "sorry, we couldn't find that page"]
    },
    "X / Twitter": {
        "url": "https://x.com/{}",
        "firmas_error": ["this account doesn’t exist", "esta cuenta no existe"]
    },
    "Threads": {
        "url": "https://www.threads.net/@{}",
        "firmas_error": ["sorry, this page isn't available"]
    },
    "BeReal": {
        "url": "https://bereal.com/{}",
        "firmas_error": ["user not found", "404"]
    },
    "Flickr": {
        "url": "https://www.flickr.com/people/{}",
        "firmas_error": ["page not found", "página no encontrada"]
    },
    "500px": {
        "url": "https://500px.com/p/{}",
        "firmas_error": ["page not found", "user not found"]
    },
    "VSCO": {
        "url": "https://vsco.co/{}/gallery",
        "firmas_error": ["page not found", "404"]
    },
    "Triller": {
        "url": "https://triller.co/@{}",
        "firmas_error": ["user not found", "404"]
    },
    "Clapper": {
        "url": "https://clapperapp.com/{}",
        "firmas_error": ["user not found"]
    },
    "Likee": {
        "url": "https://likee.video/@{}",
        "firmas_error": ["user does not exist", "user not found"]
    },
    "Rumble": {
        "url": "https://rumble.com/user/{}",
        "firmas_error": ["404 page not found", "user not found"]
    },
    "Odysee": {
        "url": "https://odysee.com/@{}",
        "firmas_error": ["there is nothing here", "channel not found"]
    },
    "BitChute": {
        "url": "https://www.bitchute.com/channel/{}/",
        "firmas_error": ["404", "channel not found"]
    },
    "Dailymotion": {
        "url": "https://www.dailymotion.com/{}",
        "firmas_error": ["this page does not exist", "esta página no existe"]
    },
    "Vimeo": {
        "url": "https://vimeo.com/{}",
        "firmas_error": ["sorry, we couldn’t find that page", "page not found"]
    },
    "Twitch": {
        "url": "https://www.twitch.tv/{}",
        "firmas_error": ["sorry. that content is unavailable", "lo sentimos"]
    },
    "Kick": {
        "url": "https://kick.com/{}",
        "firmas_error": ["404", "channel not found"]
    },
    "PeerTube": {
        "url": "https://peertube.tv/accounts/{}",
        "firmas_error": ["account not found", "404"]
    },

    # 📝 Redes, Comunidades y Perfiles
    "Reddit": {
        "url": "https://www.reddit.com/user/{}/",
        "firmas_error": ["nobody on reddit goes by that name", "sorry, nobody on reddit"]
    },
    "Quora": {
        "url": "https://www.quora.com/profile/{}",
        "firmas_error": ["page not found", "página no encontrada"]
    },
    "Medium": {
        "url": "https://medium.com/@{}",
        "firmas_error": ["out of nothing, something", "404"]
    },
    "Substack": {
        "url": "https://{}.substack.com",
        "firmas_error": ["publication not found", "404"]
    },
    "Tumblr": {
        "url": "https://{}.tumblr.com",
        "firmas_error": ["there's nothing here", "no hay nada aquí"]
    },
    "Mastodon": {
        "url": "https://mastodon.social/@{}",
        "firmas_error": ["record not found", "404"]
    },
    "Bluesky": {
        "url": "https://bsky.app/profile/{}.bsky.social",
        "firmas_error": ["could not resolve handle", "account not found"]
    },
    "DeviantArt": {
        "url": "https://www.deviantart.com/{}",
        "firmas_error": ["deviant is not found", "404 not found"]
    },
    "ArtStation": {
        "url": "https://www.artstation.com/{}",
        "firmas_error": ["page not found", "404"]
    },
    "Behance": {
        "url": "https://www.behance.net/{}",
        "firmas_error": ["we couldn't find that page", "user not found"]
    },
    "Dribbble": {
        "url": "https://dribbble.com/{}",
        "firmas_error": ["page not found", "404"]
    },
    "GitHub": {
        "url": "https://github.com/{}",
        "firmas_error": ["not found", "404"]
    },
    "GitLab": {
        "url": "https://gitlab.com/{}",
        "firmas_error": ["page not found", "404"]
    },
    "Stack Overflow": {
        "url": "https://stackoverflow.com/users/{}",
        "firmas_error": ["user does not exist", "page not found"]
    },
    "Product Hunt": {
        "url": "https://www.producthunt.com/@{}",
        "firmas_error": ["page not found", "404"]
    },
    "Hacker News": {
        "url": "https://news.ycombinator.com/user?id={}",
        "firmas_error": ["no such user"]
    },
    "MyAnimeList": {
        "url": "https://myanimelist.net/profile/{}",
        "firmas_error": ["404 not found", "could not be found"]
    },
    "Minds": {
        "url": "https://www.minds.com/{}",
        "firmas_error": ["channel not found", "404"]
    },
    "Gab": {
        "url": "https://gab.com/{}",
        "firmas_error": ["user not found", "404"]
    },
    "Truth Social": {
        "url": "https://truthsocial.com/@{}",
        "firmas_error": ["user not found", "account does not exist"]
    },
    "GETTR": {
        "url": "https://gettr.com/user/{}",
        "firmas_error": ["user not found", "404"]
    },
    "Parler": {
        "url": "https://parler.com/user/{}",
        "firmas_error": ["user not found", "404"]
    },
    "VK": {
        "url": "https://vk.com/{}",
        "firmas_error": ["page not found", "user not found"]
    },
    "Odnoklassniki": {
        "url": "https://ok.ru/{}",
        "firmas_error": ["page not found", "404"]
    },
    "Weibo": {
        "url": "https://weibo.com/u/{}",
        "firmas_error": ["page not found", "user not found"]
    },
    "Bilibili": {
        "url": "https://space.bilibili.com/{}",
        "firmas_error": ["space not found", "404"]
    },
    "Pixelfed": {
        "url": "https://pixelfed.social/{}",
        "firmas_error": ["user not found", "404"]
    },
    "SpaceHey": {
        "url": "https://spacehey.com/{}",
        "firmas_error": ["user not found", "profile not found"]
    },
    "Neocities": {
        "url": "https://{}.neocities.org",
        "firmas_error": ["site not found", "404"]
    },
    "Lemmy": {
        "url": "https://lemmy.world/u/{}",
        "firmas_error": ["could not find user", "user not found"]
    },
    "Kbin": {
        "url": "https://kbin.social/u/{}",
        "firmas_error": ["user not found", "404"]
    },
    "Misskey": {
        "url": "https://misskey.io/@{}",
        "firmas_error": ["no user found", "user not found"]
    },

    # 💰 Creadores y Monetización
    "Patreon": {
        "url": "https://www.patreon.com/{}",
        "firmas_error": ["page not found", "404"]
    },
    "Ko-fi": {
        "url": "https://ko-fi.com/{}",
        "firmas_error": ["page not found", "page missing"]
    },
    "Buy Me a Coffee": {
        "url": "https://www.buymeacoffee.com/{}",
        "firmas_error": ["page not found", "creator not found"]
    },
    "OnlyFans": {
        "url": "https://onlyfans.com/{}",
        "firmas_error": ["sorry, this page isn't available", "404"]
    },
    "Fansly": {
        "url": "https://fansly.com/{}",
        "firmas_error": ["user not found", "404"]
    },
    "JustForFans": {
        "url": "https://justfor.fans/{}",
        "firmas_error": ["user not found", "404"]
    },
    "Gumroad": {
        "url": "https://{}.gumroad.com",
        "firmas_error": ["page not found", "404"]
    },
    "Teepublic": {
        "url": "https://www.teepublic.com/user/{}",
        "firmas_error": ["artist not found", "404"]
    },
    "Redbubble": {
        "url": "https://www.redbubble.com/people/{}",
        "firmas_error": ["user not found", "404"]
    },
    "Ghost": {
        "url": "https://{}.ghost.io",
        "firmas_error": ["site not found", "404"]
    },
}







