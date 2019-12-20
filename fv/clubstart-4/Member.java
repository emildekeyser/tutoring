public class Member 
{
	private String firstName;
	private String lastName;
	private String eMail;
	private int month;
	private int year;
	
	public Member(String firstName, String lastName, String eMail, int month,
			int year) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.eMail = eMail;
		this.month = month;
		this.year = year;
	}


	/**
	 * @return the firstName
	 */
	public String getFirstName() {
		return firstName;
	}

	/**
	 * @return the lastName
	 */
	public String getLastName() {
		return lastName;
	}

	/**
	 * @return the eMail
	 */
	public String geteMail() {
		return eMail;
	}

	/**
	 * @return the month
	 */
	public int getMonth() {
		return month;
	}

	/**
	 * @return the year
	 */
	public int getYear() {
		return year;
	}


}


