2. Core Computer Science Topics & Extended CS Trivia
2.1 Data Structures (High-Yield Trading Firm Questions)

**Arrays vs Linked Lists**
- Can you binary search a sorted linked list in O(log n)? (NO - requires O(n) traversal)
- Why can't you binary search a linked list? (No random access to middle elements)
- When would you choose a linked list over an array? (Frequent insertions/deletions at unknown positions)

**Hash Maps Deep Dive**
- Explain hash maps to someone with no technical background
- What happens when two keys hash to the same bucket? (Collision handling: chaining, open addressing)
- Hash map vs TreeMap - when to use each?
- What's the worst-case complexity of hash map operations? (O(n) if all keys hash to same bucket)
- How does a hash function work? What makes a good hash function?

**Set vs List**
- Differentiate between a Set and a List
- When would you use a Set instead of a List?
- How do you implement a Set using other data structures?

**Advanced Structures**
- Explain a heap and when you'd use it
- What's the difference between a min-heap and max-heap?
- Stack vs Queue - give real-world analogies
- How would you implement a queue using two stacks?
- What's a priority queue and how does it differ from a regular queue?

2.2 Complexity & Algorithm Analysis

**Big-O Fundamentals**
- Rank these: O(1), O(log n), O(n), O(n log n), O(n²)
- What's the difference between worst-case, average-case, and best-case complexity?
- Space complexity vs time complexity tradeoffs
- Can you have O(log n) space complexity? Give an example

**Specific Algorithm Questions**
- Why is quicksort O(n log n) average but O(n²) worst case?
- What sorting algorithm would you use for nearly-sorted data?
- How do you find the median of a stream of numbers efficiently?
- What's the fastest way to check if a number is a power of 2?

2.3 Numbers, Bits & Computer Architecture

**Bit Manipulation**
- How many values can n bits represent? (2^n)
- 32-bit vs 64-bit: Does 64-bit represent 2x more values? (NO - 2^32 times more)
- What's the range of a signed 32-bit integer? (-2^31 to 2^31-1)
- How do you check if a number is even without using modulo?
- What's two's complement and why do we use it?

**Floating Point**
- Why shouldn't you use == to compare floating point numbers?
- What's the difference between float and double precision?
- How would you safely compare two floats for equality?

**Endianness**
- What's the difference between big-endian and little-endian?
- Which does x86 architecture use? (Little-endian)
- Why does endianness matter in network programming?

2.4 Networking & Systems (Trading-Specific Focus)

**Latency Ordering Questions**
- Order from fastest to slowest: DNS lookup, TCP connection, UDP socket bind, HTTP request, FTP file download
- Answer: UDP bind < DNS lookup < TCP connection < HTTP request < FTP download
- Why is UDP faster than TCP for certain applications?
- What's the difference between latency and throughput?

**Network Protocols**
- TCP vs UDP: reliability vs speed tradeoffs
- What happens during a TCP three-way handshake?
- Why might a trading system prefer UDP over TCP?
- What's the role of DNS in web requests?
- How does HTTP/HTTPS work at a high level?

**System Performance**
- What causes network latency?
- How would you optimize network performance for high-frequency trading?
- What's the difference between bandwidth and latency?

2.5 Operating Systems & Concurrency

**Process vs Thread**
- What's the difference between a process and a thread?
- When would you use threads vs processes?
- What's context switching and why is it expensive?
- How does the OS scheduler decide which process to run next?

**Memory Management**
- Stack vs heap: what goes where?
- What's a memory leak and how do you prevent it?
- What's virtual memory and why is it useful?
- How does garbage collection work in high-level languages?

**Concurrency Issues**
- What's a race condition? Give an example
- How do you prevent race conditions?
- What's a deadlock and how do you avoid it?
- Mutex vs semaphore - when to use each?
- What's the producer-consumer problem?

2.6 System Design & Architecture

**Hotel Booking System (No Database)**
- Data structures: HashMap for reservations, TreeMap for date-based availability
- How do you handle concurrent bookings?
- What happens if two people try to book the same room simultaneously?
- How would you add persistence later?

**Cache Design**
- How would you implement an LRU cache?
- Cache hit vs cache miss - performance implications
- When would you use write-through vs write-back caching?

**Scalability Questions**
- How do you scale a system horizontally vs vertically?
- What's load balancing and why is it important?
- Database sharding vs replication - tradeoffs?

2.7 Programming Language Trivia

**Memory & Performance**
- Why is C++ often faster than Python?
- What's the difference between compiled and interpreted languages?
- Stack allocation vs heap allocation - which is faster and why?
- What's the difference between pass-by-value and pass-by-reference?

**Language-Specific**
- Python: What's the GIL and how does it affect multithreading?
- Java: What's garbage collection and when does it happen?
- C++: What's the difference between malloc and new?
- What's tail recursion and why is it important?

2.8 Additional CS Trivia (Trading Firm Favorites)

**Computer Architecture**
- What's CPU cache and why does it matter for performance?
- L1 vs L2 vs L3 cache - which is fastest?
- What's branch prediction and why is it important?
- How does pipelining work in CPUs?

**Data Representation**
- How are negative numbers represented in binary?
- What's overflow and underflow in integer arithmetic?
- Why do computers use base 2 instead of base 10?
- How is text encoded (ASCII vs Unicode)?

**Algorithm Puzzles**
- How do you reverse a linked list?
- How do you detect a cycle in a linked list?
- What's the fastest way to find duplicates in an array?
- How do you find the intersection of two sorted arrays?

**System Reliability**
- What's fault tolerance in distributed systems?
- How do you ensure data consistency across multiple servers?
- What's the CAP theorem in simple terms?
- What's the difference between horizontal and vertical scaling?
