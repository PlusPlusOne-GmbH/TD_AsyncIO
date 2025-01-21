'''Info Header Start
Name : print_example
Author : Wieland@AMB-ZEPH15
Saveorigin : AsyncIO_Dev.toe
Saveversion : 2023.12000
Info Header End'''
from asyncio import sleep
from datetime import datetime
async def say(word, fifoOp):
	for index in range(2):
		fifoOp.appendRow([word, index, datetime.now().second])
		await sleep(1)


coroutines = [say("Foobar", op("fifo1")), say("Foobar", op("fifo2"))]
op("TDAsyncIO").RunSync(coroutines)