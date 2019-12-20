import static org.junit.Assert.*;

import java.sql.Connection;
import java.sql.DriverManager;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.sql.*;

public class PretparkTest
{
    Connection c = null;

    @Before
    public void setUp() throws Exception
    {
        try 
        {
            Class.forName("org.sqlite.JDBC");
            c = DriverManager.getConnection("jdbc:sqlite:LeisureParks.db");
        } 
        catch ( Exception e ) 
        {
            System.err.println( "ERROR : "+ e.getMessage() );
        }
        Solutions.c = c;
    }

    @After
    public void tearDown() throws Exception
    {
        c.close();
    }

    /**
     * check constructor and setters/getters from Attraction
     *
    @Test
    public void test1()
    {
    Attraction cobra = new Attraction("Cobra", LocalTime.of(9, 0), LocalTime.of(12, 30), 45);
    assertEquals(45, cobra.getDuration());
    assertEquals(LocalTime.of(9, 0), cobra.getStartTime());
    assertEquals(LocalTime.of(12, 30), cobra.getEndTime());
    }
     */
    /**
     * check generation of timeslots, starts from startTime, then always plus duration
     * stops when start is after endTime, returning null
     *
    @Test
    public void test2()
    {
    Attraction cobra = new Attraction("Cobra", LocalTime.of(9, 0), LocalTime.of(12, 30), 45);
    assertEquals(LocalTime.of(9, 0), cobra.getNextTimeSlot());
    assertEquals(LocalTime.of(9, 45), cobra.getNextTimeSlot());
    assertEquals(LocalTime.of(10, 30), cobra.getNextTimeSlot());
    assertEquals(LocalTime.of(11, 15), cobra.getNextTimeSlot());
    assertEquals(LocalTime.of(12, 0), cobra.getNextTimeSlot());
    assertNull(cobra.getNextTimeSlot());
    }
     */  
    /**
     * check constructor of LeisurePark + adding of Attractions
     * check if you can find an attraction by name 
     *
    @Test
    public void test3()
    {
    LeisurePark walibi = new LeisurePark("Walibi");
    assertEquals(0, walibi.getNumberOfAttractions());
    Attraction cobra = new Attraction("Cobra", LocalTime.of(9, 0), LocalTime.of(12, 30), 45);
    walibi.addAttraction(cobra);
    assertEquals(1, walibi.getNumberOfAttractions());
    Attraction pulsar = new Attraction("Pulsar", LocalTime.of(10, 0), LocalTime.of(12, 0), 30);
    walibi.addAttraction(pulsar);
    assertEquals(2, walibi.getNumberOfAttractions());
    assertNotNull(walibi.searchByName("Pulsar"));
    }
     */  
    /**
     * check basic functionality of Visitor: constructor, setters/getters and adding Attraction name to wishlist
     *
    @Test
    public void test4()
    {
    Visitor v1 = new Visitor("Donald Duck");
    assertEquals(-1, v1.getId());
    assertEquals(0, v1.getWishListCount());
    assertTrue(v1.addAttraction("Cobra"));
    assertEquals(1, v1.getWishListCount());
    }
     */
    /**
     * a Visitor can add maximum 5 Attraction names to wishlist
     *
    @Test
    public void test5()
    {
    Visitor v1 = new Visitor("Donald Duck");
    assertEquals(0, v1.getWishListCount());
    assertTrue(v1.addAttraction("Cobra"));
    assertEquals(1, v1.getWishListCount());
    assertTrue(v1.addAttraction("Cobre"));
    assertEquals(2, v1.getWishListCount());
    assertTrue(v1.addAttraction("Cobri"));
    assertEquals(3, v1.getWishListCount());
    assertTrue(v1.addAttraction("Cobro"));
    assertEquals(4, v1.getWishListCount());
    assertTrue(v1.addAttraction("Cobru"));
    assertEquals(5, v1.getWishListCount());
    assertFalse(v1.addAttraction("Pulsar"));
    assertEquals(5, v1.getWishListCount());
    }
     */  
    /**
     * before a Visitor can make his reservations, he has to register to the LeisurePark
     * as result of this registration he will receive a LeisurePark Id (simply the how maniest visitor he is)
     * a Visitor can not register multiple times (Visitors are considered equal when they have same name
     * and same id)
     *
    @Test
    public void test6()
    {
    Visitor v1 = new Visitor("Donald Duck");
    LeisurePark walibi = new LeisurePark("Walibi");
    assertTrue(walibi.registerVisitor(v1));
    assertEquals(1, v1.getId());
    Visitor v2 = new Visitor("Popeye");
    assertTrue(walibi.registerVisitor(v2));
    assertEquals(2, v2.getId());
    Visitor v3 = new Visitor("Popeye");
    assertTrue(walibi.registerVisitor(v3));
    assertEquals(3, v3.getId());
    assertFalse(walibi.registerVisitor(v2));
    assertEquals(2, v2.getId());
    }
     */  
    /**
     * check if it is possible to remove all visitors in a certain range id id's (both min and max included)
     *
    @Test
    public void test7()
    {
    LeisurePark walibi = new LeisurePark("Walibi");
    for (int index = 0; index < 100; index++)
    {
    Random rand = new Random();
    byte[] randomBytes = new byte[8];
    rand.nextBytes(randomBytes);
    Visitor v = new Visitor(new String(randomBytes));
    walibi.registerVisitor(v);
    }
    int nrOfVisitors = walibi.getNumberOfRegisteredVisitors();
    int deleted = walibi.removeVisitors(20, 29);
    assertEquals(nrOfVisitors-deleted, walibi.getNumberOfRegisteredVisitors());
    assertEquals(0, walibi.removeVisitors(20, 29));
    assertEquals(nrOfVisitors-deleted, walibi.getNumberOfRegisteredVisitors());
    }
     */  
    /**
     * load attractions from DB
     *
    @Test
    public void test8()
    {
    LeisurePark walibi = new LeisurePark("Walibi");
    assertEquals(Solutions.CountQuery(), walibi.loadAttractionsFromDB("LeisureParks.db"));
    assertEquals(Solutions.CountQuery(), walibi.getNumberOfAttractions());
    }
     */  
    /**
     * Query: how many attractions are open between 13:00 and 14:00 (both moments included)
     * You may try directly using SQLiteStudio but afterwards
     * implement this query in the method Query1() of Queries
     *
    @Test
    public void test9()
    {
        try
        {
            Queries q1 = new Queries(c);
            assertTrue(Solutions.checkResultSets(q1.query1(), Solutions.Query1()));
        }
        catch (SQLException sqle)
        {
            System.err.println( "ERROR : "+ sqle.getMessage() );
            assertTrue(false);
        }
    }
*/     
    /**
     * Query: show the name of all the available attractions together wiht the name of the park
     * You may try directly using SQLiteStudio but afterwards
     * implement this query in the method Query2() of Queries
     *
    @Test
    public void test10()
    {
        try
        {
            Queries q1 = new Queries(c);
            assertTrue(Solutions.checkResultSets(q1.query2(), Solutions.Query2()));
        }
        catch (SQLException sqle)
        {
            System.err.println( "ERROR : "+ sqle.getMessage() );
            assertTrue(false);
        }
    }
*/
    /**
     * Query: show the name of the attraction and the number of reservations ordered by
     * popularity (most reservations first) Show only those with at least 3 reservations
     * You may try directly using SQLiteStudio but afterwards
     * implement this query in the method Query3() of Queries
     *
    @Test
    public void test11()
    {
        try
        {
            Queries q1 = new Queries(c);
            assertTrue(Solutions.checkResultSets(q1.query3(), Solutions.Query3()));
        }
        catch (SQLException sqle)
        {
            System.err.println( "ERROR : "+ sqle.getMessage() );
            assertTrue(false);
        }
    }
*/
    /**
     * checks if you can process the wish-list of a visitor. The method checkReservations() 
     * tries to find a possible timeslot for the wanted attraction. 
     * If found it adds an entry in the Reservations collection of the visitor.
     *
    @Test
    public void test12()
    {
    LeisurePark walibi = new LeisurePark("Walibi");
    Attraction cobra = new Attraction("Cobra", LocalTime.of(9, 0), LocalTime.of(12, 30), 45);
    walibi.addAttraction(cobra);
    Attraction pulsar = new Attraction("Pulsar", LocalTime.of(10, 0), LocalTime.of(12, 0), 30);
    walibi.addAttraction(pulsar);
    Attraction octopus = new Attraction("Octopus", LocalTime.of(12, 0), LocalTime.of(17, 0), 25);
    walibi.addAttraction(octopus);
    Visitor v1 = new Visitor("Donald Duck");
    assertTrue(v1.addAttraction("Cobra"));
    assertTrue(v1.addAttraction("Pulsar"));
    assertTrue(v1.addAttraction("Octopus"));
    assertTrue(v1.addAttraction("Non Existing"));
    walibi.registerVisitor(v1);
    assertEquals(3, walibi.checkReservations(v1));
    HashMap<Attraction, LocalTime> result = v1.getReservation();
    assertEquals(3, result.size());
    assertEquals(LocalTime.of(10, 0), (LocalTime)result.get(pulsar));
    }
     */ 
    /**
     * Give all attractions which are occupied at a certain moment of time
     * returns an ArrayList of Attraction
     *
    @Test
    public void test13()
    {
    LeisurePark walibi = new LeisurePark("Walibi");
    Attraction cobra = new Attraction("Cobra", LocalTime.of(9, 0), LocalTime.of(12, 30), 46);
    walibi.addAttraction(cobra);
    Attraction pulsar = new Attraction("Pulsar", LocalTime.of(10, 0), LocalTime.of(12, 0), 30);
    walibi.addAttraction(pulsar);
    Attraction octopus = new Attraction("Octopus", LocalTime.of(12, 0), LocalTime.of(17, 0), 25);
    walibi.addAttraction(octopus);
    Visitor v1 = new Visitor("Donald Duck");
    assertTrue(v1.addAttraction("Cobra"));
    assertTrue(v1.addAttraction("Pulsar"));
    assertTrue(v1.addAttraction("Octopus"));
    walibi.registerVisitor(v1);
    Visitor v2 = new Visitor("Popeye");
    assertTrue(v2.addAttraction("Cobra"));
    assertTrue(v2.addAttraction("Pulsar"));
    walibi.registerVisitor(v2);
    assertEquals(3, walibi.checkReservations(v1));
    assertEquals(2, walibi.checkReservations(v2));
    ArrayList<Attraction> result = walibi.occupiedOn(LocalTime.of(10, 15));
    assertEquals(2, result.size());
    assertTrue(pulsar == result.get(0) || cobra == result.get(0));
    assertTrue(pulsar == result.get(1) || cobra == result.get(1));
    }
     */ 
}
