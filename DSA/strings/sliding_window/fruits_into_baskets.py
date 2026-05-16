class Solution:
    def totalFruit(self, fruits: list[int]) -> int:

        """
        PROBLEM: max fruits you can pick with only 2 baskets(2 fruit types)

        PATTERN: sliding window + hashmap

        THE PLAN:
        1.track fruit type in current window with a hashmap {fruit_type:count}
        2.expand:add fruits[right] to the window
        3.shrink:while more than 2 fruit tpes:
            .remove fruits[left] from hashmap
            .if count becomes 0 delete from hashmap
            .move left forward
        4.update max_fruits after each valid window

        TIME:O(n) SPACE O(1) - max 3 fruit types in map

        KEY INSIGHT: "2 baskets" = max 2 distinct fruit types in window. use hashmap to 
            track counts

        """
        left = 0
        fruit_count = {}
        max_fruits = 0

        for right in range(len(fruits)):
            #add current fruit
            fruit_count[fruits[right]]=fruit_count.get(fruits[right],0) + 1

            #shrink while more than 2 types
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -=1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left +=1
            
            # update max
            max_fruits = max(max_fruits,right-left+1)
        return max_fruits