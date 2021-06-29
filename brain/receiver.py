from botutils.constants import FFN_CHECK_STR, AO3_CHECK_STR
from .ffn_brain import ffn_searcher
from .ao3_brain import ao3_searcher

def process_message(msg):
    all_embeds = []
    if FFN_CHECK_STR in msg:
        # process all ffn links in message
        ffn_obj = ffn_searcher.FFnSearcher(msg) 
        all_embeds_ffn = ffn_obj.execute_search()
        all_embeds += all_embeds_ffn

    if AO3_CHECK_STR in msg:
        # process all ao3 links in message 
        ao3_obj = ao3_searcher.Ao3Searcher(msg) 
        all_embeds_ao3 = ao3_obj.execute_search()
        all_embeds += all_embeds_ao3
    
    return all_embeds