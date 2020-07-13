

class SortAlgo(object):
    def __init__(self, lst):
        self.origin = lst  
    
    def _Merge(self):
        def _merge(m, n):
            if m == n:
                return [self.origin[m]]
                
            else:
                res = []
                tmp1 = _merge(m, int((n+m)/2))
                tmp2 = _merge(int((n+m)/2)+1, n)
                ele1 = 0
                ele2 = 0
                while ele1 < len(tmp1) or ele2 < len(tmp2):
                    if ele1 >= len(tmp1):
                        res.extend(tmp2[ele2:])
                        break
                    if ele2 >= len(tmp2):
                        res.extend(tmp1[ele1:])
                        break
                    if tmp1[ele1] < tmp2[ele2]:
                        res.append(tmp1[ele1])
                        ele1 += 1
                    else:
                        res.append(tmp2[ele2])
                        ele2 += 1
                return res
        return _merge(0, len(self.origin) - 1)

    def _Bubble(self):
        tmp = []
        tmp.extend(self.origin)
        for ele1 in range(len(tmp)):
            for ele2 in range(ele1, len(tmp)):
                if tmp[ele1] > tmp[ele2]:
                    temp = tmp[ele1]
                    tmp[ele1] = tmp[ele2]
                    tmp[ele2] = temp
        return tmp

    def _Heap(self):
        tmp = []
        tmp.extend(self.origin)

        def heap_apf(lst, n):
            if n > len(lst):
                return
            child_left = 2*n + 1
            child_right = 2*n + 2
            aim = child_left
            if child_right >= len(lst):
                if child_left >= len(lst):
                    return
            else:
                if lst[child_left] < lst[child_right]:
                    aim = child_right
            if lst[aim] > lst[n]:
                temp = lst[aim]
                lst[aim] = lst[n]
                lst[n] = temp
            heap_apf(lst, aim)
        
        node = int((len(tmp)-1)/2)
        heap_apf(tmp, node)
        while node > 0:
            node = int((node-1)/2)
            heap_apf(tmp, node)

        for ele in range(len(tmp)):
            temp = tmp[0]
            tmp[0] = tmp[-ele-1]
            tmp[-ele-1] = temp
            tmp_ll = tmp[:-ele-1]
            heap_apf(tmp_ll, 0)
            tmp[:-ele-1] = tmp_ll
            
        return tmp

    def _Quick(self):
        tmp = []
        tmp.extend(self.origin)

        def quick(lst, left, right):
            benchmark = lst[left]
            i = left
            j = right
            while i != j:
                while i < j and lst[j] >= benchmark:
                    j -= 1
                while i < j and lst[i] <= benchmark:
                    i += 1
                if i < j:
                    temp = lst[i]
                    lst[i] = lst[j]
                    lst[j] = temp
            
            temp = lst[left]
            lst[left] = lst[i]
            lst[i] = temp
            if left != i:
                quick(lst, left, i-1)
            if right != j:
                quick(lst, i+1, right)

        quick(tmp, 0, len(tmp)-1)
        return tmp

    def _Select(self):
        pass

    def _Counting(self):
        tmp = []
        tmp.extend(self.origin)
        min_tmp = tmp[0]
        max_tmp = tmp[0]
        for ele in range(len(tmp)):
            if tmp[ele] < min_tmp:
                min_tmp = tmp[ele]
            if tmp[ele] > max_tmp:
                max_tmp = tmp[ele]
        dic = {}
        for ele in range(min_tmp, max_tmp+1):
            dic[ele] = 0
        for ele in tmp:
            dic[ele] += 1
        res = []
        for ele in dic:
            temp = dic[ele]
            while temp != 0:
                res.append(ele)
                temp -= 1
        return res

    @classmethod
    def Merge(cls, lst):
        return(SortAlgo(lst)._Merge())
    
    @classmethod
    def Bubble(cls, lst):
        return(SortAlgo(lst)._Bubble())

    @classmethod
    def Heap(cls, lst):
        return(SortAlgo(lst)._Heap())
    
    @classmethod
    def Quick(cls, lst):
        return(SortAlgo(lst)._Quick())

    @classmethod
    def Counting(cls, lst):
        return(SortAlgo(lst)._Counting())



print(SortAlgo.Counting([13,15,7,28,11,2,4,6]))
# print(sorted([4,5,2,3,1,9,8,10,3,4,6,8,9,1]))