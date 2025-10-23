class BankersAlgorithm:
    def __init__(self, allocation, max_resources, available_resources):
        self.alloc = allocation
        self.max = max_resources
        self.avail = available_resources
        self.n_proc = len(allocation)
        self.n_res = len(available_resources)

    def is_safe_state(self):
        work = self.avail.copy()
        finish = [False] * self.n_proc
        safe_seq = []
        # Calculate the Need matrix (Need = Max - Allocation)
        need = [[self.max[i][j] - self.alloc[i][j] for j in range(self.n_res)] for i in range(self.n_proc)]

        for _ in range(self.n_proc):
            for p in range(self.n_proc):
                # Check if process p is not finished and its needs can be met
                if not finish[p] and all(need[p][i] <= work[i] for i in range(self.n_res)):
                    # Release resources
                    work = [work[i] + self.alloc[p][i] for i in range(self.n_res)]
                    finish[p] = True
                    safe_seq.append(p)
                    break
        
        if all(finish):
            print("Safe Sequence:", safe_seq); return True
        print("Unsafe State"); return False

allocation_matrix = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
max_matrix = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [9, 3, 3]]
available_resources_vector = [3, 3, 2]
banker = BankersAlgorithm(allocation_matrix, max_matrix, available_resources_vector)
banker.is_safe_state()
