public class Main{
    public static void main(String... args) {
	    AdvancedHelloWorld hw = new AdvancedHelloWorld();
	    hw.sayHello();

	    hw.addGreeter(new AdvancedHelloWorld.HelloWorld(){
		    public void greet() {
			    greetSomeone("werled");
		    }
		    public void greetSomeone(String someone) {
			    System.out.println("Hallo, " + someone);
		    }
	    });
	    hw.sayHello("Sam");
    }
}
