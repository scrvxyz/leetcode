/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    void add(TreeNode **nodes, int num, int depth) {
        TreeNode *tmp = new TreeNode;
        tmp->val = num;
        nodes[depth] = tmp;
        if (!depth)
            return;
        nodes[depth - 1]->left
            ? nodes[depth - 1]->right = tmp
            : nodes[depth - 1]->left = tmp;
    }
public:
    TreeNode* recoverFromPreorder(string traversal) {
        TreeNode *nodes[1000];
        int depth = 0;
        int num = 0;
        for (char c : traversal) {
            if (c == '-') {
                if (num) {
                    add(nodes, num, depth);
                    depth = 0;
                }
                num = 0;
                depth++;
                continue;
            }
            num = num*10 + (c - '0');
        }
        add(nodes, num, depth);
        return nodes[0];
    }
};
