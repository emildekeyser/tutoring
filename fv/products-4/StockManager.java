import java.util.ArrayList;
import java.sql.*;

/**
 * Manage the stock in a business.
 * The stock is described by zero or more Products.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class StockManager
{
    // A list of the products.
    private ArrayList<Product> stock;

    /**
     * Initialise the stock manager.
     */
    public StockManager()
    {
        stock = new ArrayList<Product>();
    }

    /**
     * Add a product to the list.
     * @param item The item to be added.
     */
    public void addProduct(Product item)
    {
        stock.add(item);
    }
    
    /**
     * Receive a delivery of a particular product.
     * Increase the quantity of the product by the given amount.
     * @param id The ID of the product.
     * @param amount The amount to increase the quantity by.
     */
    public void delivery(int id, int amount)
    {
    }
    
    /**
     * Try to find a product in the stock with the given id.
     * @return The identified product, or null if there is none
     *         with a matching ID.
     */
    public Product findProduct(int id)
    {
        return null;
    }
    
    /**
     * Locate a product with the given ID, and return how
     * many of this item are in stock. If the ID does not
     * match any product, return zero.
     * @param id The ID of the product.
     * @return The quantity of the given product in stock.
     */
    public int numberInStock(int id)
    {
        return 0;
    }

    /**
     * Print details of all the products.
     */
    public void printProductDetails()
    {
    }
    
    public void populateFromDB(String dbName)
    {
       Connection c = null; //will create a connection to the database
        try {
            Class.forName("org.sqlite.JDBC"); //checks if library used to access the database is available
            c = DriverManager.getConnection("jdbc:sqlite:"+dbName); //open the specific DB, should be on same map as BlueJ project
            //will throw an exception when something goes wrong, so if we get to next line everything is OK
            System.out.println("Opened database successfully");
            //statements are used to create queries
            Statement stmt = c.createStatement();
            ResultSet rs = stmt.executeQuery( "SELECT * FROM Product;" );
            //rs is an 2D array with rows and columns, after first call to rs.next(), rs will point to the first row
            //when no more rows available, rs.next() returns false
            while ( rs.next() == true) 
            {
                //both names and indices can be used to retrieve data from a column
                int id = rs.getInt("id");
                String name = rs.getString("name");
                int quantity = rs.getInt("quantity");
                Product p = new Product(id, name);
                p.increaseQuantity(quantity);
                addProduct(p);
            }
            //close everything to clean up resources
            rs.close();
            stmt.close();
            c.close();
        } 
        catch ( Exception e ) 
        {
            System.err.println( "ERROR : "+ e.getMessage() );
        }
    }
}
