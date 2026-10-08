[app]
title = OSINT Checker
package.name = osintchecker
package.domain = org.miapp
source.dir = .
version = 0.1

requirements = python3, kivy, aiohttp

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.ndk = 25b
android.accept_sdk_license = True
android.sdk_build_tools = 33.0.2
