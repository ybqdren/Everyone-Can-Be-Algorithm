package com.github.ybqdren.month2;

/**
 * Created by Zhao Wen on 2021/2/4
 * 92 反转链表
 */

public class _92 {
    // 下一个结点存放
    ListNode nextNode = null;

    public ListNode reverseN(ListNode head, int n){
        // 反转区间为 1~1
        if(n == 1){
            // 建立被反转结点与其后结点的联结
            nextNode = head.next;
            return head;
        }

        // 反转区间为1~n 递归调用函数继续反转
        ListNode last = reverseN(head.next,n-1);

        head.next.next = head;

        // 让反转之后的head节点与后面的节点建立连接
        head.next = nextNode;

        return last;
    }

    public ListNode reverseBetween(ListNode head, int m, int n) {
        // 从1开始，反转区间为1~n
        if(m == 1){
            return reverseN(head,n);
        }

        // 非1开始，反转区间为m~n
        head.next = reverseBetween(head.next,m-1,n-1);
        return head;
    }
}

// 树
class ListNode{
    int val;
    ListNode next;

    ListNode(){}

    ListNode(int val){
        this.val = val;
    }

    ListNode(int val,ListNode next){
        this.val = val;
        this.next = next;
    }
}
