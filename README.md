# Leetcode-515-Medium-Binary-Tree
A daily Leetcode, you can use breadth first search, queues, or lists to find the maximum element in each level of the tree (see the question if you don't understand. So my way is to have two lists, one for the current level, and one for the next level. After finishing the current level, the next level list will be the current and the children will be in the next level list.

I have also seen deque method, which is like the two entry queue, where you keep track of the length of the current level and do the popleft() for a controled times. 

One intersting bug during my coding is that pop() will start at the end of an array, which means sometimes it will go directly to the null child. When I was checking whether the first element of the tree, sometimes it is the null child that got poped first. I fixed it by checking the whole array to be not None.
