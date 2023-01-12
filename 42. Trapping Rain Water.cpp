class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;
        int n = height.size();
        int ltr[20000];
        int rtl[20000];
        int maximum = 0;
        for (int i = 0; i < n; i++) {
            maximum = max(maximum, height[i]);
            ltr[i] = maximum;
        }
        maximum = 0;
        for (int i = n - 1; i > -1; i--) {
            maximum = max(maximum, height[i]);
            rtl[i] = maximum;
        }
        for (int i = 0; i < n; i++)
            ans += min(ltr[i], rtl[i]) - height[i];
        return ans;
    }
};
