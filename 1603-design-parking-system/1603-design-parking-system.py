class ParkingSystem:

    



    def __init__(self, big: int, medium: int, small: int):
        #intialize a parking space with an arr
        #one big, one medium, one small
        self.parking = {
            1 : big,
            2 : medium,
            3 : small,
        }
        #create a hashmap to keep track
    def addCar(self, carType: int) -> bool:
        i = 0
        print(self.parking)

        if carType in self.parking and self.parking[carType] != 0:
            self.parking[carType] -= 1
            return True
        return False
            
        #1 check the cartype
            # if cartype = '1', then know its big
            #....
        #2. is there any spots avaiable for the cartype, check the value of the key
        #if there is, return true, -= 1
        #return false if its zero


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)