# TouchDesigner-asyncio

TDAsyncIO.tox is a Component for using the asyncio module in TouchDesigner without blocking the TD's main thread by running the event loop only once at the start of every frame. 

## Usage

### Parameters
 - Active - The Event Loop can run asynchronous tasks while 'Active' is enabled<br>
 - Cancel All Tasks - Cancel all tasks you created.<br>

### Methods

``` python
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
```

### Code example

``` python
import asyncio

async def test():
    await asyncio.sleep(3)
    print('hello world')

# Run coroutine
coroutines = [test()]
routineFutures = op("TDAsyncIo").RunAsync(coroutines)

routineResult = op("TDAsyncIO").RunSync(coroutines)

# Cancel all tasks
op.TDAsyncIO.Cancel()
```
<br>

## License
[MIT](https://github.com/sndmtk/TouchDesigner-asyncio/blob/main/LICENSE)
