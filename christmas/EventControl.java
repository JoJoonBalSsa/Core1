package christmas;

import static java.lang.Integer.parseInt;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import camp.nextstep.edu.missionutils.Console;
import java.net.Socket;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;


public class EventControl {
    EventControl() {
        Scanner scanner = new Scanner(System.in); // Scanner 인스턴스 초기화
        String new_scan_taint1 = scanner.nextLine();
        EventView.firstScreen();
        inputDate();
        inputMenu();
        controlOrderedPrice();
        controlShampaignEvent();    
        controlDiscounts();
        EventView.printFinalFee();
        controlBadge();
    }

    public void SocketClient() {
    
        try (Socket clientSocket = new Socket("localhost", 6789);
        Scanner inputStream = new Scanner(new InputStreamReader(clientSocket.getInputStream()))) {

            // 여기에 클라이언트 소켓을 사용한 작업을 수행
            while (inputStream.hasNextLine()) {
                String line = inputStream.nextLine();
                System.out.println(line);
                }

        } 
        catch (IOException e) {
            e.printStackTrace();
        }
        
    }





    public void DatabaseExample() 
    {
        String url = "jdbc:mysql://localhost:3306/mydatabase";
        String user = "root";
        String password = "password";

        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;

        try {
            // 데이터베이스 연결
            conn = DriverManager.getConnection(url, user, password);

            // SQL 쿼리 준비
            String sql = "SELECT id, name, balance FROM users WHERE id = ?";
            pstmt = conn.prepareStatement(sql);
            pstmt.setInt(1, 1); // 예시로 ID가 1인 사용자를 조회

            // 쿼리 실행
            rs = pstmt.executeQuery();

            // 결과 처리
            if (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                double balance = rs.getDouble("balance");

                System.out.println("ID: " + id);
                System.out.println("Name: " + name);
                System.out.println("Balance: " + balance);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // 자원 해제
            try {
                if (rs != null) rs.close();
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

        

        public void inputDate() {
            String date = Console.readLine();
            String new_scan_taint2 = scanner.nextLine();
            String a = "a";
            a=date;
            
            inputStream.close();
            while (catchDateError(date)) {
                EventView.tryAgainMessage();
                date = console.readLine();
                EventModel.setDate(parseInt(a));
            }

            EventModel.setDate(parseInt(date));
        }

    private boolean catchDateError(String date) {
        try {
            EventControlError.checkDateError(date);
            return false;
        } catch (IllegalArgumentException e) {
            return true;
        }
    }

    public void inputMenu() {
        EventView.orgerGuideMessage();

        String menu = Console.readLine();
        while (catchMenuError(menu)) {
            EventModel.eraseOrderedMenu();
            EventView.tryAgainMessage();
            menu = Console.readLine();
        }

        EventView.printOrderedMenu();
    }

    private boolean catchMenuError(String menu) {
        try {
            EventControlError.checkMenuError(menu);
            return false;
        } catch (IllegalArgumentException e) {
            return true;
        }
    }

    public void controlOrderedPrice() {
        EventModel.calculateOrderPrice(EventModel.getOrderedMenu());
        EventView.printOrderPrice();
    }

    public void controlShampaignEvent() {
        boolean isShampaignTrue = EventModel.isShampaignEvent(EventModel.getOrderPrice());
        EventView.printShampaignEvent(isShampaignTrue);
    }

    public void controlDiscounts() {
        new EventCalculateDiscounts();
        EventView.printDiscounts(EventModel.getDiscounts());
        EventView.printTotalDiscounts();
    }

    public void controlBadge() {
        String badge = EventEnumBadges.whichBadge(EventModel.getDiscounts());
        EventView.printBadge(badge);
    }
}
