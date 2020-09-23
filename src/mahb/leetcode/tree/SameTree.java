package mahb.leetcode.tree;

public class SameTree {
    //Definition for a binary tree node.
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    /**
     * 我得分析是：
     * 首先可以使用前序遍历将树遍历，然后判断节点是不是不相同。
     *
     * @param p
     * @param q
     * @return
     */
    public static boolean isSameTree(TreeNode p, TreeNode q) {
        //非线性 的 前序遍历为：

        System.out.println(p.val);
        System.out.println(q.val);
        if (p.val != q.val) return false;
        if (p.left != null && q.left != null) {
            return isSameTree(p.left, q.left);
        } else if (p.left == null && q.left == null) {
            if (p.val != q.val) {
                return false;
            }
        } else if ((q.left == null && p.left != null) || (p.left == null && q.left != null)) {
            return false;
        }

        if (p.right != null && q.right != null) {
            return isSameTree(p.right, q.right);
        } else if (p.right == null && q.right == null) {
            if (p.val != q.val) {
                return false;
            }
        } else if ((q.right == null && p.right != null) || (p.right == null && q.right != null)) {
            return false;
        }
        return true;
    }

    public static void main(String[] args) {
        int[] a = new int[]{1, 2, 1};
        int[] b = new int[]{1, 1, 2};

    };

}
