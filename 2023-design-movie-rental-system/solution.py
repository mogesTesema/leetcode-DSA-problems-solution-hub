class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movie_catalog = collections.defaultdict(list)
        self.prices = {}
        for shop, movie, price in entries:
            self.movie_catalog[movie].append((price, shop))
            self.prices[(shop, movie)] = price
        for movie_id in self.movie_catalog:
            self.movie_catalog[movie_id].sort()
        self.rented_heap = []
        self.dropped_counts = collections.Counter()
        self.rented_set = set()

    def search(self, movie: int) -> List[int]:
        candidates = self.movie_catalog.get(movie, [])
        result = []
        for price, shop in candidates:
            if (shop, movie) not in self.rented_set:
                result.append(shop)
            if len(result) == 5:
                break
        return result

    def rent(self, shop: int, movie: int) -> None:
        self.rented_set.add((shop, movie))
        price = self.prices.get((shop, movie))
        heapq.heappush(self.rented_heap, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented_set.remove((shop, movie))
        price = self.prices.get((shop, movie))
        self.dropped_counts[(price, shop, movie)] += 1

    def report(self) -> List[List[int]]:
        result = []
        temp_popped = []
        while self.rented_heap and len(result) < 5:
            cheapest = heapq.heappop(self.rented_heap)
            if self.dropped_counts[cheapest] > 0:
                self.dropped_counts[cheapest] -= 1
                continue
            result.append([cheapest[1], cheapest[2]])
            temp_popped.append(cheapest)
        for item in temp_popped:
            heapq.heappush(self.rented_heap, item)
            
        return result

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
