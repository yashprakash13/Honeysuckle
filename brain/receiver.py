from botutils.constants import FFN_CHECK_STR, AO3_CHECK_STR
from .ffn_brain import ffn_searcher

def process_message(msg):
    if FFN_CHECK_STR in msg:
        # process all ffn links in message
        ffn_obj = ffn_searcher.FFnSearcher(msg) 
        all_embeds = ffn_obj.execute_search()
        return all_embeds

    elif AO3_CHECK_STR in msg:
        # process all ao3 links in message TODO
        pass