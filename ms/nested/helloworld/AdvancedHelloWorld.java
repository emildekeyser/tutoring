/*
 * Stap 1: ondersteun drie talen
 * output: Hello world
 * 	   Bonjour tout le monde
 * 	   Hola Mundo
 *
 * Stap 2: Zorg dat er makkelijk nog talen bijgevoegd kunnen worden
 *
 * Stap 3: voeg een taal bij met een anonieme classe
 * output: Hello sam
 * 	   Bonjour sam
 * 	   Hola sam
 * 	   Hallo sam
 */

public class AdvancedHelloWorld {
  
    // interface HelloWorld {
    //     public void greet();
    //     public void greetSomeone(String someone);
    // }

    public void sayHello() {
	    this.sayHello("world");
    }
    public void sayHello(String someone) {
	    System.out.println("Hello " + someone);
    }
}
