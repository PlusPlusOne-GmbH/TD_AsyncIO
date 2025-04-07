'''Info Header Start
Name : timer_example
Author : Wieland PlusPlusOne@AMB-ZEPH15
Saveorigin : AsyncIO_Dev.toe
Saveversion : 2023.12000
Info Header End'''
from asyncio import sleep

async def runTimer(timerComp, length):
    currentFrame = absTime.frame # We have to do somewankiness here because of parameter-pulse delays to end of frame.
    timerComp.par.length.val = length
    timerComp.par.initialize.pulse()
    timerComp.par.start.pulse()
    while timerComp["running"] or currentFrame == absTime.frame: 
        await sleep(0)

async def timerText(timerComp):
    debug("starting Timer")
    await runTimer( timerComp, 2)
    debug("Lets do it again")
    await runTimer( timerComp, 4)
    debug("Foobar")

op("TDAsyncIO").RunAsync( timerText( op("timer2") ) )
    