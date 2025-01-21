"""Info Header Start
Name : TDAsyncIO
Author : Wieland@AMB-ZEPH15
Saveorigin : AsyncIO_Dev.toe
Saveversion : 2023.12000
Info Header End"""
'\nTDAsyncIO - Utilities for asyncio library with TouchDesigner\n\nCopyright (C) 2021 Motoki Sonoda\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in\nall copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\nTHE SOFTWARE.\n'
import asyncio
from typing import Union, Awaitable, List, Any

class TDAsyncIO:
    """
	TDAsyncIO description
	"""

    def __init__(self, ownerComp):
        self.ownerComp = ownerComp
        self._Loop = None
        pass

    @property
    def Loop(self):
        """
			Returns the Loop specified for this instance of TDAsyncIO.
			Each instance of the COMP has itws own eventLoop.
		"""
        pass

    def RunSync(self, coroutines: Union[List[Awaitable], Awaitable]) -> List[Any]:
        """
			Runs all passed routines concurrent, but stalls the process and returns the returnvalues as a list.
		"""
        pass

    def RunAsync(self, coroutines: Union[List[Awaitable], Awaitable]) -> List[asyncio.Task]:
        """
			Runs all routines concurrently and returns a list of tasks.
		"""
        pass

    def Cancel(self, killList=[]):
        """
			Cancels all tasks currently active or the defines task in the list.
		"""
        pass