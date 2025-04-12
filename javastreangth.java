import java.util.Scanner;

public class PasswordStrengthChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your password: ");
        String password = scanner.nextLine();

        if (isStrongPassword(password)) {
            System.out.println("✅ Strong Password.....");
        } else {
            System.out.println("❌ Weak Password. Try including uppercase, lowercase, number, special character, and at least 8 characters......");
        }

        scanner.close();
    }

    public static boolean isStrongPassword(String password) {
        return password.length() >= 8 &&
               password.matches(".*[A-Z].*") &&
               password.matches(".*[a-z].*") &&
               password.matches(".*\\d.*") &&
               password.matches(".*[@#$%^&+=!].*");
    }
}
