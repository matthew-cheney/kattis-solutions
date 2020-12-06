import java.util.Scanner;

public class faktor {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int I = sc.nextInt();

        int answer = 1 + (A * (I - 1));

        System.out.println(answer);
    }

}