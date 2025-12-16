[app]
title = NeoWatch
package.name = neowatch
package.domain = org.neoncarnival

source.dir = .
source.include_exts = py,kv,json,png,jpg

version = 0.1

requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2

[android]
api = 33
minapi = 21
ndk = 23b

archs = arm64-v8a

permissions = FOREGROUND_SERVICE,INTERNET,POST_NOTIFICATIONS

accept_sdk_license = True
