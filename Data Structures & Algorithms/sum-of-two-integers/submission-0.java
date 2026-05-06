public class Solution {
    public int getSum(int a, int b) {
        // Keep looping until there is no carry left
        while (b != 0) {
            // Carry is calculated by bitwise AND and then left-shifted by 1
            // because a carry affects the next higher bit
            int carry = (a & b) << 1;

            // Sum without carrying is done using bitwise XOR
            a ^= b;

            // Assign carry to b so that it will be added in the next iteration
            b = carry;
        }

        // When carry becomes zero, a contains the result
        return a;
    }
}
