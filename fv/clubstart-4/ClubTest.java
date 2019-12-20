
import static org.junit.Assert.*;
import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.StringReader;
import java.util.ArrayList;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import java.sql.*;

public class ClubTest {
	Connection c = null;

	@Before
	public void setUp() throws Exception {
		try 
		{
			Class.forName("org.sqlite.JDBC");
			c = DriverManager.getConnection("jdbc:sqlite:clubs.db");
		} 
		catch ( Exception e ) 
		{
			System.err.println( "ERROR : "+ e.getMessage() );
		}
		Solutions.c = c;
	}

    @After
    public void tearDown() throws Exception {
    }

    /**
     * check constructor of Club, number of members should be 0
     *
    @Test
    public void test1() 
    {
        Club team = new Club("The red Devils", 300.0f);
        assertEquals(0, team.getNrOfMembers());
    }
*/
    /**
     * check constructor of Member and getters
     *
    @Test
    public void test2() 
    {
        Member captain = new Member("Vincent", "Kompany", "vince@kompany.com", 2, 2004);
        assertEquals(2004, captain.getYear());
        assertEquals("Kompany", captain.getLastName());
    }
*/
    /**
     * add Members to Club
     *
    @Test
    public void test3() 
    {
        Club team = new Club("The red Devils", 300.0f);
        Member captain = new Member("Vincent", "Kompany", "vince@kompany.com", 2, 2004);
        team.addMember(captain);
        Member keeper = new Member("Thibaut", "Courtois", "numberone@reddevils.be", 11, 2011);
        team.addMember(keeper);
        assertEquals(2, team.getNrOfMembers());
        Member alias = new Member("Vincent", "Kompany", "alias@kompany.com", 12, 2015);
        team.addMember(alias);
        assertEquals(2, team.getNrOfMembers());
    }
*/
    /**
     * populate club with info stored on sqlite db format
     * use clubs.db
     *
    @Test
    public void test4()
    {
        Club team = new Club("The red Devils", 300.0f);
        assertEquals(0, team.getNrOfMembers());
        team.populateFromDB("clubs.db");
        assertEquals(6, team.getNrOfMembers());
    }
*/
    /**
     * check showOverview
     *
    @Test
    public void test5() 
    {
        Club team = new Club("The red Devils", 300.0f);
        team.populateFromDB("clubs.db");
        team.showOverview();
        PrintStream defaultSO = System.out;  
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        System.setOut(new PrintStream(baos));
        try
        {
            team.showOverview();
            BufferedReader br = new BufferedReader(new StringReader(baos.toString()));
            String result = br.readLine();
            //use startsWith() because later on we will add info about month name and contribution
            assertTrue(result.startsWith("Overview of all members of club The red Devils"));
            result = br.readLine();
            assertTrue(result.startsWith("Member: firstName=Dries, lastName=Mertens, eMail=dries@napoli.it, joined the club in"));
        } 
        catch(Exception e)
        {
            System.setOut(defaultSO);
            System.out.println("Error while redirection System.out");
        }
        System.setOut(defaultSO);
    }
*/
    /**
     * check joined in year
     *
    @Test
    public void test6() 
    {
        Club team = new Club("The red Devils", 300.0f);
        team.populateFromDB("clubs.db");
        assertEquals(2, team.joinedInYear(2011));
        assertEquals(2, team.joinedInYear(2004));
        assertEquals(0, team.joinedInYear(2012));
    }
*/
    /**
     * check if there is a member with given last name
     *
    @Test
    public void test7() 
    {
        Club team = new Club("The red Devils", 300.0f);
        team.populateFromDB("clubs.db");
        assertEquals(true, team.isMember("Courtois"));
        assertEquals(false, team.isMember("Borre"));
        assertEquals(false, team.isMember(""));
    }
*/
    /**
     * remove members who started in a given year
     *
    @Test
    public void test8() 
    {
        Club team = new Club("The red Devils", 300.0f);
        team.populateFromDB("clubs.db");
        ArrayList<Member> gone = team.removeMembersFromYear(2010);
        assertEquals(2, gone.size());
        assertEquals("De Bruyne", gone.get(1).getLastName());
        assertEquals("Lukaku", gone.get(0).getLastName());
    }
*/
    /**
     * check alphabetical overview
     *
    @Test
    public void test9() 
    {
        Club team = new Club("The red Devils", 300.0f);
        team.populateFromDB("clubs.db");
        team.showSortedNames();
        PrintStream defaultSO = System.out;  
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        System.setOut(new PrintStream(baos));
        try
        {
            team.showSortedNames();
            BufferedReader br = new BufferedReader(new StringReader(baos.toString()));
            String result = br.readLine();
            assertEquals("Courtois", result);
            result = br.readLine();
            assertEquals("De Bruyne", result);
        } 
        catch(Exception e)
        {
            System.setOut(defaultSO);
            System.out.println("Error while redirection System.out");
        }
        System.setOut(defaultSO);
    }
*/
    /**
     * check showOverview with month names in stead of number
     *
    @Test
    public void test10() 
    {
        Club team = new Club("The red Devils", 300.0f);
        Member captain = new Member("Vincent", "Kompany", "vince@kompany.com", 2, 2004);
        team.addMember(captain);
        Member keeper = new Member("Thibaut", "Courtois", "numberone@reddevils.be", 11, 2011);
        team.addMember(keeper);
        team.showOverview();
        PrintStream defaultSO = System.out;  
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        System.setOut(new PrintStream(baos));
        try
        {
            team.showOverview();
            BufferedReader br = new BufferedReader(new StringReader(baos.toString()));
            String result = br.readLine();
            //use contains to see if name of month is written to screen
            assertTrue(result.startsWith("Overview of all members of club The red Devils"));
            result = br.readLine();
            assertTrue(result.contains("February"));
        } 
        catch(Exception e)
        {
            System.setOut(defaultSO);
            System.out.println("Error while redirection System.out");
        }
        System.setOut(defaultSO);
    }
*/
    /**
     * check calculation of contributions
     * This test will work as long as you run it in 2018
     *
    @Test
    public void test11() 
    {
        Club team = new Club("The red Devils", 300.0f);
        Member captain = new Member("Vincent", "Kompany", "vince@kompany.com", 2, 2004);
        team.addMember(captain);
        Member keeper = new Member("Thibaut", "Courtois", "numberone@reddevils.be", 11, 2011);
        team.addMember(keeper);
        Member back = new Member("Anthony", "Vanden Borre", "tony@reddevils.be", 4, 2004);
        team.addMember(back);
        Member everywhere = new Member("Kevin", "De Bruyne", "thekid@kids.kid", 8, 2010);
        team.addMember(everywhere);
        Member goalgetter = new Member("Romelu", "Lukaku", "bueno@ferrero.com", 8, 2010);
        team.addMember(goalgetter);
        team.assignContributions();
        assertEquals(90.0f, keeper.getContribution(), 0.1f);
        assertEquals(0.0f, captain.getContribution(), 0.1f);
    }
*/
    /**
     * check payStatus of contributions
     *
    @Test
    public void test12() 
    {
        Club team = new Club("The red Devils", 300.0f);
        Member captain = new Member("Vincent", "Kompany", "vince@kompany.com", 2, 2004);
        team.addMember(captain);
        Member keeper = new Member("Thibaut", "Courtois", "numberone@reddevils.be", 11, 2011);
        team.addMember(keeper);
        Member back = new Member("Anthony", "Vanden Borre", "tony@reddevils.be", 4, 2004);
        team.addMember(back);
        Member everywhere = new Member("Kevin", "De Bruyne", "thekid@kids.kid", 8, 2010);
        team.addMember(everywhere);
        Member goalgetter = new Member("Romelu", "Lukaku", "bueno@ferrero.com", 8, 2010);
        team.addMember(goalgetter);
        team.assignContributions();
	assertEquals(false, keeper.getPayStatus());
	keeper.pay(80.0f);
	assertEquals(false, keeper.getPayStatus());
	keeper.pay(10.0f);
	assertEquals(true, keeper.getPayStatus());
    }
*/
	/**
	 * Query: Give an overview of all years and the number of members who started in that year
	 * Oldest year first
	 *
	@Test
	public void test13()
	{
		try
		{
		Queries q1 = new Queries(c);
		assertTrue(Solutions.checkResultSets(q1.query1(), Solutions.Query1()));
		}
		catch (SQLException sqle)
		{
			System.err.println( "ERROR : "+ sqle.getMessage() );
		}
	}
*/	
	/**
	 * Query: Give first name, last name and payed amount of the member who payed over all the years 
	 * the biggest amount
	 *
	@Test
	public void test14()
	{
		try
		{
		Queries q1 = new Queries(c);
		assertTrue(Solutions.checkResultSets(q1.query2(), Solutions.Query2()));
		}
		catch (SQLException sqle)
		{
			System.err.println( "ERROR : "+ sqle.getMessage() );
		}
	}
*/	
    /**
     * generate list with e-mail addresses of everyone who still has to pay
     * createEmailListOfNotPaid() is called but not checked (you have the freedom in choosing the format)
     *
    @Test
    public void test15() 
    {
        Club team = new Club("The red Devils", 300.0f);
        Member captain = new Member("Vincent", "Kompany", "vince@kompany.com", 2, 2004);
        team.addMember(captain);
        Member keeper = new Member("Thibaut", "Courtois", "numberone@reddevils.be", 11, 2011);
        team.addMember(keeper);
        Member back = new Member("Anthony", "Vanden Borre", "tony@reddevils.be", 4, 2004);
        team.addMember(back);
        Member everywhere = new Member("Kevin", "De Bruyne", "thekid@kids.kid", 8, 2010);
        team.addMember(everywhere);
        Member goalgetter = new Member("Romelu", "Lukaku", "bueno@ferrero.com", 8, 2010);
        team.addMember(goalgetter);
        team.assignContributions();
	keeper.pay(90.0f);
	everywhere.pay(60.0f);
	ArrayList<String> mailAddresses = team.createEmailListOfNotPaid();
	assertEquals(1, mailAddresses.size());
	assertEquals("bueno@ferrero.com", mailAddresses.get(0));
	team.sendPersonalMessageToPay();
	goalgetter.pay(60.0f);
	mailAddresses = team.createEmailListOfNotPaid();
	assertEquals(0, mailAddresses.size());
   }
*/
    /**
     * populate club with info stored on file in format
     * firstname(String) lastname(String) e-mail(String) month(int) year(int) paystatus(boolean)
     * use members.txt
     *
    @Test
    public void test16()
    {
        Club team = new Club("The red Devils", 300.0f);
        assertEquals(0, team.getNrOfMembers());
        team.populateFromFile("members.txt");
        assertEquals(5, team.getNrOfMembers());
        ArrayList<Member> result = team.removeMembersFromYear(2010);
        assertEquals("Wrong size of removed members", 2, result.size());
        assertEquals("Lukaku", result.get(1).getLastName());
    }
*/
    /**
     * overload constructor of Member without month and year, use current date (from java.util.LocalDate)
     *
    @Test
    public void test17()
    {
        Club team = new Club("The red Devils", 300.0f);
        Member latest = new Member("Kums", "Sven", "sven.kums@aagent.be");
        assertEquals(Now.currentYear(), latest.getYear());
        assertEquals(Now.currentMonth(), latest.getMonth());
        team.addMember(latest);
        assertEquals(1, team.getNrOfMembers());

    }
*/
    /**
     * check if all payments are correct in the historical data stored in the db
     *
    @Test
    public void test18()
    {
        Club team = new Club("The red Devils", 300.0f);
        team.populateFromDB("clubs.db");
        ArrayList<Member> result = team.checkContributions();
        assertEquals("Wrong size of 'not payed correct contribution' members", 2, result.size());
        assertTrue(result.get(0).getLastName().equals("Lukaku") || result.get(1).getLastName().equals("Lukaku"));
        assertTrue(result.get(0).getLastName().equals("Vandenborre") || result.get(1).getLastName().equals("Vandenborre"));
    }
*/
}
