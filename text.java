package christmas;

public class text {
    
    public void ChainingExample2() {

        
        String taintedVariable = Console.readLine();

        // Basic method chaining
        A a = new A();
        a.b().c().d(taintedVariable);

        // Intermediate variables for method chaining
        B b = a.b();
        C c = b.c();
        c.d(taintedVariable);

        // Using qualifiers in method arguments
        D d = new D();
        d.process(c, taintedVariable, b.e(), a.f().g());

        // Complex method chaining with qualifiers
        a.h().i(b.j().k(c.l()).m(taintedVariable).n());

        // A slightly different complex chain
        E e = new E();
        e.o().p(a.q().r(b.s(c.t().u(taintedVariable))));
        
    }

    class A {
        public B b() {
            System.out.println("Method b() in class A");
            return new B();
        }

        public B f() {
            System.out.println("Method f() in class A");
            return new B();
        }

        public C h() {
            System.out.println("Method h() in class A");
            return new C();
        }

        public C q() {
            System.out.println("Method q() in class A");
            return new C();
        }
    }

    class B {
        public C c() {
            System.out.println("Method c() in class B");
            return new C();
        }

        public String e() {
            System.out.println("Method e() in class B");
            return "result from e()";
        }

        public C j() {
            System.out.println("Method j() in class B");
            return new C();
        }

        public C s(C c) {
            System.out.println("Method s() in class B");
            return c;
        }
    }

    class C {
        public void d(String input) {
            System.out.println("Method d() in class C with input: " + input);
        }

        public B g() {
            System.out.println("Method g() in class C");
            return new B();
        }

        public B i(B b) {
            System.out.println("Method i() in class C");
            return b;
        }

        public B k(C c) {
            System.out.println("Method k() in class C");
            return new B();
        }

        public B l() {
            System.out.println("Method l() in class C");
            return new B();
        }

        public B m(String input) {
            System.out.println("Method m() in class C with input: " + input);
            return new B();
        }

        public C n() {
            System.out.println("Method n() in class C");
            return this;
        }

        public C t() {
            System.out.println("Method t() in class C");
            return this;
        }

        public C u(String input) {
            System.out.println("Method u() in class C with input: " + input);
            return this;
        }
    }

    class D {
        public void process(C c, String data1, String data2, String data3) {
            System.out.println("Processing in class D with C instance and data: " + data1 + ", " + data2 + ", " + data3);
            c.d(data1);
        }
    }

    class E {
        public C o() {
            System.out.println("Method o() in class E");
            return new C();
        }

        public C p(C c) {
            System.out.println("Method p() in class E");
            return c;
        }
    }
    class Console {
        public static String readLine() {
            // Simulate reading a line from console input
            return "taintedInput";
        }
    }

}
