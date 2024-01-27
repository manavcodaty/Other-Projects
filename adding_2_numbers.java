package Java_projects;
import java.util.Scanner;
public class adding_2_numbers {
    public static void main(String[] args) {
        int num1 = 0;
        int num2 = 0;
        Scanner myObj = new Scanner(System.in);
        System.out.println("Enter first number: ");
        num1 = myObj.nextInt();
        System.out.println("Enter second number: ");
        num2 = myObj.nextInt();
        System.out.println("Sum of " + num1 + " and " + num2 + " is " + (num1 + num2));
        myObj.close();

        

    }
}
