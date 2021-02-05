package com.github.ybqdren.month2;

/**
 * Created by Zhao Wen on 2021/2/6
 */

public class _25 {
    public ListNode reverse(ListNode a,ListNode b){
        ListNode pre = null;
        ListNode cur = a;
        ListNode next = b;

        while(cur != b){
            next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;
        }

        return pre;
    }

    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode a = head;
        ListNode b = head;

        if(head == null){
            return null;
        }

        for(int i = 0;i < k;i++){
            if(b == null){
                return head;
            }
            b = b.next;
        }

        ListNode newHead = reverse(a,b);
        a.next = reverseKGroup(b,k);
        return newHead;
    }
}
