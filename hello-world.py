import asyncio # Requires Python 3.4

loop = asyncio.get_event_loop()

loop.call_soon(lambda: print("Hello World!"))

loop.run_forever()
