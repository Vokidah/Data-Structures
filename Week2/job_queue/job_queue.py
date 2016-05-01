# python3

import random
class JobQueue:

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)
        #self.num_workers, self.jobs = a, b

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        if self.num_workers < len(self.jobs):
            next_free_time = []
            for i in range(self.num_workers):
                self.assigned_workers[i] = i
                self.start_times[i] = 0
                next_free_time.append((self.jobs[i], i))
            self.build_heap(next_free_time)
            time = next_free_time[0][0]
            for count in range(self.num_workers, len(self.jobs)):
                #print(next_free_time)
                self.assigned_workers[count] = self.extract_min(next_free_time)
                self.start_times[count] = time
                self.insert(next_free_time, (time + self.jobs[count], self.assigned_workers[count]))
                time = next_free_time[0][0]
        else:
            for i in range(0, len(self.jobs)):
                self.assigned_workers[i] = i
                self.start_times[i] = 0

    def compare(self, a, b):
        if a[0] < b[0]:
            return True
        elif a[0] == b[0] and a[1] < b[1]:
            return True
        return False

    def build_heap(self, next_free_time):
        j = int(len(next_free_time) / 2)
        while j >= 0:
            self.sift_down(j, next_free_time)
            j -= 1

    def extract_min(self, next_free_time):
        next_free_time[0], next_free_time[-1] = next_free_time[-1], next_free_time[0]
        data = next_free_time.pop(-1)
        self.sift_down(0, next_free_time)
        return data[1]

    def insert(self, next_free_time, element):
        next_free_time.append(element)
        self.sift_up(len(next_free_time) - 1, next_free_time)

    def sift_up(self, i, next_free_time):
        while i > 0 and self.compare(next_free_time[i], next_free_time[int((i-1)/2)]):
            next_free_time[i], next_free_time[int((i - 1)/2)] = next_free_time[int((i-1)/2)], next_free_time[i]
            i = int((i - 1)/2)

    def sift_down(self, i, next_free_time):
        min_index = i
        if 2*i + 1 < len(next_free_time) and self.compare(next_free_time[2 * i + 1], next_free_time[min_index]):
            min_index = 2*i + 1
        if 2*i + 2 < len(next_free_time) and self.compare(next_free_time[2 * i + 2], next_free_time[min_index]):
            min_index = 2*i + 2
        if min_index != i:
            next_free_time[i], next_free_time[min_index] = next_free_time[min_index], next_free_time[i]
            self.sift_down(min_index, next_free_time)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

