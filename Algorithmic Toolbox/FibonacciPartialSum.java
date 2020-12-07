import java.util.*;

public class FibonacciPartialSum {
    private static long getFibonacciPartialSumNaive(long from, long to) {
        if (to <= 1)
            return to;

	   long prev = 0;
        long cur = 1;
        long sum;

        if(from <= 1) {
            sum = 1;
        }
        else {
            sum = 0;
        }

        for (long i = 2; i <= to; i++) {
            long temp_prev = prev;
            prev = cur;
            cur = (cur + temp_prev) % 10;

            if (i >= from) {
                sum = (sum + cur) % 10;
            }

        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long from = scanner.nextLong();
        long to = scanner.nextLong();
        //long from = 1234;
        //long to = 12345;
        System.out.println(getFibonacciPartialSumNaive(from, to));
        scanner.close();
    }
}