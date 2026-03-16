"""
Memcached Demo Program - Simulation Mode (No Memcached Server Required)
Demonstrates key-value caching concepts without requiring an active Memcached instance.
"""

import time
from typing import Optional, Any
import json


class CacheMetrics:
    """Track cache performance metrics."""
    def __init__(self):
        self.cache_hits = 0
        self.cache_misses = 0
        self.total_time = 0
        self.network_calls = 0

    def record_hit(self, time_taken: float):
        self.cache_hits += 1
        self.total_time += time_taken

    def record_miss(self, time_taken: float):
        self.cache_misses += 1
        self.network_calls += 1
        self.total_time += time_taken

    def get_hit_rate(self) -> float:
        total = self.cache_hits + self.cache_misses
        return (self.cache_hits / total * 100) if total > 0 else 0

    def print_report(self):
        print("\n" + "="*60)
        print("CACHE PERFORMANCE REPORT")
        print("="*60)
        print(f"Cache Hits:      {self.cache_hits}")
        print(f"Cache Misses:    {self.cache_misses}")
        print(f"Hit Rate:        {self.get_hit_rate():.1f}%")
        print(f"Network Calls:   {self.network_calls}")
        print(f"Total Time:      {self.total_time:.4f} seconds")
        print("="*60 + "\n")


class SimulatedDataStore:
    """Simulates a slow database or API."""
    def __init__(self, delay: float = 0.1):
        self.delay = delay
        self.data = {
            "user:1": {"id": 1, "name": "Alice", "email": "alice@example.com"},
            "user:2": {"id": 2, "name": "Bob", "email": "bob@example.com"},
            "user:3": {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
            "product:101": {"id": 101, "name": "Laptop", "price": 999.99},
            "product:102": {"id": 102, "name": "Mouse", "price": 29.99},
            "config:app_version": "1.2.3",
            "config:max_users": "1000",
        }

    def fetch(self, key: str) -> Optional[str]:
        """Simulate a network/database call with latency."""
        time.sleep(self.delay)  # Simulate network/DB latency
        return json.dumps(self.data.get(key)) if key in self.data else None


class InMemoryCache:
    """In-memory cache simulation (mimics Memcached behavior)."""
    def __init__(self, timeout: int = 3600):
        self.timeout = timeout
        self.storage = {}
        self.metrics = CacheMetrics()
        self.data_store = SimulatedDataStore(delay=0.1)

    def set(self, key: str, value: Any, expire: int = None) -> bool:
        """Store a value in cache."""
        try:
            self.storage[key] = {
                "value": str(value),
                "expires": time.time() + (expire or self.timeout)
            }
            print(f"  [SET] {key} = {value}")
            return True
        except Exception as e:
            print(f"  [SET ERROR] {key}: {e}")
            return False

    def _is_expired(self, key: str) -> bool:
        """Check if cache entry has expired."""
        if key not in self.storage:
            return True
        return time.time() > self.storage[key]["expires"]

    def get(self, key: str) -> Optional[str]:
        """Retrieve a value from cache, or fetch from data store if not cached."""
        try:
            start_time = time.time()
            
            # Check if key exists and hasn't expired
            if key in self.storage and not self._is_expired(key):
                # Cache hit
                elapsed = time.time() - start_time
                self.metrics.record_hit(elapsed)
                cached_value = self.storage[key]["value"]
                print(f"  [CACHE HIT] {key} (retrieved in {elapsed*1000:.2f}ms)")
                return cached_value
            else:
                # Cache miss - fetch from data store
                print(f"  [CACHE MISS] {key} - fetching from data store...")
                value = self.data_store.fetch(key)
                
                elapsed = time.time() - start_time
                self.metrics.record_miss(elapsed)
                
                if value:
                    # Cache the newly fetched value
                    self.set(key, value)
                    print(f"  [STORE] Cached {key} for future requests")
                    return value
                else:
                    print(f"  [NOT FOUND] {key}")
                    return None
        except Exception as e:
            print(f"  [GET ERROR] {key}: {e}")
            return None

    def delete(self, key: str) -> bool:
        """Delete a value from cache."""
        try:
            if key in self.storage:
                del self.storage[key]
                print(f"  [DELETE] {key}")
                return True
            else:
                print(f"  [DELETE] {key} (not found)")
                return False
        except Exception as e:
            print(f"  [DELETE ERROR] {key}: {e}")
            return False

    def clear(self):
        """Clear entire cache."""
        try:
            self.storage.clear()
            print("  [FLUSH] Cache cleared")
        except Exception as e:
            print(f"  [FLUSH ERROR] {e}")

    def get_stats(self) -> dict:
        """Get cache statistics."""
        return {
            "size": len(self.storage),
            "hits": self.metrics.cache_hits,
            "misses": self.metrics.cache_misses,
            "hit_rate": self.metrics.get_hit_rate()
        }


def demo_basic_operations(cache: InMemoryCache):
    """Demonstrate basic set, get, delete operations."""
    print("\n" + "="*60)
    print("DEMO 1: BASIC CACHE OPERATIONS")
    print("="*60)
    
    print("\n1. Setting values in cache:")
    cache.set("greeting", "Hello, Memcached!")
    cache.set("counter", 42)
    cache.set("user:1", {"id": 1, "name": "Alice"})
    
    print("\n2. Retrieving values from cache:")
    cache.get("greeting")
    cache.get("counter")
    cache.get("user:1")
    
    print("\n3. Deleting values from cache:")
    cache.delete("counter")
    print("  Trying to retrieve deleted key:")
    cache.get("counter")
    
    print("\n4. Testing non-existent key:")
    cache.get("nonexistent")
    
    print("\n5. Cache size after operations:")
    stats = cache.get_stats()
    print(f"  Keys in cache: {stats['size']}")


def demo_cache_efficiency(cache: InMemoryCache):
    """Demonstrate efficiency gains from caching."""
    print("\n" + "="*60)
    print("DEMO 2: CACHE EFFICIENCY - WITHOUT VS WITH CACHING")
    print("="*60)
    
    # Clear cache to start fresh
    cache.clear()
    
    print("\n--- Scenario 1: WITHOUT Cache (Simulated) ---")
    print("Making 5 identical requests without caching:")
    
    scenario1_time = 0
    for i in range(5):
        print(f"\nRequest {i+1}:")
        start = time.time()
        time.sleep(0.1)  # Simulate database latency
        scenario1_time += time.time() - start
        print(f"  [DB HIT] Fetched from database (100ms)")
    
    print(f"\nTotal time without caching: {scenario1_time:.3f} seconds")
    print(f"Total network calls: 5")
    
    # Now demonstrate WITH cache
    print("\n--- Scenario 2: WITH Cache (Using In-Memory Storage) ---")
    print("Making 5 identical requests with caching:")
    
    cache.clear()
    cache.metrics = CacheMetrics()  # Reset metrics
    
    for i in range(5):
        print(f"\nRequest {i+1}:")
        cache.get("user:1")
    
    scenario2_time = cache.metrics.total_time
    print(f"\nTotal time with caching: {scenario2_time:.3f} seconds")
    print(f"Total network calls: {cache.metrics.network_calls}")
    
    efficiency_gain = ((scenario1_time - scenario2_time) / scenario1_time) * 100
    speedup = scenario1_time / scenario2_time if scenario2_time > 0 else 0
    
    print("\n" + "-"*60)
    print(f"Efficiency Improvement: {efficiency_gain:.1f}% faster")
    print(f"Speedup Factor:        {speedup:.1f}x")
    print(f"Network Calls Saved:   {5 - cache.metrics.network_calls} out of 5")
    print(f"Time Saved:            {scenario1_time - scenario2_time:.3f} seconds")
    print("-"*60)
    
    cache.metrics.print_report()


def demo_cache_expiration(cache: InMemoryCache):
    """Demonstrate cache expiration."""
    print("\n" + "="*60)
    print("DEMO 3: CACHE EXPIRATION")
    print("="*60)
    
    cache.clear()
    
    print("\n1. Setting value with 2-second TTL:")
    cache.set("temp_data", "expires soon", expire=2)
    
    print("\n2. Immediate retrieval (should hit cache):")
    cache.get("temp_data")
    
    print("\n3. Waiting 2.5 seconds for expiration...")
    time.sleep(2.5)
    
    print("\n4. Retrieval after expiration (should miss cache):")
    cache.get("temp_data")


def demo_real_world_scenario(cache: InMemoryCache):
    """Demonstrate a real-world caching scenario."""
    print("\n" + "="*60)
    print("DEMO 4: REAL-WORLD SCENARIO - E-COMMERCE")
    print("="*60)
    
    cache.clear()
    cache.metrics = CacheMetrics()
    
    print("\nSimulating an e-commerce application with user and product data:")
    print("Scenario: 3 users viewing 2 products multiple times\n")
    
    users = ["user:1", "user:2", "user:3"]
    products = ["product:101", "product:102"]
    
    print("Simulation 1 - First page load (all cache misses):")
    for user in users:
        for product in products:
            print(f"\n  {user} viewing {product}:")
            cache.get(user)
            cache.get(product)
    
    print("\n" + "-"*40)
    print("Simulation 2 - Browsing continues (mostly cache hits):")
    print("(Users browse same data again)\n")
    for user in users:
        for product in products:
            print(f"  {user} viewing {product} again:")
            cache.get(user)
            cache.get(product)
    
    cache.metrics.print_report()


def demo_cache_statistics(cache: InMemoryCache):
    """Demonstrate cache statistics and monitoring."""
    print("\n" + "="*60)
    print("DEMO 5: CACHE STATISTICS & MONITORING")
    print("="*60)
    
    cache.clear()
    cache.metrics = CacheMetrics()
    
    print("\nGenerating varied access patterns:")
    
    # Pattern 1: Frequently accessed keys
    for _ in range(3):
        cache.get("user:1")
        cache.get("product:101")
    
    # Pattern 2: Moderately accessed keys
    for _ in range(2):
        cache.get("user:2")
        cache.get("product:102")
    
    # Pattern 3: Rarely accessed keys
    cache.get("config:app_version")
    cache.get("config:max_users")
    
    stats = cache.get_stats()
    print("\n" + "-"*40)
    print("CACHE STATISTICS")
    print("-"*40)
    print(f"Keys in Cache:       {stats['size']}")
    print(f"Cache Hits:          {stats['hits']}")
    print(f"Cache Misses:        {stats['misses']}")
    print(f"Hit Rate:            {stats['hit_rate']:.1f}%")
    print("-"*40)


def main():
    """Main entry point."""
    print("\n" + "="*60)
    print("MEMCACHED DEMO: SIMULATION MODE")
    print("(No Memcached server required)")
    print("="*60)
    
    # Initialize in-memory cache
    cache = InMemoryCache()
    
    print("\n[OK] In-memory cache initialized (simulating Memcached)\n")
    
    try:
        # Run demonstrations
        demo_basic_operations(cache)
        demo_cache_efficiency(cache)
        demo_cache_expiration(cache)
        demo_real_world_scenario(cache)
        demo_cache_statistics(cache)
        
        print("\n" + "="*60)
        print("KEY TAKEAWAYS")
        print("="*60)
        print("[+] Caching stores frequently accessed data in fast memory")
        print("[+] Cache hits are orders of magnitude faster than DB/API calls")
        print("[+] Dramatically reduces network traffic and server load")
        print("[+] Improves application response times significantly")
        print("[+] Essential for scaling high-traffic applications")
        print("[+] Requires proper TTL management and cache invalidation")
        print("[+] Monitor cache hit rate to ensure effectiveness")
        print("="*60 + "\n")
        
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user")
    except Exception as e:
        print(f"\n\nError during demo: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
