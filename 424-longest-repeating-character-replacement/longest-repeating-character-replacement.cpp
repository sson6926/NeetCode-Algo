class Solution {
public:
    int characterReplacement(string s, int k) {
        int res = 0;
        vector<int> count(26);
        int max_count = 0;
        int l = 0;
        for(int r = 0; r < s.size(); r++) {
            count[s[r]-'A']++;
            max_count = max(max_count, count[s[r]-'A']);
            if(r-l+1 - max_count > k) {
                count[s[l]-'A']--;
                l++;
            }
            res = max(res, r-l+1);
        }
        return res;
    }
};
