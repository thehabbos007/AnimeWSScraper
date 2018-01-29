
import logging
from queue import Queue
from threading import Thread
from time import time
import requests
from bs4 import BeautifulSoup
import urllib.parse as  urlparse
import random
import re

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


class DownloadWorker(Thread):
	def __init__(self, queue):
		Thread.__init__(self)
		self.queue = queue

	def run(self):
		while True:
			# Get the work from the queue and expand the tuple
			list, link, i = self.queue.get()
			(linkParse(link, list, i))
			self.queue.task_done()

def workIt(fullList):
   appendlist = {}
   #appendlist = []
   ts = time()
   links = fullList
   # Create a queue to communicate with the worker threads
   queue = Queue()
   # Create 8 worker threads
   for x in range(8):
       worker = DownloadWorker(queue)
       # Setting daemon to True will let the main thread exit even though the workers are blocking
       worker.daemon = True
       worker.start()
   # Put the tasks into the queue as a tuple
   for i, link in links.items():
       logger.info('Queueing {}'.format(link))
       queue.put((appendlist, link, i))
   # Causes the main thread to wait for the queue to finish processing all the tasks
   queue.join()
   print('Took {}'.format(time() - ts))

   return appendlist


def linkParse(link, list, i):
    req = requests.get(link)
    soup = BeautifulSoup(req.content, "html.parser")
    try:
        links = soup.find("source")['src']
    except Exception as exception:
        return ("Link not available")

    list[i] = (links)
    return list
