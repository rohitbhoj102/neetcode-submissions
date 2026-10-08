class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rotations = 0
        while students and rotations < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                rotations = 0
            else:
                students.append(students.pop(0))
                rotations += 1

        return len(students)
      ## for the first student in the queue, check the top of the sandwich stack --> if they want to eat it (1 == 1 or 0 == 0), dequeue the student, and pop the sandwich from the stack

      ## if they dont want to eat it (!= 1 or 0) --> dequeue the student and enqueue to move to end of queue
        