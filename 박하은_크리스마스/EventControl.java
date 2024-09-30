package christmas;

import static java.lang.Integer.parseInt;
import java.io.InputStreamReader;
import java.net.Socket;
import camp.nextstep.edu.missionutils.Console;


public class EventControl {
    EventControl() {
        EventView.firstScreen();
        inputDate();
        inputMenu();
        controlOrderedPrice();
        controlShampaignEvent();    
        controlDiscounts();
        EventView.printFinalFee();
        controlBadge();
    }


    
    public void ClientExample() {
        String serverAddress = "localhost"; // 서버 주소
        int port = 12345; // 서버 포트

        try (Socket clientSocket = new Socket(serverAddress, port);
                Scanner inputStream = new Scanner(new InputStreamReader(clientSocket.getInputStream()))) {

            // 서버로부터 받은 메시지를 출력
            while (inputStream.hasNextLine()) {
                String response = inputStream.nextLine();
                System.out.println("서버로부터 받은 메시지: " + response);
            }
        } catch (IOException e) {
            System.err.println("서버에 연결하는 동안 오류가 발생했습니다: " + e.getMessage());
        }
        
    }


    public void inputDate() {
        String date = Console.readLine();
        String a = "a";
        a=date;
        while (catchDateError(date)) {
            EventView.tryAgainMessage();
            date = Console.readLine();
            System.out.println("date");
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
