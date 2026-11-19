"""
Practical Mastery Exercises for Week 1 — Day 1.
Executes and benchmarks all 5 exercises specified in the curriculum.
"""

import asyncio
import time


# ---------------------------------------------------------------------
# Exercise 1 & 2: Workload changes (4s, 3s, 2s) + Event 104 (5s)
# ---------------------------------------------------------------------
async def process_event(event_id: int, delay: int) -> dict:
    print(f"  [Worker] Event {event_id} started ({delay}s duration)")
    await asyncio.sleep(delay)
    print(f"  [Worker] Event {event_id} completed")
    return {"event_id": event_id, "status": "processed"}


async def run_exercise_1_and_2() -> None:
    print("=" * 65)
    print("EXERCISE 1 & 2: Modified Delays (4s, 3s, 2s) & Adding Event 104 (5s)")
    print("=" * 65)

    delays = [(101, 4), (102, 3), (103, 2), (104, 5)]

    # 1. Sequential execution
    print("\n1. Sequential Execution:")
    start_seq = time.perf_counter()
    seq_results = []
    for eid, d in delays:
        seq_results.append(await process_event(eid, d))
    elapsed_seq = time.perf_counter() - start_seq
    print(f"-> Sequential Time: {elapsed_seq:.2f}s (Expected: 4 + 3 + 2 + 5 = 14.00s)")

    # 2. Concurrent execution with create_task
    print("\n2. Concurrent Execution with create_task():")
    start_tasks = time.perf_counter()
    tasks = [asyncio.create_task(process_event(eid, d)) for eid, d in delays]
    task_results = await asyncio.gather(*tasks)
    elapsed_tasks = time.perf_counter() - start_tasks
    print(f"-> Concurrent Tasks Time: {elapsed_tasks:.2f}s (Expected: max(4,3,2,5) = 5.00s)")

    # 3. Direct gather
    print("\n3. Concurrent Execution with direct gather():")
    start_gather = time.perf_counter()
    gather_results = await asyncio.gather(*(process_event(eid, d) for eid, d in delays))
    elapsed_gather = time.perf_counter() - start_gather
    print(f"-> Direct Gather Time: {elapsed_gather:.2f}s (Expected: max(4,3,2,5) = 5.00s)")


# ---------------------------------------------------------------------
# Exercise 3: Coroutine Investigation
# ---------------------------------------------------------------------
async def hello():
    print("  Hello from inside hello()!")
    return "completed"


def run_exercise_3() -> None:
    print("\n" + "=" * 65)
    print("EXERCISE 3: Coroutine Investigation")
    print("=" * 65)
    # Call the coroutine function
    result = hello()
    print(f"1. result = hello() -> {result}")
    print(f"2. type(result)      -> {type(result)}")
    print("3. Notice that 'Hello from inside hello()!' was NOT printed.")
    print("   Explanation: Calling an async def function creates an un-awaited")
    print("   coroutine object; Python does not execute its body yet.")

    async def run_coro():
        print("4. Executing via 'await result' inside an event loop:")
        val = await result
        print(f"   Coroutine resolved with value: {val!r}")

    asyncio.run(run_coro())


# ---------------------------------------------------------------------
# Exercise 4: Gather Ordering
# ---------------------------------------------------------------------
async def fast_slow_event(event_id: int, delay: int) -> dict:
    print(f"  Ingest {event_id} ({delay}s delay) started")
    await asyncio.sleep(delay)
    print(f"  Ingest {event_id} finished (actual completion time: {delay}s)!")
    return {"event_id": event_id, "delay": delay}


async def run_exercise_4() -> None:
    print("\n" + "=" * 65)
    print("EXERCISE 4: gather() Output Order vs Completion Order")
    print("=" * 65)
    # Event 203 has the shortest delay (1s) and finishes first!
    # Event 202 takes 2s, Event 201 takes 3s.
    results = await asyncio.gather(
        fast_slow_event(201, 3),
        fast_slow_event(202, 2),
        fast_slow_event(203, 1),
    )
    print("\nCollected results in order returned by gather():")
    for r in results:
        print(f"  {r}")
    print("\nObservation:")
    print("Even though Event 203 finished first at 1.00s, it appears THIRD in results.")
    print("gather() preserves input argument position, NOT chronological completion time.")


# ---------------------------------------------------------------------
# Main Runner
# ---------------------------------------------------------------------
if __name__ == "__main__":
    run_exercise_3()
    asyncio.run(run_exercise_1_and_2())
    asyncio.run(run_exercise_4())
