package solution;

import java.util.ArrayList;

class Matrix<T extends Comparable<T>>{
	private ArrayList<ArrayList<T>> matrix;
	private int xSize;
	private int ySize;

	Matrix(int xSize, int ySize){
		this.xSize = xSize;
		this.ySize = ySize;
		this.matrix = new ArrayList<>();
		for(int i = 0; i < this.xSize; i++){
			matrix.add(i, new ArrayList<T>());
		}
	}

	public void set(int x, int y, T value){
		if(x > this.xSize || y > this.ySize){
			throw new IllegalArgumentException();
		}
		this.matrix.get(x).add(y, value);
	}

	public T max(){
		T max = this.matrix.get(0).get(0);
		for(int x = 0; x < this.xSize; x++){
			for(int y = 0; y < this.ySize; y++){
				if(max.compareTo(this.matrix.get(x).get(y)) < 0){
					max = this.matrix.get(x).get(y);
				}
			}
		}
		return max;
	}

	public void print(){
		for(int x = 0; x < this.xSize; x++){
			for(int y = 0; y < this.ySize; y++){
				System.out.print(this.matrix.get(x).get(y));
				System.out.print("\t");
			}
			System.out.println();
		}
		System.out.println();
	}
}
