import asyncio
import time


async def ingest_event(event_id: int, delay: int) -> dict:
    print(f"Ingesting event {event_id}")
    await asyncio.sleep(delay)
    print(f"Event {event_id} ingested")
    return {
        "event_id": event_id,
        "status": "accepted",
    }


async def main() -> None:
    start = time.perf_counter()

    results = await asyncio.gather(
        ingest_event(201, 3),
        ingest_event(202, 1),
        ingest_event(203, 2),
    )
    elapsed = time.perf_counter() - start

    print("\nCollected results:")
    for result in results:
        print(result)

    print(f"\nTotal time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
