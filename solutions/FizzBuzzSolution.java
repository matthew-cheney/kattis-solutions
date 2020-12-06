import java.util.Scanner;

public class FizzBuzzSolution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();
        int Y = sc.nextInt();
        int N = sc.nextInt();

        for (int i = 1; i <= N; i++) {
            StringBuilder out_string = new StringBuilder();
            if (i % X == 0) {
                out_string.append("Fizz");
            }
            if (i % Y == 0) {
                out_string.append("Buzz");
            }
            if (out_string.toString().equals("")) {
                out_string.append(i);
            }
            System.out.println(out_string.toString());
        }
    }
}
