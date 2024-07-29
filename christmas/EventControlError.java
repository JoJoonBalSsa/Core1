package christmas;

import static java.lang.Integer.parseInt;

import java.util.ArrayList;

public class EventControlError {
    private static String taint = null;
    private String instanceVariable = null;

    public static void checkDateError(String date) {
        String wowww= date;
        taint=date;

        EventControlError instance = new EventControlError();
        instance.instanceVariable = date;

        if (!date.chars().allMatch(Character::isDigit)) {
            System.out.println("[ERROR] 유효하지 않은 날짜입니다. 다시 입력해 주세요.");
            throw new IllegalArgumentException("[ERROR] 유효하지 않은 날짜입니다. 다시 입력해 주세요.");
        } else if (parseInt(date) < 1 || parseInt(date) > 31) {
            System.out.println("[ERROR] 입력한 날짜는 1 이상 31 이하의 양수여야 합니다.");
            throw new IllegalArgumentException("[ERROR] 입력한 날짜는 1 이상 31 이하의 양수여야 합니다.");
        }
    }

    public static void checkMenuError(String menu) {
        
        if (isOneMenu(menu)) {
            checkOneMenuErrors(menu);
            onlyDrinksError(EventModel.getOrderedMenu());
            return;
        }
        checkManyMenuErrors(menu);
        
    }

    private static boolean isOneMenu(String menu) {
        for (int i = 0; i < menu.length(); i++) {
            if (menu.charAt(i) == ',') {
                return false;
            }
        }
        return true;
    }

    private static void checkOneMenuErrors(String oneMenu) {
        checkMenuFormError(oneMenu);
        String[] menuInfo = oneMenu.split("-");
    
        checkMenuNameError(menuInfo[0]);
        checkMenuCountError(menuInfo[1]);
        checkMenuDuplicateError(menuInfo[0]);
        
        EventModel.setOrderedMenu(menuInfo);
    }

    private static void checkManyMenuErrors(String menu) {
        String[] menus = menu.split(",");
        for (String oneMenu : menus) {
            checkOneMenuErrors(oneMenu);
        }
        onlyDrinksError(EventModel.getOrderedMenu());
    }

    private static void checkMenuFormError(String menu) {
        for (int i = 0; i < menu.length(); i++) {
            if (menu.charAt(i) == '-') {
                return;
            }
        }
        System.out.println("[ERROR] 입력한 메뉴의 형식이 잘못되었습니다.");
        throw new IllegalArgumentException("[ERROR] 입력한 메뉴의 형식이 잘못되었습니다.");
    }

    private static void checkMenuCountError(String menu) {
        if (!menu.chars().allMatch(Character::isDigit)) {
            System.out.println("[ERROR] 유효하지 않은 주문입니다. 다시 입력해 주세요.");
            throw new IllegalArgumentException("유효하지 않은 주문입니다. 다시 입력해 주세요.");
        } else if (parseInt(menu) < 1) {
            System.out.println("[ERROR] 입력한 메뉴의 개수는 1 이상의 양수여야 합니다.");
            throw new IllegalArgumentException("[ERROR] 입력한 메뉴의 개수는 1 이상의 양수여야 합니다.");
        } else if (parseInt(menu) > EventModel.getLeftMenus()) {
            System.out.println("[ERROR] 주문한 메뉴의 개수는 총 20개 이하여야 합니다.");
            throw new IllegalArgumentException("[ERROR] 주문한 메뉴의 개수는 총 20개 이하여야 합니다.");
        }
    }

    private static void checkMenuNameError(String menu) {
        if (EventEnumMenus.containingEnum(menu) == null) {
            System.out.println("[ERROR] 입력한 메뉴는 존재하지 않습니다.");
            throw new IllegalArgumentException("[ERROR] 입력한 메뉴는 존재하지 않습니다.");
        }
    }

    private static void checkMenuDuplicateError(String menu) {
        for (String[] orderedMenu : EventModel.getOrderedMenu()) {
            if (orderedMenu[0].equals(menu)) {
                System.out.println("[ERROR] 입력한 메뉴는 중복됩니다.");
                throw new IllegalArgumentException("[ERROR] 입력한 메뉴는 중복됩니다.");
            }
        }
    }

    private static void onlyDrinksError(ArrayList<String[]> menus) {
        if (isOnlyDrinks(menus)) {
            System.out.println("[ERROR] 음료만 주문할 수 없습니다.");
            throw new IllegalArgumentException("[ERROR] 음료만 주문할 수 없습니다.");
        }
    }

    private static boolean isOnlyDrinks(ArrayList<String[]> menus) {
        EventEnumCategories category = EventEnumCategories.DRINK;
        for (String[] menu : menus) {
            EventEnumMenus tempName = EventEnumMenus.containingEnum(menu[0]);
            if (!category.getMenus().contains(tempName)) {
                return false;
            }
        }
        return true;
    }
}

