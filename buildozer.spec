[app]
title = NeoWatch
package.name = neowatch
package.domain = org.fusion
source.dir = .
source.include_exts = py,png,jpg,kv,jsonl,sh
version = 0.1.0
requirements = python3,kivy,pyjnius,plyer,pydantic
android.api = 34
android.minapi = 34
android.sdk = 33
android.ndk = 25b
android.permissions = FOREGROUND_SERVICE, INTERNET, ACCESS_WIFI_STATE, POST_NOTIFICATIONS
android.services = ViolaService:viola_service.py
android.foreground_service = True
android.archs = arm64-v8a
