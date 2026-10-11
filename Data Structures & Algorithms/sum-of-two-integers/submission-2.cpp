class Solution {
public:
    int getSum(int a, int b) {
        while (b != 0) {
            int carryover =(a & b) << 1;
            a = a ^ b;
            b = carryover;
        }
        return a;
    }
};
