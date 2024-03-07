'''Info Header Start
Name : parameterSet_example
Author : Wieland@AMB-ZEPH15
Saveorigin : AsyncIO_Dev.toe
Saveversion : 2022.35320
Info Header End'''
from asyncio import sleep
async def say(word):
	for index in range(10):
		op("constant1").par.value0.val = index
		await sleep(1)


coroutines = [say("Foobar")]
op.TDAsyncIO.Run(coroutines)