import logging
from fp.fp import FreeProxy

from app.core.env import settings

proxy_cache = []

def get_proxy_url() -> str:
    """
        Fetching proxy from FreeProxy, and manage a proxy cache
        keep fetching until a new proxy.

        Returns:
        str
    """
    try:
        logging.info(f'Fetching proxy...')

        new_proxy = False
        while (not new_proxy):
            proxy = FreeProxy(country_id=['US'], https=False, rand=True).get()
            if not proxy in proxy_cache:
                new_proxy = True
                proxy_cache.append(proxy)
                # If we have more proxies then the threshold, pop the first one
                if len(proxy_cache) == settings.PROXY_LOOP_COUNT:
                    proxy_cache.pop(0)

        logging.info(f'Fetched proxy: {proxy}\n')
        return proxy
    
    except Exception as error:
        logging.error(f'Error in function get_proxy_url', error)
        raise error