
import static org.junit.Assert.*;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.*;
import java.io.*;
import java.text.*;
import java.time.*;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * The test class PurchasingSystemTest.
 *
 * @author  (your name)
 * @version (a version number or a date)
 */
public class PurchasingSystemTest
{
    Connection c;
    /**
     * Default constructor for test class PurchasingSystemTest
     */
    public PurchasingSystemTest()
    {
    }

    /**
     * Sets up the test fixture.
     *
     * Called before every test case method.
     */
    @Before
    public void setUp() throws Exception
    {

        try 
        {
            Class.forName("org.sqlite.JDBC");
            c = DriverManager.getConnection("jdbc:sqlite:PurchasingSystem.db");
        } 
        catch ( Exception e ) 
        {
            System.err.println( "ERROR : "+ e.getMessage() );
        }

        Solutions.c = c;

    }
    /**
     * Tears down the test fixture.
     *
     * Called after every test case method.
     */
    @After
    public void tearDown() throws Exception
    {
        try 
        {
            c.close();
        } 
        catch ( Exception e ) 
        {
            System.err.println( "ERROR : "+ e.getMessage() );
        }
    }

    /**
     * Test1 checks constructor of PurchasingSystem and method createCustomer. Every customer gets an id based on the length of its name
     * If that id does already exist in the system, the number is incremented until a unique one is found
     *
    @Test
    public void Task1()
    {
    PurchasingSystem purchasingSystem = new PurchasingSystem();        
    Customer customer0 = purchasingSystem.createCustomer("testCustom00", 10, true);
    assertEquals(12, customer0.getCustomerID());        
    Customer customer1 = purchasingSystem.createCustomer("testCust", 10, true);
    assertEquals(8, customer1.getCustomerID());        
    Customer customer2 = purchasingSystem.createCustomer("testCustom01", 10, true);
    assertEquals(13, customer2.getCustomerID());        
    Customer customer3 = purchasingSystem.createCustomer("testCustom02", 10, true);
    assertEquals(14, customer3.getCustomerID());
    }
     */    
    /**
     * Test 2 checks the constructor of Customer and Item, together with some getters and setters
     *
    @Test
    public void Task2()
    {
    int id = 5;
    String name = "TestName";
    int wallet = 20;
    boolean isStudent = true;
    Customer customer = new Customer(id, name, wallet, isStudent);        
    assertEquals(id, customer.getCustomerID());
    assertEquals(wallet, customer.getCustomerWallet());
    assertEquals(isStudent, customer.getStudentStatus());
    int newWallet0 = 40;
    customer.setCustomerWallet(newWallet0);
    assertEquals(newWallet0, customer.getCustomerWallet());        
    int newWallet1 = 30;
    customer.setCustomerWallet(newWallet1);
    assertEquals(newWallet1, customer.getCustomerWallet());
    boolean isStudent0 = false;
    customer.setStudentStatus(isStudent0);
    assertFalse(customer.getStudentStatus());        
    boolean isStudent1 = false;
    customer.setStudentStatus(isStudent1);
    assertFalse(customer.getStudentStatus());

    LocalDate expiryDate0 = LocalDate.of(2019, 2, 12);
    int itemId = 5;
    int type = 2;
    int price = 10;
    int studentPrice = 5;
    Item item = new Item(itemId, type, price, studentPrice, expiryDate0);
    assertEquals(itemId, item.getID());
    assertEquals(type, item.getType());
    assertTrue(expiryDate0.equals(item.getExpiry()));
    assertEquals(price, item.getPrice());
    assertEquals(studentPrice, item.getStudentPrice());
    }
     */    
    /**
     * Test 3 checks the constructor of a Purchase and the calculation of the total price of a purchase
     * The price depends on the "status" of the customer
     *
    @Test
    public void Task3()
    {
    Customer student = new Customer(0, "Student", 10, true);
    Customer staff = new Customer(1, "Staff", 10, false);
    ArrayList<Item> noItems = new ArrayList<>();
    Purchase purchase1 = new Purchase(0, staff, noItems);
    int actualPurchasePrice = purchase1.getPurchasePrice();
    assertEquals(0, actualPurchasePrice);
    Item drinkItem = new Item(0, 1, 2, 1, LocalDate.of(2019, 2, 10));
    Item candyItem = new Item(2, 3, 4, 1, LocalDate.of(2019, 12, 10));
    ArrayList<Item> noDealItems = new ArrayList<>();        
    noDealItems.add(drinkItem);
    noDealItems.add(candyItem);
    Purchase purchase2 = new Purchase(0, staff, noDealItems);
    actualPurchasePrice = purchase2.getPurchasePrice();
    assertEquals(6, actualPurchasePrice);
    Purchase purchase3 = new Purchase(0, student, noDealItems);
    actualPurchasePrice = purchase3.getPurchasePrice();
    assertEquals(2, actualPurchasePrice);
    }
     */    
    /**
     * Test 4 checks the method checkAffordability of a purchase
     *
    @Test
    public void Task4()
    {
    Customer customer = new Customer(0, "0", 10, false);
    Item drinkItem = new Item(0, 1, 2, 1, LocalDate.of(2019, 2, 10));
    Item candyItem = new Item(2, 3, 4, 1, LocalDate.of(2019, 12, 10));
    ArrayList<Item> noDealItems = new ArrayList<>();        
    noDealItems.add(drinkItem);
    noDealItems.add(candyItem);
    Purchase purchase = new Purchase(0, customer, noDealItems);
    boolean isAffordable = purchase.checkAffordability();
    assertTrue(isAffordable);
    customer.setCustomerWallet(6);
    isAffordable = purchase.checkAffordability();
    assertTrue(isAffordable);
    customer.setCustomerWallet(4);
    isAffordable = purchase.checkAffordability();
    assertFalse(isAffordable);
    }
     */    
    /**
     * Test 5 checks the method makeNewPurchase of PurchasingSystem, you pass a customer and an item list
     * The purchase will only be created and added to the system when the purchase is affordable.
     * If the purchase is created the wallet of the customer is decreased with the price of the purchase
     *
    @Test
    public void Task5()
    {
    PurchasingSystem purchasingSystem = new PurchasingSystem();
    assertEquals(0, purchasingSystem.getPurchases().size());
    Customer richCustomer = new Customer(0, "0", 20, false);
    Item drinkItem = new Item(0, 1, 2, 1, LocalDate.of(2019, 2, 10));
    Item sandwhichItem = new Item(1, 2, 3, 2, LocalDate.of(2019, 2, 10));
    Item candyItem = new Item(2, 3, 4, 1, LocalDate.of(2019, 12, 10));
    Item drinkItem2 = new Item(3, 1, 3, 3, LocalDate.of(2020, 2, 10));
    ArrayList<Item> allItems = new ArrayList<>();
    allItems.add(drinkItem);
    allItems.add(sandwhichItem);
    allItems.add(candyItem);
    allItems.add(drinkItem2);
    Purchase purchase0 = purchasingSystem.makeNewPurchase(richCustomer, allItems);
    Item cheapItem = new Item(0, 1, 1, 1, LocalDate.of(2019, 2, 1));
    ArrayList<Item> cheapItems = new ArrayList<Item>();
    cheapItems.add(cheapItem);
    Purchase purchase1 = purchasingSystem.makeNewPurchase(richCustomer, cheapItems);
    Purchase purchase2 = purchasingSystem.makeNewPurchase(richCustomer, cheapItems);        
    assertEquals(3, purchasingSystem.getPurchases().size());
    assertEquals(0, purchase0.getID());
    assertEquals(1, purchase1.getID());
    assertEquals(2, purchase2.getID());
    Customer poorCustomer = new Customer(0, "0", 5, false);
    Purchase purchase3 = purchasingSystem.makeNewPurchase(poorCustomer, allItems);
    assertNull(purchase3);
    assertEquals(3, purchasingSystem.getPurchases().size());
    Purchase purchase = purchasingSystem.makeNewPurchase(poorCustomer, cheapItems);
    assertEquals(4, poorCustomer.getCustomerWallet());
    assertEquals(1, purchase.getPurchasePrice());
    assertTrue(purchase.isItemInPurchase(cheapItems.get(0)));
    }
     */    
    /**
     * Test 6 checks the method checkMealDeal (students' prices apply if you buy together a drink and a sandwich)
     * and the correct calculation of the purchase price
     *
    @Test
    public void Task6()
    {
    Customer staff = new Customer(1, "Staff", 10, false);
    ArrayList<Item> noItems = new ArrayList<>();
    Purchase purchase1 = new Purchase(0, staff, noItems);
    boolean isMealDeal = purchase1.checkMealDeal();
    assertFalse(isMealDeal);
    Item drinkItem = new Item(0, 1, 2, 1, LocalDate.of(2019, 2, 10));
    Item candyItem = new Item(2, 3, 4, 1, LocalDate.of(2019, 12, 10));
    ArrayList<Item> noDealItems = new ArrayList<>();        
    noDealItems.add(drinkItem);
    noDealItems.add(candyItem);
    Purchase purchase2 = new Purchase(0, staff, noDealItems);
    isMealDeal = purchase2.checkMealDeal();
    assertFalse(isMealDeal);
    int actualPurchasePrice = purchase2.getPurchasePrice();
    assertEquals(6, actualPurchasePrice);
    Item sandwhichItem = new Item(1, 2, 3, 2, LocalDate.of(2019, 1, 25));
    ArrayList<Item> mealDealItems = new ArrayList<>();        
    mealDealItems.add(drinkItem);
    mealDealItems.add(sandwhichItem);
    Purchase purchase3 = new Purchase(0, staff, mealDealItems);
    isMealDeal = purchase3.checkMealDeal();
    assertTrue(isMealDeal);
    actualPurchasePrice = purchase3.getPurchasePrice();
    assertEquals(3, actualPurchasePrice);
    }
     */        
    /**
     * Test 7 checks if you can construct an Item when all information is stored in a text file
     *
    @Test
    public void Task7() throws Exception
    {
    LocalDate actualExpiryDate = LocalDate.of(2010, 3, 20);        
    String filename = "item.txt";
    Item item = new Item(filename);
    assertEquals(3, item.getID());
    assertEquals(2, item.getType());
    assertEquals(14, item.getPrice());
    assertEquals(8, item.getStudentPrice());
    assertTrue(actualExpiryDate.equals(item.getExpiry()));
    }
     */    
    /**
     * Test 8 checks the method studentMadeCheapestPurchase, if there is more than one cheapest purchase you should
     * check them all to see if one of them is done by a student
     *
    @Test
    public void Task8()
    {
    PurchasingSystem purchasingSystem = new PurchasingSystem();
    assertFalse(purchasingSystem.studentMadeCheapestPurchase());
    Customer richStaff = new Customer(0, "0", 100, false);
    Customer richStudent = new Customer(0, "0", 100, true);
    Item drinkItem = new Item(0, 1, 2, 1, LocalDate.of(2019, 2, 10));
    Item sandwhichItem = new Item(1, 2, 3, 2, LocalDate.of(2019, 2, 10));
    Item candyItem = new Item(2, 3, 4, 1, LocalDate.of(2019, 12, 10));
    Item drinkItem2 = new Item(3, 1, 3, 3, LocalDate.of(2020, 2, 10));
    ArrayList<Item> allItems = new ArrayList<>();
    allItems.add(drinkItem);
    allItems.add(sandwhichItem);
    allItems.add(candyItem);
    allItems.add(drinkItem2);
    purchasingSystem.makeNewPurchase(richStudent, allItems);
    Item cheapItem = new Item(0, 1, 1, 1, LocalDate.of(2019, 2, 1));
    ArrayList<Item> cheapItems = new ArrayList<Item>();
    cheapItems.add(cheapItem);
    purchasingSystem.makeNewPurchase(richStaff, cheapItems);
    Item expensiveItem = new Item(1, 1, 10, 10, LocalDate.of(2019, 2, 1));
    ArrayList<Item> expensiveItems = new ArrayList<Item>();
    expensiveItems.add(expensiveItem);
    purchasingSystem.makeNewPurchase(richStudent, expensiveItems);        
    assertFalse(purchasingSystem.studentMadeCheapestPurchase());
    purchasingSystem.makeNewPurchase(richStudent, cheapItems);
    assertTrue(purchasingSystem.studentMadeCheapestPurchase());
    }
     */        
    /**
     * Test 9 checks if you can control if a certain item appears in a purchase. 
     * You need to test only on the ID of the Item
     *
    @Test
    public void Task9()
    {
    Item drinkItem2 = new Item(3, 1, 3, 3, LocalDate.of(2020, 2, 10));
    ArrayList<Item> noItems = new ArrayList<>();
    Customer staff = new Customer(1, "Staff", 10, false);
    Purchase purchase1 = new Purchase(0, staff, noItems);
    boolean containsItem = purchase1.isItemInPurchase(drinkItem2);
    assertFalse(containsItem);
    Item drinkItem = new Item(0, 1, 2, 1, LocalDate.of(2019, 2, 10));
    Item candyItem = new Item(2, 3, 4, 1, LocalDate.of(2019, 12, 10));
    ArrayList<Item> noDealItems = new ArrayList<>();        
    noDealItems.add(drinkItem);
    noDealItems.add(candyItem);
    Purchase purchase2 = new Purchase(0, staff, noDealItems);
    containsItem = purchase2.isItemInPurchase(drinkItem2);
    assertFalse(containsItem);
    containsItem = purchase2.isItemInPurchase(candyItem);
    assertTrue(containsItem);
    }
     */
    /**
     * Test 10 checks the method removeExpiredItems, it should return a list with all items of a purchase of which the experiration date is reached
     * If the expiration date is equal to the "current date" used in the test, the item is also removed
     *    
    @Test
    public void Task10()
    {
    LocalDate currentDate = LocalDate.of(2019, Month.FEBRUARY, 20);

    Item item1 = new Item(0, 1, 0, 0, LocalDate.of(2019, 2, 10));
    boolean isExpired = item1.isExpired(currentDate);
    assertTrue(isExpired);
    Item item2 = new Item(0, 1, 0, 0, LocalDate.of(2019, 2, 21));
    isExpired = item2.isExpired(currentDate);
    assertFalse(isExpired);
    Item item3 = new Item(0, 1, 0, 0, LocalDate.of(2019, 2, 20));
    isExpired = item3.isExpired(currentDate);
    assertFalse(isExpired);
    Customer staff = new Customer(1, "Staff", 10, false);
    ArrayList<Item> noItems = new ArrayList<>();
    Purchase purchase1 = new Purchase(0, staff, noItems);
    ArrayList<Item> expiredItems = purchase1.removeExpiredItems(currentDate);
    assertEquals(0, expiredItems.size());
    Item drinkItem = new Item(0, 1, 2, 1, LocalDate.of(2019, 2, 10));
    Item sandwhichItem = new Item(1, 2, 3, 2, LocalDate.of(2019, 2, 10));
    Item candyItem = new Item(2, 3, 4, 1, LocalDate.of(2019, 12, 10));
    Item drinkItem2 = new Item(3, 1, 3, 3, LocalDate.of(2020, 2, 20));
    ArrayList<Item> allItems = new ArrayList<>();
    allItems.add(drinkItem);
    allItems.add(sandwhichItem);
    allItems.add(candyItem);
    allItems.add(drinkItem2);
    Purchase purchase2 = new Purchase(0, staff, allItems);
    currentDate = LocalDate.of(2019, 1, 20); 
    expiredItems = purchase2.removeExpiredItems(currentDate);
    assertEquals(0, expiredItems.size());
    currentDate = LocalDate.of(2019, 2, 11); 
    expiredItems = purchase2.removeExpiredItems(currentDate);
    assertEquals(2, expiredItems.size());
    assertEquals(2, purchase2.getItems().size());
    }
     */

    /**
     * Query: Give all information of items which were never purchased
     * You may try directly using SQLiteStudio but afterwards
     * implement this query in the method Query1() of Queries
     **

    @Test
    public void Task11()
    {
        try
        {
            Queries q1 = new Queries(c);
            assertTrue(Solutions.checkResultSets(q1.query1(), Solutions.Query1()));
        }
        catch (SQLException sqle)
        {
            System.err.println( "ERROR : "+ sqle.getMessage() );
            fail("An exception occurred during the execution of your query, check the error message in the terminal");
        }
    }
*/
    /**
     * Query: Give a sorted list of all unique item types which are purchased by customer with customerID=6
     * You may try directly using SQLiteStudio but afterwards
     * implement this query in the method Query2() of Queries
     **
    @Test
    public void Task12()
    {
        try
        {
            Queries q1 = new Queries(c);
            assertTrue(Solutions.checkResultSets(q1.query2(), Solutions.Query2()));
        }
        catch (SQLException sqle)
        {
            System.err.println( "ERROR : "+ sqle.getMessage() );
            fail("An exception occurred during the execution of your query, check the error message in the terminal");
        }
    }
*/
    /**
     * Query: Give all information of items which are only purchased by students
     * You may try directly using SQLiteStudio but afterwards
     * implement this query in the method Query3() of Queries
     **
    @Test
    public void Task13()
    {
        try
        {
            Queries q1 = new Queries(c);
            assertTrue(Solutions.checkResultSets(q1.query3(), Solutions.Query3()));
        }
        catch (SQLException sqle)
        {
            System.err.println( "ERROR : "+ sqle.getMessage() );
            fail("An exception occurred during the execution of your query, check the error message in the terminal");
        }
    }
*/
}
