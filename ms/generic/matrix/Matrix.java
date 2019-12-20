/*
 * Maak deze Matrix classe generic zodat hij bijvoorbeeld ook doubles kan aannemen
 * Tip: we hebben als enige speciale methode max dus we willen een matrix van 'Comparables'
 */

class Matrix{
	private int[][] array;
	private int xSize;
	private int ySize;

	Matrix(int xSize, int ySize){
		this.xSize = xSize;
		this.ySize = ySize;
		this.array = new int[xSize][ySize];
	}

	public void set(int x, int y, int value){
		if(x > this.xSize || y > this.ySize){
			throw new IllegalArgumentException();
		}
		this.array[x][y] = value;
	}

	public int max(){
		int max = this.array[0][0];
		for(int x = 0; x < this.xSize; x++){
			for(int y = 0; y < this.ySize; y++){
				if(max < this.array[x][y]){
					max = this.array[x][y];
				}
			}
		}
		return max;
	}

	public void print(){
		for(int x = 0; x < this.xSize; x++){
			for(int y = 0; y < this.ySize; y++){
				System.out.print(this.array[x][y]);
				System.out.print("\t");
			}
			System.out.println();
		}
	}
}
