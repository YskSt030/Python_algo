class Sort:
    def __init__(self):
        self.time_culc = 0
    
    def reset_time_culc(self):
        self.time_culc = 0

    def bubble_sort(self, input_array_ ):
        if len(input_array_) > 0:
            if len(input_array_) == 1:
                self.time_culc += 1
                return input_array_[0]
            while True:
                swap_count = 0
                for i in range(len(input_array_)-1, 0, -1):
                    if input_array_[i-1] > input_array_[i]:
                        input_array_[i-1], input_array_[i] =  \
                        input_array_[i], input_array_[i-1]
                        swap_count += 1
                    self.time_culc += 1
                if swap_count == 0:
                    break
            self.bubble_sort(input_array_[:-1])
        return input_array_


    def quick_sort(self, input_array_):
        pass

    def selection_sort(self, input_array_):
        pass

    def heap_sort(self, input_array_):
        pass

    def merge_sort(self, input_array_):
        pass

if __name__=='__main__':
    sort = Sort()
    array = [10,3,4,2,5,6,7,9,8,11,17,16,14,13,15]
    ret = sort.bubble_sort(array)
    print(sort.time_culc)