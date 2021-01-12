public class RandomNoGenerate{
	public final static int Mul=1234567890;
	public final static int Inc=12345;
	public final static int Mod= 2147483647;
	
	public static int value=3819201;
	
	public static int random(){
		value=(value*Mul+Inc)%Mod;
		return value;
	}
	
	public static int generator(){
		int tmp= random();
		if(tmp<0){
			value=tmp * -1;
	}
	return value;
	}
	    public static void main(String[] args) {
		for(int i=0;i<13;i++){
			
		System.out.println(generator());
		}  
    }
	
	}
	