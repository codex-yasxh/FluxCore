import asyncio
import sys
import time

"""
Demonstration of why blocking calls are hazardous in asynchronous event loops.

1. When time.sleep(3) is called, it blocks the entire operating system thread
   running the asyncio event loop. Normal operations cannot even start until the
   blocking call finishes. Total time: ~4.00s.

2. When using await asyncio.sleep(3), the coroutine yields control cooperatively,
   allowing normal_operation() to run and finish concurrently. Total time: ~3.00s.
"""


async def blocking_operation(use_async_sleep: bool = False) -> None:
    print("Blocking operation started")
    if use_async_sleep:
        await asyncio.sleep(3)
    else:
        # This blocks the event-loop thread!
        time.sleep(3)
    print("Blocking operation finished")


async def normal_operation() -> None:
    print("Normal operation started")
    await asyncio.sleep(1)
    print("Normal operation finished")


async def main() -> None:
    use_async = "--fix" in sys.argv
    if use_async:
        print("Running with cooperative non-blocking wait (FIXED: asyncio.sleep):")
    else:
        print("Running with synchronous blocking wait (DANGEROUS: time.sleep):")

    start = time.perf_counter()
    await asyncio.gather(
        blocking_operation(use_async_sleep=use_async),
        normal_operation(),
    )
    elapsed = time.perf_counter() - start
    print(f"\nTotal time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
