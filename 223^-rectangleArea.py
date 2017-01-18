'''
223. Rectangle Area
Total Accepted: 29019 Total Submissions: 100387 Difficulty: Easy

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
Rectangle Area

Assume that the total area is never beyond the maximum possible value of int.


'''
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int

        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        sumArea=(C-A)*(D-B)+(G-E)*(H-F)
        if (E>A and E> C) or (A>E and A>G) or (B>F and B>H) or (F>B and F>D):
            return sumArea

        hOverlap=max(0,min(C,G)-max(A,E))
        vOverlap=max(0,min(D,H)-max(B,F))
        return sumArea-hOverlap*vOverlap

# one line version:        return (C-A)*(D-B)+(G-E)*(H-F)-max(0,min(C,G)-max(A,E))*max(0,min(D,H)-max(B,F))


        