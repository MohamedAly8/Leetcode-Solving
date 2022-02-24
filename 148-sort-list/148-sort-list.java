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
        
                // Base case : if head is null
        if (head == null || head.next == null) {
            return head;
        }
 
        // get the middle of the list
        ListNode middle = getMiddle(head);
        ListNode nextofmiddle = middle.next;
 
        // set the next of middle node to null
        middle.next = null;
 
        // Apply mergeSort on left list
        ListNode left = sortList(head);
 
        // Apply mergeSort on right list
        ListNode right = sortList(nextofmiddle);
 
        // Merge the left and right lists
        ListNode sortedlist = sortedMerge(left, right);
        return sortedlist;
        
    }
    
        ListNode sortedMerge(ListNode a, ListNode b){
        ListNode result = null;
        /* Base cases */
        if (a == null)
            return b;
        if (b == null)
            return a;
 
        /* Pick either a or b, and recur */
        if (a.val <= b.val) {
            result = a;
            result.next = sortedMerge(a.next, b);
        }
        else {
            result = b;
            result.next = sortedMerge(a, b.next);
        }
        return result;
    }
    
    
    public ListNode getMiddle(ListNode head){
        if (head == null)
            return head;
 
        ListNode slow = head, fast = head;
 
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
    
    

}