import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.*;


public class Queries
{
	private Connection c;

	public Queries(Connection c)
	{
		this.c = c;
	}

	public ResultSet query1() throws SQLException
	{
		Statement stmt = c.createStatement();
		String query = "";
		ResultSet rs = stmt.executeQuery( query );
		return rs;
	}

	public ResultSet query2() throws SQLException
	{
		Statement stmt = c.createStatement();
		String query = "";
		ResultSet rs = stmt.executeQuery( query );
		return rs;
	}

	public ResultSet query3() throws SQLException
	{
		Statement stmt = c.createStatement();
		String query = "";
		ResultSet rs = stmt.executeQuery( query );
		return rs;
	}
	
}
