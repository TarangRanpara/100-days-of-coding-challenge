import java.util.Scanner;

public class day_17{
    
    static Scanner obj = new Scanner(System.in);
    public static void main(String[] args) {
        
        //user input
        System.out.println("Enter string:");
        String str = obj.nextLine();

        //dividing the string by space
        String arr[] = str.split(" ");

        for(int i=0; i<arr.length; i++){
            
                if(arr[i].length()>2 && arr[i].charAt(2) == 'a'){
                    //extracting first char & rest of the string
                    System.out.print(arr[i].substring(0,1).toUpperCase() + arr[i].substring(1) + " ");
                }
                else
                    System.out.print(arr[i] + " ");
        }

    }
}