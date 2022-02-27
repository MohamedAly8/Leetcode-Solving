import java.util.Arrays;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
        int max1 = m-1;
        int max2 = n-1;
        int endpointer = n+m-1;
        
        while(max1 >= 0 && max2 >= 0){
            if (nums1[max1] >= nums2[max2]){
                nums1[endpointer] = nums1[max1];
                max1--;
                endpointer--;
            }
            else{
                nums1[endpointer] = nums2[max2];
                max2--;
                endpointer--;
            }
        }
        while(max2 >= 0){
            nums1[endpointer] = nums2[max2];
            max2--;
            endpointer--;
        }
}
}