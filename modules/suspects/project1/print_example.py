'''Info Header Start
Name : print_example
Author : Wieland@AMB-ZEPH15
Saveorigin : AsyncIO_Dev.toe
Saveversion : 2023.12000
Info Header End'''
from asyncio import sleep
async def say(word):
	for index in range(2):
		op("fifo1").appendRow([word, index, absTime.seconds])
		await sleep(1)


coroutines = [say("Foobar")]
op("TDAsyncIO").RunAsync(coroutines)