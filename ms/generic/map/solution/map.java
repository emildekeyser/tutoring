import java.util.ArrayList;

class Map<K, V>{

	private static class Tuple<K, V>{
		public K key;
		public V value;

		public Tuple<K, V>(K key, V value){
			this.key = key;
			this.value = value;
		}
	}

	private ArrayList<Map.Tuple<K, V>> map;

	public Map(){
		this.map = new ArrayList<>();
	}

	public V get(K key){
		for(Tuple<K, V> t : this.map){
			if(t.key.equals(key)){
				return t.value;
			}
		}
		return null;
	}

	public void put(K key, V value){
		if(this.get(key) == null){
			Tuple<K, V> t = new Tuple<>(key, value);
			this.map.add(t);
		}
		else{


		}
	k

k
