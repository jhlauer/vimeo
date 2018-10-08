import json
import requests

ACESS_TOKEN = f9394bc6e461c4ef3c0951aeff127ef6
CLIENT_ID = a82a96cdbbf8d5bee5def75ad79d82823b32169e
CLIENT_SECRET = Fjj9/he0uiU1msr7R4Eb2O3YneZ7o5XsN09aqKHnII+XqC3RNxvTBgn3V5e6zjkJKYljHQzngI8uZn8+z9QechktamjywKbHT3Atdz65TgiVzoLVHduWxp4meQO6+I1c
AUTHORIZE_URL = https://api.vimeo.com/oauth/authorize

def vimeo(query):
    baseurl = "https://api.vimeo.com/oauth/authorize/client"

    #not sure what this is supposed to do
    authorization-header: "Authorization : basic " + base64(client_id + ":" + client_secret)

    request = requests.get(baseurl, params = {
        'response_type': "token",
        'client_id': CLIENT_ID,
        'grant_type': 'client_credentials'}
    response = request.json()
    return response 
    
