import re
import requests
import json

from botutils.constants import FFN_CHECK_STR, AO3_CHECK_STR, HS_API_URL
from botutils.embeds import get_embeds

class FFnSearcher:
    def __init__(self, message):
        self.message = message

    def execute_search(self):
        all_links = re.findall(r'(https?://[^\s]+)', self.message)
        all_links_to_get_stories_for = []
        for link in all_links:
            if FFN_CHECK_STR in link:
                all_links_to_get_stories_for.append(link)
        
        res_metadata = []
        for link in all_links_to_get_stories_for:
            try:
                story_id = link[link.index('s/')+2 : link.index('/', link.index('s/')+4)]
            except:
                story_id = link[link.index('s/')+2 :]
            response = requests.get(f'{HS_API_URL}/{story_id}')
            data = json.loads(response.text)
            res_metadata.append(data)
        
        self.res_embeds = get_embeds(res_metadata)
        return self.res_embeds

    