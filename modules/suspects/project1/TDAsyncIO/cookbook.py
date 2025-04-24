'''Info Header Start
Name : cookbook
Author : Wieland PlusPlusOne@AMB-ZEPH15
Saveorigin : AsyncIO_Dev.toe
Saveversion : 2023.12000
Info Header End'''
from asyncio import sleep
from typing import Callable

async def NextFrame(length:int = 1):
    """ Waits for the defined number of frames. """
    startFrame = absTime.frame
    while absTime.frame <= startFrame + length:
        await sleep(0)
    return True

async def Function( func:Callable):
    """ Waits for the given function (without parameters) to return a truthy value. """
    while not func():
        await sleep(0)

