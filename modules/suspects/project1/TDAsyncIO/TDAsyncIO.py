'''Info Header Start
Name : TDAsyncIO
Author : Wieland@AMB-ZEPH15
Saveorigin : AsyncIO_Dev.toe
Saveversion : 2023.12000
Info Header End'''
"""
TDAsyncIO - Utilities for asyncio library with TouchDesigner

Copyright (C) 2021 Motoki Sonoda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import asyncio
from typing import Union, Awaitable, List, Any

class TDAsyncIO:
	"""
	TDAsyncIO description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self._Loop = None

	def setNewLoop(self):
		self._Loop = asyncio.new_event_loop()
		return self._Loop

	@property
	def Loop(self):
		loop = self._Loop or self.setNewLoop()
		if loop.is_closed():
			loop = self.setNewLoop()
		return loop
	
	def _Update(self):
		# Evaluating if call_soon is really needed.
		# self.Loop.call_soon(self.Loop.stop) 

		"""
			If stop() is called while run_forever() is running, 
			the loop will run the current batch of callbacks 
			and then exit. 
			Note that new callbacks scheduled by callbacks will not run in this case; 
			instead, they will run the next time run_forever() or run_until_complete() is called.
		"""
		self.Loop.stop()
		self.Loop.run_forever()
		

	def __delTD__(self):
		self.Loop.close()
	
	def RunSync(self, coroutines:Union[ List[Awaitable], Awaitable], timeout = 0) -> List[Any]:
		returnData = []
		for coroutine in coroutines if type(coroutines) is list else [coroutines]:
			returnData.append(
				self.Loop.run_until_complete( coroutine )
			)
		return returnData
			

	def RunAsync(self, coroutines:Union[ List[Awaitable], Awaitable]) -> List[asyncio.Task]:
		returnTasks = []
		for coroutine in coroutines if type(coroutines) is list else [coroutines]:
			returnTasks.append( 
				self.Loop.create_task(coroutine)
			)
		return returnTasks
	


	def Cancel(self, killList = [] ):
		for task in killList or asyncio.all_tasks(self.Loop):
			task.cancel()