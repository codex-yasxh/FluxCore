import asyncio
import time


async def process_event(event_id: int, delay: int) -> dict:
    print(f"Starting event {event_id}")
    await asyncio.sleep(delay)
    print(f"Completed event {event_id}")
    return {
        "event_id": event_id,
        "status": "processed",
    }


async def main() -> None:
    start = time.perf_counter()

    event_101 = await process_event(101, 3)
    event_102 = await process_event(102, 2)
    event_103 = await process_event(103, 1)

    results = [event_101, event_102, event_103]
    elapsed = time.perf_counter() - start

    print("\nResults:", results)
    print(f"Total time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
