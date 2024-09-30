import java.util.Scanner;

public class SimpleTaintExample {

    public static void main(String[] args) {
        MyClass myObject = new MyClass();

        // 사용자로부터 입력을 받아 tainted 변수에 설정
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter tainted data: ");
        String userInput = scanner.nextLine(); // source로부터 입력

        // tainted 값을 설정
        myObject.setValue(userInput);

        // 다른 메서드에서 tainted 값을 사용
        myObject.printValue();
        myObject.useValueInAnotherMethod();

        // 또 다른 메서드에서 tainted 값 출력
        myObject.anotherPrint();

        scanner.close();
    }
}

class TaintTest {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input27 = scanner.nextLine();  // source function
        process(input27);
    }

    public static void process(String data) {
        String sanitizedData = sanitize(data);  // Sanitize the input
        logData(testData(formatData(sanitizedData)));     // Nested method call
    }

    public static String sanitize(String data) {
        return data.trim();  // Example of data sanitization
    }

    public static String testData(String data123) {
        return "Formatted: " + data123;  // Formatting data (this could modify the tainted data)
    }


    public static String formatData(String data) {
        return "Formatted: " + data;  // Formatting data (this could modify the tainted data)
    }

    public static void logData(String formattedData) {
        System.out.println(formattedData);  // Sink function where data ends up
    }
}


class MyClass {
    // 인스턴스 변수
    String tvalue;

    // 생성자에서 사용자 입력 받기
    MyClass() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("값을 입력하세요: ");
        this.tvalue = scanner.nextLine();
    }

    public void setValue(String input)
    {
        setTest(input);
    }

    public void printValue() {
        setTest(tvalue);
        System.out.println(tvalue);
    }

    public void setTest(String input2){
        System.out.println(input2);
    }

    public static void main(String[] args) {
        MyClass myClass = new MyClass();
        myClass.printValue();
    }
}