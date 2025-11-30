from collections import deque

class Solution:
    def countStudents(self, students, sandwiches):
        students_queue = deque(students)
        sandwich_stack = sandwiches[::-1]

        while sandwich_stack:
            curr_sandwich = sandwich_stack.pop()
            curr_len = len(students_queue)
            ate = False

            for _ in range(curr_len):
                student = students_queue.popleft()
                if student == curr_sandwich:
                    ate = True
                    break
                students_queue.append(student)

            print(len(students_queue), students_queue)

            if not ate:
                # Nobody wants the current sandwich → stop
                break

        return len(students_queue)

