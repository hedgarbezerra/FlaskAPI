import pprint
import requests
from instagram import InstagramAPI


api = InstagramAPI(client_id='6b9e76139be2402bab6d3a7ced76d6ac', client_secret='3e3e0f9493714fffac9e730254796cf3',
                   access_token='13469900807.6b9e761.10bd77c820fa4a5c9d193ecc0982a7e9')


url = 'client_id=6b9e76139be2402bab6d3a7ced76d6ac client_secret=3e3e0f9493714fffac9e730254796cf3' \
    ' grant_type=authorization_code redirect_uri=http://localhost:3000 code=f759e34504d245b7b27a8a8b86fdaa4a ' \
    'https://api.instagram.com/oauth/13469900807.6b9e761.10bd77c820fa4a5c9d193ecc0982a7e9'

ulr = 'https://api.instagram.com/v1/users/13469901107/media/recent/?access_token=13469900807.6b9e761.10bd77c820fa4a5c9d193ecc0982a7e9'

r = requests.get(ulr)
# print(r)
pprint.pprint(r.json())