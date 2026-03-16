"""
Memcached Demo Program
Demonstrates key-value caching with Memcached and showcases efficiency benefits.
"""

import time
from typing import Optional, Dict, Any
import sys

try:
    from pymemcache.client.hash import HashClient
except ImportError:
    print("pymemcache is not installed. Install it with: pip install pymemcache")
    sys.exit(1)


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
        return self.data.get(key)


class MemcachedCache:
    """Wrapper around Memcached with efficiency tracking."""
    def __init__(self, servers: list = None, timeout: int = 3600):
        if servers is None:
            servers = [("localhost", 11211)]
        
        self.servers = servers
        self.timeout = timeout
        self.metrics = CacheMetrics()
        self.client = None
        self.data_store = SimulatedDataStore(delay=0.1)
        self._connect()

    def _connect(self):
        """Connect to Memcached server."""
        try:
            self.client = HashClient(self.servers)
            # Test connection
            self.client.set(b"__test__", b"1")
            self.client.delete(b"__test__")
            print("[OK] Connected to Memcached server")
        except Exception as e:
            print(f"[FAIL] Failed to connect to Memcached: {e}")
            print("  Make sure Memcached is running on localhost:11211")
            sys.exit(1)

    def set(self, key: str, value: Any, expire: int = None) -> bool:
        """Store a value in cache."""
        try:
            expire = expire or self.timeout
            key_bytes = key.encode() if isinstance(key, str) else key
            value_bytes = str(value).encode() if not isinstance(value, bytes) else value
            self.client.set(key_bytes, value_bytes, expire=expire)
            print(f"  [SET] {key} = {value}")
            return True
        except Exception as e:
            print(f"  [SET ERROR] {key}: {e}")
            return False

    def get(self, key: str) -> Optional[str]:
        """Retrieve a value from cache, or fetch from data store if not cached."""
        try:
            key_bytes = key.encode() if isinstance(key, str) else key
            start_time = time.time()
            
            # Try to get from cache
            cached_value = self.client.get(key_bytes)
            elapsed = time.time() - start_time
            
            if cached_value:
                # Cache hit
                self.metrics.record_hit(elapsed)
                print(f"  [CACHE HIT] {key} (retrieved in {elapsed*1000:.2f}ms)")
                return cached_value.decode() if isinstance(cached_value, bytes) else cached_value
            else:
                # Cache miss - fetch from data store and cache it
                print(f"  [CACHE MISS] {key} - fetching from data store...")
                value = self.data_store.fetch(key)
                
                elapsed = time.time() - start_time + self.data_store.delay
                self.metrics.record_miss(elapsed)
                
                if value:
                    # Cache the newly fetched value
                    self.set(key, value)
                    print(f"  [STORE] Cached {key} for future requests")
                    return str(value)
                else:
                    print(f"  [NOT FOUND] {key}")
                    return None
        except Exception as e:
            print(f"  [GET ERROR] {key}: {e}")
            return None

    def delete(self, key: str) -> bool:
        """Delete a value from cache."""
        try:
            key_bytes = key.encode() if isinstance(key, str) else key
            self.client.delete(key_bytes)
            print(f"  [DELETE] {key}")
            return True
        except Exception as e:
            print(f"  [DELETE ERROR] {key}: {e}")
            return False

    def clear(self):
        """Clear entire cache."""
        try:
            self.client.flush_all()
            print("  [FLUSH] Cache cleared")
        except Exception as e:
            print(f"  [FLUSH ERROR] {e}")

    def close(self):
        """Close connection."""
        if self.client:
            self.client.close()


def demo_basic_operations(cache: MemcachedCache):
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


def demo_cache_efficiency(cache: MemcachedCache):
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
    
    # Now demonstrate WITH cache
    print("\n--- Scenario 2: WITH Cache (Using Memcached) ---")
    print("Making 5 identical requests with caching:")
    
    cache.clear()
    cache.metrics = CacheMetrics()  # Reset metrics
    
    for i in range(5):
        print(f"\nRequest {i+1}:")
        cache.get("user:1")
    
    scenario2_time = cache.metrics.total_time
    print(f"\nTotal time with caching: {scenario2_time:.3f} seconds")
    
    efficiency_gain = ((scenario1_time - scenario2_time) / scenario1_time) * 100
    speedup = scenario1_time / scenario2_time if scenario2_time > 0 else 0
    
    print("\n" + "-"*60)
    print(f"Efficiency Improvement: {efficiency_gain:.1f}% faster")
    print(f"Speedup Factor:        {speedup:.1f}x")
    print(f"Network Calls Saved:   {scenario1_time - scenario2_time:.3f} seconds")
    print("-"*60)
    
    cache.metrics.print_report()


def demo_real_world_scenario(cache: MemcachedCache):
    """Demonstrate a real-world caching scenario."""
    print("\n" + "="*60)
    print("DEMO 3: REAL-WORLD SCENARIO - E-COMMERCE")
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


def main():
    """Main entry point."""
    print("\n" + "="*60)
    print("MEMCACHED DEMO: KEY-VALUE CACHING & EFFICIENCY")
    print("="*60)
    
    # Initialize cache
    cache = MemcachedCache()
    
    try:
        # Run demonstrations
        demo_basic_operations(cache)
        demo_cache_efficiency(cache)
        demo_real_world_scenario(cache)
        
        print("\n" + "="*60)
        print("KEY TAKEAWAYS")
        print("="*60)
        print("[+] Memcached stores frequently accessed data in memory")
        print("[+] Cache hits are orders of magnitude faster than DB/API calls")
        print("[+] Reduces network traffic and server load")
        print("[+] Improves application response times significantly")
        print("[+] Essential for scaling high-traffic applications")
        print("="*60 + "\n")
        
    finally:
        cache.close()
        print("Disconnected from Memcached")


if __name__ == "__main__":
    main()
