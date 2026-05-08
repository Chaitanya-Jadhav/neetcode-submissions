class CountSquares:
    """
    A data structure that stores points and counts the number of axis-aligned 
    squares that can be formed using a given query point.
    """
    def __init__(self):
        # Dictionary to store the frequency of each point for fast O(1) lookups.
        # We use a tuple (x, y) as the key because Python lists are unhashable.
        self.ptsCount = defaultdict(int)
        
        # List to store every point added. We will iterate over this list 
        # to find potential diagonal corners when counting squares.
        self.pts = []

    def add(self, point: List[int]) -> None:
        # Convert the point [x, y] to a tuple (x, y) and increment its frequency.
        self.ptsCount[tuple(point)] += 1
        
        # Append the point to our list of all historical points.
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point # The query point (Let's call this Corner A)
        
        # Iterate through all historical points. 
        # We treat each point (x, y) as the DIAGONAL opposite corner (Corner C).
        for x, y in self.pts:
            # Check if (x, y) can form a valid diagonal for an axis-aligned square:
            # 1. abs(py - y) != abs(px - x): Checks if height != width. If they aren't equal, it's a rectangle, not a square.
            # 2. x == px or y == py: Ensures the point isn't on the exact same horizontal or vertical axis as the query point (which would mean area = 0).
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue # Not a valid diagonal, skip to the next point.
            
            # If (x, y) IS a valid diagonal, the other two missing corners MUST be:
            # Corner B: (x, py)
            # Corner D: (px, y)
            # We multiply the frequencies of Corner B and Corner D. 
            # If either doesn't exist, its count is 0, so 0 is added to the result.
            # If there are multiple overlapping points at those corners, multiplying them gives all possible combinations.
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
            
        return res