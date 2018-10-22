import java.util.Scanner;

public class day_18{

    static public Scanner obj = new Scanner(System.in);
    public static void main(String[] args) {
        
        System.out.println("\nEnter string:");
        String str = obj.nextLine();
        
        String result[] = str.split(" ");

        for (int i = 0; i < result.length; i++) {
            if(i%2 == 0)
                result[i] = new StringBuffer(result[i]).reverse().toString();

            System.out.print(result[i] + " ");
        }
        
    } 
}