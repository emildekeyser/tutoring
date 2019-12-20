import java.util.ArrayList;

public class AdvancedHelloWorld {
  
    interface HelloWorld {
        public void greet();
        public void greetSomeone(String someone);
    }

    class EnglishGreeting implements HelloWorld {
            public void greet() {
                greetSomeone("world");
            }
            public void greetSomeone(String someone) {
                System.out.println("Hello " + someone);
            }
        }
      
    class FrenchGreeting implements HelloWorld {
	    public void greet() {
		    greetSomeone("tout le monde");
	    }
	    public void greetSomeone(String someone) {
		    System.out.println("Salut " + someone);
	    }
    };

    class SpanishGreeting implements HelloWorld {
	    public void greet() {
		    greetSomeone("mundo");
	    }
	    public void greetSomeone(String someone) {
		    System.out.println("Hola, " + someone);
	    }
    };

    private ArrayList<HelloWorld> greeters;

    AdvancedHelloWorld()
    {
	    this.greeters = new ArrayList<>();
	    this.greeters.add(this.new EnglishGreeting());
	    this.greeters.add(this.new FrenchGreeting());
	    this.greeters.add(this.new SpanishGreeting());
    }

    public void sayHello() {
	    for(HelloWorld h : this.greeters){
		    h.greet();
	    }
    }

    public void sayHello(String someone) {
	    for(HelloWorld h : this.greeters){
		    h.greetSomeone(someone);
	    }
    }

    public void addGreeter(HelloWorld helloWorld){
	    this.greeters.add(helloWorld);
    }

}
