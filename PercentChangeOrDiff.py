class PercentChangeOrDiff:

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        
    def percent_change(self):
        ''' commonly used when there is an “old” and “new” number
            or an “initial” and “final” value. 
        '''
        diff = (((self.v2) - (self.v1))/(abs(self.v1)))* 100
        return diff

    def percent_diff(self):
        ''' 
            When the order of  the numbers does not matter
        ''' 

        numerator = abs(self.v1 - self.v2)
        denominator = ((self.v1+self.v2)/2)
        pct_diff = numerator * 100 / denominator
        return pct_diff
    
x1 = 20
x2 = 25
y1 = 25
y2 = 20

pc1 = PercentChangeOrDiff(x1, y1)
print(pc1.percent_change()) # 25.0
print(pc1.percent_diff()) # 25.0

pc2 = PercentChangeOrDiff(x2, y2)
print(pc2.percent_change()) # 25.0
print(pc2.percent_diff()) # 25.0