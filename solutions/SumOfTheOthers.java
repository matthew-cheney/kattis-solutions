import java.util.Scanner;
import java.util.Vector;

public class SumOfTheOthers {
    public static void main(String args[]) {
        Scanner sc=new Scanner(System.in);
        while(sc.hasNextLine()){
            String line = sc.nextLine();

            if (line.strip() == "") {
                continue;
            }

            Vector<Integer> line_ints = new Vector<Integer>();

            for (String s : line.split(" ")) {
                line_ints.add(Integer.parseInt(s));
            }

            int sum = 0;
            for (Integer i : line_ints) {
                sum += i;
            }

            for (Integer i : line_ints) {
                if (sum - i == i) {
                    System.out.println(i);
                    break;
                }
            }
        }
    }

}