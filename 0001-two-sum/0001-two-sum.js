/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 /*

    var difference = ??
    subtract target from number
    return difference location, i if they add up to target

    for (let i = 0; i < nums.length, i++){
        var difference = None

    }
 
 */
var twoSum = function(nums, target) {
    
    for (let i = 0; i < nums.length; i++){
        for (let j = i + 1; j < nums.length; j++){
            if (nums[i] + nums[j] === target){
                return [i, j]
            }
        }
    }
};