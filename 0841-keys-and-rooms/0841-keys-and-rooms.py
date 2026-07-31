# u - return true or false based on if i can visit all the rooms given a set of keys
# p - visited array to keep track of nodes visited, create a queue that pops for every room visited, have a count variable that keeps track of how many rooms visited, if the rooms visisted = len(rooms) then return true


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        q = deque([0])

        while q:
            room = q.popleft()

            if room in visited:
                continue
            visited.add(room)

            for key in rooms[room]:
                q.append(key)

        return len(visited) == n
