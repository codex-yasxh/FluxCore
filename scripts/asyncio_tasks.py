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

    # Schedule all three coroutines as independent tasks.
    task_101 = asyncio.create_task(process_event(101, 3))
    task_102 = asyncio.create_task(process_event(102, 2))
    task_103 = asyncio.create_task(process_event(103, 1))

    print("All event-processing tasks scheduled.")

    # Wait for their completion and collect results.
    results = await asyncio.gather(task_101, task_102, task_103)
    elapsed = time.perf_counter() - start

    print("\nResults:", results)
    print(f"Total time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
