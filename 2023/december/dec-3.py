"""
Minimum Time Visiting All Points 

On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

"""



class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        curr = points[0]
        next_point_idx = 1
        res = 0 

        while next_point_idx < len(points): 
            curr_x, curr_y = curr[0], curr[1]
            next_point = points[next_point_idx]
            next_x, next_y = next_point[0], next_point[1]
            res += max(abs(next_x - curr_x), abs(next_y - curr_y))
            curr = next_point
            next_point_idx += 1



        return res