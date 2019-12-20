class Main{
	public static void main(String[] args){
		Matrix<Integer> m = new Matrix<>(4, 5);
		m.set(0, 0, 30);
		m.set(0, 1, 10);
		m.set(0, 2, 6);
		m.set(0, 3, 29);
		m.set(0, 4, 17);
		m.set(1, 0, 2);
		m.set(1, 1, 26);
		m.set(1, 2, 26);
		m.set(1, 3, 2);
		m.set(1, 4, 15);
		m.set(2, 0, 2);
		m.set(2, 1, 12);
		m.set(2, 2, 6);
		m.set(2, 3, 21);
		m.set(2, 4, 15);
		m.set(3, 0, 9);
		m.set(3, 1, 30);
		m.set(3, 2, 16);
		m.set(3, 3, 19);
		m.set(3, 4, 24);

		m.print();
	}
}
