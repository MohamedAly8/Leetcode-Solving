/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode mid = getMiddle(head);
        ListNode nextMiddle = mid.next;
        
        mid.next = null;
        
        ListNode left = sortList(head);
        ListNode right = sortList(nextMiddle);
        
        ListNode sortedList = merge(left,right);
        
        return sortedList;
     
    }
    
    public ListNode merge(ListNode left, ListNode right){
        
        ListNode merged = null;
            
        if(left == null){
            return right;
        }
        if(right == null){
            return left;
        }
        
        if(right.val <= left.val){
            merged = right;
            merged.next = merge(left, right.next);
        }
        
        if(right.val > left.val){
            merged = left;
            merged.next = merge(left.next, right);
        }
        
        return merged;
    }
    
    
    public ListNode getMiddle(ListNode node){
        ListNode slow = node;
        ListNode fast = node;
        
        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}
    
    