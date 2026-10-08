[app]

title = OSINT Profile Checker
package.name = osintchecker
package.domain = org.osint

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

version = 0.1

requirements = python3,kivy,aiohttp

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2


[app:android]

android.permissions = INTERNET

android.api = 33
android.minapi = 21

android.archs = arm64-v8a

android.ndk = 25b
android.accept_sdk_license_agreements = True
android.build_tools_version = 34.0.0

