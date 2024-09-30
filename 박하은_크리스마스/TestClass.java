import org.apache.catalina.startup.Tomcat;
import org.eclipse.jetty.server.Server;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.HashMap;
import java.util.Map;

public class TestClass {

    // 직접 선언한 클래스
    private static class CustomClass {
        public int customFunction(int a, int b) {
            return a + b;
        }
    }

    // 테스트 메소드
    @Test


    private Map<String, Object> context = new HashMap<>();

    public void put(String name, Object value) {
        context.put(name, value);
        
        
    }




    public void testFunctionOrigins() {
        // 직접 선언한 객체 생성 및 함수 사용
        CustomClass customObj = new CustomClass();
        int result1 = customObj.customFunction(5, 3);

        // Tomcat 라이브러리 함수 사용
        Tomcat tomcat = new Tomcat();
        tomcat.setPort(8080);

        // Jetty 라이브러리 함수 사용
        Server server = new Server(8081);

        // 자바 내장 함수 사용 (java.lang.Math의 max 메소드)
        int result3 = Math.max(10, 20);

        // 검증
        assertEquals(8, result1, "직접 선언한 객체의 함수 테스트");
        assertEquals(8080, tomcat.getConnector().getPort(), "Tomcat 라이브러리 함수 테스트");
        assertEquals(8081, server.getURI().getPort(), "Jetty 라이브러리 함수 테스트");
        assertEquals(20, result3, "자바 내장 함수 테스트");
    }
}