import logging
from fp.fp import FreeProxy

proxy_cache = set()

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
                proxy_cache.add(proxy)

        logging.info(f'Fetched proxy: {proxy}\n')
        return proxy
    
    except Exception as error:
        logging.error(f'Error in function __get_proxy_url', error)
        raise error