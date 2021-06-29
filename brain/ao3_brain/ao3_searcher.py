import re
import requests
import json

from botutils.constants import AO3_CHECK_STR, HS_API_URL_AO3
from botutils.embeds import get_embeds_ao3

class Ao3Searcher:
    def __init__(self, message):
        self.message = message

    def execute_search(self):
        all_links = re.findall(r'(https?://[^\s]+)', self.message)
        all_links_to_get_stories_for = []
        for link in all_links:
            if AO3_CHECK_STR in link:
                all_links_to_get_stories_for.append(link)
        print(all_links_to_get_stories_for)
        res_metadata = []
        for link in all_links_to_get_stories_for:
            try:
                story_id = link[link.index('works/')+len('works/') : link.index('/', link.index('works/')+6)]
            except:
                story_id = link[link.index('works/')+len('works/') :]
            try:    
                response = requests.get(f'{HS_API_URL_AO3}/{story_id}')
                data = json.loads(response.text)
                res_metadata.append(data)
            except:
                print('Could not get metadata response for: ', story_id)
        
        self.res_embeds = get_embeds_ao3(res_metadata)
        return self.res_embeds

    