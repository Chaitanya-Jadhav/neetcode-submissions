class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task.
        # Example: tasks = ["A","A","A","B","B","B"] -> Counter({'A': 3, 'B': 3})
        count = Counter(tasks)
        
        # Step 2: Create a Max Heap based on task frequencies.
        # Python only has a min-heap (heapq), so we store the frequencies as negative numbers 
        # to simulate a max-heap. We only care about the counts, not the task names.
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        # The queue will store tasks that are on cooldown.
        # It will store pairs: [remaining_count, time_it_becomes_available]
        q = deque()

        # Step 3: Process tasks until both the heap (available tasks) and queue (cooling tasks) are empty.
        while maxHeap or q:
            time += 1 # A single unit of time passes (either we do a task or we idle)

            if not maxHeap:
                # OPTIMIZATION: If there are no tasks ready to execute, we are just idling.
                # Instead of incrementing time by 1 in a loop, we can fast-forward time 
                # to exactly when the next cooling task in the queue becomes available.
                time = q[0][1]
            else:
                # Pop the task with the highest frequency (most urgent).
                # Since counts are negative, adding 1 represents completing one instance of the task 
                # (e.g., -3 + 1 = -2).
                cnt = 1 + heapq.heappop(maxHeap)
                
                # If the count is not yet 0 (meaning cnt is still negative), it needs to run again.
                if cnt:
                    # Add it to the cooldown queue. It can run again at `current time + cooldown n`.
                    q.append([cnt, time + n])
            
            # Step 4: Check if any tasks have finished their cooldown.
            # If the queue has tasks and the task at the front is ready at the current 'time',
            # it means the cooldown period has passed.
            if q and q[0][1] == time:
                # Remove it from the queue and push it back into the max heap so it can be executed.
                heapq.heappush(maxHeap, q.popleft()[0])
                
        # Once both the heap and queue are empty, we've finished all tasks.
        return time