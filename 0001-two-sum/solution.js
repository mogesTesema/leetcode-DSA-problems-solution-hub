/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 let index1;
 let index2;
var twoSum = function(nums, target) {
    for(let i=0;i<nums.length;i++){
        index1=i;
        for(let j=i+1;j<nums.length;j++){
            if(nums[i]+nums[j]===target){
                index2=j;
                return [index1,index2];
            }

        }
    }
    
};
