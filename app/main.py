import sys
import asyncio
import logging

from app.core.env import settings
from app.services.essays_service import EssaysService

# set logging level and foramt
logging.basicConfig(stream=sys.stdout, level=settings.LOGGING_LEVEL, format='%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

async def main():
    try:
        logging.info('Starting firefly home assignment...')

        essays_service = EssaysService()
        await essays_service.run()
        
        logging.info('Finished successfully :-)')

    except Exception as error:
        logging.error('Error in function main', error)

asyncio.run(main())