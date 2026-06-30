```python
"""
Problem Number: 1700
Problem Title: Number of Students Unable to Eat Lunch
Summary: Given a queue of students with sandwich preferences (0 or 1) and a stack
         of sandwiches, students at the front of the queue take the top sandwich if
         it matches their preference, otherwise they go to the back of the queue.
         Return the number of students who are unable to eat.
Approach: Count the number of students who prefer each type of sandwich. Then iterate
          through the sandwiches stack — if no remaining student wants the current top
          sandwich, all remaining students are unable to eat. Otherwise, decrement the
          count for the matching preference and continue.
"""

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]
        for student in students:
            count[student] += 1

        for sandwich in sandwiches:
            if count[sandwich] == 0:
                return count[1 - sandwich]
            count[sandwich] -= 1

        return 0
```