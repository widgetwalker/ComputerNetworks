# Memcached Demo Programs

A comprehensive Python demonstration of Memcached key-value caching and its efficiency benefits.

## Overview

This project showcases:
- **Basic Cache Operations**: Set, get, and delete operations
- **Cache Hit/Miss Tracking**: Metrics to measure cache effectiveness
- **Efficiency Demonstration**: Before/after comparison showing how caching reduces network calls
- **Real-World Scenario**: E-commerce simulation showing practical caching benefits

## Files

- `memcache_demo_simulation.py` - In-memory cache simulation (no Memcached server required)
- `memcache_demo.py` - Real Memcached server integration (requires active server)
- `requirements.txt` - Python dependencies (pymemcache)

---

## Quick Start

### Option 1: Simulation (No Setup Required) ⭐ RECOMMENDED

```bash
py memcache_demo_simulation.py
```

This runs immediately with no additional setup!

### Option 2: Real Memcached Server

First, install and start Memcached:

**Install:**
- **Windows**: Download from [Memcached for Windows](https://github.com/microsoftarchive/memcached/wiki)
- **macOS**: `brew install memcached`
- **Linux**: `sudo apt-get install memcached`

**Start Memcached:**
```bash
# Linux/macOS
memcached -l 127.0.0.1 -p 11211

# Windows
memcached.exe -l 127.0.0.1 -p 11211
```

**Run the demo:**
```bash
py memcache_demo.py
```

---

## Program 1: Simulation Demo (No Memcached Required)

**File:** `memcache_demo_simulation.py`  
**Run:** `py memcache_demo_simulation.py`

### Features
- ✅ In-memory cache (simulates Memcached)
- ✅ No external server needed
- ✅ 5 comprehensive demonstrations
- ✅ Perfect for learning

### What It Demonstrates

**Demo 1: Basic Cache Operations**
- SET: Store key-value pairs
- GET: Retrieve from cache
- DELETE: Remove entries
- TTL/Expiration handling

**Demo 2: Cache Efficiency**
- Comparison: 5 requests without cache vs with cache
- Shows 5x speedup (80% faster)
- Network calls reduced from 5 to 1

**Demo 3: Cache Expiration**
- Time-To-Live (TTL) behavior
- Automatic cache invalidation
- Expired entry handling

**Demo 4: Real-World Scenario**
- E-commerce simulation
- 3 users viewing 2 products
- First access: cache miss
- Subsequent access: cache hit
- 79% hit rate achieved

**Demo 5: Cache Statistics**
- Performance monitoring
- Cache size tracking
- Hit/miss ratio analysis

### Sample Output

```
============================================================
MEMCACHED DEMO: SIMULATION MODE
(No Memcached server required)
============================================================

[OK] In-memory cache initialized (simulating Memcached)


============================================================
DEMO 1: BASIC CACHE OPERATIONS
============================================================

1. Setting values in cache:
  [SET] greeting = Hello, Memcached!
  [SET] counter = 42
  [SET] user:1 = {'id': 1, 'name': 'Alice'}

2. Retrieving values from cache:
  [CACHE HIT] greeting (retrieved in 0.00ms)
  [CACHE HIT] counter (retrieved in 0.00ms)
  [CACHE HIT] user:1 (retrieved in 0.00ms)

3. Deleting values from cache:
  [DELETE] counter
  Trying to retrieve deleted key:
  [CACHE MISS] counter - fetching from data store...
  [NOT FOUND] counter

4. Testing non-existent key:
  [CACHE MISS] nonexistent - fetching from data store...
  [NOT FOUND] nonexistent

5. Cache size after operations:
  Keys in cache: 2

============================================================
DEMO 2: CACHE EFFICIENCY - WITHOUT VS WITH CACHING
============================================================

--- Scenario 1: WITHOUT Cache (Simulated) ---
Making 5 identical requests without caching:

Request 1:
  [DB HIT] Fetched from database (100ms)

Request 2:
  [DB HIT] Fetched from database (100ms)

Request 3:
  [DB HIT] Fetched from database (100ms)

Request 4:
  [DB HIT] Fetched from database (100ms)

Request 5:
  [DB HIT] Fetched from database (100ms)

Total time without caching: 0.502 seconds
Total network calls: 5

--- Scenario 2: WITH Cache (Using In-Memory Storage) ---
Making 5 identical requests with caching:

Request 1:
  [CACHE MISS] user:1 - fetching from data store...
  [SET] user:1 = {"id": 1, "name": "Alice", "email": "alice@example.com"}
  [STORE] Cached user:1 for future requests

Request 2:
  [CACHE HIT] user:1 (retrieved in 0.00ms)

Request 3:
  [CACHE HIT] user:1 (retrieved in 0.00ms)

Request 4:
  [CACHE HIT] user:1 (retrieved in 0.00ms)

Request 5:
  [CACHE HIT] user:1 (retrieved in 0.00ms)

Total time with caching: 0.101 seconds
Total network calls: 1

------------------------------------------------------------
Efficiency Improvement: 80.0% faster
Speedup Factor:        5.0x
Network Calls Saved:   4 out of 5
Time Saved:            0.401 seconds
------------------------------------------------------------

============================================================
CACHE PERFORMANCE REPORT
============================================================
Cache Hits:      4
Cache Misses:    1
Hit Rate:        80.0%
Network Calls:   1
Total Time:      0.1007 seconds
============================================================

============================================================
DEMO 3: CACHE EXPIRATION
============================================================

1. Setting value with 2-second TTL:
  [SET] temp_data = expires soon

2. Immediate retrieval (should hit cache):
  [CACHE HIT] temp_data (retrieved in 0.00ms)

3. Waiting 2.5 seconds for expiration...

4. Retrieval after expiration (should miss cache):
  [CACHE MISS] temp_data - fetching from data store...
  [NOT FOUND] temp_data

============================================================
DEMO 4: REAL-WORLD SCENARIO - E-COMMERCE
============================================================

Simulating an e-commerce application with user and product data:
Scenario: 3 users viewing 2 products multiple times

Simulation 1 - First page load (all cache misses):

  user:1 viewing product:101:
  [CACHE MISS] user:1 - fetching from data store...
  [SET] user:1 = {"id": 1, "name": "Alice", "email": "alice@example.com"}
  [STORE] Cached user:1 for future requests
  [CACHE MISS] product:101 - fetching from data store...
  [SET] product:101 = {"id": 101, "name": "Laptop", "price": 999.99}
  [STORE] Cached product:101 for future requests

  user:1 viewing product:102:
  [CACHE HIT] user:1 (retrieved in 0.00ms)
  [CACHE MISS] product:102 - fetching from data store...
  [SET] product:102 = {"id": 102, "name": "Mouse", "price": 29.99}
  [STORE] Cached product:102 for future requests

  user:2 viewing product:101:
  [CACHE MISS] user:2 - fetching from data store...
  [SET] user:2 = {"id": 2, "name": "Bob", "email": "bob@example.com"}
  [STORE] Cached user:2 for future requests
  [CACHE HIT] product:101 (retrieved in 0.00ms)

  user:2 viewing product:102:
  [CACHE HIT] user:2 (retrieved in 0.00ms)
  [CACHE HIT] product:102 (retrieved in 0.00ms)

  user:3 viewing product:101:
  [CACHE MISS] user:3 - fetching from data store...
  [SET] user:3 = {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
  [STORE] Cached user:3 for future requests
  [CACHE HIT] product:101 (retrieved in 0.00ms)

  user:3 viewing product:102:
  [CACHE HIT] user:3 (retrieved in 0.00ms)
  [CACHE HIT] product:102 (retrieved in 0.00ms)

----------------------------------------
Simulation 2 - Browsing continues (mostly cache hits):
(Users browse same data again)

  user:1 viewing product:101 again:
  [CACHE HIT] user:1 (retrieved in 0.00ms)
  [CACHE HIT] product:101 (retrieved in 0.00ms)
  user:1 viewing product:102 again:
  [CACHE HIT] user:1 (retrieved in 0.00ms)
  [CACHE HIT] product:102 (retrieved in 0.00ms)
  user:2 viewing product:101 again:
  [CACHE HIT] user:2 (retrieved in 0.00ms)
  [CACHE HIT] product:101 (retrieved in 0.00ms)
  user:2 viewing product:102 again:
  [CACHE HIT] user:2 (retrieved in 0.00ms)
  [CACHE HIT] product:102 (retrieved in 0.00ms)
  user:3 viewing product:101 again:
  [CACHE HIT] user:3 (retrieved in 0.00ms)
  [CACHE HIT] product:101 (retrieved in 0.00ms)
  user:3 viewing product:102 again:
  [CACHE HIT] user:3 (retrieved in 0.00ms)
  [CACHE HIT] product:102 (retrieved in 0.00ms)

============================================================
CACHE PERFORMANCE REPORT
============================================================
Cache Hits:      19
Cache Misses:    5
Hit Rate:        79.2%
Network Calls:   5
Total Time:      0.5022 seconds
============================================================
```

---

## Program 2: Real Memcached Demo

**File:** `memcache_demo.py`  
**Requires:** Active Memcached server running  
**Run:** `py memcache_demo.py`

### Features
- ✅ Real Memcached server connection
- ✅ Actual network communication
- ✅ Production-like behavior
- ✅ 3 comprehensive demonstrations
- ✅ Error handling and fallbacks

### What It Demonstrates

**Demo 1: Basic Operations**
- SET: Store values with TTL
- GET: Retrieve with cache hit/miss tracking
- DELETE: Remove from cache
- Real network latency measurement

**Demo 2: Cache Efficiency**
- Simulated database calls (100ms latency)
- Real cache vs database comparison
- Measured performance improvement
- Network call reduction

**Demo 3: Real-World Scenario**
- E-commerce platform simulation
- Multiple users, multiple products
- First access caches data
- Subsequent access uses cache
- Performance metrics tracked

### Requirements

Make sure Memcached is running before executing:

```bash
# Check if Memcached is running
# Linux/macOS
ps aux | grep memcached

# Windows (if installed)
tasklist | findstr memcached
```

---

## Key Metrics & Performance

### Cache Performance Indicators

- **Cache Hit**: Request served from cache (~1ms)
- **Cache Miss**: Request hits database/API (~100ms)
- **Hit Rate**: Percentage of cache hits vs total requests
- **Network Calls**: Count of actual database queries
- **Speedup**: Performance improvement (5x typical)

### Results from Demo

```
Without Caching:
- 5 requests × 100ms = 500ms
- Network calls: 5

With Caching:
- 1st request: 100ms (cache miss + store)
- 4 requests: 1ms each (cache hits)
- Total: 104ms
- Network calls: 1

IMPROVEMENT: 80% faster, 80% fewer network calls
Speedup Factor: 5.0x
```

---

## How Caching Improves Network Efficiency

1. **Reduced Database Load**: Fewer queries = more scalability
2. **Faster Response Times**: Memory (~1μs) vs Database (~100ms) vs Network (~500ms)
3. **Lower Bandwidth**: Less data transmitted
4. **Better User Experience**: Faster page loads
5. **Cost Savings**: Reduced server resource usage

---

## Use Cases

- **Session Storage**: User login/session data
- **Database Query Results**: Cache expensive queries
- **API Responses**: Cache third-party API data
- **Computed Data**: Cache calculation results
- **Configuration**: Cache app configuration
- **Leaderboards**: Cache rankings
- **Rate Limiting**: Track request counts

---

## Best Practices

1. **Set Appropriate TTLs**
   - Fast-changing data: 1-5 minutes
   - Regular data: 1 hour
   - Static data: 24 hours

2. **Cache Key Naming**: Use hierarchical format
   - Example: `user:123:profile`
   - Example: `product:456:price`

3. **Cache Invalidation**
   - Time-based: Let TTL expire
   - Event-based: Invalidate on changes
   - Explicit: Manual clear

4. **Monitor Performance**
   - Aim for >80% hit rate
   - Track response times
   - Monitor memory usage

5. **Handle Failures**
   - Always have database fallback
   - Graceful degradation
   - Error logging

---

## Installation

### Python Dependencies

```bash
pip install -r requirements.txt
```

This installs `pymemcache==4.0.0`

---

## Architecture

```
Request
  ↓
Check Cache (Memcached)
  ↓
  ├─ Hit: Return data (~1ms)
  │
  └─ Miss: Query Database (~100ms)
       ↓
       Store in cache for future (~3600s TTL)
```

---

## Performance Comparison

| Operation | Time |
|-----------|------|
| Cache Hit | ~1ms |
| Database Query | ~100ms |
| Network API Call | ~500ms+ |
| Disk I/O | ~1-10ms |

**Result: Memcached provides 10-100x improvement!**

---

## Troubleshooting

**"Connection refused" Error**
- Memcached not running
- Use simulation demo instead: `py memcache_demo_simulation.py`

**"Cache miss all the time"**
- TTL might be too short
- Check key naming consistency
- Verify data store setup

**"High memory usage"**
- Set lower TTL values
- Monitor cache size
- Implement eviction policies

---

## License

MIT License - Feel free to use and modify for educational purposes.
