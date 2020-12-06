import java.util.Scanner;
import java.util.Vector;

public class Backspace {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        Vector<Character> line_out = new Vector<Character>();
        int skip = 0;
        for (int i = line.length() - 1; i >= 0; i--) {
            if (line.charAt(i) == '<') {
                skip += 1;
            } else if (skip > 0) {
                skip -= 1;
            } else {
                line_out.add(line.charAt(i));
            }
        }

        StringBuilder out_string = new StringBuilder();
        for (int i = line_out.size() - 1; i >= 0; i--) {
            out_string.append(line_out.elementAt(i));
        }
        System.out.println(out_string);
    }

}
