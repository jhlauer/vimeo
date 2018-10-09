import base64
import requests

OAUTH_TOKEN = "f9394bc6e461c4ef3c0951aeff127ef6"
CLIENT_ID = b"a82a96cdbbf8d5bee5def75ad79d82823b32169e"
CLIENT_SECRET = b"Fjj9/he0uiU1msr7R4Eb2O3YneZ7o5XsN09aqKHnII+XqC3RNxvTBgn3V5e6zjkJKYljHQzngI8uZn8+z9QechktamjywKbHT3Atdz65TgiVzoLVHduWxp4meQO6+I1c"
headers = {"Authorization": "basic " + str(base64.b64encode(CLIENT_ID + b":" + CLIENT_SECRET))}
data = {"grant_type": "client_credentials", "scope": "public"}
auth = requests.post("https://api.vimeo.com/oauth/authorize/client/", data=data, headers=headers)
print(auth)

# safe staff picks for Vimeo videos !!!
baseurl = "https://api.vimeo.com//channels/staffpicks/videos?filter=content_rating&filter_content_rating=safe,unrated"
response = requests.get(baseurl)
print(response)
